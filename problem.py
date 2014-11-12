#!/usr/bin/env python
# encoding: utf-8

class Address(object):
    def __init__(self, city, state):
        self.city = city
        self.state = state
    def __repr__(self):
        return '(%s, %s)' % (self.city, self.state)
class User(object):
    def __init__(self, name, *addresses):
        self.name = name
        self.addresses = addresses
    def __str__(self):
        return self.name
    def find_address(self):
        return self.addresses[0]

class Optional(object):
    def __init__(self, obj):
        self._obj = obj
    def __getattr__(self, attr):
        if self._obj is not None:
            self._obj = getattr(self._obj, attr)
        return self
    def __repr__(self):
        return '<Optional %s>' % self._obj
    def __call__(self, *args, **kwargs):
        self._obj = self._obj(*args, **kwargs)
        return self
    def __getitem__(self, key):
        try:
            self._obj = self._obj[key]
        except:
            self._obj = None
        return self
    def value(self):
        return self._obj

user = User('chong', Address('Tampa', 'FL'), Address('NYC', 'NY'))
print Optional(user).addresses.value()
user = User('chong')
print Optional(user).addresses[2].city.value()
