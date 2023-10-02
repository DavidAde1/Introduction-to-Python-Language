
user_input = input("input number\n")
b = int(user_input)
def show_meow(a):
    if a >= 3:
        print (f"meow")
    elif a < 3:
        print("Number cannot print word")
    else:
        print("Not valid input")
      
show_meow(b)
