import requests
import time

# URLs dos dois sites
site1 = 'https://n8n-latest-8x9d.onrender.com'
site2 = 'https://exemplo2.com'

while True:
    try:
        resposta1 = requests.get(site1)
        print(f'Site 1 ({site1}) Status: {resposta1.status_code}, Horário: {time.strftime("%Y-%m-%d %H:%M:%S")}')
    except Exception as erro:
        print(f'Erro na requisição do site 1: {erro}')
    time.sleep(45)

    try:
        resposta2 = requests.get(site2)
        print(f'Site 2 ({site2}) Status: {resposta2.status_code}, Horário: {time.strftime("%Y-%m-%d %H:%M:%S")}')
    except Exception as erro:
        print(f'Erro na requisição do site 2: {erro}')
    time.sleep(45)
