from bs4 import BeautifulSoup
import requests
import re

site = requests.get("https://pokemondb.net/pokedex/all")
soup = BeautifulSoup(site.text, "html.parser")

tabelaPoke = soup.find("table", attrs={"id":"pokedex"})

corpo = soup.tbody

#f = open("pokemons.csv", "w")
#f.write('Id, Nome, Tipo1, Tipo2, Total, Hp, Attack, Defense, Sp_attack, Sp_def, Speed\n')
#f.close()

def gravar(id, nome, tipo1, tipo2, total, hp, attack, defense, sp_attack, sp_def, speed):
    f = open("pokemons.csv", "a", encoding="utf-8")
    f.writelines('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n'.format(
        id, nome, tipo1, tipo2, total, hp, attack, defense, sp_attack, sp_def, speed))
    f.close()

for x in corpo.findAll("tr"):
    tags = x.findAll("td")
    valores = [y.text for y in tags]
    
    if len(re.findall(r'\w+',valores[2]))>1:
        tps = valores[2].split()
        tp1=tps[0]
        tp2=tps[1]
        
        valores.pop(2)
        valores.insert(2,tp1)
        valores.insert(3,tp2)  
    else:
        valores.insert(3,'-')      
    gravar(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5], valores[6], valores[7], valores[8], valores[9], valores[10])