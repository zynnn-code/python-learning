#price = input("price?") 
#print(price + 5) 
#price = float(input("price? "))
#print(price + 5)
#print(price * 2)
#print(price / 4)
price = float(input("price? "))
discount = price * 0.2
new_price = price - discount
print(new_price)
print(round(new_price,2))
print(f"£{new_price:.2f}")