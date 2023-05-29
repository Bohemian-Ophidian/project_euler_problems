def multipleOf3_5(number):
    '''to find the multiples of 3 and/or 5'''
    if number%3==0 or number%5==0:
        return number
    return 0

def summation(upperbound):
    '''to find the sum of multiples of 3 and/or 5'''
    sum = 0 
    for number in range(upperbound):
        sum+= multipleOf3_5(number)
    return sum

print(summation(10)) #should output as 23

print(summation(49)) #should output as 543

print(summation(1000)) #should output as 233168

print(summation(8456)) #should output as 16687353

print(summation(19564)) #should output as 89301183