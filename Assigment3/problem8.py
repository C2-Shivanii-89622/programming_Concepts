num=int(input("enter the  quantity"))

price=num*5

if(num>50):

    price=price-((15/100)*price)

elif(num>30):

    price=price-((10/100)*price)

print(price)


