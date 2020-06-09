import requests
from bs4 import BeautifulSoup
import json 
import csv
import os



pages = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11]


with open('C:/Code/scraping/Theros-Set.csv', 'a', encoding='utf-8', newline='') as f_output:
  print_csv = csv.writer(f_output)

  file_empty = os.stat('C:/Code/scraping/Theros-Set.csv').st_size == 0
  if file_empty:
    print_csv.writerow(['Product_id', 'Product_name', 'Product_price'])


    for page in pages:
      
      
      
      source = requests.get('https://starcitygames.com/shop/singles/english/theros-beyond-death/?sort=alphaasc&page={}'.format(page))

      soup = BeautifulSoup(source.text, 'html.parser')
      
      product_list = soup.select('tr[data-id]')

      for product in product_list:  
          print(product['data-id'])
          print(product['data-name'])

          json_source = requests.get('https://newstarcityconnector.herokuapp.com/eyApi/products/{}/'.format(product['data-id']))
          #print(json_source)
          json_data = json.loads(json_source.text)

          print(json_data['response']['data']['price'])

          print_csv.writerow([product['data-id'],product['data-name'],json_data['response']['data']['price']])


