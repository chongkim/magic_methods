#!/usr/bin/env python
# encoding: utf-8

class Logger(object):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.msgs = []
        return cls._instance
    def info(self, msg):
        self.msgs += [msg]

logger = Logger()
logger.info('good')

logger = Logger()
logger.info('bad')

print logger.msgs
