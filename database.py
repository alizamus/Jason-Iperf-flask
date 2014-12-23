import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute("CREATE TABLE test (id integer, name text)")

c.execute("INSERT INTO test VALUES (1, 'Jay')")
c.execute("INSERT INTO test VALUES (2, 'Kay')")
c.execute("INSERT INTO test VALUES (3, 'Ray')")

conn.commit()
myrows = c.execute("select * from test")

for row in myrows:
	print row

#c.execute("DELETE FROM test WHERE name = 'Kay' and id = 2") 

conn.commit()
myrows = c.execute("select * from test")
for row in myrows:
	print row

conn.close()
