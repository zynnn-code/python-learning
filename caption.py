name = input("ENTER THE PRODUCT NAME ")
colour = input("enter the colour ")
price = input("whats the price? ")

name = name.strip().title()
colour = colour.strip().title()

caption = (f"New In {colour} {name} for only £{price}")
print(caption)
lcaption = len(caption)
lcolour = colour.lower().replace(" ","")
lname = name.lower().replace(" ","")
print(f"#{lcolour}{lname}")
print(f"Length of the caption is {lcaption} ")