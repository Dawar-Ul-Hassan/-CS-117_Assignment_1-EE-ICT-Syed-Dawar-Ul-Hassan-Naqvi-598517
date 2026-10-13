def parallel_resistance(resistors):
    R_Eq = 0
    for r in resistors:
       R_Eq = R_Eq + 1/r
    R_Eq = 1/R_Eq

    return R_Eq

ListOfResistors = [10, 10]

print("parallel_resistance([10, 10])", "->",parallel_resistance(ListOfResistors))

ListOfResistors = [100, 200, 300]
print(print("parallel_resistance([100, 200, 300])", "->", round(parallel_resistance(ListOfResistors),2)))