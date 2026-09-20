# Improved Inventory Program

product_name = "Notebook"
quantity = 10
price = 50

total = quantity * price

print("=== STOCK FIRST INVENTORY SYSTEM ===")
print("Product:", product_name)
print("Quantity:", quantity)
print("Price: ₱", price)
print("Total Value: ₱", total)

if quantity > 0:
    print("Status: Product is available.")
else:
    print("Status: Product is out of stock.")

print("Updated by Member 2")