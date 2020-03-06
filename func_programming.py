# Functions are the first class object
# Functions has to be Pure without any side effects
# Ways to limit the use of loops
# Good support for recursion

def home(x):
    def work(y):
        return y+" "+x
    return work

a1 = home
a = a1("Technologies")
b = a("HCL")
c = a("wipro")

print a
print a1
print b
print c
# --------------------------------
aa = lambda x,y: x+ " "+y
bb = aa("HCL","Technologies")

print bb
# --------------------------------


def func1():
    print "I'm in Function 1"


def func2():
    print "I'm in Function 2"


def func3():
    print "I'm in Function 3"

execute = lambda f:f()

ret = map(execute, [func1, func2, func3])

# ---------------------------------
# Reduce
# ex:
#   reduce(func, seq)


li = [1,3,5,7,9]
add = lambda x,y : x+y

sun = reduce(add, li)
print "Sum :", sun

