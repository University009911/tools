'''
@file        :Log.py
@description :Log module
@time        :2020/12/10 11:58:22
@author      :Hanqing Chen
@version     :1.0
@update      :2020/12/10
'''

import time
import logging
import os
import threading
class Log(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        date_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        dirname = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(dirname,'log')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_file = os.path.join(log_dir,date_time+'.log')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - %(message)s",
            datefmt = "%m/%d/%Y %H:%M:%S %p")
        fh = logging.FileHandler(self.log_file, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Log, "_instance"):
            with Log._instance_lock:
                if not hasattr(Log, "_instance"):
                    Log._instance = object.__new__(cls)
        return Log._instance

    def _console(self,level,message):
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

    def debug(self,message):
        self._console('debug', message)

    def info(self,message):
        self._console('info', message)

    def warning(self,message):
        self._console('warning', message)

    def error(self,message):
        self._console('error', message)

logger = Log()
