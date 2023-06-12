import requests
from bs4 import BeautifulSoup

url = 'https://emojipedia.org/search/'

list_of_categories = ["nature", "music", "science"]

emojis_by_category = {}

for category in list_of_categories:
    params = {'q': category}
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find('ol', class_='search-results')
    items = elements.find_all('li')
    list_of_emojis = []
    for item in items:
        emoji_name = item.find('a').text.strip()
        emoji_description = item.find('p').text.strip()
        list_of_emojis.append((emoji_name, emoji_description))
    emojis_by_category[category] = list_of_emojis

for category, emojis in emojis_by_category.items():
    print(f'{category} category:')
    for emoji in emojis:
        print(f'{emoji[0]}: {emoji[1]}')
    print()

