import os

# 根路径
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据目录
test_data_path = os.path.join(root_path, 'data')

# 日志文件路径
log_path = os.path.join(root_path, 'test_result', 'log')

# 断言截图目录
screenshot_path = os.path.join(root_path, 'test_result', 'images')

# 测试报告路径json
test_report_json_path = os.path.join(root_path, 'test_result', 'report', 'json')

# 测试报告路径html
test_report_html_path = os.path.join(root_path, 'test_result', 'report', 'html')
