from flask import Flask, request

app = Flask(__name__)


@app.route("/webhook", methods=["GET"])
def verificar_webhook():
    modo = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    desafio = request.args.get("hub.challenge")

    if modo == "subscribe" and token == "meu_token_transzilli":
        return desafio, 200

    return "Token inválido", 403


@app.route("/webhook", methods=["POST"])
def receber_webhook():
    dados = request.get_json()

    try:
        mensagem = dados["entry"][0]["changes"][0]["value"]["messages"][0]
        texto = mensagem["text"]["body"]

        print("\nMensagem recebida:")
        print(texto)

        if texto == "1":
            print("Problema selecionado: Abastecimento não autorizado")

        elif texto == "2":
            print("Problema selecionado: Senha inválida")

        elif texto == "3":
            print("Problema selecionado: Quilometragem/Horimetro Superior")

        elif texto == "4":
            print("Problema selecionado: Cartão bloqueado")

        elif texto == "5":
            print("Problema selecionado: Saldo insuficiente")

        elif texto == "6":
            print("Problema selecionado: Problema no posto")

        elif texto == "7":
            print("Enviando lista de postos credenciados...")

        elif texto == "8":
            print("Consultando chamado...")

        else:
            print("Opção inválida.")

    except (KeyError, IndexError, TypeError):
        print("\nEvento recebido, mas não é uma mensagem de texto.")

    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(debug=True)