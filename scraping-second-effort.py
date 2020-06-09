import requests
from bs4 import BeautifulSoup
import json 
import re


source = requests.get('https://starcitygames.com/shop/singles/english/theros-beyond-death/')
soup = BeautifulSoup(source.text, 'html.parser')
paginator = soup.find_all('a', class_='pagination-link')
pattern = re.compile('&page=(.*)')
pages = {}
for child in paginator:
  cur_page = pattern.search(child.get('href'))
  result = str(re.findall(r'page=\w+', cur_page.group(0)))
  cur_page = str(result).replace("['page=","").replace("']","")
  pages[cur_page] = cur_page

for page in pages: 
  page_url = 'https://starcitygames.com/shop/singles/english/theros-beyond-death/?sort=alphaasc&page='+page
  product_list = soup.select('tr[data-id]')
  price = soup.find_all('p', class_='product-price sort-name')

  for product in product_list:  
    print(product['data-id'])
    print(product['data-name'])
    json_source = requests.get('https://newstarcityconnector.herokuapp.com/eyApi/products/{}/'.format(product['data-id']))
          #print(json_source)
    json_data = json.loads(json_source.text)

    print(json_data['response']['data']['price'])
