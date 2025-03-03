list = []
for x in range(1,4):
    list.append(int(input(f"Entre the marks of the student in {x} Subject")))

print(list)
Average_Of_subjects = (list[0] + list[1] + list[2])/3
if(100>=Average_Of_subjects>=90):
    print("Your grade is A")
elif(89>=Average_Of_subjects>=80):
    print("Your grade is B")
elif(79>=Average_Of_subjects>=70):
    print("Your grade is C")
elif(69>=Average_Of_subjects>=60):
    print("Your grade is D")
else:
    print("Your grade is F")

