# Daily Show Comedic Actor Analysis

## Project Description

This project analyzes guest appearances on *The Daily Show* to identify comedic actors by comparing guest names against lists of known comedic actors.

The project is implemented in Python and uses the `csv`, `argparse`, and `os.path` modules.

## Project Structure

```text
daily_show_course_project/
├── data/
│   ├── daily_show_guests_acting.csv
│   ├── acting_name_f.txt
│   └── acting_name_m.txt
├── scripts/
│   └── analyze_actor.py
├── src/
│   └── comedic.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3
- No external Python packages required

## Usage

From the project root directory, configure `PYTHONPATH`:

```bash
export PYTHONPATH="$PWD/src"
```

Run the analysis:

```bash
python scripts/analyze_actor.py data/daily_show_guests_acting.csv
```

Count the matching entries:

```bash
python scripts/analyze_actor.py data/daily_show_guests_acting.csv | wc -l
```

## Implementation

### comedic.py

Contains functions for identifying comedic actors:

- `is_name_in_file(name, filename)`: Checks whether an actor's name appears in a specified text file.
- `is_comedic(name)`: Checks whether an actor's name appears in either comedic actor list.

Name comparisons are case-insensitive.

### analyze_actor.py

The main program:

1. Uses `argparse` to accept a CSV filename.
2. Reads the CSV file using Python's `csv` module.
3. Extracts actor names from the last column.
4. Calls `is_comedic()` to identify matches.
5. Prints matching actor names.

## Results

Using the current dataset, the program identified 142 matching comedic actor entries.

Repeated appearances by the same actor are counted separately.

## Notes

The analysis relies on the completeness and accuracy of the comedic actor reference lists. Actors missing from those lists will not be identified as comedic actors.