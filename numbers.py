# x = 5
# y = 10
# z = (x*y)

# # print(z)



# a = 50
# b = 70
# # print(a*b)


# c = 689
# d = 700
# e = (d - c)
# f = (e + 20)

# print(f)

# Read input string

numbers_str = input( 1, 2 , 3)

# Split into list of strings
numbers_list = numbers_str.split(", ")

# Convert to integers
numbers = [int(num) for num in numbers_list]

# Calculate sum
total = sum(numbers)

# Print result
print(total)
