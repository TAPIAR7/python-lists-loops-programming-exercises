
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello = []
for i in range(len(my_list)):
    value = my_list[i]
    temp = type(value)
    if type({"name":"ricardo"}) == temp or type([2,3]) == temp:
        hello.append(my_list[i])

print(hello)
