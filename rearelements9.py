def extract_rear_elements(tuple_string):

  tuple_data = eval(tuple_string)
  rear_elements = [string[-1] for string in tuple_data]
  return rear_elements

tuple_str = "('python', 'learn', 'includehelp')"
result = extract_rear_elements(tuple_str)
print(result)