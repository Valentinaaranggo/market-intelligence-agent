import yfinance as yf


apple = yf.Ticker("AAPL")

# print(dir(apple))
# print("\n")

# Financial data is available through these attributes:
# print(apple.quarterly_financials)  # Quarterly income statement
# print("\n")
# print(apple.financials)            # Annual income statement
# print(apple.financials.head)
print(apple.quarterly_financials)
print(apple.quarterly_financials.shape)
print(apple.quarterly_financials.index)    # What are the rows?
print(apple.quarterly_financials.columns)  # What are the columns?



# # Get just 5 days of data (small and manageable)
# apple = yf.Ticker("AAPL")
# history = apple.history(period="5d")

# print("="*60)
# print("WHAT IS THE DATAFRAME?")
# print("="*60)
# print(history)
# print()

# print("="*60)
# print("LOOPING THROUGH WITH ITERROWS")
# print("="*60)

# for index, row in history.iterrows():
#     print("\n--- NEW ROW ---")
    
#     print("\nINDEX (the date):")
#     print(f"  Type: {type(index)}")
#     print(f"  Value: {index}")
#     print(f"  As date only: {index.date()}")
    
#     print("\nROW (all the data for that day):")
#     print(f"  Type: {type(row)}")
#     print(f"  Full row:\n{row}")
    
#     print("\nEXTRACTING VALUES:")
#     print(f"  Close price: ${row['Close']:.2f}")
#     print(f"  Volume: {row['Volume']:,}")
    
#     # Only show first row, then stop
#     break

# print("\n" + "="*60)
# import json

# print(dir(yf))

# apple=yf.Ticker("AAPL")

# info = apple.info
# print(json.dumps(info, indent=2)) 

# print(dir(apple))

# # info sounds simple
# print(type(apple.info))  # What is it?
# print(apple.info)        # What's in it?

# print(apple.info.keys())

# # Get specific values
# print(apple.info['longName'])
# print(apple.info['sector'])

# hist = apple.history(period="5d")

# print(type(hist))  # What type is this?
# print(hist)  

# hist1 = apple.history(period="1d")
# print(f"1 day: {len(hist1)} rows")

# hist2 = apple.history(period="1mo")
# print(f"1 month: {len(hist2)} rows")

# # What if I want a date range instead?
# hist3 = apple.history(start="2024-01-01", end="2024-12-31")
# print(f"Year 2024: {len(hist3)} rows")

# help(apple.history)