from src.api import get_data
from src.data_analysis import data_analysis


def main():
    data, days = get_data()

    prices = data['prices']
    volume = data['total_volumes']

    data_analysis(prices, volume, days)


if __name__ == "__main__":
    main()
