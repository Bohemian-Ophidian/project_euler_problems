#The goal of this program is find the largest prime factor of the number
#600851475143

#This is not a very efficient solution to the problem, I tried recursion but 
# then I learned that maximum recursion depth in python is limited to 1000
# And that python stackframes are very heavy therefore recursion wasnt the 
# better method to solve the problem.

def prime_factor(number):
    divisor = 2
    while(number>1):
        if number%divisor==0:
            number/=divisor
        else:
            divisor+=1

    print("The largest prime factor is ",divisor)

prime_factor(13195)# gives the output of 29
prime_factor(600851475143) # gives the output of 6857
