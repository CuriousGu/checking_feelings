# testando a API do GOT IT 
# Capaz de retornar o sentimento do usuário 
# usando análise semântica e redes neurais 

import json
import requests
import pprint
import base64

    
def define_sentimento(frase):
    
    ############ just to hide my API key ############
    dict_credenciais = dict()
    with open('got_it/credentials.txt', encoding='utf-8') as credencias:
        for linha in credencias:
            key, value = linha.split('=')
            dict_credenciais[key] = value
    ################################################
    
    url = 'https://api.gotit.ai/NLU/v1.5/Analyze'
    data = {"T":frase,"S":True, 'EM':True}

    got_it_secret = dict_credenciais['got_it_secret'].strip()
    print(got_it_secret)
    
    data_json = json.dumps(data)
    userAndPass = base64.b64encode(bytes(got_it_secret, encoding='utf-8')).decode("ascii")
    # userAndPass = base64.b64encode(b"your_key_identifier:your_key_secret").decode("ascii")

    headers = {'Content-type': 'application/json', "Authorization": "Basic %s" %  userAndPass}
    response = requests.post(url, data=data_json, headers=headers)

    print(f'frase:{frase}')
    pprint.pprint(response.json())
    print('\n\n')

    return response.json()
    