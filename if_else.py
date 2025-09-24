#  I want result: 270
a = 20 
b = 20
c = 0
if a <= b and not b <= 10 :
    c = 3

c *= 90
# print(c)

# The variables a and b have missing values. Fill them so that the code inside the if statement will be executed! (make sure the if condition is true)

# At the end of the program, the value of c should be 3.

a1 =10
b1 = 5
c = 0

if a > b or b >= 10:
    c = 2

    c += 1
    # print(c)

    age = 15
status = "None"
if age >= 18:
    status = "Adult"
else:
    status = "Young"
    # print(status)

# You are given a code which gets as input two numbers n1 and n2 and a character op.

# Note: we will learn in next lessons how to get input from the user, currently just don't touch the three first lines.

 

# The possible values for op are '+', '-', '/' and '*'

# Your task is to set the variable result based on the conditions:

# if op is '+', set result with n1 + n2.
# if op is '-', set result with n1 - n2.
# if op is '/', set result with n1 / n2.
# if op is '*', set result with n1 * n2.

n1 = 20
n2 = 20
result = 0

if result == "+":
    count = n1 + n1
elif result == "-":
    count = n1 - n2
else :
    count = n1 * n2
    # print(count)

numbers = 50
if numbers % 2 != 0:
    print("even")
else:
    print("odd")