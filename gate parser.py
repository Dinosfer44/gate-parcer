import requests

url = "https://api.gateio.ws/api/v4/spot/order_book"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

currency_pair = ["BTC_USDT", "ETH_USDT", "SOL_USDT"]

for pair in currency_pair:
  param = {"currency_pair": pair}
  try:
    response = requests.get(url=url, params=param, headers=headers)
    if response.status_code == 200:
      json_data = response.json()
      print (f"Orderbook для {pair}:")
      print ("Топ 5 ордеров на покупку: ")
      for bid in json_data.get("bid", [])[:5]:
        print(f"Цена: {bid[0]}, Количество: {bid[1]}")
      print("Ордера на продажу (топ-5):")
      for ask in json_data.get('asks', [])[:5]:
          print(f"Цена: {ask[0]}, Количество: {ask[1]}")
    elif response.status_code == 429:
      print('Gate API got rate limit')
  except requests.exceptions.RequestException as error:
    print(f'Произошла ошибка при выполненнии запроса для {pair}: {error}')