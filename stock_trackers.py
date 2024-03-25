import os
import json  
import csv
from alpha_vantage.timeseries import TimeSeries

# Retrieve your Alpha Vantage API key (as before)
API_KEY = 'XXMJFH6R76O1K0YU' 

class StockTracker2:
    def __init__(self, ticker):
        self.ticker = ticker
        self.ts = TimeSeries(key=API_KEY, output_format='json')  # Request JSON output


    def get_current_price(self):
        data, meta_data = self.ts.get_intraday(symbol=self.ticker, interval='5min', outputsize='compact')

        data_dict = data 
        first_timestamp = next(iter(data))  # Get the first timestamp
        first_entry = data[first_timestamp]
        return ((first_entry['4. close']),first_timestamp)
        

    