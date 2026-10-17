import os.path
import csv

module_path = os.path.dirname(__file__)

COMEDIC_FILE_LIST = [
    os.path.join(module_path, "..", 'data', 'acting_name_f.txt'),
    os.path.join(module_path, "..", 'data', 'acting_name_m.txt')
]

def read_actor_names(filename):
    """Read actor names from the last column of a CSV file."""
    acting_names = []

    with open(filename, newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            if row:  # Skip empty rows
                acting_names.append(row[-1])

    return acting_names

def is_name_in_file(name, filename):
    with open(filename, 'r') as file:
        for line in file:
            if name.lower() == line.strip().lower():
                return True
        return False
        

def is_comedic(name):
    for comedic_file in COMEDIC_FILE_LIST:
        if is_name_in_file(name, comedic_file):
            return True
    return False