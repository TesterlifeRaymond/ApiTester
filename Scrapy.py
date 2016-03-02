import urllib.request as request  

import html.parser as htmlParser

#import re
import pymysql

import time

import json
#mainUrl = 'http://cha.17173.com/dnf/list?o=equip'

url = 'http://cha.17173.com/dnf/index/tips/c/UTF-8/t/equip/l/zhCN/id/'
#
#Regex_id = re.compile(r'/dnf/info/equip/[\d]+')
#
#class AnalysisPage(htmlParser.HTMLParser):
#    def __init__(self):
#        super(AnalysisPage, self).__init__()
#        self.ID_list = []
#    
#    def handle_starttag(self,tag,attrs):
#        if tag == 'a':
#            self.ID_list.append(Regex_id.match(dict(attrs).get('href', '')))
#
class AnalysisData(htmlParser.HTMLParser):
    def __init__(self):
        super(AnalysisData, self).__init__()
        self.dataName = ''
        self.tagList = []
        self.data = {'a':[], 'b':[], 'c':[]}
        self.dataType = ''
    
    def handle_starttag(self,tag,attrs):
        attrs = dict(attrs)
        if tag == 'span':
            if attrs.get('class', '') == 'tips-n':
                self.tagList.append(tag)
                self.dataName = 'name'
            elif attrs.get('class', '') == 'tips-i':
                self.tagList.append(tag)
                self.dataName = 'id'
        elif tag == 'div':
            if attrs.get('class', '') == 'arguments arguments0':
                self.tagList.append(tag)
                self.dataName = 'a'
            elif attrs.get('class', '') == 'arguments arguments1':
                self.tagList.append(tag)
                self.dataName = 'b'
        elif tag == 'p':
            if not ('class' in attrs):
                self.tagList.append(tag)
    def handle_endtag(self, tag):
        if self.tagList and self.tagList[-1] == tag:
            self.tagList.pop()
    
    def handle_data(self,data):
        if self.tagList and data.replace('\t', ''):
            if self.dataName == 'name':
                self.data['name'] = data
            elif self.dataName == 'id':
                self.data['ID'] = data.split(':')[1]
            elif self.dataName == 'a':
                self.data['a'].append(data.split(' '))
            elif self.dataName == 'b':
                if data == '装备属性：':
                    self.dataType = 'a'
                    return 
                elif data == '附加属性：':
                    self.dataType = 'b'
                    return 
                if self.dataType == 'a':
                    self.data['b'].append(data.split(' '))
                elif self.dataType == 'b':
                    self.data['c'].append(data.replace(' ', ''))
#ap = AnalysisPage()
#s = []
#for page in range(1, 766): #766
#    data = request.urlopen(mainUrl + '&page=' + str(page)).read().decode('utf8')
#    ap.feed(data)
#    for id in (i.group().split('/')[-1] for i in ap.ID_list if i):
#        if not (id in s):
#            s.append(id)
#        try:
#            data = request.urlopen(url + id).read().decode('utf8')
#            ad = AnalysisData()
#            ad.feed(data)
#            db[id] = ad.data
#            time.sleep(0.05)
#        except BaseException as e:
#            print(id, e)
##    with open('data_%d.json' %page, 'w') as f:
##        json.dump(db, f, indent = 2, ensure_ascii=False)
#with open('id.txt', 'w') as f:
#    f.write(','.join(s))


#create table equipment(
#    id varchar(10) not null primary key, 
#    name varchar(30), 
#    mainClass varchar(10), 
#    subClass varchar(10),
#    bindingType varchar(10),
#    rarity varchar(10), 
#    weight float(5,2)
#);
#create table equipment_attr(
#    eq_id varchar(10),
#    attrName varchar(15),
#    attrValue varchar(15) 
#);
#create table add_attr(
#    eq_id varchar(10),
#    attrValue varchar(80) 
#);
#


parameters = {
    'user':'root',
    'passwd':'',
    'db':'DNF_Game_Data',
    'charset':'utf8'
}
parameters['passwd'] = input('请输入数据库密码：')
con = pymysql.Connect(**parameters)
cur = con.cursor()

with open('id.txt', 'r') as f:
    l = f.read().split(',')
for id in l:
    try:
        data = request.urlopen(url + id).read().decode('utf8')
        ad = AnalysisData()
        ad.feed(data)
        cur.execute("INSERT INTO equipment VALUES('%s','%s','%s','%s','%s','%s','%0.2f')" %(
            ad.data['ID'],
            ad.data['name'], 
            ad.data['a'][0][1],
            ad.data['a'][1][1],
            ad.data['a'][2][1],
            ad.data['a'][3][1],
            float(ad.data['a'][4][1][:-2])
        ))
        for eq_attr in ad.data['b']:
            cur.execute("INSERT INTO equipment_attr VALUES('%s','%s','%s')" %(
                ad.data['ID'],
                eq_attr[0],
                eq_attr[1]
            ))
        for add_attr in ad.data['c']:
            cur.execute("INSERT INTO add_attr VALUES('%s','%s')" %(
                ad.data['ID'],
                add_attr
            ))
        con.commit()
    except BaseException as e:
        with open('log.txt', 'a') as f:
            f.write('id:%s   [%s]'%(id, e))
input()
