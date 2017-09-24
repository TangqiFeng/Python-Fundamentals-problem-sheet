# n! means n x (n − 1) … x 3 x 2 x 1 
# e.g.  
#     10! = 10 x 9 x … x 3 x 2 x 1 = 3628800
#     the sum of the digits in the number 10! is 
#     3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

# assume a bumber n, function to get n!
def getFactionalSum(n):
    sum=1
    while(n):
        sum *= n
        n -= 1
    return sum   #-- sum is factional sum

def getDigitSum(sum):
    # function to get digit sum, get each last digit by sum%10
    sumDigit=0
    while(sum):
        sumDigit +=  int(sum%10)
        sum /= 10
    return sumDigit    #-- sum is factional digit sum

# first give n => 100
n=100
sum = getFactionalSum(n)
print(str(n)+"! = "+str(sum))
# get digit sum
sumDigit = getDigitSum(sum)
print("result is " + str(sumDigit))


