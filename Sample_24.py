# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:57:49 2019

@author: Xandr
"""
#Перевірити час запиту до сайта
def test (func):
    import time
    
    def _test():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print('Час запиту', end-start)
    return _test

@test
def webpage():
    import requests
    page = requests.get('http://www.estudysystem.pp.ua/moodle/')
    return None

webpage()