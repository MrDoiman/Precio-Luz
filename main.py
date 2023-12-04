import requests
from datetime import datetime, timedelta

api_key = 'CLAVE API'
url = 'https://api.esios.ree.es/'

fecha_manana = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

endpoint = f'indicators/102?start_date={fecha_manana}&end_date={fecha_manana}T23:59:59'

request_url = f'{url}{endpoint}'

headers = {'Authorization': f'Token token="{api_key}"'}
response = requests.get(request_url, headers=headers)

horas = int(input("Introduce las horas deseadas: "))

if response.status_code == 200:
    data = response.json()
    precios = data['Precios']

    precios_lista = []

    for precio in precios:
        hora = precio['datetime_utc'][11:16]
        valor = precio['value']
        print(f'Hora: {hora}, Precio: {valor} €/MWh')
        print("----------------------")
        precios_lista.append({'hora': hora, 'precio': valor})
    
    precios_ordenados = sorted(precios_lista, key=lambda x: x['precio'])

    print(f"Las {horas} horas con los precios más bajos")
    for i in range(min(horas, len(precios_ordenados))):
        print(f'{precios_ordenados[i]["hora"]}: {precios_ordenados[i]["precio"]} €/MWh')
else:
    print(f'Error al obtener datos. Código de estado: {response.status_code}')
    print(response.text)