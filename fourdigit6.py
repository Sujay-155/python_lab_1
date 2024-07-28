def find_sum_and_reverse(number):

  sum_of_digits = 0
  reverse_number = 0

  while number > 0:
    digit = number % 10
    sum_of_digits += digit
    reverse_number = reverse_number * 10 + digit
    number //= 10

  return sum_of_digits, reverse_number

# Example usage:
number = int(input("Enter a four-digit number: "))

sum, reverse = find_sum_and_reverse(number)

print("Sum of digits:", sum)
print("Reverse of the number:", reverse)