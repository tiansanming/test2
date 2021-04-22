# coding:utf-8


def func(x):
	return x + 3


def test_func_0():
	src = 0
	expect = 3
	assert func(src) == expect


def test_func_1():
	src = 0.1
	expect = 3.1
	assert func(src) == expect


def test_func_2():
	src = -1
	expect = 0
	assert func(src) == expect