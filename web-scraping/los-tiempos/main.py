from utils import get, join_urls
from bs4 import BeautifulSoup

URL = "https://www.lostiempos.com/"

# Obtener el HTML puro como string
content = get(URL)
# Pasar el string HTML  a BeautifulSoup (bs4 lo interpreta y ahora se 
# puede usar como un objeto para realizar todo tipo de consultas)
soup = BeautifulSoup(content, "html.parser")

# Titulo del sitio
title = soup.title.get_text()

print(title)

# Listar todas las urls del sitio
links = soup.find_all("a")
for link in links:
  url = link["href"]
  if  not ("http" in url):
    print(join_urls(URL, url))
  else: 
    print(url)


# Ver los títulos de las noticias en el sitio
news = soup.find_all("div", { 
  "class": "noticia-paywall1"
})
news = soup.select(".noticia-paywall1")
print(len(news))

for item in news:
  title = item.select(".views-field-title")
  title = title[0] if len(title) else None
  if title:
    print(title.get_text())


