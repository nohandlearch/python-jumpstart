#!/usr/bin/env python3
"""Calculate number of days between until the user's birthday"""

import datetime

def get_birthday():
    """Ask the user for birthday information, and return date"""
    print('When were you born? ')
    year_text = input('What year [YYYY]? ')
    month_text = input('What month [MM]? ')
    day_text = input('What day [DD]? ')

    return datetime.date(int(year_text), int(month_text), int(day_text))


def calc_birthday_day_of_week(bday):
    """Calculate the day of week for a given date, and return the string suitable for printing"""
    week_day = bday.weekday()
    if week_day == 0:
        return 'Monday'
    elif week_day == 1:
        return 'Tuesday'
    elif week_day == 2:
        return 'Wednesday'
    elif week_day == 3:
        return 'Thursday'
    elif week_day == 4:
        return 'Friday'
    elif week_day == 5:
        return 'Saturday'
    return 'Sunday'


def print_bday_info(bday):
    """Print the relevant information for a given birthday"""
    weekday_birth_year = calc_birthday_day_of_week(bday)
    print('Looks like you were born on a {}'.format(weekday_birth_year))

    today = datetime.date.today()
    bday_this_year = datetime.date(today.year, bday.month, bday.day)
    weekday_this_year = calc_birthday_day_of_week(bday_this_year)

    td = bday_this_year - today
    days_to_bday = td.days
    if days_to_bday < 0:
        print('Your birthday this year was on {0}, {1} days ago'.format(weekday_this_year, -days_to_bday))
    elif days_to_bday > 0:
        print('Your birthday this year is on {0}, in {1} days!'.format(weekday_this_year, days_to_bday))
    else:
        print('Happy birthday!!!')


def main():
    """Main program function"""
    separator = '--------------------------------'
    print(separator)
    print('           BIRTHDAY APP')
    print(separator)

    bday = get_birthday()
    print_bday_info(bday)


main()
