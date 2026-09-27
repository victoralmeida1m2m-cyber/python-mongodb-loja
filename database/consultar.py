from database.conexao import produtos, db
vendas = db["vendas"]


def consultar_por_categoria():
    categoria = input("Digite a categoria: ")

    for produto in produtos.find(
        {"categoria": categoria}
    ):
        print(
            "Produto:", produto["produto"],
            "| Preço:", produto["preco"],
            "| Estoque:", produto["estoque"],
            "| Categoria:", produto["categoria"]
        )


def consultar_por_avaliacao():
    avaliacao = float(input("Digite a avaliação mínima: "))

    for produto in produtos.find(
        {"avaliacao": {"$gte": avaliacao}}
    ):
        print(
            "Produto:", produto["produto"],
            "| Preço:", produto["preco"],
            "| Avaliação:", produto["avaliacao"]
        )


def consultar_por_nome():
    nome = input("Digite o nome do produto: ")

    for produto in produtos.find(
        {"produto": nome}
    ):
        print(
            "Produto:", produto["produto"],
            "| Preço:", produto["preco"],
            "| Estoque:", produto["estoque"],
            "| Categoria:", produto["categoria"]
        )

def consultar_venda():
    produto = input("Digite o produto vendido: ")

    for venda in vendas.find(
        {"produto": produto}
    ):
        print(
            "Produto:", venda["produto"],
            "| Quantidade:", venda["quantidade"],
            "| Preço unitário:", venda["preco_unitario"],
            "| Total:", venda["total"],
            "| Categoria:", venda["categoria"]
        )