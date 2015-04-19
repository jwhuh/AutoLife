#coding:utf8
import threading
__author__ = 'hao.jiang'


class ProxyHandler(threading.Thread):

    def __init__(self, client_conn):
        super(ProxyHandler, self).__init__()
        self.client = client_conn

    def run(self):
        self.get_request()
        pass

    def get_request(self):


