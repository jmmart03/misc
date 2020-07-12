#shared functions for python
#set for python3.6

#database
import pyodbc
import MySQLdb as mdb
importMySQLdb.cursors

#other
import configparser
import logging

log = logging.getLogger('jmm')

def load_config(config_file=None):
	#attempts to load default credentials file, which should be in the same directory as this file
	if config_file is None:
		config_file = 'jmm_creds.ini'
	config = configparser.ConfigParser()
	config.read(config_file)
	return config


def sqlserver_connect(creds):
	#requires dict of credentials for this database
	#returns connection object
	#uses driver v17
	conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};' +
							f'SERVER={creds.get('server')};' +
							f'DATABASE={creds.get('db')};' +
							f'uid={creds.get('user')};' +
							f'pwd={creds.get('pw')};'
	return pyodbc.connect(conn_str)


def mysql_connect(creds):
	#requires dict of credentials for this database
	#returns connection object
	#if ssl is required, add path to ca cert
	ca_cert = 'path/to/cert'
	return mdb.connect(
											host=creds.get('server')
											,port=int(creds.get('port',3306))
											,user=creds.get('user')
											,passwd=creds.get('pw')
											,db=creds.get('db')
											#,ssl = {'ca':ca_cert}
											,cursorclass=MySQLdb.cursors.DictCursor)


def oracle_connect(creds):
	#requires dict of credentials for this database
	#returns connection object
	conn_str = 'DRIVER={Oracle 12c ODBC Driver};' +
							f'DBQ={creds.get('server')}:{creds.get('port'}/{creds.get('service')};' +
							f'UID={creds.get('user')};' +
							f'PWD={creds.get('pw')};'
	return pyodbc.connect(conn_str)

