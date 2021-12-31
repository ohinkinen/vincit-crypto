from datetime import datetime


def buy_and_sell(prices, days):
    max_price = prices[days]
    min_price = prices[days]
    max_flag = True
    min_flag = True

    for i in range(days+1, len(prices)):
        if max_price[1] < prices[i][1]:
            max_price = prices[i]

        else:
            max_flag = False

    for i in range(days+1, len(prices)):
        if min_price[1] > prices[i][1]:
            min_price = prices[i]

        else:
            min_flag = False

    max_price[0] = datetime.utcfromtimestamp(max_price[0]/1000).strftime("%d-%m-%Y")
    min_price[0] = datetime.utcfromtimestamp(min_price[0]/1000).strftime("%d-%m-%Y")
    max_and_min = [max_price, min_price]
    flags = [max_flag, min_flag]

    return max_and_min, flags
