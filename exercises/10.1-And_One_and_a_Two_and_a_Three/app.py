contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
keys = contact.keys()
values = contact.values()
contacts = contact.items()
for key in keys:
    print(key, ':',contact[key])
