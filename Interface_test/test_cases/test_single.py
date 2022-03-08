import unittest
import json
import logging
from common.do_excel import DoExcel
from common.project_path import test_data_path, conf_path
from common.find_key import find_key
from common.get_header import get_header
from common.http_request import HttpRequest
from ddt import ddt, data
from common.login_token import login_token
from common.read_config import ReadConfig

test_data = DoExcel(test_data_path, 'single').read_data('CASE')  # 获取测试数据


@ddt
class TestSingle(unittest.TestCase):
    @data(*test_data)
    def test_cases(self, case):  # 执行应付管理模块的测试用例
        # 测试报告的用例描述
        self.describe = case.get('Title')
        environment = ReadConfig(conf_path).get_data('ENV', 'environment')  # 获取测试环境
        token = login_token.get_token(environment)  # 获取token
        url = ReadConfig(conf_path).get_data('URL', 'login_url')  # 获取url地址
        method = case['Method']
        # 获取请求参数
        params = case.get('Params')
        # 处理Headers值
        headers = get_header(case['Headers'], token)
        # 发起测试
        logging.info('-------正在测试【{}】模块里面第【{}】条测试用例：【{}】'.format(case['Module'], case['CaseId'], case['Title']))
        logging.info('-------接口URL:{}'.format(url))
        logging.info('-------接口入参:{}'.format(params))
        logging.info('-------请求方式:{}'.format(method))
        logging.info('-------请求头headers:{}'.format(headers))
        logging.info('-------预期结果:{}'.format(case["ExpectedResult"]))
        res = HttpRequest().http_request(method, url, params.encode(), headers=headers)  # 传参
        # 打印响应数据
        print("响应数据：" + res.text)
        try:
            for key, value in json.loads(case.get('ExpectedResult')).items():
                if isinstance(value, str):
                    self.assertIn(value, find_key(res.json(), key))
                else:
                    self.assertEqual(value, find_key(res.json(), key))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
