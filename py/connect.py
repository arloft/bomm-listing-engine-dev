import sqlite3

sqlite_file = '/Users/aarlof/CloudSync/BoMM Google Drive/Projects/listing-engine-dev/main.db'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

conn.commit()
conn.close()