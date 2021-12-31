from dateutil.parser import parse

def askDatetime(message):
    while True:
        try:
            date = parse(input(message + " (format: dd-mm-yyyy): "), dayfirst=True)
            return date
        except ValueError:
            print("Could not parse input")
