#chama a biblioteca json para salvar e ler os chamados em um arquivo json
import json
#envia o formulário para o motorista preencher com as informações necessárias para abrir um chamado
def enviar_formulario():
    print("""
Informe:

* Placa Cavalo:

* Nome do posto:

* Mensagem apresentada:

* Foto da tela (se possível).
""")
#coloca as informações coletadas do motorista em um dicionário e retorna para o app.py
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

#devolve as informações do chamado para o motorista, mostrando um resumo do que foi coletado e o status do chamado
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
#envia a lista de postos credenciados para o motorista, com um link para o Google Maps, e pergunta se deseja continuar ou encerrar o atendimento
def enviar_lista_postos():
    print("""
🚛 Lista de postos credenciados Transzilli

Segue o mapa com todos os postos credenciados.

📍 Clique no link abaixo para abrir no Google Maps:

https://www.google.com/maps/d/edit?mid=1WobvY8v1llouLrFinRP73g29gHN_Jbo&usp=drive_link

Caso não encontre um posto credenciado ou tenha qualquer dificuldade no abastecimento, retorne ao menu e escolha a opção correspondente ao seu problema.
""")
#confirma o recebimento das informações do motorista e informa que o chamado está sendo analisado
def confirmar_recebimento():
    print("""
informações recebidas.

Suas informações estão sendo analisadas... aguarde.
""")
#pergunta se o motorista se deseja continuar ou encerrar o atendimento, com as opções de SIM, NÃO e ATENDIMENTO
def perguntar_continuar():
    print("""
Deseja mais alguma coisa? 

Digite o numero correspondente à sua resposta:
1: SIM
2: NÃO
3: ATENDIMENTO
""")
#salva as informações do chamado em um arquivo json, com o problema, placa, posto, mensagem, foto e status do chamado
def salvar_chamado(problema, informacoes):
    with open("chamados.json", "r", encoding ="utf-8") as arquivo:
        chamados = json.load(arquivo)

    chamado = {
        "problema": problema,
        "placa": informacoes["placa"],
        "posto": informacoes["posto"],
        "mensagem": informacoes["mensagem"],
        "foto": informacoes["foto"],
        "status": "Em análise"

    }

    chamados.append(chamado)

    with open("chamados.json", "w", encoding="utf-8") as arquivo:
        json.dump(chamados,arquivo, indent=4, ensure_ascii=False)

#enviar uma lista de chamados já realizados, caso o motorista queira verificar o status do seu chamado, com a opção de digitar a placa do cavalo e mostrar todos os chamados relacionados a essa placa
def consultar_chamados():
    with open("chamados.json", "r", encoding="utf-8") as arquivo:
        chamados = json.load(arquivo)

    placa = input("Digite a placa do cavalo: ")

    encontrados = []

    for chamado in chamados:
        if chamado["placa"].lower() == placa.lower():
            encontrados.append(chamado)

    if not encontrados:
        print("\nNenhum chamado encontrado para essa placa.")
        return

    print(f"""
==============================
Foram encontrados {len(encontrados)} chamado(s)
==============================
""")

    for numero, chamado in enumerate(encontrados, start=1):

        print(f"""
Chamado {numero}
----------------------------------------
Problema:
{chamado["problema"]}

Placa:
{chamado["placa"]}

Posto:
{chamado["posto"]}

Mensagem:
{chamado["mensagem"]}

Foto:
{chamado["foto"]}

Status:
{chamado["status"]}
----------------------------------------
""")