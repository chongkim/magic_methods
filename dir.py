#!/usr/bin/env python
# encoding: utf-8

import os

class Dir(object):
    def __init__(self, path):
        self.path = path
        self.orig = os.getcwd()
    def __enter__(self):
        os.chdir(self.path)
    def __exit__(self, exc_type, exc_obj, traceback):
        os.chdir(self.orig)

dir = Dir(os.getcwd() + '/backup')
print os.getcwd()
with dir:
    print os.getcwd()
print os.getcwd()
