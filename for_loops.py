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

fruits1 = "mango"
for y in fruits1:
    print(y)

cars = ["porsche" , "bmw" , "mercedes" , "toyota", "Fiat"]
for x in cars:
    # print(x)
    if x == "toyota":
        break

city = ["Rome" , "oslo", "Amsterdam", "Paris" , "Madrid" , "London"]
for x  in city:
    if x == "Paris":
        break
    # print(x)


colors = ["Red" , "Pink" , "Blue" , "yellow", "Black"]
for y in colors:
    if y == "Pink":
        continue
    print(y)

for y in range(6):
    print(y)

for x in range(1, 10):
    print(x)

for u in range(2, 30, 3):
    print(u)

for i in range(5, 30, 2, ):
    print(i)

for w in range( 1, 11):
    print(w)
else:
    print("Finally finished")

for o in range(10):
    if o == 5:
        break
    print(o)
else:
    print("Finally Finished")

country = ["Norway", "France" , "Spain"]
city = ["kattegat", "paris" , "Barcelona" , "Valencia"]

for x in country:
    for y in city:
        print(x ,":", y)

for x in range (0 , 1, 2):
    print(x)
    pass