# 查找键，找到则返回该键的值，否则返回None
import jsonpath


class Find:
    flag = None

    @staticmethod
    def find_k(data, key):
        if isinstance(data, dict):
            for k, v in data.items():
                if k == key:
                    Find.flag = v
                    return
                elif isinstance(v, dict):
                    Find.find_k(v, key)
                elif isinstance(v, list):
                    for val in v:
                        Find.find_k(val, key)


# def find_key(data, key):
#     Find.find_k(data, key)
#     flag, Find.flag = Find.flag, None
#     return flag

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
