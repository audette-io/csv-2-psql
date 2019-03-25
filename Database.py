import yaml
import psycopg2

class Database():
	def __init__(self, rel_schema, table_name):
		self.schema = rel_schema
		self.table_name = table_name
		self.cfg = self.get_configuration()
		self.conn, self.cur = self.make_connection()
		self.failure_count = 0	
		self.success_count = 0

	def get_configuration(self):

		try:
			with open('config.yml', 'r') as ymlfile:
				cfg = yaml.load(ymlfile)
				return cfg['database']

		except(Exception) as e:
			print('\033[91m Error Opening Config File\033[0m')
			print('error: ', e)
			exit(1)
	
	def make_connection(self):
		print('Connecting to Database...')
		conn, cur = None, None

		try:
			# Connect to db
			conn = psycopg2.connect(host=self.cfg['host'], database=self.cfg['db'], 
									user=self.cfg['user'], password=self.cfg['passwd'], port=self.cfg['port'])
			cur = conn.cursor()
		
		# If Error Connecting, Print Given Error
		except(Exception, psycopg2.DatabaseError) as error:
			print('\033[91m Error Connecting to Database\033[0m')
			print('error: ', error)
			exit(1)
		
		return conn, cur	

	def close_connection(self):
		print('Total Failed Entries: {0} / {1}'.format(self.failure_count, self.success_count + self.failure_count))
		if self.conn is not None:
			self.conn.close()
			print('Database Connection is Closed...')

	def format_entry(self, entry):
		indexes = []
		entry_schema = self.schema.copy()
		for i in range(len(entry)):
			if not entry[i]:
				indexes.append(i)
        	
		indexes.reverse()	        
		for i in indexes:
			del entry[i]
			del entry_schema[i]
		return entry_schema, entry
	def copy_csv(self):
		statement = 'COPY {0} FROM \'/var/lib/postgresql/csv_files/{0}.csv\' delimiter \',\' CSV HEADER'.format(self.table_name)
		print(statement)
		try: 
			self.cur.execute(statement)
			self.conn.commit()
			print('Copy Succesful')
		except(Exception) as e:
			print(e)
			self.conn.rollback()
	
	def insert(self, entry):
		schema, entry = self.format_entry(entry)
		short_tuple = len(entry) is 1
		# Remove quotes from schema
		schema = str(tuple(schema)).replace("'", "")
		# Replace empty columns with 'null'
		entry = str(tuple(entry))
		# If a tuple is 'short' the trailing comma must be removed
		if short_tuple:
			schema = schema.replace(",", "")
			entry = entry.replace(",", "")
		# Generate Statement for Insert
		statement = "INSERT INTO {0} {1} VALUES {2}".format(self.table_name, schema, entry)
		print(statement) 	# Here to display progress	
		try: 
			self.cur.execute(statement)
			self.conn.commit()
			self.success_count = self.success_count + 1
		except(Exception) as e:
			print(e)
			self.conn.rollback()
			self.failure_count = self.failure_count + 1
