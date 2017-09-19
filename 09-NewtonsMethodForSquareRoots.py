# z_next = z - ((z*z - x) / (2 * z))

import math
# let's say x = 2, so need value of sqrt(2)
x = 2
sqrt = math.sqrt(x)
print("math.sqrt("+str(x)+") = "+str(sqrt))

# try loop for 10 times
# assume z0 = 1
#   z=1.0
#   for i in range(1,11):
#       tmp = z - ((z*z - x) / (2 * z))
#       print(tmp)
#       z=tmp
# by this way, some result is very close to math.sqrt(x)
# so,change loop to stop when result stopped changing (or only changes by a very small delta)
z=1.0
while True:
    tmp = z - ((z*z - x) / (2 * z))
    if(tmp == sqrt or math.fabs(tmp-sqrt)<0.000000000001):
        break
    print(tmp)
    z=tmp


