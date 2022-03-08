import time
import unittest
from BeautifulReport import BeautifulReport
from common.project_path import report_path
from common.send_main import mail
from test_cases.test_rst import TestRst
from test_cases.test_single import TestSingle

# 新建一个测试集
suite = unittest.TestSuite()

# 添加测试用例
suite.addTest(unittest.makeSuite(TestSingle))  # 单接口测试
suite.addTest(unittest.makeSuite(TestRst))  # 流程测试

# 定义测试报告文件的名称
report_name = "test_report_{}".format(time.strftime("%Y%m%d%H%M"))

# 创建BeautifulReport的对象
brt = BeautifulReport(suite)

# 使用BeautifulReport对象所提供的方法来批量运行测试用例并且生成测试报告
brt.report(filename=report_name, description="测试报告", log_path=report_path)

# 测试报告名称
filename = report_path + '/' + report_name + '.html'

# 收件人邮箱
addressee = ['3397188079@qq.com']

# 发送测试报告到邮箱里
mail(filename, addressee)
