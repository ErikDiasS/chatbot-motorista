def enviar_formulario():
    print("""
Informe:

* Placa Cavalo:

* Nome do posto:

* Mensagem apresentada:

* Foto da tela (se possível).
""")

def coletar_informacoes():

    placa = input("Digite a placa do cavalo: ")

    posto = input("Digite o nome do posto: ")

    mensagem = input("Digite a mensagem apresentada: ")

    foto = input("Encaminhe a foto (se houver): ")

    return {
        "placa": placa,
        "posto": posto,
        "mensagem": mensagem,
        "foto": foto
    }


def resumo_chamado(problema, informacoes):
    print(f"""
    Chamado recebido:

    Problema:
    {problema}

    Placa do cavalo: 
    {informacoes['placa']}

    Nome do posto:
    {informacoes['posto']}

    Mensagem apresentada:
    {informacoes['mensagem']}

    Foto:
    {informacoes['foto']}

    Status:
    Em análise.
""")

def enviar_lista_postos():
    print("""
🚛 Lista de postos credenciados Transzilli

Segue o mapa com todos os postos credenciados.

📍 Clique no link abaixo para abrir no Google Maps:

https://www.google.com/maps/d/edit?mid=1WobvY8v1llouLrFinRP73g29gHN_Jbo&usp=drive_link

Caso não encontre um posto credenciado ou tenha qualquer dificuldade no abastecimento, retorne ao menu e escolha a opção correspondente ao seu problema.
""")

def confirmar_recebimento():
    print("""
informações recebidas.

Suas informações estão sendo analisadas... aguarde.
""")

def perguntar_continuar():
    print("""
Deseja mais alguma coisa? 

Digite o numero correspondente à sua resposta:
1: SIM
2: NÃO
3: ATENDIMENTO
""")