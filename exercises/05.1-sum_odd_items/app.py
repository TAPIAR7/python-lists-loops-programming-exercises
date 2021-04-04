arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_all_values(items):

    total= 0
    #The magic happens here:
    for item in arr:
        if item % 2 != 0:
            total +=item
   

    return total
print(sum_all_values(arr))

