# Real-World Example: Multithreading for I/0-bound Tasks
# Scenario: Web Scraping
# Web scraping often involves making numerous network requests to fetch web pages.
#These tasks are I/0-bound• because they spend a lot of time waiting for responses from servers.
# Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.

import threading
import requests
from bs4 import BeautifulSoup

url = [
    "https://python.langchain.com/docs/introduction/",
    "https://python.langchain.com/docs/tutorials/",
    "https://python.langchain.com/docs/concepts/"
]

def fetch(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    print(f"Fetched {len(soup.text)} characters in {url}")

threads = []

for u in url:
    thread = threading.Thread(target=fetch,args=(u,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all web pages fetched")
