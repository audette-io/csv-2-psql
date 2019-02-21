# CSV to PostgreSQL
Python Script for Adding Entries to an Already Existing PostgreSQL DB

## Getting Started

### Prerequisites
```
python3
python3-pip
```

### Installing
1. Enter VirualEnvironment 
`source venv/bin/activate`
2. Install Pip Dependencies
`pip isntall -r requirements.txt`

### Configuration
Open config.yml in your prefered text editor
```yml
database: 
  host: localhost 	# enter the ip of machine runnign db
  user: postgres	# enter username that has correct role for db
  passwd: password 	# enter password for db
  db: timescale		# enter name of db csv is being loaded to 
```

### Running 
The following command should be executed while inside the virtualenv
```
python csv2psql.py <filename.csv>
```
* Note That the Filename Match the Name of the Table Acquiring csv.
