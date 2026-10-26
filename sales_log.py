# 1. make the price list same as till2.py
prices = {"milk": 1.20, "eggs": 2.50, "bread": 1.10,"butter": 1.80}


# 2. make a clean card that cleans the spaces make the text lowercase
def clean(text):
    return text.strip().lower()

# 3. loop forever
while True:
# 3a. ask for the item and clean it    
    item = clean(input("Item (or done to finish): "))

# 3b. if its done stop the loop
    if item == "done":
        break

# 3c. if it's in the price list, write it into sales.txt ("a") and print Added
    if item in prices:
        with open ("sales.txt", "a") as f:
            f.write(f"{item}\n")      
        print(f"Added {item} - £{prices[item]:.2f}")


# 3d. otherwise print Sorry, we don't sell ...
    else:
        print(f"Sorry, we don't sell {item}")
# 4. after the loop, start all_time at 0
all_time = 0   

# 5. open sales.txt ("r"); for each line: strip it, look up its price, add to all_time
with open("sales.txt", "r") as f:            
    for line in f:                               
        name = line.strip() 
        all_time = all_time + prices[name]  

# 6. print All-time total: £..                     
print(f"All-time total: £{all_time:.2f}") 


