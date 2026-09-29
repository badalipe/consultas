import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.get("/")
def inicio():
    return jsonify({
        "status": "online",
        "sistema": "BD Tecnologia",
        "mensagem": "Backend funcionando"
    })


@app.get("/api/status")
def status():
    return jsonify({
        "status": "online",
        "backend": "operacional",
        "apis": {
            "cpf": "aguardando configuração",
            "cnpj": "aguardando configuração",
            "processos": "aguardando configuração",
            "oab": "aguardando configuração"
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
