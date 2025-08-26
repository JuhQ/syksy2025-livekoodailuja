arvo = input("Enter a number")

pienin = int(arvo)
suurin = int(arvo)

print(min([1,2,3,4]))
print(max([1,2,3,4]))

while arvo != "":
    luku = int(arvo)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    arvo = input("anna numero: ")


print("pienin " + str(pienin))
print(f"suurin {suurin}")