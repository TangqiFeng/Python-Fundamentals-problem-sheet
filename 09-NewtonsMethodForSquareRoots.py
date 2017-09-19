# z_next = z - ((z*z - x) / (2 * z))

import math
# let's say x = 2, so need value of sqrt(2)
x = 2
sqrt = math.sqrt(x)
print("math.sqrt("+str(x)+") = "+str(sqrt))

# try loop for 10 times
# assume z0 = 1
z=1.0
for i in range(1,11):
    tmp = z - ((z*z - x) / (2 * z))
    print(tmp)
    z=tmp



