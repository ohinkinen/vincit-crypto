from dateutil.relativedelta import relativedelta
from datetime import datetime

def daysBetween(startingDate, endingDate):
    days = (relativedelta(datetime.fromtimestamp(endingDate), datetime.fromtimestamp(startingDate)).days)

    if (days < 0):
        temp = startingDate
        startingDate = endingDate
        endingDate = temp
        days = abs(days)

    return startingDate, endingDate, days
