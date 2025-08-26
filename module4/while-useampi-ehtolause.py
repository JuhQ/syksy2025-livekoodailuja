
lopetuskomento = "kissa"
lopetuskomento2 = "lopeta"
lopetuskomento3 = "stop"

kysymys = f'Anna komento ("{lopetuskomento}", "{lopetuskomento2}" ja "{lopetuskomento3}" lopettaa):'

komento = input(kysymys)
# komento = input("Anna komento (\"stop\" lopettaa):")

while komento != lopetuskomento and komento != lopetuskomento2 and komento != lopetuskomento3:
    print("hello")
    komento = input(kysymys)

print("Poistuimme while-lausekkeesta")



