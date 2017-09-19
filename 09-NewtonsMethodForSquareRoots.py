# z_next = z - ((z*z - x) / (2 * z))

# first get sqrt(z)
# set z = 2
z=2
import math
sqrt_2 = math.sqrt(z)
print("math.sqrt(2) = "+str(sqrt_2))

# now just try x from 1 to 10 using the formular
# the result : 1.25, 1.5, 1.75, 2.0 ------
# so, x should between 1 and 2
# I change the loop: x from 1.0 to 2.0, increase by 0.1
x=1.0
while(x<=2.0):
    z_next = z - ((z*z - x) / (2 * z))
    print(z_next)
    x+=0.1

