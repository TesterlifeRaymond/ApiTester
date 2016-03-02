# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup as bs
import re
import pprint

class YiXin():
    def __init__(self):
        self.reg = 'http://10.100.140.24:9090/product/dm/-/13741'
        
    def register(self):
        s = requests.Session()
        r = bs(s.get(self.reg).text , "html.parser")
        a = r.get_text().replace('\n','')
        print(a)
        with open('test.txt' , 'wb') as f:
            f.write(a.encode('utf-8'))



if __name__ == '__main__':
    yx = YiXin()
    yx.register()
