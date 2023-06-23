import itertools
import math

def div_cal(n:int)->int:
    product = 1
    limit = math.isqrt(int(n))
    for prime in prime_list:
        exponent=0 
        while(not(n%prime)):
            n/=prime
            exponent+=1
        product*=(exponent+1)
        if(n==1)or prime>limit:
            return int(product)
    return product


prime_list = [2,3,5,7]

def prime_check(n:int)->bool:
    global prime_list 
    limit = math.isqrt(n)
    for prime in prime_list:
        if prime>limit:
            break            
        if n%prime==0:
            return False
    prime_list.append(n)
    return True

for i in range(10,500000):
    prime_check(i)

#I will be using the summation formula (n*(n+1))/2 to calculate the triangle
# numbers
divisor = 0
for i in itertools.count(1):
    divisor = 0
    triangle_number = int((i*(i+1))/2)
    divisor = div_cal(triangle_number)
    if(divisor > 500):
        number = triangle_number
        break

print(triangle_number)# should ouput: 76576500


