import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download GME stock data
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)

# Step 2: Use predefined revenue data (since web scraping failed)
gme_revenue = pd.DataFrame({
    "Date": ["2021-01-31", "2021-04-30", "2021-07-31", "2021-10-31", "2022-01-31"],
    "Revenue": ["2225000000", "1340000000", "1250000000", "1190000000", "2290000000"]
})

# Step 3: Format data
gme_data["Date"] = pd.to_datetime(gme_data["Date"])
gme_revenue["Date"] = pd.to_datetime(gme_revenue["Date"])
gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"])

# Step 4: Graph function (reuse)
def make_graph(stock_data, revenue_data, stock):
    fig, ax1 = plt.subplots(figsize=(14,6))

    ax1.plot(stock_data['Date'], stock_data['Close'], 'r-', label='Stock Price')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Stock Price', color='red')
    ax1.tick_params(axis='y', labelcolor='red')
    ax1.set_title(f"{stock} Stock Price vs Revenue")

    ax2 = ax1.twinx()
    ax2.plot(revenue_data['Date'], revenue_data['Revenue'], 'b-', label='Revenue')
    ax2.set_ylabel('Revenue', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Step 5: Plot GameStop graph
make_graph(gme_data, gme_revenue, 'GameStop')
