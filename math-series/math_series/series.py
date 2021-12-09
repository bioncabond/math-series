def fibonacci(num): 
    ##base value
    if num < 0: 
        print("Incorrect Entry.Be more positive.")
    elif num == 0:
        return 0 
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)


def lucas(num):
    if num <= 0:
        print("Incorrect Entry.Be more positive.")
    if num == 1:
        return 2
    if num == 2:
        return 1
    else:
        return lucas(num-1) + lucas(num-2)

def sum_series(num, num1=0, num2=1):
  if num == 0:
    return num1
  if num == 1:
    return num2
  else:
    return sum_series(num-1, num1, num2) + (sum_series(num-2, num1, n2))
    

