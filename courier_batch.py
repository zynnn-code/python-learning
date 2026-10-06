total_cost = 0
parcel_count = 0
while True:
   parcel_weight = float(input("Parcel weight in kg (0 to finish): "))
   if parcel_weight == 0:
     break

   if parcel_weight <= 1:
      size = "Small"
      price = 3.5
   elif parcel_weight <= 5:
      size = "Medium"
      price = 6
   else:
      size = "Large"
      price = 12

   total_cost = total_cost + price
   parcel_count = parcel_count + 1
   print(f"Parcel {parcel_weight} kg: {size} - £{price:.2f}") 

print(f"Parcels: {parcel_count}")
print(f"Total cost: £{total_cost:.2f}")


