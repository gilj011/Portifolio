from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from sys import exit

print("digite o site que quer crfawlar")
# link = input()


def main():
#   conversor = link.replace(" ", "+")
  try:
    html = urlopen("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=playstation+5+adsadasd&_sacat=0&LH_TitleDesc=0&_odkw=playstation+5&_osacat=0")
  except:
    main()

  res = BeautifulSoup(html.read(), "html5lib", from_encoding='utf-8')
  precos = res.findAll("span", {"class": "s-item__price"})
  nomes = res.findAll("div",{"class": "s-item__title"})
#   print(precos[0].getText())
#   print(nomes[0].getText())

  i = 0
  while i < len(nomes):
    try:
      print(nomes[i].getText())

    except:
      print("Nome nao encontrado")

    try:
      print(precos[i].getText())
    except:
      print("Preco nao encontrado")
    i += 1

  sleep(100)

main()
 