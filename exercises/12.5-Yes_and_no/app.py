theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def wikiWoko(num):
    value = ''
    if num == 0:
        value = 'woko'
    else:
        value = 'wiki'
    return value

print(list(map(wikiWoko,theBools)))
