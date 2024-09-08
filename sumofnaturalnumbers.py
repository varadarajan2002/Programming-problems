#To find the sum of n natural numbers

number=int(input("enter the number:"))

sum=0

for i in range(0,number+1):
    sum+=i

print("The sum of the natural numbers is",sum)