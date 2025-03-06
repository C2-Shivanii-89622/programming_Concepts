string = input("Entre the string")
def is_constant(n):
    if((n !='a') and (n !='e') and (n !='i') and (n !='o') and (n !='u') and n!=' '):
        return True
    else : 
        return False

list_of_string = []
for n in string:
    list_of_string.append(n)
    if(is_constant(n)==True):
        list_of_string.append('o'+ n)

    
def list_to_string(List):
    string = ''
    for n in List:
        string = string + n

    print(string)

list_to_string(list_of_string)

