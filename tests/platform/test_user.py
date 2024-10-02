from base64 import b64encode, b64decode
import requests
import datetime
import pytest
import string
import environment
import socket
import sys
import random
import os

from common.common import Common

class TestUser:
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
        data = cls.common_obj.login()['data']
        cls.token = data['token']
        cls.refreshToken = data['refreshToken']
        cls.url = cls.urlMap["api_url"]
        cls.folder_path = __file__

    @pytest.mark.regression
    def test_register(self):
        running_param ={}
        running_param['pcname'] = socket.gethostname()
        account = "re" + datetime.datetime.now().strftime('%H%M%S%f')[0:8]
        url = self.urlMap["api_url"] + "/service_domain/accounts"
        password = self.common_obj.encrypt(environment.password).decode("utf-8")

        headers= {
            # "origin": self.urlMap["platform_url"] ,
            "referer": self.urlMap["platform_url"] , # required field
        }

        payloads = {
            "account": account,
            "password": password,
            "confirmPassword": password,
            "device": "mobile",
            "inviteCode": "",
            "clientNonce": self.common_obj.get_nonce(),
            "currency": "CNY",
            "type": 1
        }

        response = requests.post(url, headers=headers, json=payloads)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_login(self):
        
        response = self.common_obj.login()
        
        if "token" not in response['data'].keys():
            assert False, "Login Fail"

        assert response['code'] == 0

    @pytest.mark.regression
    def test_logout(self):
        token = self.common_obj.login()['data']['token']
        response = self.common_obj.logout(token)
        assert response['code'] == 0

    @pytest.mark.regression
    def test_userinfo(self):
        testdata = self.common_obj.load_testdata(self.folder_path, sys._getframe().f_code.co_name)

        endpoint = "/service_domain/userinfo"

        headers = {
            "Authorization": "Bearer " + self.token
        }

        for key, value in testdata.items():
            response = requests.request("GET", self.url + endpoint, headers=headers)

            assert response.json()['code'] == value['expected']['code']
            assert response.json()['data']['account'] == value['expected']['data']['account']


    @pytest.mark.regression
    def test_userinfo_update(self):
        endpoint = "/service_domain/userinfo"

        headers = {
            "Authorization": "Bearer " + self.token
        }

        payloads = {
            "gender": "MALE",
            "birthday": "1983-01-01",
            "pwdPromptType": 1, 
            "pwdPromptAnswer": "1234qwer", 
            "billingPassword": "",
            "oldBillingPassword": "", 
            "nickName": "autobot", 
            "name": "",
            "familyName": "",
            "ownName": "",
            "avatar": 19,
            "mode": "",
            "currency": "CNY", 
            "clientNonce": self.common_obj.get_nonce(), 
            "email": "",
            "phone": "",
            "livingCountry": "",
            "livingAddress": ""
        }

        response = requests.request("PUT", self.url + endpoint, headers=headers, json=payloads)

        assert response.json()['code'] == 0


    @pytest.mark.regression
    def test_refreshToken(self):
        endpoint = "/service_domain/refreshToken"

        headers = {
            "Authorization": "Bearer " + self.token,
            "apptype": "2",
            "referer": self.urlMap['platform_url'],
            "x-uuid": self.common_obj.general_uuid()
        }

        payload = {
            "refreshToken": self.refreshToken
        }

        response = requests.request("POST", self.url + endpoint, headers=headers, json=payload)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_checkToken(self):
        testdata = self.common_obj.load_testdata(self.folder_path, sys._getframe().f_code.co_name)
        endpoint = "/service_domain/accounts/checkToken"

        for key, value in testdata.items():

            params = value['payload']

            url = self.common_obj.add_url_params(self.url + endpoint, params)
            response = requests.request("GET", url)

            assert response.json()['code'] == value['expected']['code']
            assert response.json()['data']['result'] == value['expected']['data']['result']
        
        params['token'] = "Bearer " + self.token
        url = self.common_obj.add_url_params(self.url + endpoint, params)
        response = requests.request("GET", url)

        assert response.json()['code'] == 0
        assert response.json()['data']['result'] == True

    @pytest.mark.regression
    def test_accountExist(self):
        testdata = self.common_obj.load_testdata(self.folder_path, sys._getframe().f_code.co_name)
        endpoint = "/service_domain/accounts"

        headers = {
            "referer": self.urlMap['platform_url']
        }

        for key, value in testdata.items():

            params = value['payload']

            url = self.common_obj.add_url_params(self.url + endpoint, params)
            response = requests.request("GET", url, headers=headers)

            assert response.json()['code'] == value['expected']['code']
            assert response.json()['data']['isExist'] == value['expected']['isExist']

    @pytest.mark.regression
    def test_tokenExtension(self):

        headers = {
            "Authorization": "Bearer " + self.token,
        }

        url = self.urlMap['api_url'] + "/service_domain/token/extension"

        response = requests.put(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.trytest
    def test_accountValidation(self):
        endpoint = "/service_domain/accounts/validation"

        headers = {
            "Authorization": "Bearer " + self.token,
            "referer": self.urlMap['platform_url']
        }
        
        params = {
            "account": "autobot0001",
            "billingPassword": "E6QYv3m+pEFL5tu6Iv2O+JtmqgpI/1meVGeB/ghNDuHrkjPmftvtM7YHwsFzo7klx4lis3awCTksIS+GuMxO6ObY+KSNj9A6sNDl31WutwvC+xML82zXuyKR2s3EFQ4+JQNxiTtRWYgzX5xEFpfUgEOfqS9rwLnhRVAriiP5zIs=",
            "clientNonce": self.common_obj.get_nonce()
        }

        url = self.common_obj.add_url_params(self.url + endpoint, params)

        response = requests.get(url, headers=headers)

        print(response.json())

    @pytest.mark.regression
    def test_userChangePassword(self):
        token = self.token
        headers = {
            "Authorization": "Bearer " + token
        }

        endpoint = "/service_domain/password"

        payload = {
            "oldPassword": "RR2W/3TfZfJbZ2QJzejZuvwG7EHl2/sdkj7cdU00jX4Ff72mrQabDFA8BD5b8nIbvw1BUtz+l1Z7h0unStDlAB63ovSy7SoADfVmiEYdZDPcvN3xAJqzoEsFX74823H/rDxXkvndfg56npU2B085HWmL1yUe/x/giipPudP92WM=",
            "password": "GeO+vcbApJpoCnr5MiN7Vx1LE5Gdb50H1H5mlVc83v1J1CF+gDtjIpB3JcdYFAvQuNI5khSTgd4LkyJK/94VLiIi94WPp/Gc3YipR9A7bj7tN3XEMxTU60RyLdIxtaFHvY/MUnEX8J+oAZbkfV02zNnKnC7PbLPNk/H8dhM5NbE=",
            "confirmPassword": "S7sRMPqNbVTDb2AmDiveiKfDSEN2j/G0ogY1dAdOxz89rwbiyXHX25jmU18gZCf2vLe8PMz6gqbBW2CcM3mRIXL0sT1Y+IbhsVM4ZWoKat1RVGiJouEvhclIXOmxezMnd0ZEUX3a3apSbIqmLY9gg5ql+zJdJWWeVK3g6yJu9S0=",
            "clientNonce": self.common_obj.get_nonce()
        }

        response = requests.request("PUT", self.url + endpoint, headers=headers, json=payload)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_iplimitcheck(self):

        headers = {
            "referer": self.urlMap['platform_url']
        }

        url = self.urlMap['api_url'] + "/service_domain/iplimitcheck"

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_avatar(self):

        headers = {
            "Authorization": "Bearer " + self.token,
        }

        payload = {
            "avatar" : 19
        }

        url = self.urlMap['api_url'] + "/service_domain/userinfo/avatar"

        response = requests.put(url, headers=headers, json=payload)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_summary(self):

        headers = {
            "Authorization": "Bearer " + self.token,
        }

        today = datetime.datetime.today()

        time_change = datetime.timedelta(days=30) 
        new_time  = today - time_change

        startDate = str(new_time.year) + "-" + str(new_time.month).zfill(2) + "-" + str(new_time.day).zfill(2)
        endDate = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2)

        url = self.urlMap['api_url'] + "/service_domain/summary/v2?startDate=" + startDate + "&endDate=" + endDate

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getNonce(self):

        payload = {
            "imageWidth": 500, 
            "imageHeight": 300, 
            "jigsawWidth": 50,  
            "jigsawHeight": 50,
        }

        url = self.urlMap['api_url'] + "/service_domain/nonce"

        response = requests.post(url, json=payload)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getSMSInfo(self):

        headers = {
            "referer": self.urlMap['platform_url']
        }

        url = self.urlMap['api_url'] + "/service_domain/accounts/phone"

        params = {
            "account": "autobot0001",
            "type": 1,

        }
        url = self.common_obj.add_url_params(url, params)
        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userCommunicationSoftware(self):

        headers = {
            "referer": self.urlMap['platform_url'],
            "currency": "CNY"
        }

        url = self.urlMap['api_url'] + "/service_domain/communicationSoftware"

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userHasBillingPassword(self):
        endpoint = "/service_domain/hasBillingPassword"

        headers = {
            "referer": self.urlMap['platform_url'],
        }

        params = {
            "account": "autobot0001"
        }

        url = self.common_obj.add_url_params(self.url + endpoint, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0


    @pytest.mark.regression
    def test_userChangeBTCDisplayUnit(self):
        endpoint = "/service_domain/btc/display-unit"

        headers = {
            "Authorization": "Bearer " + self.token,
            "referer": self.urlMap['platform_url'],
        }

        payload = {
            "bitcoinDisplayUnit" : "uBTC"
        }

        response = requests.request("PUT", self.url + endpoint, headers=headers, json=payload)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userListThirdpartyLoginMethods(self):
        endpoint = "/service_domain/listThirdpartyLoginMethods"

        headers = {
            "referer": self.urlMap['platform_url'],
        }

        response = requests.request("GET", self.url + endpoint, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userEmailOtpSetting(self):
        endpoint = "/service_domain/email/otpSetting"

        headers = {
            "referer": self.urlMap['platform_url'],
        }

        response = requests.request("GET", self.url + endpoint, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getAnnouncementList(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        url = self.urlMap['api_url'] + "/service_domain/announcement/list?publishPlatform=1"

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getAnnouncementDomainList(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        url = self.urlMap['api_url'] + "/service_domain/announcement/domain/list?publishPlatform=1"

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getAnnouncementUpdateList(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        url = self.urlMap['api_url'] + "/service_domain/announcement/update/list?publishPlatform=1"

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getMessageUnreadCount(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "type": 1
        }

        url = self.urlMap['api_url'] + "/service_domain/message/unreadCount"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getMessageList(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "type": 1,
            "cursor": ""
        }

        url = self.urlMap['api_url'] + "/service_domain/message/list"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getMessageDetail(self):
        endpoint = "/service_domain/message/detail"

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "messageId": "33576"
        }

        url = self.url + endpoint

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0


    @pytest.mark.regression
    def test_deleteMessage(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }
        	
        payload = {
            "messageIds": "4,11"
        }

        url = self.urlMap['api_url'] + "/service_domain/message/messages"

        response = requests.delete(url, headers=headers, json=payload)

        assert response.json()['code'] == 0


    @pytest.mark.regression
    def test_getMessageListPaging(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "type": 0,
            "pageNum": 1,
            "pageSize": 10
        }

        url = self.urlMap['api_url'] + "/service_domain/message/list/paging"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getMessageListPaging(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        params = {
            "appType": 2,
            "pageSize": 10,
            "timeRange": 0,
        }

        url = self.urlMap['api_url'] + "/service_domainMasters"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getGuanggaos(self):

        params = {
            "device": 3,
            "currency": "CNY",
        }

        headers = {
            "referer": self.urlMap['platform_url']
        }

        url = self.urlMap['api_url'] + "/service_domain/guanggaos"

        url = self.common_obj.add_url_params(url, params)

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getPromotionBrTriggering(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        url = self.urlMap['api_url'] + "/service_domain/br/triggering"

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getAgentPromotionCode(self):

        url = self.urlMap['api_url'] + "/service_domain/agent/promotionCode"

        response = requests.get(url)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_getPromotionRewardNotificationsUnread(self):

        headers = {
            "Authorization": "Bearer " + self.token
        }

        url = self.urlMap['api_url'] + "/service_domain/reward/notifications/unread"

        response = requests.get(url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_passwordNotify(self):
        testdata = self.common_obj.load_testdata(self.folder_path, sys._getframe().f_code.co_name)
        endpoint = "/service_domain/password/notify"

        headers = {
            "Authorization": "Bearer " + self.token,
            "referer": self.urlMap['platform_url']
        }

        for key, value in testdata.items():
            response = requests.request("GET", self.url + endpoint, headers=headers)

            assert response.json()['code'] == value['expected']['code']

    @pytest.mark.regression
    def test_userTigerSystemConfig(self):
        endpoint = '/service_domain/tiger-system/config'

        headers= {
            "referer": self.urlMap['platform_url'],
        }

        params = {
            "terminal": 1
        }
        
        url = self.common_obj.add_url_params(self.url + endpoint, params)

        response = requests.request("GET", url, headers=headers)
        
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userMerchantSetting(self):
        endpoint = '/service_domain/merchantSetting'

        headers= {
            "referer": self.urlMap['platform_url'],
        }

        response = requests.request("GET", self.url + endpoint, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userMerchantSettingAgent(self):
        endpoint = '/service_domain/merchantSetting/agent'

        headers= {
            "referer": self.urlMap['platform_url'],
        }

        response = requests.request("GET", self.url + endpoint, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userExpertKey(self):
        endpoint = '/service_domain/expert/key'

        headers= {
            "referer": self.urlMap['platform_url'],
            "Authorization": "Bearer " + self.token
        }

        response = requests.request("GET", self.url + endpoint, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userMessageSettings(self):
        endpoint = '/service_domain/message/settings'

        headers= {
            "Authorization": "Bearer " + self.token
        }

        response = requests.request("GET", self.url + endpoint, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userStakeholdersSwitch(self):
        endpoint = '/service_domain/stakeholders/switch'

        headers= {
            "referer": self.urlMap['platform_url']
        }

        params = {
            "currency": "CNY"
        }

        url = self.common_obj.add_url_params(self.url + endpoint, params)

        response = requests.request("GET", url, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userStakeholdersSwitch(self):
        endpoint = '/service_domain/vipLevel'

        headers= {
            "referer": self.urlMap['platform_url']
        }

        response = requests.request("GET", self.url + endpoint, headers=headers)
        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userDownloadAppUrls(self):
        endpoint = '/service_domain/download/app/urls'

        headers= {
            "referer": self.urlMap['platform_url']
        }

        response = requests.request("GET", self.url + endpoint, headers=headers)

        assert response.json()['code'] == 0

    @pytest.mark.regression
    def test_userListThirdPartyLoginMethods(self):
        endpoint = '/service_domain/listThirdpartyLoginMethods'

        headers= {
            "referer": self.urlMap['platform_url']
        }

        response = requests.request("GET", self.url + endpoint, headers=headers)
        assert response.json()['code'] == 0
