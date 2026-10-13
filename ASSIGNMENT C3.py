def decimal_to_binary(n):
    if n == 0:
        return 0

    binarystr = ""

    while n > 0:
        remainder = n % 2
        binarystr = str(remainder) + binarystr
        n = n // 2 #integer division to make sure integer value is available

    return binarystr

print("decimal_to_binary(10) ->", decimal_to_binary(10))
print("decimal_to_binary(25) ->", decimal_to_binary(25))

print("")
num = int(input("Enter a number to turn to binary: "))
print("your num in binary = ", decimal_to_binary(num))