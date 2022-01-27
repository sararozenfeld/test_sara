import requests
import unittest
from urllib.parse import urlencode
# from jsonpath_ng import parse
# from lxml import html


class Tests(unittest.TestCase):

    def test_get___ready(self):
        # GET http://alertmanager-main.monitoring/-/ready (endp 2)
        resp = requests.get("http://alertmanager-main.monitoring" + '/-/ready')
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert resp.elapsed.total_seconds() < 0.00036930719647210094 # this is based on in-cluster average response time
