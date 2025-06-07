calc1 = int(input("Input a number: "))
calcx = int(input("now input what you owuld like to do with the number (1 = +, 2 = -, 3 = *, 4 = /): "))
if calcx == "1":
    addition()
elif calcx == "2":
    subtraction()
elif calcx == "3":
    multiplication()
elif calcx == "4":
    division()
else:
    print("please input a valid number next time")

def addition():
    calc2 = int(input("Input another number: "))
    ans = (calc1) + (calc2)
    print(ans)

addition()
