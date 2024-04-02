import requests

api_key = '###'

app_id_rimworld = 294100
base_url = 'https://store.steampowered.com/api/'

endpoint = f'appdetails?appids={app_id_rimworld}'

url = f'{base_url}{endpoint}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    if str(app_id_rimworld) in data:
        game_data = data[str(app_id_rimworld)]
        if game_data['success']:
            game_details = game_data['data']
            name = game_details['name']
            
            if 'price_overview' in game_details:
                price_overview = game_details['price_overview']
                if 'discount_percent' in price_overview:
                    discount_percent = price_overview['discount_percent']
                    print(f'Nombre del juego: {name}')
                    print(f'Descuento: {discount_percent}%')
                else:
                    print(f'El juego no tiene descuento en este momento.')
            else:
                print(f'No se encontró información de precios para el juego.')
        else:
            print(f'No se pudo obtener detalles del juego (Código de error: {game_details["success"]})')
    else:
        print(f'El juego con ID {app_id_rimworld} no se encontró en la respuesta.')
else:
    print('Error en la solicitud a la Steam Web API')