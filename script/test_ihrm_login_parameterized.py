import unittest

from parameterized import parameterized

import logging
from api.login_api import LoginApi
from utils import assert_common, read_login_data


class TestIHRMLogin(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @parameterized.expand(read_login_data)
    def test01_login_success(self,mobile,password,http_code,success,code,message):
        response = self.login_api.login(mobile,password)
        logging.info("登录接口返回数据为：{}".format(response.json()))
        # 断言
        assert_common(self,response,http_code,success,code,message)



