import requests
from urllib import parse

def get(url):
  response = requests.get(url, headers={

  })
  content = response.content
  return content


def join_urls(base, url):
  return parse.urljoin(base, url)
