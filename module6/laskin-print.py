def laskin(operaatio, num1, num2):
    if operaatio == "*":
        print(num1 * num2)

    elif operaatio == "+":
        print(num1 + num2)

    elif operaatio == "/":
        print(num1 / num2)

    elif operaatio == "potenssi" or operaatio == "**":
        print(num1 ** num2)
    else:
        print("en tiedä mitä tehdä")


laskin("*", 3, 5)
"""
laskin("+", 3, 5)
laskin("/", 3, 5)
laskin("potenssi", 3,5)
laskin("**", 3, 5)
"""


