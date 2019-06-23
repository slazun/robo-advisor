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
#print(type(response)) <class 'requests.models.Response'> its a string and need to use json module to treat as dictionary
#print(response.status_code) 200
#print(response.text)

parsed_response = json.loads(response.text) #parsing string to dictionary
latest_day = "2019-06-21"
tsd = parsed_response["Time Series (Daily)"]
date_keys = tsd.keys()
dates = list(date_keys)
print(dates)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"] #nested dictionary
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"] #need to make date not hard coded
recent_high = parsed_response["Time Series (Daily)"][latest_day]["2. high"] #need to make date not hard coded
recent_low = parsed_response["Time Series (Daily)"][latest_day]["3. low"] #need to make date not hard coded
#breakpoint() 

# Prompt user to input a stock symbol or symbols

# Validate input with if/elif statements 

# Get API if potentially valid input

# Reformat API error message to be user friendly. Prompt user to try again

# parse data output to make sense of and create variables

# Write historical stock prices to prices.csv

# Calculate recommendation

print("-------------------------")
print("SELECTED SYMBOL:" + " " + str(symbol))
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY:" + " " + str(last_refreshed))
print("LATEST CLOSE:" + " " + str(to_usd(float(latest_close)))) #need to convert string to float to use usd function
print("RECENT HIGH:" + " " + str(to_usd(float(recent_high)))) 
print("RECENT LOW:" + " " + str(to_usd(float(recent_low)))) 
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")