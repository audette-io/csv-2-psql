from CSV import CSV
from Database import Database

import sys

def start():
	
	csv = CSV()
	database = Database(csv.get_schema(), csv.get_table_name())	
	
	try:
		print('Inserting Entries')
		for entry in csv.get_entries():
			database.insert(entry)
		print('Done Inserting')

	except(Exception) as e:
		print(e)
		print('Failed to Insert Data')
	# When Finished, Disconnect
	finally: 
		database.close_connection()	


if __name__ == '__main__':
	start()
