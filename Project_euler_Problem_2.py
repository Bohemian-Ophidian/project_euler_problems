#The goal of this program is to find the sum even fibonacci number, where 'n'
# is the limit for the highest value in fibonacci series.
#Also 'n' must not exceed four million
#This is not the most elegant solution to the problem.
n = int(input("Please enter the limit of the program:"))

def fibo_gen(first=1, second=1):
    if second>n:
        return 0
    if second%2==0:
        return second+fibo_gen(second, first+second)
    else:
        return 0+fibo_gen(second,first+second)

print(fibo_gen())

