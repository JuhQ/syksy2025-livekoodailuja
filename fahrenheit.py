fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
print(fahrenheit_str)
print(fahrenheit)
celsius = (fahrenheit-32)*5/9

hieno_merkkijono = f"Lämpötila: {celsius}"

print(hieno_merkkijono)

print("Lämpötila Celsius-asteina: " + str(celsius))

print()

print(f"Lämpötila Celsius-asteina: {celsius:9.3f}")
print(f"Lämpötila Celsius-asteina: {celsius:<2.2f}")
print(f"Lämpötila Celsius-asteina: {celsius:<9.3f}")
print(f"Lämpötila Celsius-asteina: {celsius:<15.4f}")
print()

print(f"Lämpötila Celsius-asteina: {celsius:2.2f}")
print(f"Lämpötila Celsius-asteina: {celsius:9.3f}")
print(f"Lämpötila Celsius-asteina: {celsius:15.4f}")
print(f"Lämpötila Celsius-asteina: {celsius:.4f}")

print()

print(f"Lämpötila Celsius-asteina: {celsius:.4f}, {celsius}, {fahrenheit}, {fahrenheit_str}")
