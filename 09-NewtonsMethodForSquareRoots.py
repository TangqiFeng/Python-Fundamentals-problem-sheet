# z_next = z - ((z*z - x) / (2 * z))

# first get sqrt(z)
# set z = 2
z=2
import math
sqrt_2 = math.sqrt(z)
print("math.sqrt(2) = "+str(sqrt_2))

# step 1:now just try x from 1 to 10 using the formular
    # the result : 1.25, 1.5, 1.75, 2.0 ------
    # so, x should between 1 and 2
    # I change the loop: x from 1.0 to 2.0, increase by 0.1
# step 2:the result :1.25  1.275   1.3    1.3250000000000002
    #         1.35  1.375   1.4000000000000001
    #         1.4250000000000003   1.4500000000000002
    #         1.475
    # so, x should between 1.6 and 1.7
    # then,I change the loop: x from 1.6 to 1.7, increase by 0.01
# step 3:I get the result:
    #   1.4    1.4025    1.405    1.4075    1.4100000000000001
    #   1.4125  1.415    1.4175   1.42      1.4225
    # then, change the loop: x from 1.64 to 1.66, increase by 0.001
# step 4:
    # the results shows x should between 1.656 and 1.657
    # then, change the loop: x from 1.656 to 1.657, increase by 0.000001
x=1.656
while(x<=1.657):
    z_next = z - ((z*z - x) / (2 * z))
    print(z_next)
    x+=0.000001

