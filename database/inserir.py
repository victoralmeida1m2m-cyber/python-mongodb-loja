
from conexao import produtos


def inserir_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    estoque = int(input("Digite o estoque: "))
    categoria = input("Digite a categoria: ")
    avaliacao = float(input("Digite a avaliação: "))
    cor = input("Digite a cor: ")

    novo_produto = {
        "produto": nome,
        "preco": preco,
        "estoque": estoque,
        "categoria": categoria,
        "avaliacao": avaliacao,
        "cor": cor
    }

    resultado = produtos.insert_one(novo_produto)

    print("Produto inserido com sucesso!")
    print("ID:", resultado.inserted_id)