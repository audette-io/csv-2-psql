import yaml
import psycopg2

def get_db_configuration():
	with open('config.yml', 'r') as ymlfile:
		cfg = yaml.load(ymlfile)

	return cfg['database']


# Beggining of Script

db_cfg = get_db_configuration()

conn = psycopg2.connect(host=db_cfg['host'], database=db_cfg['db'], 
						user=db_cfg['user'], password=db_cfg['passwd'])

