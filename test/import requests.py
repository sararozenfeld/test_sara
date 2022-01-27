import requests
import unittest
from urllib.parse import urlencode
# from jsonpath_ng import parse
# from lxml import html


class Tests(unittest.TestCase):

    def test_get_health(self):
        # GET http://catalogue.sock-shop-p/health (endp 6)
        resp = requests.get("http://catalogue.sock-shop-p" + '/health')
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert parse("$.health[*].status").find(resp.json())[0].value == "OK"
        # assert resp.elapsed.total_seconds() < 0.00034237665738286443 # this is based on in-cluster average response time
