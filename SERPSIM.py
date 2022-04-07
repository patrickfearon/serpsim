import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.co.uk/news'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

metas = soup.find_all('meta')

print ("Title of the website is : ")
for title in soup.find_all('title'):
    print(title.get_text())

print ([ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ])



