from fastapi import FastAPI, Query
import requests

app = FastAPI()

'''
Endpoint que exibe uma mensagem incrível do mundo da programção!
'''

@app.get('/api/hello')
def hello_word():
    return [
            {
                "Cliente": "Brad",
                "CPF": "143.333.666",
                "Renda": "3000"

            },
            {
                "Cliente": "Cristiano", 
                "CPF": "598.092.789", 
                "Renda": "5000"
            },
            {
                "Cliente": "Lucas",
                "CPF": "598.092.7988",
                "Renda": "1000"
            }
        ]

@app.get('/api/restaurantes/')

def get_restaurantes(restaurante: str = Query(None)):

    '''
    Endpoint para ver os cardápios dos restaurantes

    '''

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if (response.status_code == 200):
        dados_json = response.json()
        if  restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company']  == restaurante:
            
            
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                    
                })
        return {'Restaurante': restaurante, 'Cardápio': dados_restaurante}
    else:
       return {'Erro': f'{response.status_code} - {response.text}'}


