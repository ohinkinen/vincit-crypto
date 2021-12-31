import calendar
from askDatetime import askDatetime

def parseUTCTimestamp(message):
    while True:
        date = askDatetime(message)

        try:
            utc_time = calendar.timegm(date.utctimetuple())
            break
        except ValueError:
            print(message + " in dd-mm-yyyy format")

    return utc_time
