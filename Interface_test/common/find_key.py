# 查找键，找到则返回该键的值，否则返回None
import jsonpath


def find_key(data, key):
    value = jsonpath.jsonpath(data, '$..{}'.format(key))
    if value:
        return value[0]
    else:
        return None


if __name__ == '__main__':
    data1 = {"code": 0}
    data2 = '{"code":0}'
    print(find_key(data1, "code"))
