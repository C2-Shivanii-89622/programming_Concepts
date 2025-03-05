list1=[]
for n in range(5):
    num=int(input("enter the number"))
    list1.append(num)
length = len(list1)
list1.sort()
print(list1[length-1])

