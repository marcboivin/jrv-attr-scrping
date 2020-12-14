import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from urllib.parse import urlencode
import json
import requests

params = {
            'key': 'AIzaSyCCO9y4jQhb5BpMHDBYrgIHNyZJM9NMELk',
            'cx' : 'db59bff0fc9813531',
            'q' : 'SCN INDUSTRIEL	SEA431'
        }

base_url = 'https://www.googleapis.com/customsearch/v1'

target_url = "{0}?{1}".format(base_url, urlencode(params))

s = requests.Session()
s.headers.update({'referer': 'http://localhost/'})
response = s.get(target_url)

data = response.json()

from pprint import pprint

pprint(data['items'][0])

# referer localhost

# Google search API 
# Trouver le produit
# Ouvrir la page Chrome headless
# Chercher la div produit qui fait le plus de bon sang
# Trouver le SKU
# Extrire les infos produits: surtout table tou tt td

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)  
#driver.get(target_url)

print(driver.page_source)

driver.close()




