from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Convert date string to datetime
        input_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Get the current date
        today = datetime.today().date()

        # Calculation of difference
        delta = abs(input_date - today)
        return delta.days
    except ValueError:
        # Handle error with an incorrect date format
        print ("Incorrect date format. Use:'YYYY-MM-DD'")


def get_days_from_today_small(date: str) -> int:
    try:
        return abs(datetime.strptime(date, '%Y-%m-%d').date() - datetime.today().date()).days
    except ValueError:
        # Handle error with an incorrect date format
        print ("Incorrect date format. Use:'YYYY-MM-DD'")


dates = ['2000-11-09', '2024-10-09', '2012-07-05', '1989-01-20']
for i in dates:
     print(f"Number of days between {i} and today: {get_days_from_today(i)}")

for i in dates:
     print(f"Number of days between {i} and today: {get_days_from_today_small(i)}")


error_dates = ['202-11-09', '12-10-09']
for i in error_dates:
     print(f"Number of days between {i} and today: {get_days_from_today(i)}")

for i in error_dates:
     print(f"Number of days between {i} and today: {get_days_from_today_small(i)}")