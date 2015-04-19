#coding:utf8
__author__ = 'hao.jiang'


import os
import sys
import thread
import requests
import socket
import logging
import logging.handlers

ISDEBUG = True
PORT = 5000  # default proxy server port
HOST = '127.0.0.1'
LOG_FILE = 'proxy.log'
LOG_LEVER = logging.INFO

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024*1024, backupCount=5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('proxy')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def print_log(tip, variable, tp=True, model=ISDEBUG, level=LOG_LEVER):  # tp: True--print xx; False--print repr(xx)
    if model:
        print '＊'*40, '>', tip, '<', '＊'*40
        content = variable if tp else repr(variable)
        print content
        print '*'*40, '> end ', tip, '<', '*'*40
        logger.log(level, ''.join(('*'*40, '>', tip, '<', '*'*40)))
        logger.log(level, variable)
        logger.log(level, ''.join(('*'*40, '> end ', tip, '<', '*'*40)))





def main():
    serverport = int(sys.argv[2]) if len(sys.argv) >= 2 else PORT
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, serverport))
    print_log('proxy server', 'start')

    try:
        client_conn, source_address = server.accept()
        thread.start_new_thread()


if __name__ == "__main__":
    main()

