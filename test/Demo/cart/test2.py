import requests
import unittest
from urllib.parse import urlencode
# from jsonpath_ng import parse
# from lxml import html

url_payment_sock_shop = "http://payment.sock-shop"

url_catalogue_sock_shop = "http://catalogue.sock-shop"

class Tests(unittest.TestCase):

    def test_get_catalogue(self, size=None):
        # GET http://catalogue.sock-shop/catalogue (endp 8)
        size = '5' if size is None else size
        qstr = '?' + urlencode({
            'size': size
        })
        resp = requests.get(url_catalogue_sock_shop + '/catalogue' + qstr)
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert parse("$[*].tag[*]").find(resp.json())
        # assert resp.elapsed.total_seconds() < 0.00916664752775956 # this is based on in-cluster average response time


    def test_get_health(self):
        # GET http://payment.sock-shop/health (endp 15)
        resp = requests.get(url_payment_sock_shop + '/health')
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert parse("$.health[*].status").find(resp.json())[0].value == "OK"
        # assert resp.elapsed.total_seconds() < 0.00031989608030705426 # this is based on in-cluster average response time


    def test_post_paymentAuth(self, json_payload=None):
        # POST http://payment.sock-shop/paymentAuth (endp 527)
        json_payload = {   'address': {   'city': 'Glasgow',
                           'country': 'United Kingdom',
                           'id': None,
                           'number': '246',
                           'postcode': 'G67 3DL',
                           'street': 'Whitelees Road'},
            'amount': 22.99,
            'card': {   'ccv': '958',
                        'expires': '08/19',
                        'id': None,
                        'longNum': '5544154011345918'},
            'customer': {   'addresses': [],
                            'cards': [],
                            'firstName': 'User',
                            'id': None,
                            'lastName': 'Name',
                            'username': 'user'}} if json_payload is None else json_payload
        headers = {
            'accept': 'application/json', 
            'x-span-name': 'http:/paymentAuth'
        }
        resp = requests.post(url_payment_sock_shop + '/paymentAuth', json=json_payload, headers=headers)
        resp.raise_for_status()
        


        # assert resp.status_code in [200]
        # assert resp.elapsed.total_seconds() < 0.0012200279934006008 # this is based on in-cluster average response time
