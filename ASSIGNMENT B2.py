NumOfR = int(input("How many resistors are connected? "))

Rtotal = 0

for x in range(1, NumOfR + 1):
    R = input(f"Enter R{x}: ")
    Rtotal = Rtotal + int(R)

print(Rtotal)