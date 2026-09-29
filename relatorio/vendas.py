from database.conexao import db


vendas = db["vendas"]


def relatorio_vendas():
    total_vendas = 0
    quantidade_produtos = 0

    print("\n===== RELATÓRIO DE VENDAS =====")

    for venda in vendas.find():
        total_vendas += venda["total"]
        quantidade_produtos += venda["quantidade"]

        print(
            "Produto:", venda["produto"],
            "| Quantidade:", venda["quantidade"],
            "| Preço unitário:", venda["preco_unitario"],
            "| Total:", venda["total"],
            "| Categoria:", venda["categoria"]
        )

    print("\n===== RESUMO =====")
    print("Total vendido: R$", total_vendas)
    print("Quantidade de produtos vendidos:", quantidade_produtos)

def produto_mais_vendido():
    vendas_por_produto = {}

    for venda in vendas.find():
        produto = venda["produto"]
        quantidade = venda["quantidade"]

        if produto in vendas_por_produto:
            vendas_por_produto[produto] += quantidade
        else:
            vendas_por_produto[produto] = quantidade

    if not vendas_por_produto:
        print("Nenhuma venda registrada.")
        return

    produto = max(
        vendas_por_produto,
        key=vendas_por_produto.get
    )

    quantidade = vendas_por_produto[produto]

    print("\n===== PRODUTO MAIS VENDIDO =====")
    print("Produto:", produto)
    print("Quantidade vendida:", quantidade)
    

    #aqui começa a agregação ( filtragem do valor toral das vendas de cada categoria)
def vendas_por_categoria():
    vendas_por_categoria = {}

    for venda in vendas.find():
        categoria = venda["categoria"]
        total = venda["total"]

        if categoria in vendas_por_categoria:
            vendas_por_categoria[categoria] += total
        else:
            vendas_por_categoria[categoria] = total

    if not vendas_por_categoria:
        print("Nenhuma venda registrada.")
        return

    print("\n===== VENDAS POR CATEGORIA =====")

    for categoria, total in vendas_por_categoria.items():
        print(
            "Categoria:", categoria,
            "| Total vendido: R$", total
        )