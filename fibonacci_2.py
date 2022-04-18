def fibonacci(n):
    if n<=1:
        return n
    else:
        f =  fibonacci(n-1)+ fibonacci(n-2)
        return f
 
 
if __name__ == "__main__":
    print(fibonacci(9))
