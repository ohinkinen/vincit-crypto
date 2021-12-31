from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime
import calendar

def dateParserToUTCtime():
    while True:
        isDateValid = True
        try:
            date = parse(input("Starting date in dd-mm-yyyy format: "), dayfirst=True)
        except ValueError:
            print("Input the date in dd-mm-yyyy format")
            isDateValid = False

        if isDateValid:
            try:
                utc_time1 = calendar.timegm(date.utctimetuple())
                break
            except ValueError:
                print("Input the date in dd-mm-yyyy format")


    while True:
        isDateValid = True
        try:
            date = parse(input("Ending date in dd-mm-yyyy format: "), dayfirst=True)
        except ValueError:
            print("Input the date in dd-mm-yyyy format")
            isDateValid = False

        if isDateValid:
            try:
                utc_time2 = calendar.timegm(date.utctimetuple())
                break
            except ValueError:
                print("Input the date in dd-mm-yyyy format")

    days = (relativedelta(datetime.fromtimestamp(utc_time2), datetime.fromtimestamp(utc_time1)).days)

    if(days < 0):
        temp = utc_time1
        utc_time1 = utc_time2
        utc_time2 = temp
        days = abs(days)

    days = 90 - days

    return utc_time1, utc_time2, days
