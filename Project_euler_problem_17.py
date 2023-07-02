#The goal of this program is to find out how many letters are used if numbers 
# from 1 to 1000 are written in words
import time
start = time.perf_counter()
numbers = {
    0:'', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand',
}

def letter_count(limit:int=1000)->int:
    sum = 0
    for num in range(1,limit+1):
        last_two_digits=num%100
        if len(str(num))==3:
            hundreds = num//100
            conjunctor = 3 #variable that accounts for 'and' length
            if last_two_digits==0:#this checks whether we should length of 'and' or not
                conjunctor = 0
            sum += len(numbers[hundreds])+len(numbers[100])+conjunctor
        if last_two_digits>20:
            tens = (last_two_digits)//10
            ones = (last_two_digits)%10
            sum +=len(numbers[tens*10])+len(numbers[ones])
        elif(last_two_digits!=0):
            tens = last_two_digits
            sum +=len(numbers[tens])
        if num == 1000:
            sum+=len(numbers[1])+len(numbers[1000])
    return sum

print(letter_count())
stop = time.perf_counter()

print("The time elapsed:",stop-start)
