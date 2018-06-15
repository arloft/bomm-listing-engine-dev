import sqlite3

sqlite_file = '/Users/aarlof/CloudSync/BoMM Google Drive/Projects/listing-engine-dev/main.db'

table_name = 'products'
id_column = 'sku'
column_name = 'title'

# connect to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# insert an ID with a specific value in column 2

try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

# tries to insert an ID (if it does not exist yet)
c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
          format(tn=table_name, idf=id_column, cn=column_name))

# updates the newly inserted or pre-existing entry
c.execute("UPDATE {tn} SET {cn}=('Hi World') WHERE {idf}=(123456)".\
          format(tn=table_name, idf=id_column, cn=column_name))

conn.commit()
conn.close()