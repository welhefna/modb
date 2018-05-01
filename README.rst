MoDB Module Repository
========================

MoDB module is a custom python module to handle mongodb database dynamic queries.



Usage
--------------
	
	from modb import MoDB as mongo_driver

Example
---------------

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
		
Setup
---------------
	
	python setup.y

