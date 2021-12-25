#Find the sum of digits in an integer
def get_sum_digits(num):
    """
    Get sum of digits in integer
    
    Args:
        num (int): integer to get sum of digits of
    
    Returns:
        int: sum of digits in integer
    """
    s = 0
    x1 = num % 10
    num//=10
    
    x2 = num % 10
    num//=10

    x3 = num % 10
    num//=10

    x4 = num % 10
    num//=10

    x5 = num % 10
    num//=10
    
    s = x1+x2+x3+x4+x5
    
    # return sum of digits in integer
    return  s
x=get_sum_digits(24)
print(x)