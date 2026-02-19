produce = ["Tomatoes", "Lettuce"]
dairy   = ["Milk", "Cheese"]

# Wrap the two lists as elements in a new list
groceries = [produce, dairy]

for section in groceries:
    for item in section:
        print("Item name:", item)