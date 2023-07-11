#The goal of this program is to print the sum of all amicable numbers under 10k
#This program can be made more easier if one uses theorems to generate the 
# amicable numbers, two of the methods are Thābit ibn Qurra theorem and 
# Euler's rule
# both of the methods can be found on wikipedia, which is exactly where I read 
# about these methods
# but since both those methods are very complex I won't be using them but instead 
# I will be using a more simple strategy 

def sum_divisors(num):
    sum = 0
    for div in range(1,num//2+1):
        if num%div==0:
            sum+=div
    return sum

def amicable_check(limit=10000):
    sum = 0
    for num in range(1, 10001):
        sum_of_divisors = sum_divisors(num)
        if sum_divisors(sum_of_divisors)==num and sum_of_divisors!=num:
            sum+=sum_of_divisors + num
            print(num, sum_of_divisors)
    print(sum/2)

amicable_check()
