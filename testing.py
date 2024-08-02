from os import path

PROJ_DIR = '.'

def case1():
	assert path.isfile(path.join(PROJ_DIR, 'file1'))
	assert path.isfile(path.join(PROJ_DIR, 'file2'))
	assert path.isfile(path.join(PROJ_DIR, 'file3'))

try:
	case1()
except AssertionError as e:
	print('Test: failure.')
else:
	print('Test: success.')
