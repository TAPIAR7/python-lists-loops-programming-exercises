names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return "My name is: " + name
#Your code go here:
print(list(map(prepender,names)))