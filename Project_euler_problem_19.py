# The goal of this program is to solve the 19 problem
# The goal of the program is to find the number of sundays between 1 jan 1901 
# and 31 dec 2000
import calendar

print(
    sum(
        list(
            1
            for i in range(1901,2000+1)
            for j in range(1,12+1)
            if calendar.weekday(i,j,1) == 6
            )
        )
    )