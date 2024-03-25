import datetime
import pyEX  
from pyEX import Client

class StockTracker:
    def __init__(self, ticker):
        self.ticker = ticker
        self.api_token = 'pk_0eb499c51ecc47d79cf1b44484fb7648'  # Replace with your actual token
        self.client = Client(api_token=self.api_token, version='v1')

    def get_current_price(self):
        quote_data = self.client.quoteDF(symbol=self.ticker)
        price = float(quote_data['latestPrice'])
        time_stamp = quote_data.get('latestTime', None)  # Adjust timestamp field if needed
        dt_object = datetime.datetime.strptime(time_stamp, '%Y-%m-%d %H:%M:%S') 

        return price, dt_object

    def get_company_info(self):
        company_data = self.client.companyDF(symbol=self.ticker)
        company_name = company_data['companyName']
        sector = company_data['sector']
        # ... extract other relevant fields from company_data 
        return company_name, sector,  # ... and more 

    def get_key_stats(self):
        stats_data = self.client.keyStatsDF(symbol=self.ticker)
        pe_ratio = stats_data['peRatio']
        market_cap = stats_data['marketcap']
        # ... extract other relevant stats from stats_data
        return pe_ratio, market_cap,  # ... and more 
