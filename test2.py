import requests
import unittest
from urllib.parse import urlencode
# from jsonpath_ng import parse
# from lxml import html


class Tests(unittest.TestCase):

    def test_get_catalogue_itemId(self, itemId=None):
        # GET http://catalogue.sock-shop/catalogue/{itemId} (endp 149)
        itemId = '510a0d7e-8e83-4193-b483-e27e09ddc34d' if itemId is None else itemId
        resp = requests.get("http://catalogue.sock-shop" + f'/catalogue/{itemId}')
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert parse("$.name").find(resp.json())[0].value == "SuperSport XL"
        # assert resp.elapsed.total_seconds() < 0.004734253766449238 # this is based on in-cluster average response time


    def test_get_carts_cartId_items(self, cartId=None, x_span_name=None):
        # GET http://carts.sock-shop/carts/{cartId}/items (endp 147)
        cartId = '61f1617008135b0001709e6d' if cartId is None else cartId
        x_span_name = 'http:/carts/61f1617008135b0001709e6d/items' if x_span_name is None else x_span_name
        resp = requests.get("http://carts.sock-shop" + f'/carts/{cartId}/items', headers={'accept': 'application/json', 'x-span-name': x_span_name})
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert parse("$[*].id").find(resp.json())
        # assert resp.elapsed.total_seconds() < 0.026840168540998896 # this is based on in-cluster average response time
