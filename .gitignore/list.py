list = [[1,2,3], [4,5,6], [7,8,9]]
list = [num for elem in list for num in elem]
print(list)

for elem in list:
    for num in elem:
        print(list)
