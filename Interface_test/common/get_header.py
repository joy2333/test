import ast


def get_header(headers, token):
    """
    headers:字符串类型json数据的headers
    token:字符串类型的token
    """
    headers = ast.literal_eval(headers)  # 将读取出来的headers转换成字典
    headers['token'] = token
    return headers


if __name__ == '__main__':
    header = get_header("{'Content-Type': 'application/json;charset=UTF-8'}", "77aa-0a4f-468e-b3b9-ede1")
    print(header)
