import logging
import unittest
import pymysql
import app
from api.emp import EmpApi
from utils import assert_common, DBUtils


class TestIHRMEmp(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.emp_api = EmpApi()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test01_add_emp(self):
        # 调用添加员工接口
        response = self.emp_api.add_emp("哪吒16","1342442123409")
        logging.info("添加员工接口返回的数据是：{}".format(response.json()))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")

        # 获取添加员工接口返回的json数据
        jsonData = response.json()
        # 获取员工id
        emp_id = jsonData.get('data').get('id')
        # 保存员工id到全局变量
        # 注意这里需要新建一个员工共id到app.py中，然后导入app
        app.EMPID = emp_id
        # 打印查看有没有保存成功
        logging.info("保存的员工ID：{}".format(app.EMPID))

    def test02_query_emp(self):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 打印
        logging.info("查询员工接口返回的数据为：{}".format(response.json()))

        # 断言响应数据
        assert_common(self,response,200,True,10000,"操作成功")

    def test03_modify_emp(self):
        # 调用修改员工接口
        response = self.emp_api.modify_emp("奥特曼")
        # 打印
        logging.info("修改员工接口返回的数据：{}".format(response.json()))
        # 断言
        assert_common(self,response,200,True,10000,"操作成功")

        # 连接数据库
        with DBUtils("182.92.81.159","readuser","iHRM_user_2019","ihrm")as db:
            # 执行查询语句
            query_sql = "select username from bs_user where id={} limit 1".format(app.EMPID)
            db.execute(query_sql)
            result = db.fetchone()
        logging.info("--------------------查询数据库中员工id为{}的username是{}".format(app.EMPID,result[0]))
        # 断言数据库中的数据
        self.assertEqual("奥特曼",result[0])


    def test04_delete_emp(self):
        # 调用删除员工接口
        response = self.emp_api.delete_emp()
        logging.info("删除员工接口返回的数据：{}".format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")


