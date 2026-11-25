inventory = {
    "Bag": 5,
    "Ball": 8,
    "Laptop": 3,
    "Mouse": 10,
    "Flash memory": 14
}

if "Bag" in inventory:
    print("Bag is in inventory")
else:
    print("Bag is not in inventory")

removed_value = inventory.pop("Bag")
print("removed value:",removed_value)

if "Bag" in inventory:
    print("Bag is in inventory")
else:
    print("Bag is not in inventory")

print(inventory)