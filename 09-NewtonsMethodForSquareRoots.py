# z_next = z - ((z*z - x) / (2 * z))

# first get sqrt(z)
# set z = 2
z=2
import math
sqrt_2 = math.sqrt(z)
print("math.sqrt(2) = "+str(sqrt_2))

# now just try x from 1 to 10 using the formular
for x in range(1,11):
    z_next = z - ((z*z - x) / (2 * z))
    print(z_next)

