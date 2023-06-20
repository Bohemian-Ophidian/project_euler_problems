#The goal of this program is to solve the problem 9 in project euler problems
#We have to find the product of pythogorean triplets which also sum up to 1000
#I have a different approach here instead of check for pythogorean triplets
#I simply generate triplets and check for required condition

import itertools
def find_triplets()->int:
    '''This function uses Euclid's formula to generate pythogorean triplets.
    Euclid's formula is a fundamental formula for generating Pythagorean 
    triples given an arbitrary pair of integers m and n with m > n > 0.'''
    for m in itertools.count(1):
        for n in range(m):
            if(2*(m**2)+2*m*n)==1000:
                return((m**2)-(n**2))*(2*m*n)*((m**2)+(n**2))
    

print(find_triplets())#Should give an output of 31875000