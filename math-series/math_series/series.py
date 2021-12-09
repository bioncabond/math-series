def fibonacci(num): 
    """
    This will be fibonacci.
    If number is tested/passed return the integer of the fibonacci sequence 
    If the the function is called with no optional numbers, the first two numbers are a 0 and 1 return the integer of the fibonacci sequence 
    fibonacci(1) -> 1
    fibonacci(7) -> 13
    """
    if num < 0: 
        print("Incorrect Entry.Be more positive.")
    elif num == 0:
        return 0 
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def lucas(num):
    """
    This will be lucas.
    If number is tested/passed return the integer of the lucas sequence
    If the the function is called with optional numbers,the optional two numbers are a 2 and 1 return the integer of the lucas sequence 
    lucas(1) -> 2
    lucas(8) -> 29
    """
    if num <= 0:
        print("Incorrect Entry.Be more positive.")
    if num == 1:
        return 2
    if num == 2:
        return 1
    else:
        return lucas(num-1) + lucas(num-2)

def sum_series(num, num1=0, num2=1):
    """
    This will be sum_series.
    sum_series(8,2,1) -> 29 (lucas number since optional params 2,1)
    sum_series(2,0,1) -> 1 (fibonacci number since optional params 0,1)
    sum_series(5) -> 5 (since no optional parameters were entered defaulted to 0,1 as the optional::fibonacci)
    """
  if num == 0:
    return num1
  if num == 1:
    return num2
  else:
    return (sum_series(num-1, num1, num2)) + (sum_series(num-2, num1, num2))
    

