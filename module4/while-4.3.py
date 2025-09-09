arvo = input("Enter a number")

if arvo == "":
    print("Ensimmäinen arvo ei saa olla tyhjä merkkijono")

pienin = int(arvo)
suurin = int(arvo)


while arvo != "":
    luku = int(arvo)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    arvo = input("anna numero: ")


print("pienin " + str(pienin))
print(f"suurin {suurin}")