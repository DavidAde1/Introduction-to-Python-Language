#Using a dictionary to store data of names and number
people = {
    "David": "+234 567890352",
    "Divine": "+234 567896543",
    "Paul": "+234 67853378998",
    "Bill": "+234 5766334567",
    
}

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number : {number}")


