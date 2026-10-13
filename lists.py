items = ["milk", "eggs", "bread"]
print(items[1])
print(len(items))


items = ["milk", "eggs", "bread"]
items.append("butter")
for item in items:
    print("Buy", item)


prices = [2.5, 1, 4]
total = 0
for price in prices:
    total = total + price
print(f"Total: £{total:.2f}")