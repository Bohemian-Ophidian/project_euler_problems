import math
import time
# Properties that are important to know 
# multiples of abundant numbers are also abundant numbers
# every multiple of perfect number is abundant
start = time.perf_counter()
abundant_numbers = []
for num in range(1,28124):
    # checking for abundant numbers
    limit = math.isqrt(num)
    sum_of_div = 1
    for div in range(2,limit+1):
        
        if num%div ==0:
            if (div**2)==num:
                sum_of_div+=div
            else:
                sum_of_div+=div+(num//div)
    if sum_of_div <=num:
        continue
    abundant_numbers.append(num)

#addition
sums_of_abundant = []
for i, num in enumerate(abundant_numbers):
    for number in abundant_numbers[i:]:
        addition = num+number
        if addition <=28123:
            sums_of_abundant.append(addition)
sum_of_nonAb=0
for num in range(28124):
    if num in sums_of_abundant:
        continue
    sum_of_nonAb+=num

print(sum_of_nonAb)# it is a slow operation taking about 2 minutes and 50 seconds
# should give an output of 4179871
stop = time.perf_counter()
print(stop - start)

