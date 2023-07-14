#the goal of this program is find the index of the first number in fibonacci 
# series with 1000 digits 
import itertools
import time
start = time.perf_counter()

def fib_gen():
    f0, f1, fn = 1, 1, None
    for index in itertools.count(3):
        fn = f0 + f1
        if(len(str(fn))==1000):
            break
        f0 = f1
        f1 = fn
    return index

print(fib_gen())#should generate an output of 4782
stop = time.perf_counter()

print("Time elapsed: {}".format(stop - start))