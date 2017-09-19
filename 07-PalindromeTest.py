# tests whether a string is a palindrome.
# get idea from website: https://stackoverflow.com/questions/8444710/java-way-to-check-if-a-string-is-palindrome

# flag: is/not a palindrome
# type in a string
string = str(input("input a string: \n"))
flag = True
# check is/not a palindrome
for i in range(0,int(len(string)/2)):
    if(string[i] != string[int(len(string))-i-1]):
        flag=False
if(flag):
    print("the string:\n"+string+"\nis a palindrome")
else:
    print("the string:\n"+string+"\nis not a palindrome")