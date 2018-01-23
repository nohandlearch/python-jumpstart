"""
Manage the lifecycle of a journal object (create, update, save)
"""

import csv
import datetime
import os

def get_journal_filename(journal_name):
    """
    Return the file path of a journal based on the name
    """
    return os.path.join('data', journal_name + '.csv')

def load(journal_name):
    """
    Load a journal file from disk, or create a new blank journal if none exists
    """
    journal = list()

    filename = get_journal_filename(journal_name)

    if os.path.exists(filename):
        with open(filename, 'r', newline='') as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                journal.append((datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f'), row[1]))

    return journal


def show(journal_data):
    """
    Prints the journal data to screen
    """
    for (entry_date, entry) in reversed(journal_data):
        print("Entry from {0}: {1}".format(entry_date.strftime('%Y-%m-%d %I:%M %p'), entry))


def save(journal_data, journal_name):
    """
    Saves the journal file out to disk as json file
    """
    filename = get_journal_filename(journal_name)

    with open(filename, 'w', newline='') as out_file:
        journal_writer = csv.writer(out_file, doublequote=True)
        journal_writer.writerows(journal_data)
