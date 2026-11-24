menu = {
    "1": "Math Quiz",
    "2": "Geography Quiz",
    "3": "Exit"
}

math_quiz = {
    "2 + 2 = ?": "4",
    "5 * 3 = ?": "15",
    "10 - 7 = ?": "3"
}

geo_quiz = {
    "Capital of Iran?": "Tehran",
    "Capital of France?": "Paris",
    "Capital of Japan?": "Tokyo"
}

print("Welcome to Quiz Game!")
print("Menu:")
for key in menu:
    print(key, "-", menu[key])

choice = input("Select an option: ")
score = 0

if choice == "1":
    print("\nMath Quiz")
    for question in math_quiz:
        answer = input(question + " ")
        if answer == math_quiz[question]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

elif choice == "2":
    print("\nGeography Quiz")
    for question in geo_quiz:
        answer = input(question + " ")
        if answer == geo_quiz[question]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

elif choice == "3":
    print("Exiting the game...")

else:
    print("Invalid option")