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

class TestThirdpartyReport:
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
    
    @pytest.mark.regression
    def test_getThirdpartyReportUserOrderSummary(self):

        headers = {
            "Authorization": "Bearer " + self.token

        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "onlySport": True
        }

        url = self.urlMap['api_url'] + "/service_domain/summary"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrderCurrencySummary(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "onlySport": True,
            "dataType": 0,
            "unsettled": False
        }

        url = self.urlMap['api_url'] + "/service_domain/currencySummary"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersAll(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/all"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersSport(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": "",
            "dataType": 0,
            "timeConditionType": "BET"
        }

        url = self.urlMap['api_url'] + "/service_domain/sport"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersWgLottery(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": "",
            "dataType": 0,
        }

        url = self.urlMap['api_url'] + "/service_domain/wgLottery"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersMgSlot(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/mgSlot"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersDtSlot(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/dtSlot"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersAgFishing(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/agFishing"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersAgLive(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/agLive"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersBgLive(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/bgLive"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersKyBoard(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/kyBoard"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersAgSlot(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/ag-slot"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersEzLive(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/ezLive"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersPtSlot(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/ptSlot"

        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrders(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "betStatus": 2,
            "cursor": ""
        }

        GameList = ["jdb-slot", "pg-slot", "cq9Slot", "evoLive", "ppSlot", "ksFishing", "bsSlot", "jdbFishing", "v8Board", "rcbHorse",
                    "aeLive", "lyBoard", "30", "31", "32"]

        for item in GameList:
            url = self.urlMap['api_url'] + "/service_domain/" + item

            url = self.common_obj.add_url_params(url, params)
            response = requests.get(url, headers=headers)
            assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersPage(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "pageNum": 1,
            "pageSize": 10
        }

        GameList = ["ezLive", "ag-slot", "dtSlot", "ptSlot", "jdb-slot", "pg-slot", "cq9Slot", "evoLive", "ppSlot", "ksFishing", "bsSlot", "jdbFishing", "v8Board", "rcbHorse",
                    "aeLive", "lyBoard", "30", "31", "32", "agLive", "mgSlot", "kyBoard", "bgLive", "agFishing"]

        for item in sorted(GameList):
            url = self.urlMap['api_url'] + "/service_domain/page/" + item
            url = self.common_obj.add_url_params(url, params)
            response = requests.get(url, headers=headers)
            assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersPageSport(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "pageNum": 1,
            "pageSize": 10,
            "betStatus": 2,
            "dataType": 0,
            "timeConditionType": "BET"

        }

        url = self.urlMap['api_url'] + "/service_domain/page/sport"
        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersPageWgLottery(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "pageNum": 1,
            "pageSize": 10,
            "betStatus": 2,
        }

        url = self.urlMap['api_url'] + "/service_domain/page/wgLottery"
        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getThirdpartyReportUserOrdersPagePpSlot(self):

        headers = {
            "Authorization": "Bearer " + self.token,
            "currency": "ALL"
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=1) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2) + " 00:00:00"
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2) + " 00:00:00"

        params = {
            "startDate": startDate,
            "endDate": endDate,
            "pageNum": 1,
            "pageSize": 10,
            "betStatus": 2,
        }

        url = self.urlMap['api_url'] + "/service_domain/page/ppSlot"
        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)
        assert response.json()['code'] == 0
