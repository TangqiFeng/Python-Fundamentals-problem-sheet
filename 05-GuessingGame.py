# There are conditions:
# 1.the system generate a secret number.
# 2.compare guess number and secret number, give feedback, too large/small
# 3.figure out the number of tries
# 4.avoid the number of tries if input the same number multiple times consecutively

# adapt from website https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

# define the secret number range: 1~100, type: int
from random import randint
print(randint(1,100))