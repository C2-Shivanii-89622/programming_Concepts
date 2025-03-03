Principal = float(input("Entre the Principal Aount"))
Rate = float(input("Entre the Rate of Interest"))
Time = float(input("Entre the Time for lending"))
number = int(input("Entre the number of cycles"))
percentRate= Rate / 100
CI = Principal*((1 +(percentRate/number)) ** (number * Time))

print(f"{CI}")