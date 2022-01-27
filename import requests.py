import requests
import unittest
from urllib.parse import urlencode
# from jsonpath_ng import parse
# from lxml import html


class Tests(unittest.TestCase):

    def test_get_carts_cartId_items(self, cartId=None):
        # GET http://carts.sock-shop-no-p/carts/{cartId}/items (endp 9)
        cartId = 'Jwu6OzyhQN-s83YFlHSA6eC2NfU7q1Dj' if cartId is None else cartId
        resp = requests.get("http://carts.sock-shop-no-p" + f'/carts/{cartId}/items')
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert parse("$[*].id").find(resp.json())
        # assert resp.elapsed.total_seconds() < 0.004474692379085791 # this is based on in-cluster average response time
