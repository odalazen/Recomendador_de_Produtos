import json

def get_all_products():
    with open('./data/products.json','r', encoding='utf-8') as arquivo:
        conteudo = json.load(arquivo)

    return conteudo