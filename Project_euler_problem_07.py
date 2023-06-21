#This program is made with the intention of solving the Problem 7 in 
#Project Euler problems
import itertools

def check_prime(n:int)->bool:
    '''to find the whether the given number is prime or not'''
    if n%3==0 or n%5==0 or n%7==0:
        return False
    limit = int(n**0.5)
    for i in range(3,limit+1,2):
        if n%i==0:
            return False
    return True  

def prime_count(n:int)->int:
    '''to find the n th prime number'''
    counter = 4
    for i in itertools.count(9,2):
        if check_prime(i):
            counter+=1
        if counter == n:
            return i

print(prime_count(6)) #Should result with an output of 13
print(prime_count(10001)) #Should result with an output of 104743
