#The goal is to longest collatz sequence of numbers under one million
import itertools
import time
start = time.perf_counter()
sequence = {}
def collatz_gen(n:int)->int:
    global sequence
    num,length = n,0
    for _ in itertools.count(1):
        if n in sequence:
            return length + sequence[n]
        length+=1
        if n==1:
            sequence[num]=length
            return length
        n = (n>>1)*(1-(n%2))+(3*n+1)*(n%2)

max_len = -1
for i in range(1,1000001):
    length = collatz_gen(i)
    if max_len<length:
        max_len=length
        max_int = i
    
print(max_int)#should output : 837799
#this code takes a bit of time if your machine is decent enough it should take around 19 seconds
stop = time.perf_counter()
print("The time elapsed", stop-start)    


