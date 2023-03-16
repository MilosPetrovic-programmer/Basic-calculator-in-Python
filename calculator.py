def sabiranje(x,y):
    return x + y

def oduzimanje(x,y):
    return x - y

def mnozenje(x,y):
    return x * y

def podeli(x,y):
    x / y

print("Izaberi operaciju: ")
print("1. saberi")
print("2. oduzmi")
print("3. mnozi")
print("4. podeli")

while True:

    izaberi = input("Izaberite(1/2/3/4): ")

    if izaberi in ("1","2","3","4"):
        broj1 = float(input("unesite prvi broj: "))
        broj2 = float(input("unesite prvi broj: "))

        if izaberi== '1':
            print(sabiranje(broj1, broj2))

        elif izaberi == '2':
            print(oduzimanje(broj1, broj2))

        elif izaberi== '3':
            print(mnozenje(broj1, broj2))

        elif izaberi== '4':
            print(podeli(broj1, broj2))

        next_calculation = input("Racunam dalje: (y/n): ")
        if next_calculation == "n":
          break
    
    else:
        print("Invalid Input")
