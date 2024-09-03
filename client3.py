import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server requests
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return None
    return price_a / price_b


# Main
if __name__ == "__main__":
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(
            QUERY.format(random.random())).read())

        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" %
                  (stock, bid_price, ask_price, price))

        stock_a = "ABC"
        stock_b = "DEF"
        if stock_a in prices and stock_b in prices:
            ratio = getRatio(prices[stock_a], prices[stock_b])
            if ratio is not None:
                print("Ratio %s" % ratio)
            else:
                print(f"Cannot compute ratio for {stock_a} and {
                      stock_b} due to zero price.")
