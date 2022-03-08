import requests
from common.get_header import get_header
from common.login_token import login_token


class HttpRequest:
    """该类完成http的get 以及post请求，并返回结果"""

    @staticmethod
    def http_request(method, url, param, headers):
        """根据请求方法来决定发起get请求还是post请求
        method: get post http的请求方式
        url:发送请求的接口地址
        param:随接口发送的请求参数 以字典格式传递
        rtype:有返回值，返回结果是响应报文
        """
        resp = None
        if method.upper() == 'GET':
            try:
                resp = requests.get(url, params=param, headers=headers)
            except Exception as e:
                print('get请求出错了：{}'.format(e))
        elif method.upper() == 'POST':
            try:
                resp = requests.post(url, data=param, headers=headers)
            except Exception as e:
                print('post请求出错了：{}'.format(e))
        else:
            print('不支持该种方式')
            resp = None
        return resp


if __name__ == '__main__':
    request_url = 'http://47.97.33.96:5000/login'
    header = "{'Content-Type': 'application/json;charset=UTF-8'}"
    token = login_token.get_token("uat")
    params = '{"account":"admin","password":"123456"}'
    header = get_header(header, token)
    response = HttpRequest.http_request('POST', request_url, params.encode(), header)
    print(response.text)
