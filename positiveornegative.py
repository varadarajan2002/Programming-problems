#To check the given number is positive or negative

number=int(input("enter the number to check for positive or negative:"))

if number >0:
    print(f"The  given number {number} is an positive number")
elif number<0:
    print(f"The given number {number} is an negative number")
else:
    print("Please check the giveenn number")