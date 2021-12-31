from src.longest_downward_trend import longest_downward
from src.highest_volume import highest_volume_date
from src.buy_and_sell import buy_and_sell


def data_analysis(prices, volume, days):
    longest = longest_downward(prices, days)
    highest_volume = highest_volume_date(volume, days)
    max_and_min, flags = buy_and_sell(prices, days)

    print("\nBitcoin data:\n")
    print("Longest downward trend during the date range: ", longest, "\n")
    print("Highest trading volume in eur: ", int(highest_volume[1]), "\nDate: ", highest_volume[0], "\n")

    if flags[0] and flags[1]:
        print("No suitable date for selling or buying")
    elif flags[0] and not (flags[1]):
        print("No suitable selling date \n")
        print("Buying date: ", max_and_min[1][0], "\nBest buying price: ", max_and_min[1][1])
    elif not (flags[0]) and flags[1]:
        print("No suitable buying date \n")
        print("Selling date: ", max_and_min[0][0], "\nBest selling price: ", max_and_min[0][1])
    else:
        print("Best date for selling in the date range: ", max_and_min[0][0], "\nBest selling price in eur: ",
              f'{max_and_min[0][1]:.2f}', "\n")
        print("Best date for buying in the date range: ", max_and_min[1][0], "\nBest buying price in eur: ",
              f'{max_and_min[1][1]:.2f}')
