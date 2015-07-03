import mysql.connector
from mysql.connector import errorcode


class DB_Manager:

	def __init__(self):
		self.dbase = "condominio"
		self.username = "root"
		self.passwrd = "jkgs1234"

		self.connect_db()
		self.create_database()

	def connect_db(self):
		try:
			self.connection = mysql.connector.connect(user=self.username, password=self.passwrd, host='127.0.0.1', database=self.dbase)
			self.cursor = self.connection.cursor()
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print ('Something is wrong with yout username and password.')
				return False
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print ('Database does not exist, attempting to create it...')
				self.create_database(self.cursor)
				return True
			else:
				print (err)
				return False

		else:
			print ('Connected')
			return True

	def create_database(self):
		try:
			self.cursor.execute(
				"CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.dbase))
		except mysql.connector.Error as err: 
			print ('Failed creating database: {}'.format(err))
			exit(1)

		try:
			self.connection.database=self.dbase
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_BAD_DB_ERROR:
				self.create_database()
				self.connection.database(self.dbase)
		else:
			print(err)
			exit(1)

	def create_table(self):
		self.table = {}

		self.table['usuario'] = (
			"CREATE TABLE 'usuario' ("
			" 'tag_id' VARCHAR(8) NOT NULL,"
			" 'nome_morador' VARCHAR NOT NULL,"
			" 'numero_casa' INT NOT NULL,"
			" 'xbee_destino' VARCHAR(16) NOT NULL"
			" 'data_cadastro' DATETIME NOT NULL "
			" PRIMARY KEY ('tag_id')")

		for name, ddl in dictionary.iteritems():
			try:
				print ('Creating table {}: '.format(name))
				self.cursor.execute(ddl)
			except mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
	 				print ('Table already exists')
				else:
					print (err.msg)
			else:
				print ('OK')


	def connected(self):
		if (self.connection.is_connected()):
			print 'Connected'
		else:
			print 'Not connected'