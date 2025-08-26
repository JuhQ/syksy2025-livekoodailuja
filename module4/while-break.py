komento = input('Anna komento ("lopeta" lopettaa): ')

while komento != "lopeta":
    print("suoritetaan")
    if komento == "lähdetään tauolle":
        print("Ensin attend sovellus")
        break
    if komento == "MAYDAY":
        break
    print("Ollaan iffin ulkopuolella, suoritus jatkuu")
    print("Suoritan toiminnon " + komento)

    komento = input("Anna komento: ")

    print("\n\n\n\n")

print("Poistuimme while loopista")