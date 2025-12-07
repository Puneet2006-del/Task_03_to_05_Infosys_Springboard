# 1. Print numbers from 1 to 10 using a for loop.
# 2. Print all even numbers from 1 to 20.
# 3. Print each character of the string: 'Python'.
# 4. Using a while loop, print numbers from 5 down to 1.
# 5. Write a loop to find the sum of numbers from 1 to 50.
# 6. Print the multiplication table of 5 (from 5×1 to 5×10).
# 7. Find how many vowels are present in the string 'Programming'.
# 8. Use a loop to reverse the string 'PythonLoops'.
# 9. Print numbers from 1–10, but skip 5 using continue.
# 10. Print numbers from 1–20, but stop when number reaches 13 using break.
# 11. Write a loop to check if a number is prime.
# 12. Count how many times each character occurs in 'mississippi'.
# 13. Using nested loops, print the pattern: *, **, ***, ****, *****.
# 14. Write a loop to find the largest digit in the number 5847361.
# 15. Write a loop to print the pattern: *****, ****, ***, **, *.

#1
for i in range(1, 11):
    print(i)

#2
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#3
for ch in "Python":
    print(ch)

#4
i = 5
while i >= 1:
    print(i)
    i -= 1

#5
total = 0
for i in range(1, 51):
    total += i
print(total)

#6
for i in range(1, 11):
    print(5 * i)

#7
word = "Programming"
vowels = "aeiouAEIOU"
count = 0
for ch in word:
    if ch in vowels:
        count += 1
print(count)

#8
text = "PythonLoops"
rev = ""
for ch in text:
    rev = ch + rev
print(rev)

#9
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#10
for i in range(1, 21):
    if i == 13:
        break
    print(i)

#11
num = int(input("Enter a number: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
print("Prime" if is_prime else "Not Prime")

#12
text = "mississippi"
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
print(count)

#13
for i in range(1, 6):
    print("*" * i)

#14
num = "5847361"
largest = 0
for digit in num:
    if int(digit) > largest:
        largest = int(digit)
print(largest)

#15
for i in range(5, 0, -1):
    print("*" * i)
