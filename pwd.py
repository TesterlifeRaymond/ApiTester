#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2016-03-21 09:36:17
import threading
from random import choice
import string
import time 

#python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters

def GenPassword(length=8,chars=string.ascii_letters+string.digits):
    for x in range(100):    
        return ''.join([choice(chars) for i in range(length)])


if __name__=="__main__":
    threads = []
    num = 999
    
    for i in range(1,num + 1):
        t = threading.Thread(target=GenPassword)
        threads.append(t)
    
    with open('pwd.txt','a') as f:   
        for t in threads:
            t.start()
            print(time.time())
            f.write(GenPassword(8)+"\n")
            print(GenPassword(8))  
            t.join()
    
