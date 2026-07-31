#importa menu e formulario
from menus import mostrar_menu
from atendimentos import enviar_formulario, enviar_lista_postos


problemas = {
    "1": "Abastecimento não autorizado",
    "2": "Senha inválida",
    "3": "Quilometragem",
    "4": "Cartão bloqueado",
    "5": "Saldo insuficiente",
    "6": "Problema no posto"
}

while True:
    mostrar_menu()

    opcao = input('Digite a opção desejada: ')

    if opcao.lower() == " sair":
        print('Atendimento encerrado')
        break


    elif opcao in problemas:
        print(f"""
Problema selecionado:
{problemas[opcao]}
""")

        enviar_formulario()

    elif opcao == "7":
        enviar_lista_postos()

    elif opcao == "8":
         print("Encaminhando para um atendente humano...")

else:
    print("Opção inválida. Tente novamente.")