# Decorators are used in logging and find the Time taken for execution
from functools import wraps


def my_logger(func):
    import logging
    logging.basicConfig(filename='{}'.format(func.__name__ +".log"), level=logging.INFO)
    @wraps(func)   # This line will prevent creating a new log file when using double wrapper
    def wrapper(*args, **kwargs):
        logging.info("Executing function {0} with args {1} and kwargs {2}".format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return wrapper

def my_timer(func):
    import time
    start_time = time.time()
    @wraps(func)  # This line will prevent creating a new log file when using double wrapper
    def wrapper(*args, **kwargs):
        print("Start executing the function {} with args ".format(func.__name__, args, kwargs))
        res = func(*args, **kwargs)
        print("Time to execute the function {} is {} ".format(func.__name__, time.time() - start_time))
        return res
    return wrapper

@my_timer
@my_logger
def caller(name, age=0):
    print("Name : {0} Age : {1}".format(name, age))


caller("Hen", 4)
