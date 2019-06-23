# set up imports
from dotenv import load_dotenv
import json
import os
import requests
import datetime
import csv

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# Need to securely input API credentials
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
symbol = input("Please input a valid stock symbol in all caps: ") #https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters
chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
if any((c not in chars) for c in symbol):
    print("Stock symbol invalid. Please try again with a valid symbol.")
    exit()    
elif len(symbol) > 4:
    print("Stock symbol invalid. Please try again with a valid symbol.")
    exit()
else:
    pass

#print(type(symbol)) 

requests_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=demo{api_key}"
response = requests.get(requests_url)
#print(type(response)) <class 'requests.models.Response'> its a string and need to use json module to treat as dictionary
#print(response.status_code) 200
#print(response.text)
if response.status_code != 200:
    print("Sorry we have encountered an error with the data request. Please try again.")
    exit()

parsed_response = json.loads(response.text) #parsing string to dictionary

try:
   parsed_response['Time Series (Daily)']
except:
   print("Sorry we have encountered an error with the data request. Please try again.")
   exit()

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

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")# the csv file is not viewing in visual studio but it is showing when i open the csv on my desktop
csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
    #loop to write each row. create dictionary
        writer.writerow({
            "timestamp": date,
            "open": tsd[date]["1. open"],
            "high": tsd[date]["2. high"],
            "low": tsd[date]["3. low"],
            "close": tsd[date]["4. close"],
            "volume": tsd[date]["5. volume"]
        })
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
if float(latest_close) > float(recent_high):
    print("RECOMMENDATION: SELL\nRECOMMENDATION REASON: Latest close is greater than recent highs. Don't you like money?") #https://stackoverflow.com/questions/34980251/how-to-print-multiple-lines-of-text-with-python
elif float(latest_close) < float(recent_low):
    print("RECOMMENDATION: BUY\nRECOMMENDATION REASON: Latest close is less than recent lows. Don't you like money?")
else: 
    print("RECOMMENDATION: HOLD\nRECOMMENDATION REASON: Data is inconclusive. We're feeling risk averse")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
