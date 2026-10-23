def apply_discount(price, percent):
   
    return price - ( price * percent / 100)
price = float(input("Price: £"))
percent = float(input("Discount %: "))
sale = apply_discount(price, percent)
print(f"Sale price: £{sale:.2f}")
