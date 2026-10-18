prices = {"milk": 1.20, "eggs": 2.50, "bread": 1.10}
print(prices["eggs"])
print(len(prices))


prices = {"milk": 1.20, "eggs": 2.50}
prices["milk"] = 1.30
prices["butter"] = 1.80
print(prices["milk"])
print(len(prices))


prices = {"milk": 1.20, "eggs":2.50, "bread": 1.10}
for item in prices:
    print(f"{item}: £{prices[item]:.2f}")

# print(prices["cheese"])   # KeyError - cheese isn't a key 