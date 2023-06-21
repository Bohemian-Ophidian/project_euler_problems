#The goal of this program is solve the problem 10 in the Project euler problems
#In this code I will be re-using the code from previous code in problem 7
import time
start = time.perf_counter()
def check_prime(n:int)->bool:
    '''to find the whether the given number is prime or not'''
    if n%3==0 or n%5==0 or n%7==0:
        return False
    limit = int(n**0.5)
    for i in range(3,limit+1,2):
        if n%i==0:
            return False
    return True

def prime_sum()->int:
    sum=17
    for num in range(3,2000001,2):
        if check_prime(num):
            sum+=num
        
    return sum

print(prime_sum()) # output : 142913828922
stop = time.perf_counter()
print("time elapsed: ",(stop-start))