arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
new_list = []
for i in range(len(arr)):
    new_list.append(arr[len(arr)-1 -i])
print(new_list)