#To check which number is greatest among the three numbers.
num1=int(input("enter the number:"))

num2=int(input("enter the number:"))

num3=int(input("enter the number:"))

if num1>num2 and num1>num3:
    print(f"The number {num1} is the greatest among the three numbers.")
elif num2>num1 and num2>num3:
    print(f"The number {num2} is greates among the three numbers.")


else:
    print(f"The number {num3} is the greatest among three numbers.")