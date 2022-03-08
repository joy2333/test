import os
from base.project_path import test_report_json_path, test_report_html_path

if __name__ == '__main__':
    os.system('pytest')

    # 将test_result/report/json目录中json数据转换成html文件
    instruct = 'allure generate {} -o {} --clean'.format(test_report_json_path, test_report_html_path)
    os.system(instruct)
