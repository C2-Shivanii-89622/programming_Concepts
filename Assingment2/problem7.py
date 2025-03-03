num = int(input("Enter the number of Quantities pruchased"))

if(num<=30):
    amount = num * 5
    
elif(num>30 and num<=50):
    amount = (num * 5) - (10/100)*(num*5)
    
else:
    amount = (num*5) - (15/100)*(num*5)

print(amount)