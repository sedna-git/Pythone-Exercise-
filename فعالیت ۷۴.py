import random

number = random.randint(1, 10)
guess = int(input("حدس بزن: "))
count = 1
while guess != number:
    guess = int(input("اشتباهه! دوباره حدس بزن: "))
    count += 1
    
print("موفق شدی!")
print("تعداد تلاش:", count)