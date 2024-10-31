import pandas as pd
import numpy as np
import requests as req
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Forbes_list_of_the_world%27s_highest-paid_athletes'
page = req.get(url)
page_content_text = page.text


soup = BeautifulSoup(page_content_text, 'html.parser')

div_with_tables_through_id = soup.find('div', id='mw-content-text')



#TODO
# 1. Get all P tags -> Loop over them and extract date from content e.g The 2024 list Forbes
# 2. Split everything and map to a dictionary using numbers as index
# 3. 