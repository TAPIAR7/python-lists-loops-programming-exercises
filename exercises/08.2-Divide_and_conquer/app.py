list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(list_of_numbers):
    #Your code go here:
    new_list = [[],[]]
    for number in list_of_numbers:
        if number % 2 == 0:
            new_list[1].append(number)
        else:
            new_list[0].append(number)
        
    return new_list

print(merge_two_list(list_of_numbers))

