# -*- coding: utf-8 -*-

import requests
import json

class YiXin():
    def __init__(self):
        self.s = requests.Session()
        self.get_Aes = 'http://10.100.140.24:9090/mobile/app/other/getSecretString.json?data={}&debugFlag=true'
        ###get_Aes 访问一次会获取到sign,如果要是获取AES，就在data中加上sign值 然后调用这个接口就可以
        self.reg = 'http://10.100.140.24:9090/mobile/app/user/msgSend.json?data={"appReqData": {"mobile": "%s","msgtype": %s},"appid":"8aead9a64cc04c8b014cc04c8b1e0000","sign": "%s"}'
        self.red = 'http://10.100.140.24:9090/mobile/redMarketView.shtml'
        self.sendred = 'http://10.100.140.24:9090/mobile/app/redMarket/sendRed.json/?data={"appReqData": {"selectedUserids":" %s,%s "，"prizeApplyid":%s,"fconut":1},"token": " %s ","sign": "%s","appid": "%s"}'
        self.userlist = 'http://10.100.140.24:9090/mobile/app/redMarket/sendUserList.json/?data={"appReqData": {"prizeApplyid": %s},"token": "%s","sign": "%s","appid": "%s"}'
        self.redApply = 'http://10.100.140.24:9090/mobile/app/redMarket/redApply.json/?data={"appReqData": {"applyNum": %s，"activityId":%s},"token": "%s","sign": "%s","appid": "%s"}'
        self.redactivitylist = 'http://10.100.140.24:9090/mobile/app/redMarket/redActivityList.json/?data={"appReqData": {"pageNo": %s,"pageSize": %s,"acStatus":%s},"token": "%s","sign": "%s","appid": "%s"}'
        self.modifyPwd = 'http://10.100.140.24:9090/mobile/app/user/modifyPwd.json?data={"appReqData": {"mobile": "%s ","userPassWord ": "%s", "secretKey": "%s"},"token": "%s""sign": "%s"}'
        self.queryUserInfo = 'http://10.100.140.24:9090/mobile/app/user/queryUserInfo.json?data={ "appReqData": { "userId": "%s" }, "token": "%s" "sign": "%s" }'
        self.getUserSettlement = 'http://10.100.140.24:9090/mobile/app/user/getUserSettlement.json?data={"appReqData": {  "settleStatus":"%s"},"token": "%s","sign": "%s"}'
        self.bindBankC ='http://10.100.140.24:9090/mobile/app/ user/bindBankCard.json?data={"appReqData": {"userId": "%s","bankCode": "%s","accountNo": "%s","authCode": "%s"},"token": "%s","sign": "%s"}'
        self.get_bankL = 'http://10.100.140.24:9090/mobile/app/ user/getBankList.json?data={"appResData":{},"token": "%s""sign": "%s"}'
        self.Bemail = 'http://10.100.140.24:9090/mobile/app/user/bindEmail.json?data={"appReqData": {"emailUrl": %s},"token": "%s","sign": "%s"}'
        self.settleDetails = 'http://10.100.140.24:9090/mobile/app/user/settleDetails.json?data={"appReqData":{"pageNo":"%s","settleStatus":"%s","settleDate":"%s","subProductType":"%s"},"token": "%s","sign": "%s"}'
        self.sxbser = 'http://10.100.140.24:9090/mobile/app/user/suiXinBaoSettleDetails.json?data={"appReqData":{"settleDate":"%s","pageNo": %s,"pageSize": %s},"token": "%s","sign": "%s"}'
        self.MobileExit = 'http://10.100.140.24:9090/mobile/app/user/mobileExist.json?data={"appReqData":{"mobile":"%s"},"sign": "%s"}'
        self.checkN = 'http://10.100.140.24:9090/mobile/app/user/checkname.json?data={"appReqData": {"realname": "%s","documentno": "%s","mobile": "%s","authCode": "%s"},"token": "%s","sign": "%s"}'
        self.chujiexy = 'http://10.100.140.24:9090/mobile/productProtocolApp.shtml?subproductId=120&type=”chujie”'
        self.shuzixy = 'http://10.100.140.24:9090/mobile/productProtocolApp.shtml? type= “shuzi”'




    def register(self): #注册
        self.mobile = '13810682940'
        self.msgtype = 1
        self.sign = '0700DB5C2FEC9F8698488328763B1779'
        r = self.s.get(self.reg%(self.mobile , self.msgtype , self.sign))
        print(r.text)
        print(r.json()['result'])




    def redmarker(self):#except: requests.exceptions.InvalidURL: Failed to parse: 10.100.140.24:9090  无法获取html内容    #红包
        r = self.s.get(self.red)

    def sendredmarker(self):#发红包接口
        self.sele = '100082385833'
        self.sele2 = '100123847809'
        self.prizeApplyid = '75'
        self.token = '01d2a1cc7da70c857afb8a3adb0555dc'
        self.appid = '43640A57B18E842E11C86CF2293F4871'
        self.sign = '43640A57B18E842E11C86CF2293F4871'
        r = self.s.get(self.sendred%(self.sele , self.sele2 ,self.prizeApplyid , self.token , self.sign , self.appid ))

    def send_userlist(self):#获取发红包列表
        self.prizeApplyid = 1
        self.token = 'c4ca4238a0b923820dcc509a6f75849b'
        self.sign = '43640A57B18E842E11C86CF2293F4871'
        self.appid = '43640A57B18E842E11C86CF2293F4871'

        r = self.s.get(self.userlist%(self.prizeApplyid , self.token , self.sign , self.appid))
        print(r.text)

    def red_Apply(self):#申请红包接口
        self.applyNum = 1
        self.activityId = 1
        self.token = "c4ca4238a0b923820dcc509a6f75849b"
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        self.appid = "43640A57B18E842E11C86CF2293F4871"

        r = self.s.get(self.redApply%(self.applyNum , self.activityId , self.token , self.sign , self.appid))
        print(r.text)

    def red_activityList(self): #申请红包活动列表
        self.pageNo = 1
        self.pageSize = 1
        self.acStatus = 1
        self.token = "76072ce60d0a3950c47d17bb3c71e9b4"
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        self.appid = "43640A57B18E842E11C86CF2293F4871"

        r = self.s.get(self.redactivitylist%(self.pageNo , self.pageSize , self.acStatus , self.token , self.sign , self.appid))
        print(r.json()['result'] + ":" + r.json()["errMsg"])

    def redDisplay(self):
        pass

    def modPwd(self):#修改密码      : code = 404 页面丢失
        self.mobile = 13439791955
        self.userPassWord ="abc123321"
        self.secretKey = "70545f147ea0d682f5ba02a05d6cc778"
        self.token = "c4ca4238a0b923820dcc509a6f75849b"
        self.sign ="43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.modifyPwd%(self.mobile, self.userPassWord,self.secretKey , self.token , self.sign))
        print(r.text)


    def quserinfo(self):    #查询用户完整信息(AES加密) code = 404 页面丢失
        self.userId = 100019459223
        self.token = "c4ca4238a0b923820dcc509a6f75849b"
        self.sign ="43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.queryUserInfo%(self.userId , self.token , self.sign))
        print(r.text)

    def getUserslt(self):  #获取用户结算信息
        self.settleStatus = "0"
        self.token = "c4ca4238a0b923820dcc509a6f75849b"
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.getUserSettlement%(self.settleStatus , self.token , self.sign))
        print(r.text)

    def bindBankCard(self): #银行卡绑定
        self.userId = "100019459223"
        self.bankCode = "308"
        self.accountNo = "6214830102425235"
        self.authCode = "841589"
        self.token = "c4ca4238a0b923820dcc509a6f75849b"
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.bindBankC%(self.userId , self.bankCode , self.accountNo , self.authCode , self.token , self.sign))
        print(r.text)

    def getBankList(self):  #获取银行列表
        self.token = "c4ca4238a0b923820dcc509a6f75849b"
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.get_bankL%(self.token , self.sign))
        print(r.text)

    def BindEmail(self):    #邮箱绑定
        self.emailUrl = "100019459223@163.com"
        self.token = "c4ca4238a0b923820dcc509a6f75849b"
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.Bemail%(self.emailUrl , self.token , self.sign))
        print(r.text)

    def sDetails(self):     #佣金明细
        self.pageNo = "1"
        self.settleStatus = "0",
        self.settleDate = "2015-05"
        self.subProductType = "2"
        self.token = "d8d479c0b55ca09572330666ee83e1be"
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.settleDetails%(self.pageNo , self.settleStatus , self.settleDate , self.subProductType , self.token , self.sign))
        print(r.text)

    def SxbSd(self):    #随心宝佣金详情
        self.settleDate = "2015-05"
        self.pageNo = 1
        self.pageSize = 1
        self.token = "d8d479c0b55ca09572330666ee83e1be",
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.sxbser %(self.settleDate , self.pageNo ,self.pageSize , self.token , self.sign))
        print(r)

    def MobileExitJ(self):  #查询手机号是否存在(出借人专用)
        self.mobile = "18712267878"
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.MobileExit %(self.mobile , self.sign))
        print(r)

    def checkname(self):    #实名认证(出借人专用)
        self.realname = "308"
        self.documentno = "73984893849308"
        self.mobile = "18712278787"
        self.authCode = "841589"
        self.token = "c4ca4238a0b923820dcc509a6f75849b"
        self.sign = "43640A57B18E842E11C86CF2293F4871"
        r = self.s.get(self.checkN%(self.realname , self.documentno , self.mobile ,self.authCode , self.token , self.sign))
        print(r,r.text)

    def chujie(self): #借咨询与服务协议
        r = self.s.get(self.chujiexy)
        with open('chujie.txt' , 'wb') as f:
            f.write(r.content)

    def shuzi(self):
        r = self.s.get(self.chujiexy)
        with open('shuzi.txt','wb') as f :
            f.write(r.content)

if __name__ == '__main__':
    yx = YiXin()
    yx.chujie()


