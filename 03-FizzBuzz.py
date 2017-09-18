# prints the numbers from 1 to 100, with conditions
# 1.For multiples of three print "Fizz" instead of the number
# 2.For the multiples of five print "Buzz"
# 3.For numbers which are multiples of both three and five print "FizzBuzz"

# Consider: 
#   three conditions:
#       1. x%3==0 => "Fizz"
#       2. x%5==0 => "Buzz"
#       3. x%3==0 && x%5==0 => "FizzBuzz"

# First, the loop from number 1 to 100
for x in range(1,101):
    # Second, find all numbers fit condition 3 
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    else:
        # Then, the rest numbers can just fit only one condition of 1 and 2
        if x%3==0:
            print("Fizz")
        elif x%5==0:
            print("Buzz")
        else:
            print(x)
        
