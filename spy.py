#!/usr/bin/env python
# encoding: utf-8

import inspect

class Spy(object):
    def __get__(self, obj, obj_type):
        frame = inspect.currentframe()
        info = inspect.getframeinfo(frame.f_back)
        print 'get %s:%d' % (info.filename, info.lineno)
        return 1
    def __set__(self, obj, value):
        frame = inspect.currentframe()
        info = inspect.getframeinfo(frame.f_back)
        print 'set %s:%d' % (info.filename, info.lineno)

class Foo(object):
    x = Spy()
    def __init__(self, n):
        self.x = n

foo = Foo(1)

foo.x = 12
y = foo.x + 1

foo.x = 12
y = foo.x + 1
