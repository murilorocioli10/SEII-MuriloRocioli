import my_module as mm
courses = ['History', 'Math', 'Physics', 'CompSci']
index = mm.find_index(courses, 'Math')
print(index)

from my_module import find_index as fi, test #fi -> find_index
courses = ['History', 'Math', 'Physics', 'CompSci']
index = fi(courses, 'Math')
print(index)
print(test)

from my_module import * # the '*' imports everything
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(index)
print(test)

from my_module import *
import sys
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(sys.path)

import random
courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)

import math
courses = ['History', 'Math', 'Physics', 'CompSci']
rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2021))

import os
print(os.getcwd())
print(os.__file__)

import antigravity


print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    
    return -1
