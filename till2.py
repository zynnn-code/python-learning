# 1. make the price list and start the total at 0
total = 0
prices = {"milk": 1.20, "eggs": 2.50, "bread": 1.10, "butter": 1.80}
def show_prices(prices):
    print("Price list:")
    for item in prices:
        print(f"{item}: £{prices[item]:.2f}")

# 2. show the customer every item on the list
show_prices(prices)

def clean(text):
    return text.strip().lower()
while True:
    item = clean(input("Item (or done to finish): "))
    if item == "done":
        break

# 5. if the item is in the price list, add its price to the total and print "Added..."
    if item in prices:
       total = total + prices[item]
       print(f"Added {item} - £{prices[item]:.2f}")
# 6. otherwise, print "Sorry, we don't sell ..."
    else:
      print(f"Sorry, we don't sell {item}")
    
# 7. print the total at the end
print(f"Total: £{total:.2f}")

