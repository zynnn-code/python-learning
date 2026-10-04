product_weight = float(input("Enter weight of the product? "))
if product_weight <= 1:
    size = "Small"
    price = 3.5
elif product_weight <= 5:
    size = "Medium"
    price = 6
else:
    size = "Large"
    price = 12
print(f"Weight: {product_weight} kg")      
print(f"Size: {size}")
print(f"Price: £{price:.2f}")
       

