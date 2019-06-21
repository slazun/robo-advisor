# set up imports
from dotenv import load_dotenv
import json
import os
import requests

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# Need to securely input API credentials
api_key = os.environ.get("ALPHAVANTAGE_API_KEY", "demo")
symbol = "MSFT" #need user input here
requests_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=demo{api_key}"
response = requests.get(requests_url)
print(type(response))
print(response.status_code)
print(response.text)

# Prompt user to input a stock symbol or symbols

# Validate input with if/elif statements 

# Get API if potentially valid input

# Reformat API error message to be user friendly. Prompt user to try again

# parse data output to make sense of and create variables

# Write historical stock prices to prices.csv

# Calculate recommendation

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")