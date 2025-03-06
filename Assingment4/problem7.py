#Write a Python program that filters out numbers greater than 10 from a list 
#of numbers using the filter() function

num1=[]

for x in range(10):
    num1.append(int(input(f" enter the {x} number")))

num2=list(filter(lambda n:n>10,num1))
print(num2)