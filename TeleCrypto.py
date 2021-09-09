"""
@author: gelistirici
"""

import requests
import datetime
import time
import json

with open('config.json', 'r', encoding='UTF-8') as f:
    config = json.loads(f.read())
API_KEY = config['API_KEY']
chat_id = config['chat_id']
coins = config['coins']
delay = config['delay']

def check_response(response):
    if response['ok']:
        return True
    else:
        return False

def send_messsage(content):
    response = requests.post(f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={chat_id}', {'text': content}).json()
    return check_response(response)

def coin_price(coin):
    try:
        data = json.loads(requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={coin}&tsyms=USD', headers={'User-agent': 'Mozilla/5.0'}).text)['DISPLAY'][coin]['USD']
        content = f'''#{coin}USD Paritesi
Fiyat: {data['PRICE']}
24 Saatte en yüksek: {data['HIGH24HOUR']}
24 Saatte en düşük: {data['LOW24HOUR']}
Saatlik hacim: {data['VOLUMEHOURTO']}
@Coded by: gelistirici
'''
        return content
    except:
        return False

while True:
    for coin in coins:
        content = coin_price(coin)
        if content:
            send_messsage(content)
            if send_messsage:
                print(f"{coin}USD Paritesi sunucuda paylaşıldı!")
            else:
                print(f"Bir sorunla karşılaşıldı! Coin: {coin}")

    print(f"\nBeklemeye alındı: {delay} saniye...\n")
    time.sleep(delay)
