from dateutil.parser import parse


def ask_datetime(message):
    while True:
        try:
            date = parse(input(message + " (format: dd-mm-yyyy): "), dayfirst=True)
            return date
        except ValueError:
            print("Could not parse input")
