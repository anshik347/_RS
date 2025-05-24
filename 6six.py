
list = ['apple', 'banana', 'cherry', 'date']
dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}

K = input("Enter the key to check: ")

if K in list and K in dict:
    print("The value of '{K}' is: {dict[K]}")
else:
    print("'{K}' is not present")
