all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors(numb):
    return numb["sexy"] == True
def generate_li(color):
    return "<li>" + color["label"] + "</li>"

filter_colors = list(filter(filter_colors, all_colors))
generate_li = list(map(generate_li,filter_colors))
li_string = ''
for item in generate_li:
    li_string += item


print(li_string)