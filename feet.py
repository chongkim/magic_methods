#!/usr/bin/env python
# encoding: utf-8

class Feet(object):
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return '%d ft' % self.n
    def __add__(self, other):
        return Feet(self.n + other.n)

print Feet(1) + Feet(2)

