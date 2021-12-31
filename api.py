from pycoingecko import CoinGeckoAPI
from timestampParser import parseUTCTimestamp
from daysFromStartToEnd import daysBetween

cg = CoinGeckoAPI()

def getdata():
    startingDate = parseUTCTimestamp("Starting date")
    endingDate = parseUTCTimestamp("Ending date")
    utc_day = 86400
    startingDate, endingDate, days = daysBetween(startingDate, endingDate)
    days = 90-days

    data = cg.get_coin_market_chart_range_by_id("bitcoin", "eur", str(startingDate - utc_day*days), str(endingDate + 3600))

    return data, days
