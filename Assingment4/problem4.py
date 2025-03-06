#Write a Python program that calculates the sum of the squares of all odd 
#numbers in a list of integers using map() and filter()
num1=[]
for x in range(5):
    num1.append(int(input("  Enter the number")))
    is_value=lambda n:n%2!=0
Square_of_num1=list(map(lambda n:n**2, filter(is_value,num1)))
print(Square_of_num1)