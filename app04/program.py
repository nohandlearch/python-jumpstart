#!/usr/bin/env python
"""
Main program file for journal application

App #4 from the Python Jumpstart course from TalkPython.fm
"""

import datetime
import sys
import journal


def event_loop(journal_data, journal_name):
    """
    Event loop to handle user input and logic
    """
    user_input = None

    while user_input != 'x':
        user_input = input('What do you want to do? [L]ist, [A]dd, or E[x]it? ')
        user_input = user_input.lower().strip()
        if user_input == 'l':
            journal.show(journal_data)
        elif user_input == 'a':
            entry = input('Enter your journal entry:\n')
            entry_date = datetime.datetime.now()
            journal_data.append((entry_date, entry))
        elif user_input != 'x':
            print('Could not understand your input {}'.format(user_input))

    journal.save(journal_data, journal_name)


def main(argv):
    """
    Main progam function to setup data and call event loop
    """
    if len(argv) > 1:
        journal_name = argv[1]
    else:
        journal_name = 'default'
    journal_data = journal.load(journal_name)

    event_loop(journal_data, journal_name)


if __name__ == '__main__':
    main(sys.argv)
