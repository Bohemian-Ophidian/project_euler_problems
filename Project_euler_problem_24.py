# The goal of this program is find the 1 millionth lexicographic 
# permutation of the digits 0,1,2,3,4,5,6,7,8,9
import itertools

for i,x in enumerate(itertools.permutations('0123456789')):
    if i==999999:
        break

str = ''
for ele in x:
    str += ele

print(str) #should give an output of 2783915460