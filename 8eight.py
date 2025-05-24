tuples= [(2, 4), (1, 3), (6, 8), (7, 2), (0, 0)]
for i in tuples:
    if ((i[0]%2==0) and (i[1]%2==0)):
        print(i)
    else:
        print("No even numbers are present")