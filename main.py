import requests
import time

# URLs dos dois sites
site1 = 'https://n8n-latest-8x9d.onrender.com'

while True:
    try:
        resposta1 = requests.get(site1)
        print(f'({site1}) Status: {resposta1.status_code}, Horário: {time.strftime("%Y-%m-%d %H:%M:%S")}')
    except Exception as erro:
        print(f'Erro na requisição do site: {erro}')
    time.sleep(30)