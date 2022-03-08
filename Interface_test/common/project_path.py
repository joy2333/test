import os

# 文件的路径 放到这里
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例表格的路径
test_data_path = os.path.join(root_path, 'test_data', 'test_api.xlsx')

# 测试报告的路径
report_path = os.path.join(root_path, 'test_result', 'test_report')

# 日志的路径
log_path = os.path.join(root_path, 'test_result', 'test_log', 'test.log')

# 配置文件的路径
conf_path = os.path.join(root_path, 'conf', 'case.conf')

