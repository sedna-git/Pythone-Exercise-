cities = []
quantity = int(input("تعداد شهرها: "))
for i in range(quantity):
    city = input("نام شهر: ")
    cities.append(city)

cities.sort(reverse=True)
print(cities)