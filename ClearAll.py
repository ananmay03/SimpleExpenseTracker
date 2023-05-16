#Only run this if you want to clear all the data from the expense report

import sqlite3

conn = sqlite3.connect("expenses.db")

clear = conn.execute("DELETE FROM expenses")

conn.commit()
conn.close()