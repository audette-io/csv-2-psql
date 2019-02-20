import sys
import csv

class CSV():
	def __init__(self):	
		self.file_name = self.get_file_name()
		self.scheme, self.entries = self.open_csv()
		print(self.scheme)
		print(self.entries)	
	def open_csv(self):
		scheme, entries = [], []
		try:
			with open(self.file_name, newline='\n') as csvfile:
				reader = csv.reader(csvfile, delimiter=' ')
				csv_list = list(reader)
				scheme = csv_list[0][0].split(',') 
				for row in csv_list[1:]:	
					entries.append(row[0].split(','))
		except(Exception) as e:
			print(e)
			print('Cannot Read File,')
			print('please make sure csv file follows the convention')
			exit(1)
		finally: 
			print('Open File - Success')
		return scheme, entries

	def get_file_name(self):
		file_name = None
		try:
			file_name = sys.argv[1]
		except(Exception) as e:
			print('Please Enter a File Name as the First Arg')
			exit(1)
		return file_name
	
	def get_scheme(self):
		pass
