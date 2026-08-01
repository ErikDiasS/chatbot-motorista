#importa menu e formulario
from menus import mostrar_menu
from atendimentos import enviar_formulario, enviar_lista_postos, confirmar_recebimento, perguntar_continuar, coletar_informacoes, resumo_chamado


problemas = {
    "1": "Abastecimento não autorizado",
    "2": "Senha inválida",
    "3": "Quilometragem/Horimetro Superior",
    "4": "Cartão bloqueado",
    "5": "Saldo insuficiente",
    "6": "Problema no posto",
}

while True:
    mostrar_menu()

    opcao = input('Digite a opção desejada: ')

    if opcao.lower() == "sair":
        print('Atendimento encerrado')
        break


    elif opcao in problemas:
        print(f"""
Problema selecionado:
{problemas[opcao]}
""")        

        enviar_formulario()

        informacoes_motorista = coletar_informacoes()

        resumo_chamado(problemas[opcao], informacoes_motorista)

        confirmar_recebimento()

        break


    elif opcao == "7":
    
         enviar_lista_postos()

         perguntar_continuar()

         resposta = input('Digite sua resposta: ')

         if resposta.lower() == "sim":
            continue

         elif resposta.lower() == "não":
            print("Atendimento encerrado.")
            break

         elif resposta.lower() == "atendimento":
            print("Encaminhando para um analista.")
            break

else:
    print("Opção inválida.")
