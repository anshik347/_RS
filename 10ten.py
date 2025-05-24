arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 1, 5]

missing = list(set(arr1) - set(arr2))[0]

print("Missing element is:", missing)