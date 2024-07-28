import calendar

def get_days_in_month(month_name, year=None):
  months = {
      "January": 1,
      "February": 2,
      "March": 3,
      "April": 4,
      "May": 5,
      "June": 6,
      "July": 7,
      "August": 8,
      "September": 9,
      "October": 10,
      "November": 11,
      "December": 12
  }

  month_number = months.get(month_name.capitalize())
  if month_number is None:
    return "Invalid month name"

  if month_number == 2 and year is not None:
    # Check for leap year
    return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
  else:
    return calendar.monthrange(year or 2023, month_number)[1]

if __name__ == "__main__":
  month_name = input("Enter the month name: ")
  year = None
  if month_name.lower() == "february":
    year = int(input("Enter the year: "))

  days_in_month = get_days_in_month(month_name, year)
  print(f"The number of days in {month_name} is: {days_in_month}")
