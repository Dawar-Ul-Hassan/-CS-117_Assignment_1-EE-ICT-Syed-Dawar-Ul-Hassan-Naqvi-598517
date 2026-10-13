voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

max = 1
startingvoltage = voltages[0]
endingvoltage = voltages[0]

currentvoltage = voltages[0]

current_streak = 1
current_start = voltages[0]

for i in range (1, len(voltages)):
    if voltages[i] < voltages [i - 1]:
        current_streak += 1
    else:
        if current_streak > max:
            max = current_streak
            startingvoltage = current_start
            endingvoltage = voltages[i -1]

        current_streak = 1
        current_start = voltages[i]


if current_streak > max:
    max = current_streak
    startingvoltage = current_start
    endingvoltage = voltage[-1]

print("longest continuous drop:", max, "minutes started at: ", startingvoltage, "V", "Ended at: ", endingvoltage)