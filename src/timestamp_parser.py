import calendar
from src.ask_datetime import ask_datetime


def parse_utc_timestamp(message):
    while True:
        date = ask_datetime(message)

        try:
            utc_time = calendar.timegm(date.utctimetuple())
            break
        except ValueError:
            print(message + " in dd-mm-yyyy format")

    return utc_time
