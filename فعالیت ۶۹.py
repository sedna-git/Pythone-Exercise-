def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = []
quantity = int(input("تعداد اعداد لیست: "))
for i in range(quantity):
    num = float(input("number: "))
    my_list.append(num)
result = sum_list(my_list)
print(result)