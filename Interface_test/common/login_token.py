import json
import requests


class login_token:

    @staticmethod
    def get_token(environment):
        """
        获取token
        environment:环境uat/stg
        """
        login_header = {'Content-Type': "application/json;charset=UTF-8"}
        login_response = None
        login_data = None
        url = None
        if environment == 'uat':
            url = "http://47.97.33.96:5000/login"
            login_data = {"account": "admin", "password": "123456"}
        elif environment == 'stg':
            url = "http://47.97.33.96:5000/login"
            login_data = {"account": "admin", "password": "123456"}
        login_data = json.dumps(login_data)
        try:
            login_response = requests.post(url=url, data=login_data, headers=login_header)
        except Exception as e:
            print('获取token请求出错了：{}'.format(e))
        return login_response.json()["data"]


'''测试代码'''
if __name__ == '__main__':
    token = login_token.get_token('uat')
    print(token)
