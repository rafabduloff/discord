import time
import requests

url = "https://t2-gifts.ru/"

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Сайт {url} работает.")
        else:
            print(f"Сайт {url} недоступен. Статус код: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения к сайту {url}: {e}")

while True:
    check_website(url)
    time.sleep(5)
