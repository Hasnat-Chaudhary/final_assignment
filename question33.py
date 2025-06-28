import yfinance as yf

# Create a Ticker object for GameStop
gme = yf.Ticker("GME")

# Download historical data
gme_data = gme.history(period="max")

# Reset the index
gme_data.reset_index(inplace=True)

# Display the first five rows
print(gme_data.head())
