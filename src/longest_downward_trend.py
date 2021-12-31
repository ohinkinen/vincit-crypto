def longest_downward(prices, days):
    counter = 0
    longest = 0
    last_days_price = prices[days][1]

    for i in range(days, len(prices)):
        days_price = prices[i][1]

        if days_price < last_days_price:
            counter += 1
        else:
            if longest < counter:
                longest = counter

            counter = 0

        last_days_price = days_price

    return longest
