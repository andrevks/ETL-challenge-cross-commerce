import pytest
import requests
import json
import pytest
from src.server.instance import server
from src.controllers.load import *


# @pytest.fixture(scope='session', autouse=True)
# def setup_server():
#    server.run()

def test_api_numbers():
   url = 'http://127.0.0.1:5000/api/numbers/'

   resp = requests.get(url)
   numbers = resp.json()


   print(f'\n{len(numbers)}')

   assert resp.status_code == 200
   assert resp.url == url
   assert len(numbers) == 100

def test_api_numbers_page():
   page = 1
   while True:

      url = f'http://127.0.0.1:5000/api/numbers?page={page}'
      resp = requests.get(url)
      numbers = resp.json()
      if 'numbers' in numbers:
         numbers = numbers['numbers']
         if not numbers:
            break
      if resp.status_code != 200:
         assert False
      page += 1000

   assert numbers == []

def test_api_numbers_page_and_pagesize():

   page_size = 5000
   page = 100
   url = f'http://127.0.0.1:5000/api/numbers/?page_size={page_size}&page={page}'

   resp = requests.get(url)
   numbers = resp.json()


   print(f'\n{len(numbers)}')

   assert resp.status_code == 200
   assert resp.url == url
   assert len(numbers['numbers']) == page_size

