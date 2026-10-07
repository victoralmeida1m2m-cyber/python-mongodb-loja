import secrets
from datetime import datetime, timezone

from database.conexao import produtos, db


vendas = db["vendas"]
pedidos = db["pedidos"]

PAGAMENTOS = {"pix", "cartao", "boleto"}


def efetuar_venda(nome, quantidade):
    """Registra uma venda e devolve um dicionário (sem print/input).

    Usada pelo site (server.py) e pelo menu de terminal.
    """
    try:
        quantidade = int(quantidade)
    except (TypeError, ValueError):
        return {"ok": False, "erro": "Quantidade inválida."}

    if quantidade <= 0:
        return {"ok": False, "erro": "A quantidade deve ser maior que zero."}

    produto = produtos.find_one({"produto": nome})

    if produto is None:
        return {"ok": False, "erro": "Produto não encontrado."}

    # Baixa de estoque atômica: só desconta se ainda houver estoque suficiente.
    # Evita vender a mesma unidade para duas pessoas ao mesmo tempo.
    baixa = produtos.update_one(
        {"produto": nome, "estoque": {"$gte": quantidade}},
        {"$inc": {"estoque": -quantidade}},
    )

    if baixa.modified_count == 0:
        return {"ok": False, "erro": "Estoque insuficiente."}

    preco_unitario = produto["preco"]
    total = quantidade * preco_unitario

    resultado = vendas.insert_one({
        "produto": produto["produto"],
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "total": total,
        "categoria": produto["categoria"],
    })

    restante = produtos.find_one({"produto": nome}, {"estoque": 1})["estoque"]

    return {
        "ok": True,
        "id": str(resultado.inserted_id),
        "total": float(total),
        "estoque": int(restante),
    }


def registrar_venda():
    """Versão de terminal (a mesma que você já usava)."""
    nome = input("Digite o nome do produto: ")

    try:
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Quantidade inválida.")
        return

    resultado = efetuar_venda(nome, quantidade)

    if resultado["ok"]:
        print("Venda registrada com sucesso!")
        print("ID da venda:", resultado["id"])
    else:
        print(resultado["erro"])


def efetuar_pedido(cliente, pagamento, itens):
    """Fecha um pedido com vários itens (pagamento SIMULADO).

    - O preço vem sempre do banco, nunca do navegador.
    - Se algum item falhar, o estoque dos anteriores é devolvido.
    - Cada item vira uma linha em "vendas" (com pedido_id), então o
      relatorio/vendas.py continua funcionando.
    """
    nome = str(cliente.get("nome", "")).strip()[:80]
    email = str(cliente.get("email", "")).strip()[:120]

    if len(nome) < 2:
        return {"ok": False, "erro": "Informe seu nome."}
    if "@" not in email or "." not in email.split("@")[-1]:
        return {"ok": False, "erro": "E-mail inválido."}
    if pagamento not in PAGAMENTOS:
        return {"ok": False, "erro": "Forma de pagamento inválida."}
    if not isinstance(itens, list) or not itens or len(itens) > 30:
        return {"ok": False, "erro": "Carrinho vazio."}

    # Junta itens repetidos e valida as quantidades.
    quantidades = {}
    for item in itens:
        try:
            q = int(item.get("quantidade", 0))
        except (TypeError, ValueError, AttributeError):
            return {"ok": False, "erro": "Quantidade inválida."}
        if q <= 0 or q > 99:
            return {"ok": False, "erro": "Quantidade inválida."}
        chave = str(item.get("produto", ""))
        quantidades[chave] = quantidades.get(chave, 0) + q

    baixados = []  # (produto, quantidade) já descontados do estoque

    def desfazer():
        for nome_produto, q in baixados:
            produtos.update_one({"produto": nome_produto}, {"$inc": {"estoque": q}})

    linhas = []
    try:
        for nome_produto, q in quantidades.items():
            produto = produtos.find_one({"produto": nome_produto})
            if produto is None:
                desfazer()
                return {"ok": False, "erro": f"Produto não encontrado: {nome_produto}"}

            baixa = produtos.update_one(
                {"produto": nome_produto, "estoque": {"$gte": q}},
                {"$inc": {"estoque": -q}},
            )
            if baixa.modified_count == 0:
                desfazer()
                return {"ok": False, "erro": f"Estoque insuficiente: {nome_produto}"}

            baixados.append((nome_produto, q))
            linhas.append({
                "produto": produto["produto"],
                "quantidade": q,
                "preco_unitario": produto["preco"],
                "total": q * produto["preco"],
                "categoria": produto["categoria"],
            })

        total = sum(l["total"] for l in linhas)
        agora = datetime.now(timezone.utc)
        numero = f"LA-{agora:%y%m%d}-{secrets.token_hex(2).upper()}"

        pedido = pedidos.insert_one({
            "numero": numero,
            "cliente": {"nome": nome, "email": email},
            "pagamento": pagamento,
            "status": "pago (simulado)",
            "itens": linhas,
            "total": total,
            "criado_em": agora,
        })
        for linha in linhas:
            vendas.insert_one({**linha, "pedido_id": pedido.inserted_id})
    except Exception:
        desfazer()
        return {"ok": False, "erro": "Não foi possível concluir o pedido."}

    estoques = {
        n: int(produtos.find_one({"produto": n}, {"estoque": 1})["estoque"])
        for n, _ in baixados
    }
    return {"ok": True, "numero": numero, "total": float(total), "estoques": estoques}