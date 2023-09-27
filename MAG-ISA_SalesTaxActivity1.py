# Input purchase amount for tax
Purchase_Tax = float(input("Purchase Tax:"))

# Use sales tax value
sales_tax = float(input("Sales Tax Value in Decimal:"))

# Find sales tax result
result = (Purchase_Tax * sales_tax)
result1 = "{:.2f}".format(result)
print(result1)