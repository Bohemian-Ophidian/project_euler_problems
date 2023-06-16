#the point of this program is find the smallest multiple of a number
#This is program is built to solve the problem 5 of project euler problems
#funny enough I got this right in the first try 

def least_common_multiple(n:int)->int:
    '''to find the smallest multiple that is evenly divisible by numbers from 1 to n'''
    multiple=1
    for number in range(1,n+1):
        if(multiple%number==0):
            continue
        elif not(is_prime(number)):
            multiple*=number/(multiple%number)
        else:
            multiple*=number
    return multiple

def is_prime(n:int)->bool:
    '''To find whether the given number is prime or not'''
    if n==2:
        return True
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

print(least_common_multiple(10))# Result with the output of 2520
print(least_common_multiple(20))# Result with the output of 232792560