from CSV import CSV
import yaml
import psycopg2
import sys

def start():
	db_cfg = get_db_configuration()
	table_name = 'campus_campus'
	csv = CSV()
	
	# Init Connection
	conn, cur = get_db_connection(db_cfg)
	try: 
		print('Trying to Insert Data to db')
	except(Exception) as e:
		print(e)
		print('Failed to Insert Data')
	# When Finished, Disconnect
	finally: 
		if conn is not None:
			conn.close()
			print('Database Connection is Closed...')


# -- Helper Functions --
def get_db_configuration():
	with open('config.yml', 'r') as ymlfile:
		cfg = yaml.load(ymlfile)

	return cfg['database']

def get_db_connection(db_cfg):
	print('Connecting to Database...')
	try:
		# Connect to db
		conn = psycopg2.connect(host=db_cfg['host'], database=db_cfg['db'], 
								user=db_cfg['user'], password=db_cfg['passwd'])
		cur = conn.cursor()
		return conn, cur
	# If Error Connecting, Print Given Error
	except(Exception, psycopg2.DatabaseError) as error:
		print(error)


# Set Global Variables

if __name__ == '__main__':
	start()
