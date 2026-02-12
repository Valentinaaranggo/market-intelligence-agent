import yfinance as yf
import psycopg2

conn = psycopg2.connect(
    dbname="investment_research",
    user="valentinaarango",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT ticker FROM companies")
rows= cur.fetchall()

print(rows)

tickers = [row[0] for row in rows]

print(tickers)
