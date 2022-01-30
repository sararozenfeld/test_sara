import requests
import unittest
from urllib.parse import urlencode
# from jsonpath_ng import parse
# from lxml import html


class Tests3(unittest.TestCase):

    def test_get_catalogue(self, size=None, tags=None):
        # GET http://catalogue.sock-shop/catalogue (endp 20)
        size = '5' if size is None else size
        tags = '' if tags is None else tags
        qstr = '?' + urlencode({'page': '1', 'size': size, 'sort': 'id', 'tags': tags})
        resp = requests.get("http://catalogue.sock-shop" + '/catalogue' + qstr)
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert resp.elapsed.total_seconds() < 0.003887970125795556 # this is based on in-cluster average response time


    def test_get_catalogue_id(self, id_=None):
        # GET http://catalogue.sock-shop/catalogue/{id} (endp 19)
        id_ = 'a0a4f044-b040-410d-8ead-4de0446aec7e' if id_ is None else id_
        resp = requests.get("http://catalogue.sock-shop" + f'/catalogue/{id_}')
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert resp.elapsed.total_seconds() < 0.0013226794138109933 # this is based on in-cluster average response time
