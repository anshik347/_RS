n = int(input("Enter a natural number (n ≥ 1): "))

if n >= 1:
    for i in range(1, n + 1):
        total = 0
        for j in range(1, i + 1):
            total += j * j
        print(total)
else:
    print("Please enter a natural number greater than or equal to 1.")