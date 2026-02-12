import yfinance as yf
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    dbname="investment_research",
    user="valentinaarango",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("DELETE FROM financials;")

cur.execute("SELECT ticker FROM companies")
rows= cur.fetchall()

print(rows)

tickers = [row[0] for row in rows]

print(tickers)

for ticker in tickers:
    stock = yf.Ticker(ticker)
    #dataframe
    quarterly_financials = stock.quarterly_financials
    #dataframe transposed
    quarterly_financials_t = quarterly_financials.T

    for index, row in quarterly_financials_t.iterrows():
        date = index

        # Check if both values exist and are not NaN
        if 'Net Income' in row and "Total Revenue" in row:
            profit = row['Net Income']
            revenue = row['Total Revenue']

            if pd.notna(profit) and pd.notna(revenue):
                profit = float(profit)
                revenue = float(revenue)

                cur.execute("""
                    INSERT INTO financials (ticker, quarter_end_date, revenue, profit)
                    VALUES (%s, %s, %s, %s)
                """, (ticker,date,revenue,profit))

conn.commit()
cur.close()
conn.close()


    



  
 

    
