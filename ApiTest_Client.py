#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-26 21:28:27
# @Author  : Liu jin jia  (jinjialiu@creditease.cn)
# @Version : 2016-03-25

import requests
import json
import hashlib
import time
import string
from random import choice
import random
import threading
import random
import pymysql


# conn = pymysql.connect(host='localhost', user='root',  # 与数据库建立连接

#                        passwd='Raymond1988', db='Books', charset="utf8")

def makeNew():  # 生成身份证
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    u''' 随机生成新的18为身份证号码 '''
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                          random.randint(1, 99),
                                          random.randint(1, 99),
                                          random.randint(t - 80, t - 18),
                                          random.randint(1, 12),
                                          random.randint(1, 28),
                                          random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' % (x, LAST[y % 11])


def Random_Name():  # 生成RealName
    f_name = []
    l_name = []
    A_Name = []
    num =   
    with open('source_Name.txt', 'r') as x:
        for F in x:
            f_name.append(F.strip())

    with open('Second_Name.txt', 'r') as m:
        for S in m:
            l_name.append(S.strip())

    for F in f_name:
        F = F
    for L in l_name:
        L = L
    FL = random.randint(1, len(F) - 1)
    FL2 = random.randint(2, len(F) - 1)
    LL = random.randint(1, len(L) - 1)
    LL2 = random.randint(1, len(L) - 1)
    AL = F[FL] + L[LL]
    BL = F[FL2] + L[LL] + L[LL2]
    Name_Dick = {"1": "AL", "2": "BL"}
    Key = str("%s" % random.randint(1, 2))
    AL = F[FL] + L[LL]
    BL = F[FL2] + L[LL] + L[LL2]
    if Name_Dick[Key] == "AL":
        return AL
    if Name_Dick[Key] == "BL":
        return BL


def GenEmail(length=8, chars=string.ascii_letters + string.digits):  # 随机生成邮箱
    NewEmail = ''.join([choice(chars) for i in range(5, 11)])
    NE_Dict = {"1": "163.com", "2": "sina.com", "3": "qq.com"}
    v = random.randint(1, 3)
    v = "%s" % v
    return (NewEmail + "@" + NE_Dict[v])


# 该方法自动生成密码，默认位数8
def GenPassword(length=8, chars=string.ascii_letters + string.digits):
    password = ''.join([choice(chars) for i in range(length)])
    return password


def GenMobileNum(length=11, chars=string.digits):  # 该方法自动生成11位乱序数字(模拟错误的手机号码)
    MobNum = ''.join([choice(chars) for i in range(length)])
    return MobNum


def random_PT():  # 随机获取list中的元素作为参数
    Pt_Dict = {"PC": 0, "WAP": 1, "IPHONE": 2, "ANDROID": 3}
    for PT in Pt_Dict:
        return PT


def AuthDocumentType():  # 证件类型包含
    AuthDT = list(WRZ(0, "N/A"), ID_CARD(1, "身份证"),
                  PASSPORT(2, "护照"), TAIWAN(3, "台胞证"), HK(4, "港澳居民通行证"))


def get_md5(psd):  # 该方法是md5 加密方法,如果需要加密,调用该方法
    password_r = psd.encode(encoding="utf-8")
    password_md5 = hashlib.md5(password_r).hexdigest()
    return password_md5


def createPhone():  # 该方法是生成手机号的格式，如果需要生成手机号码，则调用该方法
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147",
               "150", "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


# 该方法是写入数据库方法，如果需要将数据入库， 则调用该方法
def insertinfo(name, userid, mobile, password):
    try:

        cur = conn.cursor()
        cur.execute("SET NAMES utf8")
        insertSql = ("INSERT INTO XHAPI (name,userid,presetKey,mobile,password,responseKey) VALUES(\"%s\",%d,\"%s\",%d,\"%s\",\"%s\");") % (
            name, userid, presetKey, mobile, password, responseKey)
        cur.execute(insertSql)
        conn.commit()
    except Exception as e:
        print(e)
        cur.close()
        conn.close()




class Qy_Api:  # 企业星火 Api 测试类

    def __init__(self):  # 模块初始化
        self.s = requests.Session()
        self.UserRegFromEnum = random_PT()
        self.realName = ''
        self.Error_Code = ''
        self.md5psd = ''
        self.ResponseDiff = ''
        self.documentType = ''
        self.documentNo = ''
        self.acqld = ''
        self.resCode = ''
        self.userName = ''
        self.newmoblie = ''
        self.mobile = ''  # 初始化电话号码
        self.regFrom = ''  # 初始化用户平台
        self.password = ''  # 初始化用户密码
        self.email = ''
        self.userId = ''
        self.updateTime = ''
        self.createTime = ''
        self.lastLoginTime = ''
        self.docValidateTime = ''
        self.LoginTwoDict = ''
        self.Transmit_id = ''
        self.safekey = ''  # 接口访问必要的safekey参数
        # 注册接口
        self.userservice =  "userRegister"
        # 登录接口
        self.userlogin =  "userLogin"
        # 查询用户信息
        self.usermsg =  "queryUserInfoById"
        # 修改手机号码
        self.modifyMobile =  "modifyMobile"
        # 用户实名认证
        self.authRealName =  "authRealName"
        # 用户密码找回
        self.retPassword =  "retrievePassword"
        # 绑定激活邮箱
        self.BindEmail =  "bindActivationEmail"
        # 修改密码
        self.modPassWord =  "modifyPassWord"
        # 绑定银行卡
        self.BinBankCard =  "bindBankCard"

    def userReg(self):  # 用户注册接口
        # -----------------------------------
        #   调用预设方法，生成参数
        # -----------------------------------
        self.password = GenPassword(8)
        self.mobile = createPhone()
        self.UserRegFromEnum = random_PT()
        integer = random.randint(5, 15)  # 密码调用GenPassword方法,传参为 5-15位随机
        Genpwd = GenPassword(integer)
        MobNum = GenMobileNum(11)
    # -----------------------------------
    #   data参数预设
    # -----------------------------------
        data = {
            "password": "%s" % self.password,
            "mobile": "%s" % self.mobile,
            "regFrom": "%s" % self.UserRegFromEnum,
        }
    # -----------------------------------
    #   将data排序后拼接成字符串result，并调用get_md5方法对data进行加密，生成sign值
    #   将sign值update到data中
    # #--------------------------------------------------
        list = sorted(data.items(), key=lambda d: d[0])
        result = ""
        for item in list:
            result += "%s=%s&" % (item[0], item[1])
        if result[-1] == "&":
            result = result[0:-1] + self.safekey
        data.update({"sign": "%s" % get_md5(result)})
    # #--------------------------------------------------
        r = self.s.post(self.userservice, data=data)
        self.ResponseDiff = r.json()
        self.Error_Code = r.json()['errorCode']

        try:
            self.Transmit_id = r.json()['userId']
            self.resCode = r.json()['resCode']
            self.userId = r.json()['userId']
            self.Error_Code = r.json()['errorCode']
        except KeyError as k:
            pass
        dj.userReg_diff()
        # print('UserReg :' + str("%s" %
        # time.strftime("%Y:%M:%D %T")), data, str(r.json()), "验证结果 ：" +
        # dj.Validation_results)
        with open('name_data.log', 'a') as file:
            file.write('UserReg : ' + str("%s" % time.strftime("%Y:%M:%D %T")
                                          ) + str(data) + str(r.json()) + "验证结果 ：" + dj.Validation_results + "\n")

    def post_Login(self):  # 用户登录接口
        self.password = GenPassword(8)
        self.mobile = GenMobileNum(11)
        # -------------------------------------
        #   构造data
        # -------------------------------------
        data = {
            "password": "%s" % self.password,
            "mobile": "%s" % createPhone(),
            "regFrom": "PC",
        }
        self.md5psd = "%s" % self.password
        self.md5psd = self.md5psd.encode(encoding="utf-8")
        self.md5psd = hashlib.sha512(self.md5psd).hexdigest()
    # -----------------------------------
    #   将data排序后拼接成字符串result，并调用get_md5方法对data进行加密，生成sign值
    #   将sign值update到data中
    #
        list = sorted(data.items(), key=lambda d: d[0])
        result = ""
        for item in list:
            result += "%s=%s&" % (item[0], item[1])
        if result[-1] == "&":
            result = result[0:-1] + self.safekey
        data.update({"sign": "%s" % get_md5(result)})
    # #--------------------------------------------------
        r = self.s.post(self.userlogin, data=data)

        self.resCode = r.json()['resCode']
        self.Error_Code = r.json()['errorCode']
        if self.resCode == '0':
            self.ResponseDiff = r.json()
        else:
            self.ResponseDiff = r.json()['userInfoResDto']
            try:
                self.UserRegFromEnum = r.json()['userInfoResDto']['regFrom']
                self.realName = r.json()['userInfoResDto']['realName']
                self.lastLoginTime = r.json()['userInfoResDto'][
                    'lastLoginTime']
                self.createTime = r.json()['userInfoResDto']['createTime']
                self.updateTime = r.json()['userInfoResDto']['updateTime']
                self.userId = r.json()['userInfoResDto']['userId']
                self.email = r.json()['userInfoResDto']['email']
                self.docValidateTime = r.json()['userInfoResDto'][
                    'docValidateTime']
                self.mobile = r.json()['userInfoResDto']['mobile']
                self.documentNo = r.json()['userInfoResDto']['documentNo']
                self.documentType = r.json()['userInfoResDto']['documentType']
                self.password = r.json()['userInfoResDto']['password']
                self.regFrom = r.json()['userInfoResDto']['regFrom']
            except KeyError as k:
                pass

        dj.Login_diff()
        # print('Login : ' + str("%s" % time.strftime("%Y:%M:%D %T")) +
        # str(data) + str(r.json()) + "验证结果 ：" + dj.Validation_results + "\n")
        with open('name_data.log', 'a') as file:
            file.write('Login : ' + str("%s" % time.strftime("%Y:%M:%D %T")
                                        ) + str(data) + str(r.json()) + "\n")

    def post_Uersmsg(self):  # 用户登录接口
        # -------------------------------------
        #   构造data
        # -------------------------------------
        data = {"userId": "%s" % self.Transmit_id}
    # -------------------------------------
    #   将data排序后拼接成字符串result，并调用get_md5方法对data进行加密，生成sign值
    #   将sign值update到data中
    # #--------------------------------------------------

    # #--------------------------------------------------
    # #--------------------------------------------------
        self.md5psd = "%s" % self.password
        self.md5psd = self.md5psd.encode(encoding="utf-8")
        self.md5psd = hashlib.sha512(self.md5psd).hexdigest()
    # #--------------------------------------------------
    # #--------------------------------------------------
        list = sorted(data.items(), key=lambda d: d[0])
        result = ""
        for item in list:
            result += "%s=%s&" % (item[0], item[1])
        if result[-1] == "&":
            result = result[0:-1] + self.safekey
        data.update({"sign": "%s" % get_md5(result)})
    # #--------------------------------------------------
        r = self.s.post(self.usermsg, data=data)
        print(data)
        self.ResponseDiff = r.json()
        self.resCode = r.json()['resCode']
        self.Error_Code = r.json()['errorCode']

        try:
            self.realName = r.json()['realName']
            self.lastLoginTime = r.json()['lastLoginTime']
            self.createTime = r.json()['createTime']
            self.updateTime = r.json()['updateTime']
            self.userId = r.json()['userId']
            self.ResponseDiff = r.json()
            self.Error_Code = r.json()['errorCode']
            self.email = r.json()['email']
            self.docValidateTime = r.json()['docValidateTime']
            self.mobile = r.json()['mobile']
            self.documentNo = r.json()['documentNo']
            self.documentType = r.json()['documentType']
            self.password = r.json()['password']
            self.regFrom = r.json()['regFrom']
        except KeyError as k:
            pass
        dj.userMsg_diff()
        # print('UserMsg : ' + str("%s" % time.strftime("%Y:%M:%D %T")) +
        # str(data) + str(r.json()) + " 验证结果 ：" + dj.Validation_results + "\n")
        with open('name_data.log', 'a') as file:
            file.write('UserMsg : ' + str("%s" % time.strftime("%Y:%M:%D %T")
                                          ) + str(data) + str(r.json()) + " 验证结果 ：" + dj.Validation_results + "\n")

    def modMobile(self):
        # -----------------------------------
        #   调用预设方法，生成参数
        # -----------------------------------
        self.newmobile = GenMobileNum(11)
    # -----------------------------------
    #   data参数预设
    # -----------------------------------
        data = {
            "userId": "%s" % self.userId,
            "mobile": "%s" % createPhone(),
            "oldMobile": "%s" % self.mobile,
        }
    # -------------------------------------
    #   将data排序后拼接成字符串result，并调用get_md5方法对data进行加密，生成sign值
    #   将sign值update到data中
    # #--------------------------------------------------
        list = sorted(data.items(), key=lambda d: d[0])
        result = ""
        for item in list:
            result += "%s=%s&" % (item[0], item[1])
        if result[-1] == "&":
            result = result[0:-1] + self.safekey
        data.update({"sign": "%s" % get_md5(result)})
    # #--------------------------------------------------
        r = self.s.post(self.modifyMobile, data=data)

        self.ResponseDiff = r.json()
        self.resCode = r.json()['resCode']
        self.Error_Code = r.json()['errorCode']
        dj.modMobile_diff()
        # print('modMobile : ' + str("%s" % time.strftime("%Y:%M:%D %T")) +
        # str(data) + str(r.json()) + "验证结果 ：" + dj.Validation_results + "\n")
        with open('name_data.log', 'a') as file:
            file.write('modMobile : ' + str("%s" %
                                            time.strftime("%Y:%M:%D %T")) + str(data) + str(r.json()) + "验证结果 ：" + dj.Validation_results + "\n")

    def authReal(self):

        # -----------------------------------
        #   调用预设方法，生成参数
        # -----------------------------------
        self.realName = Random_Name()
        self.documentNo = makeNew()
        self.documentType = "ID_CARD"
        # -----------------------------------
        #   data参数预设
        # -----------------------------------
        data = {
            "userId": "%s" % self.userId,
            "realName": "%s" % self.realName,
            "documentType": "%s" % self.documentType,
            "documentNo": "%s" % self.documentNo,
            "acqId": "01",
            "terminalType": "WEB"
        }
    # -------------------------------------
    #   将data排序后拼接成字符串result，并调用get_md5方法对data进行加密，生成sign值
    #   将sign值update到data中
    # #--------------------------------------------------
        list = sorted(data.items(), key=lambda d: d[0])
        result = ""
        for item in list:
            result += "%s=%s&" % (item[0], item[1])
        if result[-1] == "&":
            result = result[0:-1] + self.safekey
        data.update({"sign": "%s" % get_md5(result)})
    # #--------------------------------------------------
        r = self.s.post(self.authRealName, data=data)
        self.ResponseDiff = r.json()
        self.resCode = r.json()['resCode']
        dj.auth_diff()

        # print('authReal : ' + str("%s" % time.strftime("%Y:%M:%D %T")) +
        # str(data) + str(r.json()) + "验证结果 ：" + dj.Validation_results + "\n")
        with open('name_data.log', 'a') as file:
            file.write('authReal : ' + str("%s" %
                                           time.strftime("%Y:%M:%D %T")) + str(data) + str(r.json()) + "验证结果 ：" + dj.Validation_results + "\n")

    def BindActivationEmail(self):
        # -----------------------------------
        #   data参数预设
        # -----------------------------------
        data = {
            "userId": "%s" % self.Transmit_id,
            "email": "%s" % GenEmail(),
            "optionType": "BIND_EMAIL",
        }
    # -------------------------------------
    #   将data排序后拼接成字符串result，并调用get_md5方法对data进行加密，生成sign值
    #   将sign值update到data中
    # #--------------------------------------------------
        list = sorted(data.items(), key=lambda d: d[0])
        result = ""
        for item in list:
            result += "%s=%s&" % (item[0], item[1])
        if result[-1] == "&":
            result = result[0:-1] + self.safekey
        data.update({"sign": "%s" % get_md5(result)})
    # #--------------------------------------------------
        r = self.s.post(self.BindEmail, data=data)
        self.ResponseDiff = r.json()
        self.Error_Code = r.json()['errorCode']
        try:
            self.resCode = r.json()['resCode']
            self.ResponseDiff = r.json()
            self.Error_Code = r.json()['errorCode']
        except TypeError as t:
            pass
        except KeyError as k:
            pass
        dj.BindEmail_diff()
        # print('BindActivationEmail : ' + str("%s" %
        # time.strftime("%Y:%M:%D %T")) + str(data) + str(r.json()) + "验证结果 ："
        # + dj.Validation_results + "\n")
        with open('name_data.log', 'a') as file:
            file.write(BindActivationEmail.__name__ + str("%s" %
                                                          time.strftime("%Y:%M:%D %T")) + str(data) + str(r.json()) + "验证结果 ：" + dj.Validation_results + "\n")
        # list = sorted(r.json().items(), key=lambda d: d[0])
        # result = ""
        # for item in list:
        #     result += "%s=%s&" % (item[0], item[1])
        # if result[-1] == "&":
        #     result = result[0:-1] + self.safekey
        # result = get_md5(result)

    def ModPassword(self):
        # -----------------------------------
        #   data参数预设
        # -----------------------------------
        data = {
            "userId": "%s" % self.Transmit_id,  # %self.Transmit_id,
            "password": "%s" % GenPassword(),
            "newPassword": "%s" % GenPassword(),
        }
    # -------------------------------------
    #   将data排序后拼接成字符串result，并调用get_md5方法对data进行加密，生成sign值
    #   将sign值update到data中
    # #--------------------------------------------------
        list = sorted(data.items(), key=lambda d: d[0])
        result = ""
        for item in list:
            result += "%s=%s&" % (item[0], item[1])
        if result[-1] == "&":
            result = result[0:-1] + self.safekey
        data.update({"sign": "%s" % get_md5(result)})
    # #--------------------------------------------------
        r = self.s.post(self.modPassWord, data=data)

        self.ResponseDiff = r.json()
        self.resCode = r.json()['resCode']
        dj.ModPassword_diff()
        # print('ModPassword : ' + str("%s" %
        # time.strftime("%Y:%M:%D %T")) + str(data) + str(r.json()) + "验证结果 ："
        # + dj.Validation_results + "\n")
        with open('name_data.log', 'a') as file:
            file.write(ModPassword.__name__ + str("%s" %
                                                  time.strftime("%Y:%M:%D %T")) + str(data) + str(r.json()) + "验证结果 ：" + dj.Validation_results + "\n")

    def restPassword(self):
        self.password = GenPassword()
        # -----------------------------------
        #   data参数预设
        # -----------------------------------
        data = {
            "userId": "%s" % self.Transmit_id,  # %self.Transmit_id,
            "password": "%s" % self.password,
            "newPassword": "%s" % GenPassword(),
        }
    # -------------------------------------
    #   将data排序后拼接成字符串result，并调用get_md5方法对data进行加密，生成sign值
    #   将sign值update到data中
    # #--------------------------------------------------
        list = sorted(data.items(), key=lambda d: d[0])
        result = ""
        for item in list:
            result += "%s=%s&" % (item[0], item[1])
        if result[-1] == "&":
            result = result[0:-1] + self.safekey
        data.update({"sign": "%s" % get_md5(result)})
    # #--------------------------------------------------
        r = self.s.post(self.retPassword, data=data)

        self.ResponseDiff = r.json()
        self.resCode = r.json()['resCode']
        dj.restPassword_diff()
        # print('ModPassword : ' + str("%s" %
        # time.strftime("%Y:%M:%D %T")) + str(data) + str(r.json()) + "验证结果 ："
        # + dj.Validation_results + "\n")
        with open('name_data.log', 'a') as file:
            file.write('ModPassword : ' + str("%s" %
                                              time.strftime("%Y:%M:%D %T")) + str(data) + str(r.json()) + "验证结果 ：" + dj.Validation_results + "\n")

    def BindBank(self):
        # -----------------------------------
        #   调用预设方法，生成参数
        # -----------------------------------
        self.realName = Random_Name()
        self.documentNo = makeNew()
        self.documentType = "ID_CARD"
        # -----------------------------------
        #   data参数预设
        # -----------------------------------
        data = {
            "userId": "%s" % self.userId,
            "realName": "%s" % self.realName,
            "docType": "%s" % self.documentType,
            "documentNo": "%s" % self.documentNo,
            "acqId": "01",
            "bankCardType": "",
            "signInfo": "",
            "cityCode": "",
            "provinceCode": "",
            "branchBankName": "",
            "mobile": "",
            "remark": "",
            "cardNo": "",
            "cardFlag": "",
            "bankName": "",
            "bankCode": ""
        }
    # -------------------------------------
    #   将data排序后拼接成字符串result，并调用get_md5方法对data进行加密，生成sign值
    #   将sign值update到data中
    # #--------------------------------------------------
        list = sorted(data.items(), key=lambda d: d[0])
        result = ""
        for item in list:
            result += "%s=%s&" % (item[0], item[1])
        if result[-1] == "&":
            result = result[0:-1] + self.safekey
        data.update({"sign": "%s" % get_md5(result)})
    # #--------------------------------------------------
        r = self.s.post(self.authRealName, data=data)


class Diff_Json:

    def __init__(self):
        self.Validation_results = ''
        self.name = ''
        self.Res_response_ErrorPass = {}
        self.Res_response = {}
        self.Res_response_True = {}
        self.Res_response_Arna = {}
        self.Res_response_Dif = {}
        self.Res_response_Null = {}
        self.Res_response_Propertyempty = {}
        self.Res_response_repeat = {}
        self.Dict_code = {"  1": "参数校验失败:手机号不合法", "  2": "参数校验失败:密码不合法",
                          "  3": "参数校验失败:对象不能为空", "  4": "参数校验失败:邮箱地址不合法",
                          "  2": "安全秘钥验证不通过", "  1": "系统错误", "  3": "不支持此类操作",
                          "  1": "手机号格式错误", "  2": "该手机号已注册", "  3": "该用户不存在",
                          "  4": "用户名密码错误", "  5": "用户邮箱已存在", "  6": "实名认证失败",
                          "  7": "旧密码不正确", "  8": "已经实名认证", "  9": "新密码与旧密码相同",
                          "  10": "支持的银行列表不存在", "  11": "银行不存在", "  12": "企业用户对公银行卡不存在",
                          "  13": "企业用户不存在", "  14": "企业账号已存在", "  15": "实名认证信息已被占用",
                          "  16": "银行卡鉴权失败", "  17": "旧密码不正确"}

    def diff_service(self):
        #--------------------------------------------------
        list_Rd = sorted(self.Res_response_Dif.items(), key=lambda d: d[0])
        result_D = ""
        for item_D in list_Rd:
            result_D += "%s=%s&" % (item_D[0], item_D[1])
#--------------------------------------------------
#--------------------------------------------------
        list_False = sorted(self.Res_response.items(), key=lambda d: d[0])
        result_F = ""
        for item_F in list_False:
            result_F += "%s=%s&" % (item_F[0], item_F[1])
#--------------------------------------------------
#--------------------------------------------------
        list_Null = sorted(self.Res_response_Null.items(), key=lambda d: d[0])
        result_Null = ""
        for item_Null in list_Null:
            result_Null += "%s=%s&" % (item_Null[0], item_Null[1])
#--------------------------------------------------
#--------------------------------------------------
        result_T = ""
        list_True = sorted(self.Res_response_True.items(), key=lambda d: d[0])
        for item_T in list_True:
            result_T += "%s=%s&" % (item_T[0], item_T[1])
#--------------------------------------------------
#--------------------------------------------------
        result_ErrorPass = ""
        list_ErrorPass = sorted(
            self.Res_response_ErrorPass.items(), key=lambda d: d[0])
        for item_ErrorPass in list_ErrorPass:
            result_ErrorPass += "%s=%s&" % (
                item_ErrorPass[0], item_ErrorPass[1])
#--------------------------------------------------
#--------------------------------------------------
        result_Arna = ""
        list_Arna = sorted(self.Res_response_Arna.items(), key=lambda d: d[0])
        for item_Arna in list_Arna:
            result_Arna += "%s=%s&" % (item_Arna[0], item_Arna[1])
#--------------------------------------------------
#--------------------------------------------------
        result_Propertyempty = ""
        list_Propertyempty = sorted(
            self.Res_response_Propertyempty.items(), key=lambda d: d[0])
        for item_Propertyempty in list_Propertyempty:
            result_Propertyempty += "%s=%s&" % (
                item_Propertyempty[0], item_Propertyempty[1])
#--------------------------------------------------
#--------------------------------------------------
        result_repeat = ""
        list_repeat = sorted(
            self.Res_response_repeat.items(), key=lambda d: d[0])
        for item_repeat in list_repeat:
            result_repeat += "%s=%s&" % (item_repeat[0], item_repeat[1])
#--------------------------------------------------
#--------------------------------------------------
        result_mobile = ""
        list_mobile = sorted(
            self.Res_response_mobile.items(), key=lambda d: d[0])
        for item_mobile in list_mobile:
            result_mobile += "%s=%s&" % (item_mobile[0], item_mobile[1])
#--------------------------------------------------
#--------------------------------------------------
        response_repeat = get_md5(result_repeat)  # 内容重复参数加密后md5
        response_Arna = get_md5(result_Arna)
        response_ErrorPass = get_md5(result_ErrorPass)
        response_Propertyempty = get_md5(result_Propertyempty)
        response_Null = get_md5(result_Null)
        response_mobile = get_md5(result_mobile)
#--------------------------------------------------
#--------------------------------------------------
        response_D = get_md5(result_D)  # 返回参数加密后md5
        response_F = get_md5(result_F)  # 错误的验证字段md5
        response_T = get_md5(result_T)  # 正确的验证字段md5
#--------------------------------------------------
#--------------------------------------------------
        print("--" * 10)
        print(result_Null)
        print(result_ErrorPass)
        print(result_D)
        print("--" * 40)
        print(result_F)
        print(result_Propertyempty)
        print(result_T)
        print("--"*40)
        print(result_Arna)
#--------------------------------------------------
#--------------------------------------------------
        if qa.resCode == '0':
            if response_D == response_F:
                print("错误返回的验证通过：", True)
                self.Validation_results = "True"
            elif response_D == response_Arna:
                print("错误返回的验证通过：", True)
                self.Validation_results = "True"
            elif response_D == response_Null:
                print("错误返回的验证通过：", True)
                self.Validation_results = "True"
            elif response_D == response_Propertyempty:
                print("错误返回的验证通过：", True)
                self.Validation_results = "True"
            elif response_D == response_ErrorPass:
                print("错误返回的验证通过：", True)
                self.Validation_results = "True"
            elif response_D == response_repeat:
                print("错误返回的验证通过：", True)
                self.Validation_results = "True"
            elif response_D == response_mobile:
                print("错误返回的验证通过：", True)
                self.Validation_results = "True"

            else:
                print("错误返回的验证通过：", False)
                self.Validation_results = "False"
        if qa.resCode == '1':
            if response_T == response_D:
                print("正确返回的验证通过：", True)
                self.Validation_results = "True"
            else:
                print("正确返回的验证通过：", False)
                self.Validation_results = "False"

    def userReg_diff(self):
        name = Random_Name()
        self.Res_response = {'errorDesc': '安全秘钥验证不通过',
                             'resCode': '0', 'errorCode': '  2'}
        self.Res_response_mobile = {'resCode': '0', 'SUCCESS': '1', 'errorCode': '  1',
                                    'errorDesc': '参数校验失败:手机号不合法', 'FAILED': '0', 'serialVersionUID': 1529715049189201265}  # 错误的验证字段
        self.Res_response_True = {'userId': qa.userId, 'errorCode': None,
                                  'resCode': '1', 'errorDesc': None}   # 正确的验证字段
        self.Res_response_Arna = {'resCode': '0',
                                  'errorCode': '  9', 'errorDesc': '新密码与旧密码相同'}
        self.Res_response_Dif = qa.ResponseDiff
        dj.diff_service()

    def modMobile_diff(self):
        name = Random_Name()
        self.Res_response = {'errorDesc': '安全秘钥验证不通过',
                             'resCode': '0', 'errorCode': '  2'}
        self.Res_response_mobile = {'resCode': '0', 'SUCCESS': '1', 'errorCode': '  1',
                                    'errorDesc': '参数校验失败:手机号不合法', 'FAILED': '0', 'serialVersionUID': 1529715049189201265}  # 错误的验证字段
        self.Res_response_True = {
            'resCode': '1', 'errorCode': None, 'errorDesc': None}  # 正确的验证字段
        self.Res_response_Null = {
            'errorCode': '  3', 'errorDesc': '该用户不存在', 'resCode': '0'}
        self.Res_response_Dif = qa.ResponseDiff
        dj.diff_service()

    def restPassword_diff(self):
        name = Random_Name()
        self.Res_response = {'errorDesc': '安全秘钥验证不通过',
                             'resCode': '0', 'errorCode': '  2'}
        self.Res_response_mobile = {'resCode': '0', 'SUCCESS': '1', 'errorCode': '  1',
                                    'errorDesc': '参数校验失败:手机号不合法', 'FAILED': '0', 'serialVersionUID': 1529715049189201265}  # 错误的验证字段
        self.Res_response_True = {
            'resCode': '1', 'errorCode': None, 'errorDesc': None}  # 正确的验证字段
        self.Res_response_Null = {
            'errorCode': '  3', 'errorDesc': '该用户不存在', 'resCode': '0'}
        self.Res_response_Dif = qa.ResponseDiff
        dj.diff_service()

    def Login_diff(self):
        name = Random_Name()
        self.Res_response_Null = {
            'errorCode': '  3', 'userInfoResDto': None, 'errorDesc': '该用户不存在', 'resCode': '0'}
        self.Res_response = {'errorDesc': '安全秘钥验证不通过',
                             'resCode': '0', 'errorCode': '  2'}

        self.Res_response_mobile = {'resCode': '0', 'SUCCESS': '1', 'errorCode': '  1',
                                    'errorDesc': '参数校验失败:手机号不合法', 'FAILED': '0', 'serialVersionUID': 1529715049189201265}  # 错误的验证字段
        self.Res_response_True = {'mobile': '%s' % qa.mobile, 'updateTime': '%s' % qa.updateTime, 'documentNo': None, 'lastLoginTime': '%s' % qa.lastLoginTime,
                                  'lenderId': None, 'address': None, 'regFrom': '%s' % qa.UserRegFromEnum, "status": "ACTIVE", 'emailValidateTime': None, 'cardValidated': None, 'docValidated': None, 'emailValidated': None, 'birthDay': None,
                                  'userName': None, 'zipCode': None, 'userId': '%s' % qa.userId,
                                  'email': "%s" % qa.email, 'documentType': '%s' % qa.documentType, 'realName': None, 'orgName': None,
                                  'docValidateTime': None, 'createTime': '%s' % qa.createTime, 'sysSourceId': None, 'cardValidateTime': None, 'memberNo': None,
                                  'errorDesc': None, 'errorCode': None, 'orgCode': None,
                                  'password': '%s' % qa.password, 'resCode': None, 'avatar': None, 'gender': None}   # 正确的验证字段
        self.Res_response_Dif = qa.ResponseDiff
        dj.diff_service()

    def auth_diff(self):
        self.Res_response = {'errorDesc': '安全秘钥验证不通过',
                             'resCode': '0', 'errorCode': '  2'}
        self.Res_response_Arna = {
            'errorDesc': '已经实名认证', 'resCode': '0', 'errorCode': '  8'}
        self.Res_response_Null = {'errorCode': '  3',
                                  'errorDesc': '该用户不存在', 'resCode': '0'}
        self.Res_response_True = {'resCode': '1',
                                  'errorCode': None, 'errorDesc': None}
        self.Res_response_Dif = qa.ResponseDiff
        dj.diff_service()

    def userMsg_diff(self):
        self.Res_response = {'errorDesc': '安全秘钥验证不通过',
                             'resCode': '0', 'errorCode': '  2'}
        self.Res_response_Arna = {'lastLoginTime': None, 'emailValidateTime': None, 'docValidateTime': None, 'memberNo': None, 'address': None, 'cardValidated': None, 'orgName': None, 'regFrom': None,
                                  'realName': None, 'createTime': None}
        self.Res_response_True = {'orgName': None, 'password': '%s' % qa.password,
                                  'mobile': '%s' % qa.mobile, 'emailValidateTime': None, 'cardValidateTime': None, 'errorCode': None, 'docValidateTime': "%s" % qa.docValidateTime,
                                  'documentNo': "%s" % ,'memberNo': None}
        self.Res_response_Dif = qa.ResponseDiff
        dj.diff_service()

    def BindEmail_diff(self):
        self.Res_response = {'errorDesc': '安全秘钥验证不通过',
                             'resCode': '0', 'errorCode': '  2'}
        self.Res_response_Null = {'errorCode': '  3',
                                  'errorDesc': '该用户不存在', 'resCode': '0'}
        self.Res_response_True = {'resCode': '1',
                                  'errorDesc': None, 'errorCode': None}
        self.Res_response_Dif = qa.ResponseDiff
        dj.diff_service()

    def ModPassword_diff(self):
        self.Res_response = {'errorDesc': '安全秘钥验证不通过',
                             'resCode': '0', 'errorCode': '  2'}
        self.Res_response_Null = {'errorCode': '  3',
                                  'errorDesc': '该用户不存在', 'resCode': '0'}
        self.Res_response_True = {'resCode': '1',
                                  'errorDesc': None, 'errorCode': None}
        self.Res_response_Propertyempty = {'resCode': '0', 'FAILED': '0', 'errorDesc': '参数校验失败:newPassword属性不能为空',
                                           'serialVersionUID': 1529715049189201265, 'errorCode': '  5', 'SUCCESS': '1'}
        self.Res_response_ErrorPass = {
            'resCode': '0', 'errorDesc': '旧密码不正确', 'errorCode': '  17'}
        self.Res_response_repeat = {
            'errorCode': '  9', 'errorDesc': '新密码与旧密码相同', 'resCode': '0'}
        self.Res_response_Dif = qa.ResponseDiff
        dj.diff_service()


def Start_Test():
    qa.userReg()
    qa.ModPassword()
    qa.post_Login()
    qa.modMobile()
    qa.post_Uersmsg()
    qa.authReal()
    qa.BindActivationEmail()
    qa.restPassword()

    # insertinfo(self.userName , int(self.userId),int(self.mobile) , self.password)
    # print(self.userName, int(self.userId),
    #       int(self.mobile), self.password)

if __name__ == '__main__':
    qa = Qy_Api()
    dj = Diff_Json()
    qa.userReg()
