from database.conexao import produtos, db


vendas = db["vendas"]


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