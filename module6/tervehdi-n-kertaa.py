def tervehdi(tervehdys, kerrat):
    for i in range(kerrat):
        print (tervehdys + " " + str(i+1) + ". kerran")
    return

kerrat = int(input("Kuinka monta kertaa tervehditään: "))

tervehdi("Moi", kerrat)

tervehdi("Hello", 1)

tervehdi("Bonjour", 2)