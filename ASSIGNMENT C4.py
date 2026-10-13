def loaded_divider(vs,r1,r2,rl):
    ReqOfRlR2 = (r2 * rl) / (r2 + rl)
    RUnloaded = round(vs * (r2 / (r2 + r1)), 2)
    RLoaded = round(vs * (ReqOfRlR2 / (r1 + ReqOfRlR2)), 2)

    return RUnloaded, RLoaded

print("loaded_divider(12, 1000, 1000, 500) -> ", loaded_divider(12, 1000, 1000, 500))

print("")
Vs = int(input("Enter Vs: "))
R1 = int(input("Enter R1: "))
R2 = int(input("Enter R2: "))
Rl = int(input("Enter Rl: "))

print(loaded_divider(Vs,R1,R2,Rl))