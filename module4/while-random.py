import random
noppa1 = noppa2 = heitot = 0
while (noppa1!=6 or noppa2!=6):
    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)

    print(f"noppa1: {noppa1}, noppa2: {noppa2}")

    heitot = heitot + 1

print(f"Tarvittiin {heitot:d} heittoa.")