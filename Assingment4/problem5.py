#Write a Python program that adds two lists element-wise using the map() 
#function list

list1= [1, 2, 3, 4, 5]
list2=[5, 4, 3, 2, 1] 
for n in range(len(list1)):

    list1[n]=list1[n]+list2[n]

print(list1)


