def laskin(operaatio, num1, num2):
    if operaatio == "*":
        # return avainsana pysäyttää funktion suorituksen ja palauttaa sen jälkeen olevan arvon funktiota kutsuvalle taholle
        return num1 * num2
        # print funktiota ei tässä kutsuta sillä return on pysäyttänyt funktion suorituksen edelliselle riville
        print("hello")
    if operaatio == "+":
        return num1 + num2
    if operaatio == "/":
        return num1 / num2
    if operaatio == "potenssi" or operaatio == "**":
        return num1 ** num2

    if operaatio == "-":
        return num1 - num2

    return "en tiedä mitä tehdä"



kertolaskun_tulos = laskin("*", 3, 5)
print(kertolaskun_tulos)
tulos = laskin("+", kertolaskun_tulos, 10)

print(f"tulos = {tulos}")

print(laskin("kissa", 3, 5))

print(laskin("+", 3, laskin("-", 10, 8)))


toinen_arvo = laskin("-", 10, 8)
lopputulos = laskin("+", 3, toinen_arvo)
print(lopputulos)


laskin("/", 3, 5)
laskin("potenssi", 3,5)
laskin("**", 3, 5)


