items = int(input("How many items? "))
items_per_box = int(input("How many items fit in one box? "))
full_boxes = items // items_per_box
left_over = items % items_per_box
print(f"Order: {items} items, {items_per_box} per box")
print(f"Full boxes: {full_boxes}")
print(f"Items left over: {left_over}") 
