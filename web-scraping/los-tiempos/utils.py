import requests
from urllib import parse
import os 
import wget

def get(url):
  response = requests.get(url, headers={

  })
  content = response.content
  return content

def join_urls(base, url):
  return parse.urljoin(base, url)

def download_file(url, name="", base_dir="./data"):
    dir_name = os.path.join(base_dir, name)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    return wget.download(url, out=dir_name)