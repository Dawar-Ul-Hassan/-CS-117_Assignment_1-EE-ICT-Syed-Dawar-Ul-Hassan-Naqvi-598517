def ohms_current(v, r):
    i = v / r

    return i

def power_dissipated(i, r):
    Power = i**2 * r

    return Power

V = 12
R = 6
I = ohms_current(V, R)
power = power_dissipated(I, R)

print("Current = ", I, "A")
print("Power = ", power, "W")