from dateutil.relativedelta import relativedelta
from datetime import datetime


def days_between(starting_date, ending_date):
    days = relativedelta(datetime.fromtimestamp(ending_date), datetime.fromtimestamp(starting_date)).days

    if days < 0:
        temp = starting_date
        starting_date = ending_date
        ending_date = temp
        days = abs(days)

    return starting_date, ending_date, days
