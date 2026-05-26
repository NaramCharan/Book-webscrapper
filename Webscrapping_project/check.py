import sqlite3
import pandas as pd

conn = sqlite3.connect("Data/books_data.db")

df = pd.read_sql("SELECT * FROM Books", conn)

df.to_csv("books_data.csv", index=False)

conn.close()