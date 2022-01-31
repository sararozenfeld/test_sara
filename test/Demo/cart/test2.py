import requests
import unittest
from urllib.parse import urlencode
# from jsonpath_ng import parse
# from lxml import html


class TestsCatalog(unittest.TestCase):

    def test_get_catalogue_size(self):
        # GET http://catalogue.sock-shop/catalogue/size (endp 33)
        qstr = '?' + urlencode({'tags': ''})
        resp = requests.get("http://catalogue.sock-shop" + '/catalogue/size' + qstr)
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert resp.elapsed.total_seconds() < 0.0000307979170558726 # this is based on in-cluster average response time
