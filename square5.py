def print_even_numbers_and_squares(start, end):
  for num in range(start, end + 1):
    if num % 2 == 0:
      print(f"Number: {num}, Square: {num * num}")

# Example usage:
print("Range (1, 50):")
print_even_numbers_and_squares(1, 50)
print("\nRange (1, 100):")
print_even_numbers_and_squares(1, 100)