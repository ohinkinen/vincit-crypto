from datetime import datetime

def buyAndSell(prices, days):
    maxPrice = prices[days]
    minPrice = prices[days]
    maxFlag = True
    minFlag = True

    for i in range(days+1, len(prices)):
        if(maxPrice[1] < prices[i][1]):
            maxPrice = prices[i]

        else:
            maxFlag = False

    for i in range(days+1, len(prices)):
        if(minPrice[1] > prices[i][1]):
            minPrice = prices[i]

        else:
            minFlag = False

    maxPrice[0] = datetime.utcfromtimestamp(maxPrice[0]/1000).strftime("%d-%m-%Y")
    minPrice[0] = datetime.utcfromtimestamp(minPrice[0]/1000).strftime("%d-%m-%Y")
    maxAndMin = [maxPrice, minPrice]
    flags = [maxFlag, minFlag]

    return maxAndMin, flags
