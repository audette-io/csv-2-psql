import yaml
import psycopg2

def get_db_configuration():
	with open('config.yml', 'r') as ymlfile:
		cfg = yaml.load(ymlfile)

	return cfg['database']

db_cfg = get_db_configuration()


def start():
	
	conn = None
	
	print('Connecting to Database...')
	
	try:
		conn = psycopg2.connect(host=db_cfg['host'], database=db_cfg['db'], 
								user=db_cfg['user'], password=db_cfg['passwd'])
	
	# If Error Connecting, Print Given Error
	except(Exception, psycopg2.DatabaseError) as error:
		print(error)
	# When Finished, Disconnect
	finally: 
		if conn is not None:
			conn.close()
			print('Database Connection is Closed...')


if __name__ == '__main__':
	start()
