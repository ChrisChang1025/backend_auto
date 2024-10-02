from base64 import b64encode, b64decode
import requests
import datetime
import pytest
import string
import environment
import socket
import sys
import random

from common.common import Common

class TestPromotion:
    common_obj = ()
    urlMap = {}
    token = ""
    url = ""
    headers = {}
    folder_path = ""

    @pytest.fixture(autouse=True)
    @classmethod
    def setup_class(cls, get_url):
        cls.urlMap = get_url
        cls.common_obj = Common(get_url)
        cls.token = cls.common_obj.login()['data']['token']
        cls.url = cls.urlMap["api_url"]
        cls.folder_path = __file__

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionBr(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "appType": 2,
            "id": 1,
        }

        url = self.urlMap['api_url'] + "/service_domain/br"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionBc(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "promotionType": 3,
            "id": 1,
        }

        url = self.urlMap['api_url'] + "/service_domain/bc"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionDz(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "appType": 2,
            "id": 1,
        }

        url = self.urlMap['api_url'] + "/service_domain/dz"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionWk(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "appType": 2,
            "id": 1,
        }

        url = self.urlMap['api_url'] + "/service_domain/wk"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionDp(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "appType": 2,
            "id": 1,
        }

        url = self.urlMap['api_url'] + "/service_domain/dp"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionGoalBrFootbal(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "id": 1,
            "appType": 2
        }

        url = self.urlMap['api_url'] + "/service_domain/goalBr/football"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionDm(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "id": 1,
            "appType": 2
        }

        url = self.urlMap['api_url'] + "/service_domain/dm"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionCompleteUserInfo(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "id": 1,
            "appType": 2
        }

        url = self.urlMap['api_url'] + "/service_domain/complete-user-info"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionCompleteUserInfo(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "id": 1,
            "appType": 2
        }

        url = self.urlMap['api_url'] + "/service_domain/complete-user-info"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.skip(reason="No promotion id")
    def test_getPromotionQualified(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "id": 1
        }

        url = self.urlMap['api_url'] + "/service_domain/qualified"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0