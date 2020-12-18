import requests
from bs4 import BeautifulSoup


def get_words():
    URL = 'https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    my_section = soup.find("section", {"class": "col-md-12"})

    words = (str(my_section).split('</p>')[1][4:].split("<br/>"))

    with open('words.txt', 'w', encoding='utf8') as file:
        for word in words:
            file.write(word + '\n')
