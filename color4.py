ListColour = ["Black", "Red", "Maroon", "Yellow"]
ListCode = ["000000", "FF0000", "800000", "FFFF00"]

def convert_to_dict(color_names, color_codes):
    return [{"colorName": name, "colorCode": code} for name, code in zip(color_names, color_codes)]

result = convert_to_dict(ListColour, ListCode)
print(result)