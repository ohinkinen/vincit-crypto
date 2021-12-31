from api import getdata
from dataAnalysis import dataAnalysis

def main():
    data, days = getdata()

    prices = data['prices']
    volume = data['total_volumes']

    dataAnalysis(prices, volume, days)

if __name__ == "__main__":
    main()
