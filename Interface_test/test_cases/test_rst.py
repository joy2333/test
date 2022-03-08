import time
import unittest
import json
import logging
from common.do_excel import DoExcel
from common.project_path import test_data_path, conf_path
from common.get_header import get_header
from common.http_request import HttpRequest
from ddt import ddt, data
from common.login_token import login_token
from common.read_config import ReadConfig

test_data = DoExcel(test_data_path, 'rst').read_data('CASE')  # 获取测试数据
plan_date = time.strftime("%Y-%m-%d")  # 获取当前时间格式为：年月日
start_time = time.strftime('%Y-%m-%d 00:00:00', time.localtime(time.time()))  # 获取当天凌晨的时间格式为：年月日时分秒
end_time = time.strftime('%Y-%m-%d 23:59:59', time.localtime(time.time()))  # 获取当天最后一秒的时间格式为：年月日时分秒


@ddt
class TestRst(unittest.TestCase):
    bxn = None
    token = None
    url = None

    def setUp(self):  # 测试之前的准备工作
        environment = ReadConfig(conf_path).get_data('ENV', 'environment')  # 获取测试环境
        TestRst.token = login_token.get_token(environment)  # 获取token
        TestRst.url = ReadConfig(conf_path).get_data('URL', 'uat_url')  # 获取url地址

    def tearDown(self):
        pass

    @staticmethod
    def get_Params(params):  # 处理param
        params = json.loads(params)  # 将字符串转换为字典
        if params.get('expenseNumber') is not None:
            params['expenseNumber'] = TestRst.bxn
        params = json.dumps(params)  # 将字典转换为字符串
        return params

    @data(*test_data)
    def test_cases(self, case):  # 执行应付管理模块的测试用例

        method = case['Method']
        # 处理Params值
        params = TestRst.get_Params(case['Params'])
        # 测试报告的用例描述
        self.describe = case['Title']
        # 处理Headers值
        headers = get_header(case['Headers'], TestRst.token)
        # 发起测试
        logging.info('-------正在测试【{}】模块里面第【{}】条测试用例：【{}】'.format(case['Module'], case['CaseId'], case['Title']))
        logging.info('-------接口URL:{}'.format(TestRst.url))
        logging.info('-------接口入参:{}'.format(params))
        logging.info('-------请求方式:{}'.format(method))
        logging.info('-------请求头headers:{}'.format(headers))
        logging.info('-------预期结果:{}'.format(case["ExpectedResult"]))

        res = HttpRequest().http_request(method, TestRst.url, params.encode(), headers=headers)  # 传参
        # 打印响应数据
        print("响应数据：" + res.text)

        self.assertEqual(json.loads(case['ExpectedResult'])['msg'], res.json()['msg'])
        self.assertEqual(json.loads(case['ExpectedResult'])['code'], res.json()['code'])
        if case['CaseId'] == 1:
            TestRst.bxn = res.json().get('data')
            print(TestRst.bxn)


if __name__ == '__main__':
    unittest.main()
