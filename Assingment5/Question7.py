numbers = []
for n in range(1,7):
    numbers.append(int(input(f"Enter the {n}th number")))

print(numbers)

extract_even = lambda n : n % 2 == 0
extract_odd = lambda n : n % 2 != 0

Even_Nums = list(filter(extract_even,numbers))
Odd_Nums = list(filter(extract_odd,numbers))

dicttionary = {"Even":Even_Nums,"Odd":Odd_Nums}
print(dicttionary)