import csv

class CSV():
	def __init__(self, args):	
		self.args = args
		self.file_name = self.get_file_name()
		self.schema, self.entries = self.open_csv()
	
	def open_csv(self):
		schema, entries = [], []

		try:
			with open(self.file_name, newline='\n') as csvfile:
				reader = csv.reader(csvfile, delimiter=',')
				csv_list = list(reader)
				schema = csv_list[0]
				for row in csv_list[1:]:	
					entries.append(row)

		except(Exception) as e:
			print(e)
			print('\033[91m Cannot Read File,')
			print('please make sure csv file follows the convention stated in documentation')
			exit(1)

		return schema, entries

	def get_file_name(self):
		file_name = None
		try:
			file_name = self.args.file 
			self.table_name = self.args.file[:-4]
		except(Exception) as e:
			print('Please Enter a File Name as the First Arg')
			exit(1)
		return file_name
	
	def get_schema(self):
		return self.schema

	def get_entries(self):
		return self.entries
	
	def get_table_name(self):
		return self.table_name

