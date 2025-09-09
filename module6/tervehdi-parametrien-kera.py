def tervehdi(kerrat):
    # kerrat on parametri, eli funktion sisällä näkyvä muuttuja
    # kerrat = 5
    print(kerrat)
    for i in range(kerrat):
        print("Kutsutaan " + str(i + 1) + ". kertaa")

tervehdi(2)

tervehdi(5)

print(kerrat)