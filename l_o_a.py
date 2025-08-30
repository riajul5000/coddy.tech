age = 20
has_license = True
result =  age >= 18 and has_license
# print(result)

a = 5
b = 5 
c = ( a * b) >= (a + b)
# print(c)

b1 = False
b2 = False
b3 = True
c2 = b1 or b2 or ( not b3)
# print(c2)

# Initialize variables
has_license = False
has_space = True 
has_experience = False
# Calculate conditions
can_sell_regular_pet = (has_license or has_experience) and has_space
can_sell_exotic_pet = has_license and has_space and has_experience
cannot_sell_any_pet =(not has_license and not has_experience) or not has_space

# Don't delete the lines below

# print("Can sell regular pet:", can_sell_regular_pet)
# print("Can sell exotic pet:", can_sell_exotic_pet)
# print("Cannot sell any pet:", cannot_sell_any_pet)

# Let's check if a number is NOT (between 1 and 10)
number = 15

# These two expressions are equivalent:
result1 = not (number >= 1 and number <= 10)
result2 = (not number >= 1) or (not number >= 10)

# print(result1) 
# print(result2) 
# i want result3 = false result4 = True
is_student = True
has_experience1 = False

result3 = not (is_student or has_experience1) and is_student or has_experience1
result4 = (not is_student or has_experience1) or (not has_experience1 and is_student)

print(result3)
print(result4)
