
"""
    这个脚本服务是为后台数据与需求方数据做对比的脚本服务
    该脚本服务是用多线程+queue队列实现
"""

import queue
import threading

Q = queue.Queue()   #当有多个线程共享一个东西的时候就可以用它了
NUM_WORKERS = 4

class MyThread(threading.Thread):
    """
        多线程处理对比excel类
    """
    def __init__(self, job, work):
        """

        :rtype: object
        """
        self._job = job
        self._work = work
        threading.Thread.__init__(self)

    def run(self):
        """
            执行测试脚本
        """
        while 1:
            if self._job.qsize() > 0:
                self._process_job(self._job.get(), self._work)
            else:
                break

    def _process_job(self, job, work):
        """
            这是队列中的任务情况
        :param job:
        :param work:
        :return:
        """
        return self.do_job(job, work)

    def do_job(self, job, work):
        """
            这是脚本要做的事情
        :param job:
        :param work:
        :return:
        """
        print("doing", job, " work ", work)

if __name__ == '__main__':
    for i in range(NUM_WORKERS * 2+1):
        Q.put(i)    #放入到任务队列中去

    for x in range(NUM_WORKERS):
        MyThread(Q, x).start()
