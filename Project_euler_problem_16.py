#The goal of this program is to solve the 16th problem in the project euler 
#problems
import time
start = time.perf_counter()
value = 1<<1000
result = sum([int(x) for x in str(value)])
stop = time.perf_counter()
print("The time elapsed:", stop-start)
print(result)



