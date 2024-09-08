#To find the sum of given numbers in a range

low=int(input("enter the staring value of the range number:"))
high=int(input("enter the ending values of the range numbers:"))

sum=0

for i in range(low,high+1):
    sum+=i
print("The sum of numbers in a range :",sum)