status = input("order status: ")
if status == "Delivered":
    print("Your order has been successfully delivered")
elif status == "Sent":
    print("Your order is on the way")
elif status == "Registered":
    print("Your order id being processed")
else:
    print("Status unknown")