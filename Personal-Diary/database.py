import sqlite3

conn=sqlite3.connect('data.db')
c=conn.cursor()

c.execute('''
          CREATE TABLE diary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    date_created TEXT NOT NULL
);
''')

conn.commit()
conn.close()