"""MoDB 

A database custom handler

usage :
	from modb import Mongo
	
Example:
	
	
	try:
		#open datbase connection
		p = MoDB('127.0.0.1', 27017, database = 'fragdb', collection = 'L20')
		
		#database pymongo query
		query = '{"sequence_id":{"$lt":5}},{"sequence_id":1, "aa_sequence":1}'
		
		#excute pymongo query using db_query method
		L = p.db_query('find(' + query + ')')
		
		#print query results
		for l in L:
			print l
		
		L = p.db_query('find({"sequence_id" : {"$lt" : 5}},{"sequence_id":1, "pdb_id":1, "aa_sequence":1})')
		
		print p.db_query('find().skip(100)')
		
	except:
		#exception handler
		print "Exception is raised !", sys.exc_info()
	else:
		#print results of 
		for l in L:
			print l['sequence_id'], l['aa_sequence']
	finally:
		p.close()	

Requirements:
	pymongo == 3.6.1
	
TODO:
	*Extend db_query method
	*Apply pytest
	
"""

import sys
import socket
import pymongo
import pprint

 

class MoDB(object):
	"""MoDB Class

	Mongodb module for managing database qurey based on pymongo driver.
	MoDB support all kind of pymongo queries.
	
	Attributes:
		_connection (str) : database connection information
		_server_info (str) : server information.
		_database (str) : database name.
		_collection (str) : collection name.
	
	"""
	
	__slots__=['_connection','_server_info','_database','_collection']
	
	def __init__(self, host, port, database=None, collection=None):
		"""MoDB Initialization

		This method Initializae the connection with mongodb database, and validate the connection.

		Args:
			host (str): mongodb host ip address.
			port (int): mongodb port number.

		Kwargs:
			database (str) : mongodb database name.
			collection (str) : mongodb collection name.

		Returns:
			None

		Rasis:
			ValueError : IP address is not in valid format.
			ValueError : Port number is not in vaild format.
			ConnecionFailure : connection to mongodb failure.
			ServerSelectionTimeoutError :  connection time out.
		"""
		
		try:
			self._is_valid_host_ip_address(host)
		except ValueError:
			raise ValueError("Host IP address is invalid " + str(host))

			
		try:
			self._is_valid_port(port)
		except ValueError:
			raise ValueError("Port Number is not valid " + str(port))
			

		try:
			self._connection = pymongo.MongoClient("mongodb://{}:{}/".format(host,port), serverSelectionTimeoutMS=10, connectTimeoutMS=20000)
			self._server_info = self._connection.server_info()
			
		except pymongo.errors.ConnectionFailure as err:
			print "\nMongodb connection failure ConnectionFailure {}".format(err)
			raise

		except pymongo.errors.ServerSelectionTimeoutError as err:
			print "\nAlways remember to edit the /etc/mongod.conf file and set your bind_ip = 0.0.0.0 in order to make connections externally."
			print "\nMongodb Connection Failure ServerSelectionTimeoutError {}".format(err)
			raise
			
		else:

			self._database = database
			self._collection = collection

			if database :
				self._connection[database]
				
			if database:
				if collection : 
					self._connection[database][collection]

			
	def db_query(self, query):
		"""Query 
		
		Query method excute Mongodb query, it accept the mongodb curd query as string
		and return the results as it is.
		
		Args:
			query (str): mongodb query in string format.
		kwargs:
			None.
		Returns:
			results : documents iterators of query results.
		Raises:
			None.
			
		"""
		
		if self._database == None :
			raise IOError("Mongodb database is None.")
			
		if self._collection == None :
			raise IOError("Mongodb collection is None.")
			
		if self._collection == None :
			raise IOError("Mongodb collection is None.")
			
		results = None

		try:
			exec( pymongo_expression % query)
		except:
			print "Operation failure : ", sys.exc_info()[1]
			raise
		
		return results
		
		
	def _check_connection(self):
		"""Check connection
		
		Check if the connection is alive
		
		"""
		
		return self._connection
		
	def _check_database(self, database):
		"""Check if database is in mongodb databases
		
		"""
		
		database_names = self._connection.database_names()
		return True if database in database_names else False

	
	def _check_collection(self, collection):
		"""Check collection
		
		"""
		
		collection_names = self._connection[self._database].collection_names()
		return True if collection in collection_names else False
		
	@property
	def server_info(self):
		return self._server_info
		
	@property
	def database(self):
		return self._database
	
	@property
	def collection(self):
		return _collection
	
	@property
	def connection(self):
		return self._connection
		
	@database.setter
	def database(self,database):
		self._database = databse
		self._connection[database]
		
	@collection.setter
	def collection(self,collection):
		self._collection = collection
		self._connection[self._database][self._collection]
		
	
	def _is_valid_host_ip_address(self,host):
		"""Is Valid IP Address
		
		Check wheather the IP address of mongodb server is a live or not.
		
		Args:
			host (str): IP address is string format.
		Kwargs:
			None.
		Returns:
			None.
		Raises:
			ValueError : IP address is not valid.
			
		"""
		
		try:
			socket.inet_aton(host)
		except socket.error:
			raise ValueError("Invalid IP address : " + str(sys.exc_info()[1]))
			
	def _is_valid_port(self,port):
		"""Is Valid Port
		
		Vaildate the connection port 
		
		Args:
			port (int) :  port number in integer format.
		Kwargs:
			None.
		Returns:
			None.
		Raises:
			ValueError : Port number is not an integer.
			ValueError : Port number is not in valid range.
			
		"""
		
		try:
			port = int(port)
		except:
			raise ValueError("Port Number is not an integer." + str(sys.exc_info()[1]))
			
		if port < 0 or port > 65535:
			raise ValueError("Port number is out of range [ 0 : 65535 ]. ")
		
		
			
	def close(self):
		"""Close
		Close Mongodb connection
		
		Args:
			None.
		Kwargs:
			None.
		Returns:
			None.
		Raises:
			None.
		
		"""
		
		self._connection.close()




pymongo_expression = """
try: 
	results = self._connection[self._database][self._collection].%s 
except: 
	raise
"""		
		
if __name__ == "__main__":
	
	try:
		p = MoDB('127.0.0.1', 27017, database = 'fragdb', collection = 'L20')
		query = '{"sequence_id":{"$lt":5}},{"sequence_id":1, "aa_sequence":1}'
		
		L = p.db_query('find(' + query + ')')
		
		for l in L:
			print l
			
		L = p.db_query('find({"sequence_id" : {"$lt" : 5}},{"sequence_id":1, "pdb_id":1, "aa_sequence":1})')
		
		print p.db_query('find().skip(100)')
		
	except:
		print "Exception is raised !", sys.exc_info()
	else:
		for l in L:
			print l['sequence_id'], l['aa_sequence']
	finally:
		p.close()
		