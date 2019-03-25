from CSV import CSV
from Database import Database
from argparse import ArgumentParser

# Init Argument Parser and Acquire Arguments
parser = ArgumentParser()
parser.add_argument('-p', '--path', dest='path', default='/var/lib/postgresql/csv_files/', help='Set the Path to the Csv Files that are Being Copied to Postgres')
parser.add_argument('-c', '--copy', dest='copy', const=True, nargs='?', default=False, type=bool, help='Set Copy Flag if PSQL Copy Method Should be Used')
parser.add_argument('-f', '--file', dest='file', help='Specify File Name of CSV Being Inserted')
args = parser.parse_args()

def start():

	csv = CSV(args)
	database = Database(csv.get_schema(), csv.get_table_name())	
	if not args.file:
		print('Please include a filename using the -f flag')
	try:
		print('Inserting Entries')
		if args.copy:
			database.copy_csv();
		
		else:
			for entry in csv.get_entries():
				database.insert(entry)
			print('\033[92mDone Inserting\033[0m')

	except(Exception) as e:
		print(e)
		print('Failed to Insert Data')
	# When Finished, Disconnect
	finally: 
		print('done')
		database.close_connection()	


if __name__ == '__main__':
	start()
