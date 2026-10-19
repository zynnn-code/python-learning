# 1. make the price list and start the total at 0
total = 0
prices = {"milk": 1.20, "eggs": 2.50, "bread": 1.10, "butter": 1.80}

# 2. show the customer every item on the list
print("Price list:")
for item in prices:
    print(f"{item}: £{prices[item]:.2f}")

# 3. keep asking the customer for an item until they type done
while True:
    item = (input("Item (or done to finish): "))
    
# 4. tidy up what they typed (remove spaces, make it lower case)
    item = (item.lower().strip())
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

