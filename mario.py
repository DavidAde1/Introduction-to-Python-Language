
while True:
    try:
        n = int(input("Height: "))
        if n > 0:
          break
    except ValueError:
        print("Not a valid integer")


for i in range(n):
    print("#")