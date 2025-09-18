def my_function():
    print("Hello from a functions")
# my_function()

def my_city():
    print("Rome")
# my_city()

def my_fall():
    print("Hello World")
n = 5
# for i in range(n):
#  my_fall()

num1 = 3
num2 = 5
def my_count(num1, num2):
    print(num1 / num2)
# my_count(num1, num2)


n = 5
def square_number(n):
    return n * n
result = square_number(5)
# print(result)


def cube_number(n):
    return n ** 3
input_num = 89
result = cube_number(input_num)
# print(result)


def sigma(n):
    sum = 0
    for i in range(1, n + 1):
     sum += i
    return sum 
result = sigma(5)
# print(result)


def count_numbers(x):
    total = 0
    for i in range(10, x):
     total += i
    return total
result1 = count_numbers(60)
# print(result1)

def have_car(y):
   total = 1
   for i in range(20, y):
      total *= i
   return total
result = have_car(60)
# print(result)


def tour_area(z):
   total = 7
   for i in range(10, z):
      total /= i 
   return total
result = tour_area(70)
print(result)