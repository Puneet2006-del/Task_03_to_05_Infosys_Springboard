# 1. Use math.sqrt() to find the square root of a number.
# 2. Use math.floor() and math.ceil() to round 5.67.
# 3. Generate a random number between 1 and 100.
# 4. Print 5 random integers between 10 and 20.
# 5. Print today’s date using datetime.date.today().
# 6. Print the current year, month, and day separately.
# 7. Print the current working directory using os.getcwd().
# 8. List all files in the current directory using os.listdir().
# 9. Print the current Python version using sys.version.
# 10. Convert a JSON string to a dictionary using json.loads().
# 11. Use math functions to compute cos(0), sin(90°), and log(10).
# 12. Simulate rolling a dice 10 times and store the results.
# 13. Print how many days are left for your next birthday.
# 14. Convert the date '2022-05-15' to a datetime object and add 30 days.
# 15. Create a new folder named 'backup' using os.mkdir().
# 16. Convert a dictionary to JSON using json.dumps().
# 17. Use regex to extract all digits from a string.
# 18. Check if a string starts with 'Hello' using regex.
# 19. Find mean, median, and mode using the statistics module.
# 20. Measure execution time of a loop from 1 to 1,000,000 using time module.

#1
import math
print(math.sqrt(25))

#2
print(math.floor(5.67))
print(math.ceil(5.67))

#3
import random
print(random.randint(1, 100))

#4
for _ in range(5):
    print(random.randint(10, 20))

#5
from datetime import date
print(date.today())

#6
today = date.today()
print(today.year, today.month, today.day)

#7
import os
print(os.getcwd())

#8
print(os.listdir())

#9
import sys
print(sys.version)

#10
import json
data = '{"name":"John","age":25}'
print(json.loads(data))

#11
print(math.cos(0))
print(math.sin(math.radians(90)))
print(math.log(10))

#12
dice_rolls = []
for _ in range(10):
    dice_rolls.append(random.randint(1, 6))
print(dice_rolls)

#13
birthday = date(today.year, 12, 7)
if birthday < today:
    birthday = date(today.year + 1, 12, 7)
print((birthday - today).days)

#14
from datetime import datetime, timedelta
d = datetime.strptime("2022-05-15", "%Y-%m-%d")
print(d + timedelta(days=30))

#15
os.mkdir("backup")

#16
my_dict = {"name": "Alice", "age": 22}
print(json.dumps(my_dict))

#17
import re
text = "My number is 987654"
print(re.findall(r'\d+', text))

#18
print(bool(re.match(r'^Hello', "Hello world")))

#19
import statistics
nums = [2, 3, 5, 3, 8, 3]
print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))

#20
import time
start = time.time()
for i in range(1, 1000001):
    pass
end = time.time()
print(end - start)
