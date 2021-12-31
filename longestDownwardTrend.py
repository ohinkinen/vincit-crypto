def longestDownward(prices, days):
    counter = 0
    longest = 0
    lastDaysPrice = prices[days][1]

    for i in range(days, len(prices)):
        daysPrice = prices[i][1]

        if(daysPrice < lastDaysPrice):
            counter += 1
        else:
            if(longest < counter):
                longest = counter

            counter = 0

        lastDaysPrice = daysPrice


    return longest
