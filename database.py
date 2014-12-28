import sqlite3
import json
from pprint import pprint
from sys import argv

script , todo = argv

conn = sqlite3.connect('example.db')

c = conn.cursor()

with open('test') as data_file:    
    data = json.load(data_file)

if todo == 'create':
	c.execute("CREATE TABLE test (id integer, start_connected_socket integer, start_connected_local_host string, start_connected_local_port integer, start_connected_remote_host string, start_connected_remote_port integer, start_version string, start_system_info string, start_timestamp_time string, start_timestamp_timesecs integer, start_connecting_to_host string, start_connecting_to_port integer, start_cookie string, start_tcp_mss_default string, start_test_start_protocol string, start_test_start_num_streams integer, start_test_start_blksize integer, start_test_start_omit integer, start_test_start_duration integer, start_test_start_bytes integer, start_test_start_blocks integer, start_test_start_reverse integer, end_streams_sender_socket integer, end_streams_sender_start integer, end_streams_sender_end integer, end_streams_sender_seconds integer, end_streams_sender_bytes integer, end_streams_sender_bits_per_second integer, end_streams_sender_retrasmits integer, end_streams_sender_max_snd_cwnd integer, end_streams_sender_max_rtt integer, end_streams_sender_min_rtt integer, end_streams_sender_mean_rtt integer, end_streams_receiver_socket integer, end_streams_receiver_start integer, end_streams_receiver_end integer, end_streams_receiver_seconds integer, end_streams_receiver_bytes integer, end_streams_receiver_bits_per_second integer, end_sum_sent_start integer, end_sum_sent_end integer, end_sum_sent_seconds integer, end_sum_sent_bytes integer, end_sum_sent_bits_per_second integer, end_sum_sent_retransmits integer, end_sum_received_start integer, end_sum_received_end integer, end_sum_received_seconds integer, end_sum_received_bytes integer, end_sum_received_bits_per_second integer,end_cpu_utilization_percent_host_total integer, end_cpu_utilization_percent_host_user integer, end_cpu_utilization_percent_host_system integer,end_cpu_utilization_percent_remote_total integer, end_cpu_utilization_percent_remote_user integer, end_cpu_utilization_percent_remote_system integer )")
elif todo == 'add':
	c.execute("DELETE FROM test WHERE id = 1")
	c.execute('insert into test (id, start_connected_socket, start_connected_local_host, start_connected_local_port, start_connected_remote_host, start_connected_remote_port, start_version, start_system_info, start_timestamp_time, start_timestamp_timesecs, start_connecting_to_host, start_connecting_to_port, start_cookie, start_tcp_mss_default, start_test_start_protocol, start_test_start_num_streams, start_test_start_blksize, start_test_start_omit, start_test_start_duration, start_test_start_bytes, start_test_start_blocks, start_test_start_reverse, end_streams_sender_socket, end_streams_sender_start, end_streams_sender_end, end_streams_sender_seconds, end_streams_sender_bytes, end_streams_sender_bits_per_second, end_streams_sender_retrasmits, end_streams_sender_max_snd_cwnd, end_streams_sender_max_rtt, end_streams_sender_min_rtt, end_streams_sender_mean_rtt, end_streams_receiver_socket, end_streams_receiver_start, end_streams_receiver_end, end_streams_receiver_seconds, end_streams_receiver_bytes, end_streams_receiver_bits_per_second, end_sum_sent_start, end_sum_sent_end, end_sum_sent_seconds, end_sum_sent_bytes, end_sum_sent_bits_per_second, end_sum_sent_retransmits, end_sum_received_start, end_sum_received_end, end_sum_received_seconds, end_sum_received_bytes, end_sum_received_bits_per_second, end_cpu_utilization_percent_host_total, end_cpu_utilization_percent_host_user, end_cpu_utilization_percent_host_system, end_cpu_utilization_percent_remote_total, end_cpu_utilization_percent_remote_user, end_cpu_utilization_percent_remote_system) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
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
			data['start']['test_start']['reverse'],
			data['end']['streams'][0]['sender']['socket'],
			data['end']['streams'][0]['sender']['start'],
			data['end']['streams'][0]['sender']['end'],
			data['end']['streams'][0]['sender']['seconds'],
			data['end']['streams'][0]['sender']['bytes'],
			data['end']['streams'][0]['sender']['bits_per_second'],
			data['end']['streams'][0]['sender']['retransmits'],
			data['end']['streams'][0]['sender']['max_snd_cwnd'],
			data['end']['streams'][0]['sender']['max_rtt'],
			data['end']['streams'][0]['sender']['min_rtt'],
			data['end']['streams'][0]['sender']['mean_rtt'],
			data['end']['streams'][0]['receiver']['socket'],
			data['end']['streams'][0]['receiver']['start'],
			data['end']['streams'][0]['receiver']['end'],
			data['end']['streams'][0]['receiver']['seconds'],
			data['end']['streams'][0]['receiver']['bytes'],
			data['end']['streams'][0]['receiver']['bits_per_second'],
			data['end']['sum_sent']['start'],
			data['end']['sum_sent']['end'],
			data['end']['sum_sent']['seconds'],
			data['end']['sum_sent']['bytes'],
			data['end']['sum_sent']['bits_per_second'],
			data['end']['sum_sent']['retransmits'],
			data['end']['sum_received']['start'],
			data['end']['sum_received']['end'],
			data['end']['sum_received']['seconds'],
			data['end']['sum_received']['bytes'],
			data['end']['sum_received']['bits_per_second'],
			data['end']['cpu_utilization_percent']['host_total'],
			data['end']['cpu_utilization_percent']['host_user'],
			data['end']['cpu_utilization_percent']['host_system'],
			data['end']['cpu_utilization_percent']['remote_total'],
			data['end']['cpu_utilization_percent']['remote_user'],
			data['end']['cpu_utilization_percent']['remote_system']))

	myrows = c.execute("select * from test")

	for row in myrows:
		print row

else:
	print "================================="
	print "you can use one of these methodes"
	print "1. python database.py create ----> in order to create database"
	print "2. python database.py add    ----> in order to add your data from Json text file to database"
	print "================================="

conn.commit()
 

conn.close()
