import yfinance as yf
import psycopg2


# Connect to database
conn = psycopg2.connect(
    dbname="investment_research",
    user="valentinaarango",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# List of stocks to fetch
tickers = ['AAPL', 'MSFT', 'TSLA', 'NVDA', 'GOOGL']

for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info

    cur.execute ( """ 
        INSERT INTO companies (ticker, company_name, industry)
        VALUES (%s, %s, %s)
        ON CONFLICT (ticker) DO NOTHING;
        """, (ticker, info['longName'], info.get('industry', 'Unknown')))

    print(f"Added {info['longName'], info['sector']}")

conn.commit()
cur.close()
conn.close()
print("\nAll companies added!")





######### Example #############
apple = yf.Ticker("AAPL")

# info = apple.info

# # print(info.keys())
#  #Print ALL available fields
# for key, value in info.items():
#     print(f"{key}: {value}")

# print(f"Company: {info['longName']}")
# print(f"Industry: {info['industry']}")
# print(f"Sector: {info['sector']}")

# history = apple.history(period = "5d")
# print("\nRecent Prices:")
# print(history[['Close']])