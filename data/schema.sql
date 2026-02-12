CREATE TABLE companies (
    company_name VARCHAR(255) NOT NULL,
    ticker VARCHAR(10) PRIMARY KEY,
    industry TEXT
);

CREATE TABLE stock_prices (
    ticker VARCHAR(10) NOT NULL REFERENCES companies(ticker),
    date DATE NOT NULL,
    stock_price DECIMAL(10,2) NOT NULL
);

CREATE TABLE financials (
    ticker VARCHAR(10) NOT NULL REFERENCES companies(ticker),
    quarter_end_date DATE NOT NULL,
    revenue DECIMAL(15,2) NOT NULL,
    profit DECIMAL(15,2) NOT NULL
);

