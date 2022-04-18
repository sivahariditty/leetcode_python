# check_prime(n) checks the given input is prime or not 
# n:int otherwise raise an error
# return boolean
def check_prime(n:int) -> bool:
    """
    Check whether input argument is prime.

    """
    if isinstance(n,int):
        for i in range(2, n//2): # 8 2-->4 ; 11 2-->5
            if(n%i == 0):
                return False
        return True
    else:
        raise TypeError('Input argument should be int type')


check_prime(11)

# write psuedo code while thinking
# PEP 8 - read once again
