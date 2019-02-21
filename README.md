# CSV to PostgreSQL
Python Script for Adding Entries to an Already Existing PostgreSQL DB

## Getting Started

### Prerequisites
```
python3
python3-pip
```

### Installing
Install Pip Dependencies
```
pip3 isntall -r requirements.txt
```

### Configuration
Open `config.yml` in your prefered text editor and fill in with specific db information.

```yml
database: 
  host: localhost 	# enter the ip of machine runnign db
  user: postgres	# enter username that has correct role for db
  passwd: password 	# enter password for db
  db: timescale		# enter name of db csv is being loaded to 
```

### Running 
```
python3 csv2psql.py <filename.csv>
```
* Note That the Filename MUST Match the Name of the Table Acquiring csv.

## Gotchas
1. Columns must match db type for that column
2. When populating a db, order of table population matters
3. If there are issues installing PyYAML, try downgrading pip
```
sudo -H pip3 install pip==8.1.1
```
