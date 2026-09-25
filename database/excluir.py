from conexao import produtos


def excluir_produto():
    nome = input("Digite o nome do produto: ")

    resultado = produtos.delete_one(
        {"produto": nome}
    )

    if resultado.deleted_count > 0:
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado.")