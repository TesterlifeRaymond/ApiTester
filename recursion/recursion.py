
"""
    这是一个递归函数的python包
    使用例子：

    1 :get_value(dict, get_values_key)

        data = {"code": 0, "message": "操作成功","result": {"amount": 950.0000,
                "totalBaoLiFee": None, "pageNo": 1,"data": [{"goodsId": 100}]}}

        print(get_value(data, "code"))


    2: list_for_key_to_dict(*args, dict)
        print(list_for_key_to_dict("code", "pageNo", "goodsId", my_dict=data))

"""

class GetDictParam:
    """
        这是一个解析dict 参数的类
        可以用于多参数的指定key 、 指定key集合解析key
    """
    def __init__(self):
        """
            初始化函数
        """
        pass

    def get_value(self, my_dict, key):
        """
            这是一个递归函数
        """

        if isinstance(my_dict, dict):

            if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == ''\
                    and my_dict.get(key) is False:
                return my_dict.get(key)

            for my_dict_key in my_dict:
                if self.get_value(my_dict.get(my_dict_key), key) or \
                                self.get_value(my_dict.get(my_dict_key), key) is False:
                    return self.get_value(my_dict.get(my_dict_key), key)

        if isinstance(my_dict, list):
            for my_dict_arr in my_dict:
                if self.get_value(my_dict_arr, key) \
                        or self.get_value(my_dict_arr, key) is False:
                    return self.get_value(my_dict_arr, key)


    def list_for_key_to_dict(self, *args, my_dict):
        """
            接收需要解析的dict和 需要包含需要解析my_dict的keys的list

        :param my_dict: 需要解析的字典
        :param args: 包含需要解析的key的多个字符串
            # list_for_key_to_dict("code", "pageNo", "goodsId", my_dict=dict)
        :return: 一个解析后重新拼装的dict
        """
        result = {}
        if len(args) > 0:
            for key in args:
                result.update({key: self.get_value(my_dict, key)})
        return result

