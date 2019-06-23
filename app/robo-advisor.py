# set up imports
from dotenv import load_dotenv
import json
import os
import requests
import datetime

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# Need to securely input API credentials
api_key = os.environ.get("ALPHAVANTAGE_API_KEY", "demo")
symbol = input("Please input a valid stock symbol: ") #need user input here
requests_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=demo{api_key}"
response = requests.get(requests_url)
#print(type(response)) <class 'requests.models.Response'> its a string and need to use json module to treat as dictionary
#print(response.status_code) 200
#print(response.text)

#parse json data
parsed_response = json.loads(response.text) #parsing string to dictionary

#create a list of dates to reference
tsd = parsed_response["Time Series (Daily)"]
date_keys = tsd.keys() #to do: sort to ensure latest date is first
dates = list(date_keys) #need to reference first in list as most recent date
#print(dates)
latest_day = dates[0]
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"] #nested dictionary
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"] 

high_prices = []
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))

recent_high = max(high_prices)
#recent_high = parsed_response["Time Series (Daily)"][latest_day]["2. high"] #recent high is maximum of all recent

low_prices = []
for date in dates:
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_low = min(low_prices)
#recent_low = parsed_response["Time Series (Daily)"][latest_day]["3. low"] #minimum of recent not latest
#breakpoint() 


# Validate input with if/elif statements 

# Get API if potentially valid input

# Reformat API error message to be user friendly. Prompt user to try again

# parse data output to make sense of and create variables

# Write historical stock prices to prices.csv

# Calculate recommendation
now = datetime.datetime.now() 
print("-------------------------")
print("SELECTED SYMBOL:" + " " + str(symbol))
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + " " + now.strftime("%Y-%m-%d %H:%M:%S"))
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