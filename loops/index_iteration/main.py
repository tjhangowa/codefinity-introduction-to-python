prices = [29.99, 45.50, 12.75, 38.20]

for item in range(len(prices)):
    updated_prices = []
    if item == 0:
        prices[item] -= prices[item] * .10
        print(f"Updated price for item {item}: ${prices[item]:.2f}")
    if item == 1:
        prices[item] -= prices[item] * .20
        print(f"Updated price for item {item}: ${prices[item]:.2f}")
    if item == 2:
        prices[item] -= prices[item] * .15
        print(f"Updated price for item {item}: ${prices[item]:.2f}")
    if item == 3:
        prices[item] -= prices[item] * .05
        print(f"Updated price for item {item}: ${prices[item]:.2f}")

    
