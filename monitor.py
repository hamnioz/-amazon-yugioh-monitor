import requests

from bs4 import BeautifulSoup

URL = "https://www.amazon.co.jp/dp/B0H62FPQ4S"

headers = {

    "User-Agent": "Mozilla/5.0"

}

response = requests.get(URL, headers=headers)

html = response.text

print(html[:500])