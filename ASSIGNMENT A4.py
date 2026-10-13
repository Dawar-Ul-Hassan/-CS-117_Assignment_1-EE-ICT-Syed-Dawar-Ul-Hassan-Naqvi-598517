A = int(input("Enter A: "))
B = int(input("Enter B: "))

if (A != 1 or 0) and (B != 1 or 0):
    print("Bits must be 0 or 1")
else:
    if A ==1 and B==1:
        AND = 1
    else:
        AND = 0
    if A == 1 or B == 1:
        OR = 1
    else:
        OR = 0
    if (A==1 and B==0) or (B==1 and A==0):
        XOR = 1
    else:
        XOR = 0

    print("AND = ", AND)
    print("OR = ", OR)
    print("XOR = ", XOR)