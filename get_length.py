#get number of digits in an int?
def get_length(num):
    """
    Get length of integer

    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    k=6
    
    num//=10
    k-=pow(0,num)
    
    num//=10
    k-=pow(0,num)

    num//=10
    k-=pow(0,num)

    num//=10
    k-=pow(0,num)


    # return number of digits in integer
    return k



print(get_length(10000))
 
