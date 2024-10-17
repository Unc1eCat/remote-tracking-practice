#! /bin/python3.10

from os import path
from datetime import datetime

PROJ_DIR = '.'

def case1():
	assert path.isfile(path.join(PROJ_DIR, 'file1'))
	assert path.isfile(path.join(PROJ_DIR, 'file2'))
	assert path.isfile(path.join(PROJ_DIR, 'file3'))

try:
	case1()
except AssertionError as e:
	with open(path.join(PROJ_DIR, 'test.report'), 'a') as reportf:
		reportf.write('[' + str(datetime.now()) + ']  -  ' + 'Test: failure.\n')
	print('Test: failure.')
else:
	with open(path.join(PROJ_DIR, 'test.report'), 'a') as reportf:
		reportf.write('[' + str(datetime.now()) + ']  -  ' + 'Test: success.\n')
	print('Test: success.')
