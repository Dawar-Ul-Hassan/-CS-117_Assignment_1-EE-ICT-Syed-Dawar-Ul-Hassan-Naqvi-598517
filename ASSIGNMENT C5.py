def star_to_delta(Ra,Rb, Rc):
    RNumerator = (Ra * Rb) + (Rc * Rb) + (Ra * Rc)

    Rab = RNumerator / Rc
    Rbc = RNumerator / Ra
    Rac = RNumerator / Rb

    Rab = round(Rab, 2)
    Rbc = round(Rbc, 2)
    Rac = round(Rac, 2)

    return Rab, Rbc, Rac

print("star_to_delta(10, 20, 30) ->", star_to_delta(10, 20, 30))

print("")
R1 = int(input("Enter first resistor value: "))
R2 = int(input("Enter second resistor value: "))
R3 = int(input("Enter third resistor value: "))

print(star_to_delta(R1, R2, R3))
