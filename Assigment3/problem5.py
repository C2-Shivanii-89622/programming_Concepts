list1=[1,2,3,4,5]
list2=[5,6,7,8]

for n in range (len(list1)):
  for x in range(len(list2)):
   if((list1[n])==list2[x]):
    Duplicate=True
    break
    
   else:
    Duplicate=False
    break

print(Duplicate)


   


