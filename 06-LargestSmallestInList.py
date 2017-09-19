# get largest and smallest number from a list
# get help from website https://stackoverflow.com/questions/252703/append-vs-extend

# type in a list, type:int
list = []
# set the length of list: 5
for i in range(0,5):
    list.extend([int(input())])
print("the list: "+str(list))
max,min = list[0],list[0]
# compare each element, get the max and min
for x in list:
    if(x>max):
        max = x
    if(x<min):
        min = x
print("largest: "+str(max)+"\nsmallest "+str(min)) 
