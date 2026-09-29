product_name = input ("Enter name of the product. ")
product_name = product_name .strip().title()
price = float (input("Enter price of the product. £")) 
discount = int (input("Enter discount % "))
discount_amount = price * discount / 100
sale_price = (price - discount_amount)
print (product_name)
print  ( f"Was £{price:.2f} - now £{sale_price:.2f}" )
print (f"You save £{discount_amount:.2f} ({discount}% off)")
