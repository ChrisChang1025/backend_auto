from common.common import Common

import pytest
import requests
import sys
import datetime

class TestBusiness:
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


    @pytest.mark.skip(reason="invalid token")
    def test_getGamePeriodMatchScore(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "referer": self.urlMap['platform_url']
        }

        params = {
            "iid": 8767499,
            "sid": 1
        }

        url = self.urlMap['api_url'] + "/service_domain/period-match-score"
        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        print (response.json())

    @pytest.mark.regression
    def test_productCashoutSetting(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "referer": self.urlMap['platform_url']
        }

        payload = {
            "msg": "",
            "code": 0,
            "data": {
                "platform": "",
                "cashOut": True
            }
        }

        url = self.urlMap['api_url'] + "/service_domain/setting"
        response = requests.get(url, headers=headers, json=payload)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_productSportIndexMenu(self):
        testdata = self.common_obj.load_testdata(self.folder_path, sys._getframe().f_code.co_name)
        endpoint = "/service_domain/sport/index/menu"

        headers = {
            "Authorization": "Bearer " + self.token,
            "referer": self.urlMap["platform_url"]
        }

        for key, value in testdata.items():
            response = requests.request("GET", self.url + endpoint, headers=headers)

            assert response.json()['code'] == value['expected']['code']


    @pytest.mark.regression
    def test_getBusinessMatchBulletin(self):

        today = datetime.datetime.today()
        date = str(today.year).zfill(4) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2)

        params = {
            "days": 1,
            "date": date
        }

        url = self.urlMap['api_url'] + "/service_domain/match/bulletin"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url)

        assert response.json()['code'] == 0