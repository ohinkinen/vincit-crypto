from pycoingecko import CoinGeckoAPI
from timestamp_parser import parse_utc_timestamp
from days_from_start_to_end import days_between

cg = CoinGeckoAPI()


def get_data():
    starting_date = parse_utc_timestamp("Starting date")
    ending_date = parse_utc_timestamp("Ending date")
    utc_day = 86400
    starting_date, ending_date, days = days_between(starting_date, ending_date)
    days = 90-days

    data = cg.get_coin_market_chart_range_by_id("bitcoin", "eur", str(starting_date - utc_day*days),
                                                str(ending_date + 3600))

    return data, days
