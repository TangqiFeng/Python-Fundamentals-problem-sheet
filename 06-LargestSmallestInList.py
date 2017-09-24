# get largest and smallest number from a list
# get help from website https://stackoverflow.com/questions/252703/append-vs-extend

def getList (x):
    list = []
    for i in range(0,x):
        list.extend([int(input())])
    return list

def compare (list):
    max,min = list[0],list[0]
    # compare each element, get the max and min
    for x in list:
        if(x>max):
            max = x
        if(x<min):
            min = x
    print("largest: "+str(max)+"\nsmallest "+str(min)) 


# type in a list, type:int
# set the length of list: 5
list = getList(5)
print("the list: "+str(list))
# get the largest and smallest value
compare(list)
