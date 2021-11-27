# IN: student's grade 1..10
# OUT: good, ok, bad

# x -----> x -----> x-----> x
# 1        5        7      10

import math

grade = int(input("Your grade : "))
if grade > 7 and grade <= 10:
     print("GOOD :")
elif grade > 4 and grade <= 7:
    print("OK! :")
elif grade > 1 and grade <= 4:
    print("BAD! :")
else:
    grade > 10
    print("WRONG VALUR") 
    # HW3 : continue wich -WROUNG VALUE