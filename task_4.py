import datetime

def get_upcoming_birthdays(users):
    # Current date
    today = datetime.datetime.today().date()
    # Date in 7 days
    upcoming_week = today + datetime.timedelta(days=7)
    result = []

    for user in users:
        # Convert date of birth from a string to a datetime
        birthday = datetime.datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        
        # Check if birthday has passed this year
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            # The birthday has already passed
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Check whether birthday is within the next 7 days
        if today <= birthday_this_year <= upcoming_week:
            # If birthday falls on this weekend (Saturday or Sunday)
            if birthday_this_year.weekday() >= 5:  # 5 - Saturday, 6 - Sunday
                # Postponed to next Monday
                birthday_this_year += datetime.timedelta(days=(7 - birthday_this_year.weekday()))
            
            result.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")
            })

    return result


users = [
    {'name': 'Олександр', 'birthday': '1990.10.05'},
    {'name': 'Марія', 'birthday': '1985.10.06'},
    {'name': 'Андрій', 'birthday': '1992.10.10'},
    {'name': 'Олена', 'birthday': '1995.10.07'},
    {'name': 'Петро', 'birthday': '1988.10.12'}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)