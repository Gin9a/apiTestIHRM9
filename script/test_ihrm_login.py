import unittest
import app,logging
from api.login_api import LoginApi
from utils import assert_common
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

    def test01_login_success(self):
        response = self.login_api.login("13800000002","123456")
        logging.info("登陆接口返回数据为:{}".format(response.json()))
        # 断言
        # self.assertEqual(200,response.status_code)
        # self.assertEqual(True,response.json().get("success"))
        # self.assertEqual(10000,response.json().get("code"))
        # self.assertEqual("操作成功！",response.json().get("message"))
        assert_common(self,response,200,True,10000,"操作成功！")

        # 获取json数据
        jsonData = response.json()
        # 拼接token组成全局变量
        token = "Bearer " + jsonData.get('data')
        # 把token保存到全局变量app.py中
        # 注意，要先在app中创建HEADERS变量才能保存
        app.HEADERS = {"Content-Type":"application/json","Authorization":token}
        logging.info("保存的登陆token和Content_Type：{}".format(app.HEADERS))


    def test02_mobile_error(self):
        response = self.login_api.login("13890000001","123456")
        logging.info("登陆接口返回数据为:{}".format(response.json()))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test03_password_error(self):
        response = self.login_api.login("13800000002","error")
        logging.info("登陆接口返回数据为:{}".format(response.json()))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_none_params(self):
        response = self.login_api.login_none_params()
        logging.info("登陆接口返回数据为:{}".format(response.json()))
        assert_common(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    def test05_mobile_none(self):
        response = self.login_api.login("", "error")
        logging.info("登陆接口返回数据为:{}".format(response.json()))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test06_password_none(self):
        response = self.login_api.login("13800000002", "")
        logging.info("登陆接口返回数据为:{}".format(response.json()))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test07_extra_params(self):
        response = self.login_api.login_extra_params()
        logging.info("登陆接口返回数据为:{}".format(response.json()))
        assert_common(self, response, 200, True, 10000, "操作成功！")

    def test08_less_params(self):
        response = self.login_api.login_less_paramse()
        logging.info("登陆接口返回数据为:{}".format(response.json()))
        assert_common(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")











