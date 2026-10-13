R1 = int22(input("Enter R1: "))
R2 = int(input("Enter R2: "))
R3 = int(input("Enter R3: "))

if R1 > R2 and R1 > R3:
    highest = R1
elif R2 > R1 and R2 > R3:
    highest = R2
elif R3 > R1 and R3 > R2:
    highest = R3

if R1 < R2 and R1 < R3:
    smallest = R1
elif R2 < R1 and R2 < R3:
    smallest = R2
elif R3 < R1 and R3 < R2:
    smallest = R3

print("Smallest = ", smallest, "ohm")
print("Largest = ", highest, "ohm")