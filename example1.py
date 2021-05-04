'''def fix_teen(n):
  if n>= 13 and n<=19 and n != 15 and n !=16:
    return 0
  else:
    return n

def no_teen_sum(a, b, c):
  if fix_teen(n):
        if a >= 13 and a <= 19 and a !=15 and a != 16:
            return b+c
        elif b >=13 and b <=19 and b !=15 and b !=16:
            return a+c
        elif c>=13 and c <=19 and c!=15 and c !=16:
            return b+a
        else:
            return a+b+c

print(no_teen_sum(2, 1, 14))
import pytest

import pytest

def func(num):
    return num * 2

def test_answer():
    assert func(6) == 1
    return test_answer
print(test_answer())
'''
import pytest
import double

def test_answer():
    assert double.func(6) == 12
print(test_answer())