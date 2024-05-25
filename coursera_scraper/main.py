#  Using the find_all method for bs objects we can get a list of tags, not just the first occurence
from turtle import title
from bs4 import BeautifulSoup
from urllib.request import urlopen

from utils.urls import url2
from utils.functions import get_title

#html = urlopen('https://www.linkedin.com')

# bs = BeautifulSoup(html.read(), 'html.parser')

#name_list = bs.findAll('span', {'class': 'green'})
#for name in name_list:
    #print(name.get_text())

title = get_title(url2)
print(title)