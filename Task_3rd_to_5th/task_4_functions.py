# 1. Write a function welcome() that prints 'Welcome to Python!'.
# 2. Write a function greet(name) that prints 'Hello '.
# 3. Write a function square(n) that returns the square of n.
# 4. Write a function calculator(a, b) that returns the sum, difference, and product of a & b.
# 5. Write a function country(name='India') that prints 'I am from '.
# 6. Write a function total(*nums) that returns the sum of all numbers passed.
# 7. Write a function student_info(**data) that prints key : value for all items.
# 8. Write a function count_vowels(text) that returns the number of vowels in the string.
# 9. Write a lambda function to return the cube of a number.
# 10. Write a function unique_letters(text) that returns unique letters in the order they appear.

#1
def welcome():
    print("Welcome to Python!")

#2
def greet(name):
    print("Hello", name)

#3
def square(n):
    return n * n

#4
def calculator(a, b):
    return a + b, a - b, a * b

#5
def country(name="India"):
    print("I am from", name)

#6
def total(*nums):
    return sum(nums)

#7
def student_info(**data):
    for k, v in data.items():
        print(k, ":", v)

#8
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

#9
cube = lambda x: x ** 3

#10
def unique_letters(text):
    result = ""
    for ch in text:
        if ch not in result:
            result += ch
    return result
