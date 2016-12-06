
"""
    这是一个递归函数的python包
    使用例子：

    get_value(dict, get_values_key)

    data = {"code": 0, "message": "操作成功","result": {"amount": 950.0000,
            "totalBaoLiFee": None, "pageNo": 1,"data": [{"goodsId": 100}]}}

    print(get_value(data, "messages"))

"""

def get_value(my_dict, key):
    """
        这是一个递归函数
    """

    if isinstance(my_dict, dict):
        if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == '':
            return my_dict[key]

        for my_dict_key in my_dict:
            if get_value(my_dict[my_dict_key], key):
                return get_value(my_dict[my_dict_key], key)

    if isinstance(my_dict, list):
        for my_dict_arr in my_dict:
            if get_value(my_dict_arr, key):
                return get_value(my_dict_arr, key)
