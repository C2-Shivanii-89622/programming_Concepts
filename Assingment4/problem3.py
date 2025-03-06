#Write a Python program that calculates the sum of the squares of all odd 
#numbers in a list of integers using map() and filter() 

num1=[1,2,3,4,5,6,7]
tuple=1,2,3,4,5,6,7

print(f" list of intgers={num1}")
str_num=list(map(str,num1))
print(f" Tuple of integer{tuple} ")

str_tuple= list(map(str,tuple))

final_num1= str_num+ str_tuple

print(final_num1)