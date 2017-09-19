# There are conditions:
# 1.the system generate a secret number.
# 2.compare guess number and secret number, give feedback, too large/small
# 3.figure out the number of tries
# 4.avoid the number of tries if input the same number multiple times consecutively

# adapted from website https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

# define the secret number range: 1~100, type: int
from random import randint
secret = randint(1,100)
# control the loop
flag = True
# initial try times
tried = 0
# compare guess number and secret number with while loop
while(flag):
    # input guess number
    guess = input("enter the guess number \n")
    if(int(guess) > secret):
        print("too large")
    elif (int(guess) < secret):
        print("too small")
    else:
        print("Bingo !" )
        flag = False
    tried += 1
print("game over `.`\n you tried "+str(tried)+" times")
