numbers = [2, 4, 6, 8, 10]

# (a) Sum of all items
sum_of_items = sum(numbers)
print("Sum of all items:", sum_of_items)

# (b) Multiply all the items
product = 1
for num in numbers:
    product *= num
print("Product of all items:", product)

# (c) Largest number
largest_number = max(numbers)
print("Largest number:", largest_number)

# (d) Smallest number
smallest_number = min(numbers)
print("Smallest number:", smallest_number)