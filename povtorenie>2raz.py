arr1 = [1, 1, 2, 1, 3, 4, 5, 4, 4, 6, 7, 8, 9]
arr2 =[]

for i in arr1:
    if arr1.count(i) > 2:
        arr2.append(i)
print(arr1)
print(arr2)