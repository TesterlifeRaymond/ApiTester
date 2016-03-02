# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup as bs

class Yanshi:
    def __init__(self):
        self.s = requests.Session()
        self.Login = 'http://www.ishansong.com/user/doLogin'
        self.admin = 'http://www.ishansong.com/web/userlevelinfo/show_pc?cityid=1'

    def ssLogin(self):
        self.Name = input('Please Enter your name :')
        self.Pwd = input('Enter your PassWord :')
        headers = {
            "Host":"www.ishansong.com",
            "Upgrade-Insecure-Requests":1,
            "Origin":"http://www.ishansong.com",
            "Referer":"http://www.ishansong.com/user/login",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"
                }

        data = {
            "service":"",
            "tab":"tab2",
            "username":"%s"%self.Name,
            "password":,
                }
        r = self.s.post(self.Login , headers = headers , data = data )
        if r.status_code == 200:
            return 1
        else:
            print("登陆失败，请重新登录！")




    def get_page(self):
        r = bs(self.s.get(self.admin).text , "html.parser")
        a = r.find_all("li","cityName")
        for i in a:
            print(i["data-name"])


if __name__ == '__main__':
    ys = Yanshi()
    print("--"*29)
    print('|本系统自动完成登陆，真实测试工具可手动填写参数。(按回车继续)|')
    print("--"*29)
    b = input("")
    ys.ssLogin()
    if ys.ssLogin() == 1:
        while True:
            a = input('''请选择您要测试的接口:
                1:查询城市信息
                2:查询账号信息
                3:查询FAQ
                x:退出系统
                    '''
                    )
            if a == "x":
                print("退出成功！")
                break

            try:
                if int(a) == 1:
                    ys.get_page()
                elif int(a) == 2:
                    print("888")
                elif int(a) == 3:
                    print("777")

            except:
                print("Error!! Please Enter Again!")