#!/usr/bin/env python3

from not_none_functions import return_not_none

# def test_return_not_none():
#     '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
#     assert False

# all the code above this line is the original from git Repo, below is the code I wrote for this new test:
def test_return_not_none():
    '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
    assert return_not_none() != None

