#This program is made with the intention to solve the problem number 6 in the
#Project euler programs
#I will be using some mathematical formulas to solve the given problem
#One of the formulas used is summation of squares fromula

def sum_square_difference(n:int)->int:
    '''to find the difference between square of sum and sum of squares of a 
    given series of numbers from 1 to n'''
    sum_of_squares= n*(n+1)*(2*n+1)*1/6 
    #use of formula of summation of squares of a given series from 1 to n
    square_of_sum=(n*(n+1)*0.5)**2
    #use of formula of summation of a given series from 1 to n
    return abs((square_of_sum)-(sum_of_squares))

print(sum_square_difference(10)) #Should result with a output of 2640
print(sum_square_difference(100)) #Should result with a output of 25164150