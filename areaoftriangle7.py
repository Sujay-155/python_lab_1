import math

def calculate_triangle_area(a, b, c):
  s = (a + b + c) / 2
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  return area

def main():
  # Get sides of the first triangle
  a1 = float(input("Enter side a of the first triangle: "))
  b1 = float(input("Enter side b of the first triangle: "))
  c1 = float(input("Enter side c of the first triangle: "))

  # Get sides of the second triangle
  a2 = float(input("Enter side a of the second triangle: "))
  b2 = float(input("Enter side b of the second triangle: "))
  c2 = float(input("Enter side c of the second triangle: "))

  # Calculate areas
  area1 = float(calculate_triangle_area(a1, b1, c1))
  area2 = float(calculate_triangle_area(a2, b2, c2))

  # Calculate total area
  total_area = area1 + area2

  # Calculate percentage contribution
  percentage1 = (area1 / total_area) * 100
  percentage2 = (area2 / total_area) * 100

  print("Area of the first triangle:", area1)
  print("Area of the second triangle:", area2)
  print("Total area:", total_area)
  print("First triangle's contribution:", percentage1, "%")
  print("Second triangle's contribution:", percentage2, "%")

if __name__ == "__main__":
  main()