import pytest 
from math_series.series import fibonacci,lucas


def test_one(): 
        actual = fibonacci(1) 
        expected = 1 
        assert actual == expected  

def test_seven():
        actual = fibonacci(7)
        expected = 13
        assert actual == expected 

def test_eight():
        actual = fibonacci(8)
        expected = 21
        assert actual == expected 

def test_two():
        actual = fibonacci(2)
        expected = 1
        assert actual == expected 

def test_one_lucas(): 
        actual = lucas(1) 
        expected = 2
        assert actual == expected  

def test_seven_lucas():
        actual = lucas(7)
        expected = 18
        assert actual == expected 

def test_eight_lucas():
        actual = lucas(8)
        expected = 29
        assert actual == expected 

def test_two_lucas():
        actual = lucas(2)
        expected = 1
        assert actual == expected 

def test_two_sum_series():
        actual = sum_series(2,0,1)
        expected = 1
        assert actual == expected 

def test_three_sum_series():
        actual = sum_series(8,2,1)
        expected = 29
        assert actual == expected  





