from turtle import title
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError



def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return e
    except URLError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError:
        return None
    return title.text

