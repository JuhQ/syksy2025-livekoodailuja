eka = 1
# sisäkkäiset while loopit
# englanniksi nested while loop
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1

        komento = input("Anna komento: ")
        while komento != "lopeta":
            print("hello")
            komento = input("Anna komento: ")
    eka = eka + 1