def max_number(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [10, 5, 20, 8, 15, 19, 18, 13, 14]
print("Max:", max_number(numbers))