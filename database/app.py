from consultar import (
    consultar_por_categoria,
    consultar_por_avaliacao,
    consultar_por_nome
)

from inserir import inserir_produto
from atualizar import atualizar_produto
from excluir import excluir_produto

while True:
    print("\n===== LOJA DO ALUNO =====")
    print("1 - Consultar por categoria")
    print("2 - Consultar por avaliação")
    print("3 - Consultar por nome")
    print("4 - Inserir produto")
    print("5 - Atualizar produto")
    print("6 - Excluir produto")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        consultar_por_categoria()

    elif opcao == "2":
        consultar_por_avaliacao()

    elif opcao == "3":
        consultar_por_nome()

    elif opcao == "4":
        inserir_produto()

    elif opcao == "5":
        atualizar_produto()

    elif opcao == "6":
        excluir_produto()

    elif opcao == "7":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")