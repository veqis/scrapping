from bs4 import BeautifulSoup
import requests

site = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(site.text, "html.parser")
frases = soup.findAll("span", attrs={"class":"text"})
autores = soup.findAll("small", attrs={"class":"author"})

for frase, autor in zip(frases, autores):
    print(frase.text + " - " + autor.text)