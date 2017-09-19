# n! means n x (n − 1) … x 3 x 2 x 1 
# e.g.  
#     10! = 10 x 9 x … x 3 x 2 x 1 = 3628800
#     the sum of the digits in the number 10! is 
#     3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

# assume a bumber n, function to get n!
# first give n => 100
n=100
sum=1
while(n):
    sum *= n
    n -= 1
print(sum)   #-- sum is factional sum
# function to get digit sum, get each last digit by sum%10
sumDigit=0
while(sum):
    sumDigit +=  int(sum%10)
    sum /= 10
print(sumDigit)    #-- sum is factional digit sum

