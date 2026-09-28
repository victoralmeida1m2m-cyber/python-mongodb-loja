from database.conexao import produtos, db


vendas = db["vendas"]


def registrar_venda():
    nome = input("Digite o nome do produto: ")

    produto = produtos.find_one(
        {"produto": nome}
    )

    if produto is None:
        print("Produto não encontrado.")
        return

    quantidade = int(input("Digite a quantidade: "))

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    if quantidade > produto["estoque"]:
        print("Estoque insuficiente.")
        return

    preco_unitario = produto["preco"]

    total = quantidade * preco_unitario

    nova_venda = {
        "produto": produto["produto"],
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "total": total,
        "categoria": produto["categoria"]
    }

    produtos.update_one(
        {"produto": produto["produto"]},
        {"$inc": {"estoque": -quantidade}}
    )

    resultado = vendas.insert_one(nova_venda)

    print("Venda registrada com sucesso!")
    print("ID da venda:", resultado.inserted_id)