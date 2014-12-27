import sqlite3
import json
from pprint import pprint

conn = sqlite3.connect('example.db')

c = conn.cursor()

with open('test') as data_file:    
    data = json.load(data_file)

c.execute("CREATE TABLE test (id integer, start_connected_socket integer, start_connected_local_host string, start_connected_local_port integer, start_connected_remote_host string, start_connected_remote_port integer, start_version string, start_system_info string, start_timestamp_time string, start_timestamp_timesecs integer, start_connecting_to_host string, start_connecting_to_port integer, start_cookie string, start_tcp_mss_default string, start_test_start_protocol string, start_test_start_num_streams integer, start_test_start_blksize integer, start_test_start_omit integer, start_test_start_duration integer, start_test_start_bytes integer, start_test_start_blocks integer, start_test_start_reverse integer)")
#c.execute("INSERT INTO test VALUES (1, 2, 3, 4, 5)")
c.execute('insert into test (id, start_connected_socket, start_connected_local_host, start_connected_local_port, start_connected_remote_host, start_connected_remote_port, start_version, start_system_info, start_timestamp_time, start_timestamp_timesecs, start_connecting_to_host, start_connecting_to_port, start_cookie, start_tcp_mss_default, start_test_start_protocol, start_test_start_num_streams, start_test_start_blksize, start_test_start_omit, start_test_start_duration, start_test_start_bytes, start_test_start_blocks, start_test_start_reverse) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
			(1, 
			data['start']['connected'][0]['socket'],
			data['start']['connected'][0]['local_host'],
			data['start']['connected'][0]['local_port'],
			data['start']['connected'][0]['remote_host'],
			data['start']['connected'][0]['remote_port'],
			data['start']['version'],
			data['start']['system_info'],
			data['start']['timestamp']['time'],
			data['start']['timestamp']['timesecs'],
			data['start']['connecting_to']['host'],
			data['start']['connecting_to']['port'],
			data['start']['cookie'],
			data['start']['tcp_mss_default'],
			data['start']['test_start']['protocol'],
			data['start']['test_start']['num_streams'],
			data['start']['test_start']['blksize'],
			data['start']['test_start']['omit'],
			data['start']['test_start']['duration'],
			data['start']['test_start']['bytes'],
			data['start']['test_start']['blocks'],
			data['start']['test_start']['reverse']))

conn.commit()
myrows = c.execute("select * from test")

for row in myrows:
	print row

#c.execute("DELETE FROM test WHERE name = 'Kay' and id = 2") 

conn.close()
