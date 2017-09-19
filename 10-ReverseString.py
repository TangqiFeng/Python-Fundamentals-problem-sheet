# reverse a string.

#  read a string
string = input("input a string:\n")
# the best way from website:https://stackoverflow.com/questions/931092/reverse-a-string-in-python
print(string[::-1])

# my own way:
tmp = []
i = len(string)-1
while(i>=0):
    tmp.extend(string[i])
    i -=1
print(str(tmp))