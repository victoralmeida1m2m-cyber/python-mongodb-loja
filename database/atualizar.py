from conexao import produtos


def atualizar_produto():
    nome = input("Digite o nome do produto: ")
    novo_preco = float(input("Digite o novo preço: "))

    resultado = produtos.update_one(
        {"produto": nome},
        {"$set": {"preco": novo_preco}}
    )

    if resultado.modified_count > 0:
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado ou o preço já é esse.")