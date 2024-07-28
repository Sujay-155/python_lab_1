A = ['abc', 'xyz', 'aba', '1221']

# Checking the whole list and its condition.
for index in range(len(A)):
    string = A[index]
    if len(string) > 0 and string[0] == string[-1]:
        print(f"String: '{string}', Index: {index}")