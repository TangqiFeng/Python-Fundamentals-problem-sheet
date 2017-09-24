# reverse a string.

#  read a string
def getString ():
    string = input("input a string:\n")
    return string
# the best way from website:https://stackoverflow.com/questions/931092/reverse-a-string-in-python
def reverse (s):
    print(s[::-1])

# my own way:
def reverse2 (s):
    tmp = []
    i = len(s)-1
    while(i>=0):
        tmp.extend(s[i])
        i -=1
    print(str(tmp))

String = getString()
reverse(String)
reverse2(String)