def PrintFibonacci(n,second_last,last):
    if(n-1 == 0):
        return second_last
    else:
        new_last = second_last + last
        return PrintFibonacci(n-1,last,new_last)

print(PrintFibonacci(8,0,1))
