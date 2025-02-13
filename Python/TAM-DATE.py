from datetime import datetime

def convert_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return "Invalid date format. Please enter in mm/dd/yyyy format."

# Get user input and display the formatted date
date_input = input("Enter the date (mm/dd/yyyy): ")
print("Date Output:", convert_date(date_input))
