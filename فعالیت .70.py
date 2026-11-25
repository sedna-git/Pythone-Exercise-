def num_diff(score1, score2):
    diff = score1 - score2
    if diff < 0:
        diff = - diff
    return diff

score1 = int(input("Enter score1: "))
score2 = int(input("Enter score2: "))
print(num_diff(score1, score2))