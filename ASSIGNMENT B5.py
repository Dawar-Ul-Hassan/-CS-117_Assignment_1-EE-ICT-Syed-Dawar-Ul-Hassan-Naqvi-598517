count_for_1percent = 0
count_for_5percent = 0
count_for_reject = 0

print("Enter measured resistances, or enter 0 to stop the program.")

while True:
    resistance = float(input("Enter resistance: "))

    if resistance == 0:
        break

    if 99.0 <= resistance <= 101.0:
        count_for_1percent = count_for_1percent + 1
    elif 95.0 <= resistance <= 105.0:
        count_for_5percent = count_for_5percent + 1
    else:
        count_for_reject = count_for_reject + 1

print("1% tolerance counts: ", count_for_1percent)
print("5% tolerance counts: ", count_for_5percent)
print("Reject count: ", count_for_reject)