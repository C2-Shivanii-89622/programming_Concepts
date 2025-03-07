#to find out face and place value of a four digit no and reversing it

num = input(" Entre a 4 digit number :- ")

def to_display_Facevalue(str):
    print(f"{str[0]}     {str[1]}    {str[2]}    {str[3]}")

to_display_Facevalue(num)

def to_display_placevalue(str):
    print(f"{str} = {int(str[0])}*1000  +  {int(str[1])}*100   +   {int(str[2])}*10    +  {int(str[3])}*1")

to_display_placevalue(num)

def Print_Rev_num(str):
    print(f"{str[3]}{str[2]}{str[1]}{str[0]}")   

