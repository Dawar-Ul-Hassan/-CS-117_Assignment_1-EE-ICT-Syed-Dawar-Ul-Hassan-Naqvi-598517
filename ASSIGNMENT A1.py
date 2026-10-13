V = int(input("Enter the Voltage (V):"))
R = int(input("Enter the Resistance (R):"))

I = V / R

print("Current is = ", I, "A")

if R <= 0:
    print("Invalid Resistance")
else:
     if I > 2:
        print("Fuse will blow")
     else:
        print("Circuit is safe")
