import json
import requests
import base64


def define_sentimento(frase):
    
    if type(frase) == str and frase.strip() != '':        
        url = 'https://api.gotit.ai/NLU/v1.5/Analyze'
        data = {"T":frase,"S":True, 'EM':True}
        data_json = json.dumps(data)
        userAndPass = base64.b64encode(b"2501-ZrmjxXGI:y0XfiNa3HG/L4MvVrrcvE1JgHYPGRQEbGRMOi1LX9vxh").decode("ascii")
        headers = {'Content-type': 'application/json', "Authorization": "Basic %s" %  userAndPass}
        
        response = requests.post(url, data=data_json, headers=headers)
        
        return response.json()
    
    else:
        return False
