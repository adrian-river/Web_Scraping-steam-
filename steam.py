import requests

api_key = '###'

game_id = 457140
base_url = 'https://store.steampowered.com/api/'

endpoint = f'appdetails?appids={game_id}'

url = f'{base_url}{endpoint}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    if str(game_id) in data:
        game_data = data[str(game_id)]
        if game_data['success']:
            game_details = game_data['data']
            name = game_details['name']
            
            if 'price_overview' in game_details:
                price_overview = game_details['price_overview']
                if 'discount_percent' in price_overview:
                    discount_percent = price_overview['discount_percent']
                    initial_formatted = price_overview['initial_formatted']
                    final_formatted = price_overview['final_formatted']
                    print(f'{price_overview}')
                    print(f'Nombre del juego: {name}')
                    print(f'Descuento: {discount_percent}%')
                    print(f'Precio antes: {initial_formatted}')
                    print(f'Precio con el descuento: {final_formatted}')
                else:
                    print(f'El juego no tiene descuento en este momento.')
            else:
                print(f'No se encontró información de precios para el juego.')
        else:
            print(f'No se pudo obtener detalles del juego (Código de error: {game_details["success"]})')
    else:
        print(f'El juego con ID {game_id} no se encontró en la respuesta.')
else:
    print('Error en la solicitud a la Steam Web API')