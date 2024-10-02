from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.PublicKey import RSA

from base64 import b64encode, b64decode

import requests
import environment
import json
import re
import random


class Common:
    urlMap = {}

    def __init__(self, get_url):
        self.urlMap = get_url

    def login(self):

        url = self.urlMap['api_url'] + "/service_domain/token"

        pwd = self.encrypt(environment.password).decode("utf-8")

        header= {
            "origin": self.urlMap['platform_url'],
            "referer": self.urlMap['platform_url'],
            "apptype": "16",
        }
        payload = {
            "account": environment.user_account,
            "password": pwd,
            "device": "mobile",
            "clientNonce": "None"
        }

        r = requests.post(url, json=payload, headers= header)

        return r.json()
    

    def logout(self, token):

        url = self.urlMap['api_url'] + "/service_domain/token"

        header= {
            "Authorization": "Bearer " + token
        }

        r = requests.delete(url, headers= header)

        return r.json()

    def encrypt(self, text):
        s = str.encode(text)
        rsa_public_key = RSA.importKey(environment.public_key)
        rsa_public_key = PKCS1_v1_5.new(rsa_public_key)
        encrypted_text = rsa_public_key.encrypt(s)
        encrypted_text = b64encode(encrypted_text)
        return encrypted_text

    def decrypt(self, text):
        rsa_private_key = RSA.importKey(environment.private_key)
        rsa_private_key = PKCS1_v1_5.new(rsa_private_key)
        decrypted_text = rsa_private_key.decrypt(b64decode(text), 0)
        return decrypted_text

    def add_url_params(self, url, param):
        if param == "":
            return url

        url += "?"

        for item in param:
            if param[item] != "":
                url += item + "=" + str(param[item])+ "&"

        return url[:-1]
    
    def get_nonce(self):

        payload = {
            "imageWidth": 500, 
            "imageHeight": 300, 
            "jigsawWidth": 50,  
            "jigsawHeight": 50,
        }

        url = self.urlMap['api_url'] + "/service_domain/nonce"

        response = requests.post(url, json=payload)

        return response.json()['data']['clientNonce']
    
    def general_uuid(self):
        return ''.join(random.choice("0123456789abcdef") for i in range(32))
    
    def load_testdata(self, folder_name, func_name):
        try:
            folder_name = re.sub("/tests/", "/testdata/", re.sub("test_", "", re.sub(".py", "", folder_name)))

            if re.search("^test_", func_name):
                func_name = re.sub("^test_", "", func_name)

            with open(folder_name + "/" + func_name + ".json", "r") as file:
                testdata = json.load(file)
        
            return testdata
        except:
            print("Loading test data fail on: " + folder_name)