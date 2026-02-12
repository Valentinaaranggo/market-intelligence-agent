import psycopg2

conn = psycopg2.connect(
    dbname = "investment_research",
    user = "valentinaarango",
    host = "localhost",
    port = "5432"
)

# f is like a handle to the opened file
with open('../data/schema.sql', 'r') as f:
    # f lets you do things with the file
    schema_sql = f.read()  # read everything

cur = conn.cursor()
cur.execute(schema_sql)

conn.commit()

cur.close()
conn.close()

print("Database tables created successfully!")
  