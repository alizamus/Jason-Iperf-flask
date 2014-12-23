import sqlite3
import json
from pprint import pprint

conn = sqlite3.connect('example.db')

c = conn.cursor()

with open('test') as data_file:    
    data = json.load(data_file)
c.execute("CREATE TABLE test (id integer, sum_sent_start integer, sum_sent_end integer,sum_sent_seconds integer, sum_sent_bytes integer,sum_sent_bits_per_second integer, sum_sent_retransmits integer)")
#c.execute("INSERT INTO test VALUES (1, 2, 3, 4, 5)")
c.execute('insert into test (id, sum_sent_start, sum_sent_end, sum_sent_seconds, sum_sent_bytes, sum_sent_bits_per_second, sum_sent_retransmits) values (?, ?, ?, ?, ?, ?, ?)',
			(1, 
			data['end']['sum_sent']['start'],
			data['end']['sum_sent']['end'],
			data['end']['sum_sent']['seconds'],
			data['end']['sum_sent']['bytes'],
			data['end']['sum_sent']['bits_per_second'],
			data['end']['sum_sent']['retransmits']))

pprint (data['end']['sum_sent']['end'])

conn.commit()
myrows = c.execute("select * from test")

for row in myrows:
	print row

#c.execute("DELETE FROM test WHERE name = 'Kay' and id = 2") 

conn.close()
