import sqlite3
import json
from pprint import pprint

conn = sqlite3.connect('example.db')

c = conn.cursor()

with open('test') as data_file:    
    data = json.load(data_file)

c.execute("CREATE TABLE test (id integer, start_connected_socket integer, start_connected_local_host string, start_connected_local_port integer, start_connected_remote_host string, start_connected_remote_port integer)")
#c.execute("INSERT INTO test VALUES (1, 2, 3, 4, 5)")
c.execute('insert into test (id, start_connected_socket, start_connected_local_host, start_connected_local_port, start_connected_remote_host, start_connected_remote_port) values (?, ?, ?, ?, ?, ?)',
			(1, 
			data['start']['connected'][0]['socket'],
			data['start']['connected'][0]['local_host'],
			data['start']['connected'][0]['local_port'],
			data['start']['connected'][0]['remote_host'],
			data['start']['connected'][0]['remote_port']))

conn.commit()
myrows = c.execute("select * from test")

for row in myrows:
	print row

#c.execute("DELETE FROM test WHERE name = 'Kay' and id = 2") 

conn.close()
