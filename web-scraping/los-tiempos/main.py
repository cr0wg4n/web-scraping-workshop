from utils import get, join_urls
from bs4 import BeautifulSoup
import logging

URL = "https://www.lostiempos.com/"

# # Configurando un logger
# logging.basicConfig(filename="ejemplo.log", encoding="utf-8", level=logging.INFO)


# # Obtener el HTML puro como string
# content = get(URL)
# # Pasar el string HTML  a BeautifulSoup (bs4 lo interpreta y ahora se
# # puede usar como un objeto para realizar todo tipo de consultas)
# soup = BeautifulSoup(content, "html.parser")

# # Obtener título del sitio
# title = soup.title.get_text()
# print(title)

# # Listar todas las urls del sitio
# links = soup.find_all("a")
# for link in links:
#     url = link["href"]
#     if "http" in url:
#         print(url)
#     else:
#         print(join_urls(URL, url))


# # Ver los títulos de las noticias en el sitio
# news = soup.find_all("div", {"class": "noticia-paywall1"})
# news = soup.select(".noticia-paywall1")
# for item in news:
#     title = item.select(".views-field-title")
#     title = title[0] if len(title) else None
#     if title:
#         print(title.get_text().strip())


class LosTiemposPage:
    def __init__(self, url) -> None:
        self.url = url
        content = get(URL)
        self.soup = BeautifulSoup(content, "html.parser")

    def get_urls(self):
        urls = []
        links = self.soup.find_all("a")
        for link in links:
            url = link["href"]
            if "http" in url:
                urls.append(url)
            else:
                urls.append(join_urls(URL, url))
        return urls

    def get_title(self):
        return self.soup.title.get_text()

    def get_body(self):
        return

    def get_images(self):
        urls = []
        images = self.soup.find_all("img")
        for image in images:
            url = image["src"]
            if "http" in url:
                urls.append(url)
            else:
                urls.append(join_urls(self.url, url))
        return urls

losTiempos = LosTiemposPage(url=URL)

print(losTiempos.get_title())

# logging.info('Mensaje de prueba')
