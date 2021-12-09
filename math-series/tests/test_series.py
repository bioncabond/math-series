import pytest 
from math_series.series import fibonacci,lucas, sum_series

# “”” 
# (<-Called doc string. Have a good description of what the function is doing)
# This will be math series.
# If number is tested/passed return the integer of the fibonacci sequence 
# If number is tested/passed return the integer of the lucas sequence 
# If the the function is called with no optional numbers, the first two numbers are a 0 and 1 return the integer of the fibonacci sequence 
# If the the function is called with optional numbers,the optional two numbers are a 2 and 1 return the integer of the lucas sequence 
# fibonacci(1) -> 1
# fibonacci(7) -> 13
# lucas(1) -> 2
# lucas(8) -> 29
# sum_series(8,2,1) -> 29 (lucas number since optional params 2,1)
# sum_series(2,0,1) -> 1 (fibonacci number since optional params 0,1)
# “””







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
        expected = 47
        assert actual == expected  
def test_none_sum_series():
        actual = sum_series(5)
        expected = 5
        assert actual == expected  





