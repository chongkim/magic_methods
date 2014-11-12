#!/usr/bin/env python
# encoding: utf-8

class SuperUser(object):
    def __init__(self, name):
        self.name = name
class RegularUser(object):
    def __init__(self, name):
        self.name = name

class User(object):
    def __new__(cls, name):
        if name == 'admin':
            return SuperUser(name)
        else:
            return RegularUser(name)

user = User('admin')
print type(user)

user = User('ckim')
print type(user)
