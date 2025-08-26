
lopetuskomento = "kissa"

komento = input(f'Anna komento ("{lopetuskomento}" lopettaa):')
# komento = input("Anna komento (\"stop\" lopettaa):")

while komento != lopetuskomento:
    print("hello")
    komento = input(f'Anna komento ("{lopetuskomento}" lopettaa):')

print("Poistuimme while-lausekkeesta")
