import yaml
import psycopg2

class Database():
	def __init__(self, rel_schema, table_name):
		self.schema = rel_schema
		self.table_name = table_name
		self.cfg = self.get_configuration()
		self.conn, self.cur = self.make_connection()
		self.failure_count = 0	

	def get_configuration(self):

		try:
			with open('config.yml', 'r') as ymlfile:
				cfg = yaml.load(ymlfile)
				return cfg['database']

		except(Exception) as e:
			print('\033[91m Error Opening Config File')
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
			print('\033[91m Error Connecting to Database')
			print('error: ', error)
			exit(1)
		
		return conn, cur	

	def close_connection(self):
		print('Total Failed Entries: ', self.failure_count)
		if self.conn is not None:
			self.conn.close()
			print('Database Connection is Closed...')
	
	def insert(self, entry):
		# Remove quotes from schema
		schema = str(tuple(self.schema)).replace("'", "")
		# Replace empty columns with 'null'
		entry = str(tuple(entry)).replace("''", 'null')
		# Generate Statement for Insert
		statement = "INSERT INTO {0} {1} VALUES {2}".format(self.table_name, schema, entry)
		
		try: 
			self.cur.execute(statement)
		except(Exception) as e:
			print(e)
			self.failure_count = self.failure_count + 1
		finally:
			self.conn.commit()
		pass	
