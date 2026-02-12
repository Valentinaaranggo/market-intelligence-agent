import yfinance as yf
import psycopg2

conn = psycopg2.connect(
    dbname="investment_research",
    user="valentinaarango",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Clear existing stock prices
cur.execute("DELETE FROM stock_prices;")
conn.commit()

# Then continue with your existing code...

cur.execute( "SELECT ticker FROM companies")
rows = cur.fetchall()



print(rows)

# tickers =[]
# for row in rows:
#     ticker = row[0]
#     # print(f"{ticker} from {row}")
#     tickers.append(ticker)
#     # print(tickers)

##[WHAT_TO_COLLECT for ITEM in LIST] ##
tickers= [row[0] for row in rows]


for ticker in tickers:
    stock = yf.Ticker(ticker)
    history = stock.history(period="1y")
    # print(history)

    for index, row in history.iterrows():
        # print(index)
        date = index.date()  # The index is the date
        # print(date)
        price = float(row['Close'])  # Get the closing price

        
        # print(f"{ticker} on {date}: ${price}")

        cur.execute("""
            INSERT INTO stock_prices (ticker, date, stock_price)
            VALUES (%s, %s, %s)
        """, (ticker, date, price))

conn.commit()
cur.close()
conn.close()  
    