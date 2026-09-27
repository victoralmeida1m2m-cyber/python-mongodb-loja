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