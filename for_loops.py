count_even = 0
for i in range(10, 51):
    if i % 3 == 0:
        count_even += 1
# print(count_even)

num1 = 30
num2 = 20
for num in range(num1, num2):
    if num > 5 and num % 2 == 0:
        # print(f"First even number greater than 5: {num}")
        break

for num in range(num1, num2):
    if num % 7 == 0:
        # print(f"First number divisible by 7: {num}")
        break

for i in range(1, 20):
 if i % 2 == 1:
     continue
# print(i)

fruits = ["apple" , "mango", "orange"]
for x in fruits:
    # print(x)


# fruits2 = "mango"
# for y in fruits2:
    # print(y)