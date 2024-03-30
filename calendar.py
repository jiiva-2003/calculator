import calendar

def display_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar(calendar.Monday)
    
    # Get the calendar for the specified year and month
    month_calendar = cal.formatmonth(year, month)
    
    # Display the calendar
    print(month_calendar)

if __name__ == "__main__":
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    display_calendar(year, month)
