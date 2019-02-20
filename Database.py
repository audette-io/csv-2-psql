import yaml
import psycopg2

class Database():
	def __init__(self, rel_schema, table_name):
		self.schema = rel_schema
		self.table_name = table_name
		self.cfg = self.get_configuration()
		self.conn, self.cur = self.make_connection()
	
	def get_configuration(self):
		try:
			with open('config.yml', 'r') as ymlfile:
				cfg = yaml.load(ymlfile)
				return cfg['database']
		except(Exception) as e:
			print('Error Opening Config File')
			print('error: ', e)
			exit(1)
	
	def make_connection(self):
		print('Connecting to Database...')
		conn, cur = None, None
		try:
			# Connect to db
			conn = psycopg2.connect(host=self.cfg['host'], database=self.cfg['db'], 
									user=self.cfg['user'], password=self.cfg['passwd'])
			cur = conn.cursor()
		
		# If Error Connecting, Print Given Error
		except(Exception, psycopg2.DatabaseError) as error:
			print('Error Connecting to Database')
			print('error: ', error)
			exit(1)
		return conn, cur	

	def close_connection(self):
		if self.conn is not None:
			self.conn.close()
			print('Database Connection is Closed...')
	
	def insert(self, item):
		pass	
