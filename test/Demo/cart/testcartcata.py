import requests
import unittest
from urllib.parse import urlencode
# from jsonpath_ng import parse
# from lxml import html


class Tests(unittest.TestCase):

    def test_get_carts_customerId_items(self, customerId=None):
        # GET http://carts.sock-shop/carts/{customerId}/items (endp 5)
        customerId = '57a98d98e4b00679b4a830b2' if customerId is None else customerId
        resp = requests.get("http://carts.sock-shop" + f'/carts/{customerId}/items', headers={'accept': 'application/json'})
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert resp.elapsed.total_seconds() < 0.02004675091939744 # this is based on in-cluster average response time


    def test_get_catalogue(self, size=None, tags=None):
        # GET http://catalogue.sock-shop/catalogue (endp 20)
        size = '5' if size is None else size
        tags = '' if tags is None else tags
        qstr = '?' + urlencode({'page': '1', 'size': size, 'sort': 'id', 'tags': tags})
        resp = requests.get("http://catalogue.sock-shop" + '/catalogue' + qstr)
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert resp.elapsed.total_seconds() < 0.003887970125795556 # this is based on in-cluster average response time
