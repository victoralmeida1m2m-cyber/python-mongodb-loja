from database.consultar import (
    consultar_por_categoria,
    consultar_por_avaliacao,
    consultar_por_nome,
    consultar_venda
)

from database.inserir import inserir_produto
from database.atualizar import atualizar_produto
from database.excluir import excluir_produto
from database.registrar_venda import registrar_venda

from relatorio.vendas import relatorio_vendas


while True:
    print("\n===== LOJA DO ALUNO =====")
    print("1 - Consultar por categoria")
    print("2 - Consultar por avaliação")
    print("3 - Consultar por nome")
    print("4 - Inserir produto")
    print("5 - Atualizar produto")
    print("6 - Excluir produto")
    print("7 - Registrar venda")
    print("8 - Relatório de vendas")
    print("9 - Consultar venda")
    print("10 - Sair")

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
        registrar_venda()

    elif opcao == "8":
        relatorio_vendas()

    elif opcao == "9":
        consultar_venda()

    elif opcao == "10":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")