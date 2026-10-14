# 1. make an empty basket list

basket = []
# 2. keep asking for a price - if it's 0, stop the loop, otherwise .append() it to the basket

while True:
    price = float(input("Item price (0 to finish): £"))
    if price == 0:
        break
    basket.append(price)   
# 3. go through the basket with a for loop and print each item with its number

count = 0
for price in basket:
    count = count + 1
    print(f"Item {count}: £{price:.2f}")
# 4. print how many items are in the basket using len()

print(f"Items: {len(basket)}")
# 5. add up all the prices and print the total

print(f"Total: £{sum(basket):.2f}")