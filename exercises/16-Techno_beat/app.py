def lyrics_generator(arr):
    count = 0
    itwas1 = False
    my_string = ''
    for num in arr:
        if itwas1 == True:
            if num == 1:
                my_string += 'Drop the base '
                count += 1
                if count == 3:
                    my_string += '!!!Break the base!!! '
                    count = 0
                    itwas1 = False
            else:
                my_string += 'Boom '
                itwas1 = False


        else:
            if num == 1:
                my_string += 'Drop the base '
                itwas1 = True
                count += 1
            else:
                my_string += 'Boom '
                itwas1 = False
    return my_string


        
        


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))