n = int(input("Enter the number of values you want to sum: "))

sumnumbers = 0
count = 0

while count < n:
    number = float(input("Enter number {count + 1}: ")) 
    sumnumbers += number  
    count += 1 

print("The sum of the {n} numbers is: {sumnumbers}")