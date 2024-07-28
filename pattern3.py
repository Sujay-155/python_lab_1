def print_pattern(rows):
  for i in range(1, rows + 1):
    print("".join(chr(ord('A') + j) for j in range(i)))

# Example usage:
rows = 5
print_pattern(rows)

print("\n")

def print_pattern(rows):
  for i in range(1, rows + 1):
    print('*' * i)

# Example usage:
rows = 5
print_pattern(rows)