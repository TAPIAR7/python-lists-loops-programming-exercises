par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for letter in par:
    if letter != ' ':
        if letter.lower() in counts:
            counts[letter.lower()] += 1
        else:
            counts[letter.lower()] = 1
print(counts)

