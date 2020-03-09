# implementing polynomial
# p(x) = a.x*x + b.x + c


def polynomial_func(a,b,c):
    def poly(x):
        return (a*x**2 + b*x + c)
    return poly


nm1 = polynomial_func(-1, 2, 2)
nm2 = polynomial_func(2, 1, 0)

print (nm1)
print (nm2)

print(nm1(2))
print(nm2(5))

# Simple Decorator

def wrapper(func):
    def func_wrapper(x):
        print ("Before calling the function")
        res = func(x)
        print ("After calling the function")
        return res
    return func_wrapper

@wrapper
def foo(x):
    print ("Im in function foo with arg : " + str(x))

foo("hi")



