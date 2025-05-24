# Input number from the user
num = int(input("Enter a number: "))

# Check if the number is a power of 2
if num > 0 and (num & (num - 1)) == 0:
    print(f"{num} is a power of 2.")
else:
    print(f"{num} is not a power of 2.")
