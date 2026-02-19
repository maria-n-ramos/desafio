import requests
import json
import os

def ingestao(termo="python"):
    HEADERS = {
        "user-agent": "Mozilla/5.0"
    }

    params = {
        "name": "python",
        "offset": 0,
        "limit": 10
    }

    url = "https://portal.api.gupy.io/api/job"



    try:
        resposta = requests.get(url,headers=HEADERS,params=params)

        #Sucesso?
        if resposta.status_code == 200:
            dados = resposta.json()

            #Pasta vagas
            os.makedirs("dados/vagas", exist_ok=True)

            #Salvar em json
            with open("dados/vagas/vagas_{termo}.json","w",encoding="utf-8") as f:
                    json.dump(dados, f, ensure_ascii=False, indent = 4)
            print("Dados salvos.")

        else:
            print("Erro:",resposta.status_code)
    except requests.exceptions.Timeout:
        print("Erro: tempo de resposta excedido.")
    except requests.exceptions.RequestException as e:
        print("Erro na requisição.", e)

