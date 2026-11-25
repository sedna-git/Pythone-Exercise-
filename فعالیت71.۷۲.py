print("Simple Calculator")
print("1- Addition")
print("2- Absolute Difference")
print("3- Power")
print("4- Division (Quotient & Remainder)")
print("5- Round a Number")
print("6- Max & Min")
print("7- (sum)")
print("8-  Convert to Integer (int)")
print("9- Convert to Float (float)")

choice = input("Select an option (1-9): ")

if choice == "1":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result", sum([a, b]))

elif choice == "2":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", abs(a - b))

elif choice == "3":
    a = int(input("Enter base: "))
    b = int(input("Enter exponent: "))
    print("Result:", pow(a, b))

elif choice == "4":
    a = int(input("Enter dividend: "))
    b = int(input("Enter divisor: "))
    q, r = divmod(a, b)
    print("Quotient:", q)
    print("Remainder:", r)

elif choice == "5":
    a = float(input("Enter a number: "))
    print("Result:", round(a))

elif choice == "6":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Max:", max(a, b))
    print("Min:", min(a, b))

elif choice == "7":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print("Sum:", sum([a, b, c]))

elif choice == "8":
    num = float(input("Enter a number: "))
    print("Integer value =", int(num))

elif choice == "9":
    num = int(input("Enter a number: "))
    print("Float value =", float(num))

else:
    print("Invalid choice")