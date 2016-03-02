# -*- coding: utf-8 -*-
import datetime
import time
import threading
import requests


class url_request():
    times = []
    error = []
    def __init__(self):
        self.s = requests.Session()

    def req(self):
        yl = url_request()
        url = 'https://testerhome.com/'
        r = self.s.get(url)
        ResponseTime = float(r.elapsed.microseconds) / 1000  # 获取响应时间，单位ms
        yl.times.append(ResponseTime)  # 将响应时间写入数组
        if r.status_code != 200:
            yl.error.append("0")

if __name__ == '__main__':
    yl = url_request()
    threads = []
    starttime = datetime.datetime.now()
    print("request start time %s" % starttime)
    nub = 200  # 设置并发线程数
    ThinkTime = 0.2  # 设置思考时间
    for i in range(1, nub + 1):
        t = threading.Thread(target=yl.req)
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
    # print "thread %s" %t #打印线程
        t.setDaemon(True)
        t.start()
        t.join()
    endtime = datetime.datetime.now()
    print("request end time %s" % endtime)
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(yl.times)) / float(len(yl.times)))  # 计算数组的平均值，保留3位小数
    print("Average Response Time %s ms" % AverageTime)  # 打印平均响应时间
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour) * 60 * 60 + float(minute) * 60 + float(second)  # 计算总的思考时间+请求时间
    print("Concurrent processing %s" % nub)  # 打印并发数
    print("use total time %s s" % (totaltime - float(nub * ThinkTime)))  # 打印总共消耗的时间
    print("fail request %s" % yl.error.count("0")) # 打印错误请求数