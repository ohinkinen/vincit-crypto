from pycoingecko import CoinGeckoAPI
from dateParser import dateParserToUTCtime
from longestDownwardTrend import longestDownward
from highestVolume import highestVolumeDate
from buyAndSell import buyAndSell

def main():
    cg = CoinGeckoAPI()

    utc_time1, utc_time2, days = dateParserToUTCtime()
    utc_day = 86400

    data = cg.get_coin_market_chart_range_by_id("bitcoin", "eur", str(utc_time1 - utc_day*days), str(utc_time2 + 3600))

    prices = data['prices']
    volume = data['total_volumes']

    longest = longestDownward(prices, days)
    highestVolume = highestVolumeDate(volume, days)
    maxAndMin, flags = buyAndSell(prices, days)

    print("Longest downward trend during the date range: ", longest, "\n")
    print("Date: ", highestVolume[0], "\nHighest trading volume in eur: ", int(highestVolume[1]), "\n")

    if flags[0] and flags[1]:
        print("No suitable date for selling or buying")
    elif flags[0] and not(flags[1]):
        print("No suitable selling date \n")
        print("Buying date: ", maxAndMin[1][0], "\nBest buying price: ", maxAndMin[1][1])
    elif not(flags[0]) and flags[1]:
        print("No suitable buying date \n")
        print("Selling date: ", maxAndMin[0][0], "\nBest selling price: ", maxAndMin[0][1])
    else:
        print("Best selling date in the date range: ", maxAndMin[0][0], "\nBest selling price in eur: ", f'{maxAndMin[0][1]:.2f}', "\n")
        print("Best buying date in the date range: ", maxAndMin[1][0], "\nBest buying price in eur: ", f'{maxAndMin[1][1]:.2f}')

if __name__ == "__main__":
    main()
