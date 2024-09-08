#To check whether the given number is odd number or even number

number=int(input("Enter the number to check whether odd or even:"))

if number %2==0:
    print(f"The given number {number} is an even number")
else:
    print(f"The given number{number} is an odd number")