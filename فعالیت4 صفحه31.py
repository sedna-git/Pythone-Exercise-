score = int(input("score: "))
if score >= 1 and score <= 100:
    if score >= 90:
        print("exelent")
    elif score > 69 and score < 90:
        print("good")
    elif score > 50 and score < 69:
        print("pass")
    else:
        print("fail")
    