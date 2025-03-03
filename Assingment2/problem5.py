def Calculate_price(n):
    if(n<=100):
        price = 200
    elif(100<n<=150):
        extra = n - 100
        price = 200 + (extra* .6 )
    elif(150<n<=200):
        extra =  n - 150
        price = 200 + (50*.6) + (extra*.5)
    else:
        extra = n - 200 
        price = 200 + (50*.6) + (50*.5) +(extra*.4)
    return price

Number_Of_Calls = (int(input("Entre the number of calls made :- ")))
Total_Price = Calculate_price(Number_Of_Calls)
print(Total_Price)