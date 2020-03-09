
# write fibonocci number function

from timeit import Timer

def fact(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        sum = n * fib(n-1)
    return sum


def fib(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibi(n):
    old,new = 0,1
    if n==0:
        return 0
    for i in range(n-1):
        #print i
        old,new = new, old + new
    return n

print(fibi(5)) # => this will be faster to execute

print(fib(5))

# Form a pascals triangle

