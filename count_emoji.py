import requests
from bs4 import BeautifulSoup


url = 'https://emojipedia.org/search/'

list_of_categories = ["nature", "music", "science"]

for category in list_of_categories:
  params = {'q': category}
  response = requests.get(url, params=params)
  soup = BeautifulSoup(response.text, 'html.parser')
  elements = soup.find('ol', class_='search-results')
  items = elements.find_all('a')
  list_of_emojis = []
  count = 0
  for item in items:
    list_of_emojis.append((item.text)[:2])
    count +=1
  print(f'The {category} category has {count} emojis.')
  print(list_of_emojis)