# 1. ask for the price
price = float(input("Price per item: £")) 

# 2. print the heading
print(f"Price table for £{price:.2f} each")

# 3. loop 1 to 10 and print each line
for quantity in range(1, 11):
    total = price * quantity
    print(f"{quantity} x £{price:.2f} = £{total:.2f}")


