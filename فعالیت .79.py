def count_chars(text):
    upper = 0
    lower = 0
    digit = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1

    print("حروف بزرگ:", upper)
    print("حروف کوچک:", lower)
    print("اعداد:", digit)


text = input("یک رشته وارد کنید: ")
count_chars(text)