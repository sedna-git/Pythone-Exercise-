def game():
    word = "python"
    chance = len(word)
    for i in range(chance):
        guess = input("کلمه را حدس بزن: ")
        if guess == word:
            print(word)
            print("تبریک! درست حدس زدی.")
            break
    else:
        print("پایان بازی")