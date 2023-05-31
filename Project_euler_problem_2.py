#The goal of this program is to find the sum even fibonacci number, where 'n'
# is the limit for the highest value in fibonacci series.
#Also 'n' must not exceed four million
#This is not the most elegant solution to the problem.
n = int(input("Please enter the limit of the program:"))

def fibo_gen(first=1, second=1):
    '''to find the sum of even fibonacci numbers'''
    if second>n:
        return 0
    if second%2==0:
        return second+fibo_gen(second, first+second)
    else:
        return 0+fibo_gen(second,first+second)

print(fibo_gen())

#n = 8 ; should result with an output of 10 
#n = 10; should result with an output of 10
#n = 34; should result with an output of 44
#n = 60; should result with an output of 44
#n = 1000; should result with an output of 798
#n = 100000; should result with an output of 60696
#n = 4000000; should result with an output of 4613732
