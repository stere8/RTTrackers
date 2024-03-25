from flask import Flask, render_template, request
from stock_trackers import StockTracker2
from stock_trackers2 import StockTracker
from Stock import Stock

app = Flask(__name__)


stocks = StockTracker
trackers_List = [stocks,stocks]
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/stocktracker', methods=['GET','POST'])
def stock_tracker():
    global selected_tickers
    if request.method == 'POST':
        selected_tickers = request.form.getlist('selected_stocks')  # Get selected tickers
        search_query = request.form.get('search')  # Get the search query

    # Filter stocks based on search query (if provided)
        if search_query:
            stocks = [stock for stock in selected_tickers if search_query.lower() in stock['name'].lower()]

    # Fetch prices for selected stocks
    stock_data = []
    for ticker in selected_tickers:
        try:
            # Attempt to use StockTracker first (Alpha Vantage)
            tracker = StockTracker(ticker)
            price, time_stamp = tracker.get_current_price()
        except Exception as e:
            # If StockTracker fails, try StockTracker2 (IEX Cloud)
            print(f"Error using StockTracker for {ticker}: {e}") 
            try:
                tracker = StockTracker2(ticker)
                price, time_stamp = tracker.get_current_price() 
            except Exception as e:
                print(f"Error using StockTracker2 for {ticker}: {e}") 
                price = None  # Placeholder if both trackers fail
                time_stamp = None 

        stock_data.append({
            'ticker': ticker,
            'price': price,
            'timestamp': time_stamp
        })           

    return render_template('stocktracker.html', stock_data=stock_data)


@app.route('/selectstocks')
def stock_selector():
    stocks_List = [
    Stock('Apple', 'AAPL',0),
    Stock('Microsoft', 'MSFT',0),
    Stock('Amazon', 'AMZN',0),
    Stock('Google', 'GOOGL',0),
    Stock('Facebook', 'FB',0),
    Stock('Tesla', 'TSLA',0),
    Stock('Alphabet', 'GOOG',0),
    Stock('Nvidia', 'NVDA',0),
    Stock('Netflix', 'NFLX',0),
    Stock('PayPal', 'PYPL',0),
    Stock('Adobe', 'ADBE',0),
    Stock('Intel', 'INTC',0),
    Stock('Cisco', 'CSCO',0),
    Stock('IBM', 'IBM',0),
    Stock('Oracle', 'ORCL',0),
    Stock('Disney', 'DIS',0),
    Stock('Visa', 'V',0),
    Stock('Mastercard', 'MA',0),
    Stock('Salesforce', 'CRM',0),
    Stock('Walmart', 'WMT',0)]
    return render_template('selectstocks.html',stocks_List=stocks_List)


if __name__ == '__main__':
    app.run()
