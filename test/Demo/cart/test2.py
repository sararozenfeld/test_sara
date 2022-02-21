import requests
import unittest
from urllib.parse import urlencode
# from jsonpath_ng import parse
# from lxml import html


class Tests(unittest.TestCase):
    
    url = "http://catalogue.sock-shop"
    
    def test_get_catalogue(self, size=None):
        # GET http://catalogue.sock-shop/catalogue (endp 8)
        size = '5' if size is None else size
        qstr = '?' + urlencode({'size': size})
        resp = requests.get(Tests.url + '/catalogue' + qstr)
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert parse("$[*].tag[*]").find(resp.json())
        # assert resp.elapsed.total_seconds() < 0.00916664752775956 # this is based on in-cluster average response time


   