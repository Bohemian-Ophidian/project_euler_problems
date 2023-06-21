#The goal of this program is find the largest palindrome number made from the
# product of two 3-digit numbers
#This is solution is probably the most ugliest solution out there 
#You have a better chance at bruteforcing the answer than this 
#This solution is just shot in the dark, I dont know how it works either

def find_palindrome(n):
    largest_number=((10**n)-1)**2
    length = len(str(largest_number))
    base = largest_number//(pow(10, length//2))
    while(True):
        base -=1
        reverse_base = str(base)[::-1]
        if length%2==0:
            palindrome = int(str(base)+ reverse_base)
        else:
            palindrome = int(str(base)+ reverse_base[1:-1])
        if factors_less_than_3(palindrome,n):
            break
    return palindrome

def factors_less_than_3(number,n):
    divisor = (10**n)-1
    duplicate = number
    while(divisor>(((10**n)-1)//2)):
        if number%divisor==0:
            break
        else:
            divisor-=1 
    other_divisor = str(duplicate//divisor)
    if len(str(divisor))==n and len(other_divisor)==n:
        return True
    else:
        return False

print(find_palindrome(3))

