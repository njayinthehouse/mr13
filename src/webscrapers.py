# This should define functions to scrape the HTML of websites and the images which are the pages.

from bs4 import BeautifulSoup
import requests

# UrlString -> BeautifulSoup
def get_soup(url):
    return BeautifulSoup(requests.get(url).content, 'html.parser')

# UrlString * PathString -> void
def get_image(url, path):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r:
                f.write(chunk)