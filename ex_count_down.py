import time
import sys


def sleep_time(n):
    for remaining in range(n, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.flush()


#sleep_time(5)

sleep = sleep_time

n = 30
print "The script will wait for %s seconds to start recording" %n
sleep(n)
