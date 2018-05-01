# -*- coding: utf-8 -*-

import doctest
from context import modb as mongo_driver
	

def basic_find_query():
	"""Basic Find Query
	
	>>> p = mongo_driver.MoDB('127.0.0.1', 27017, database = 'fragdb', collection = 'L20')
	>>> query = '{"sequence_id":{"$lt":5}},{"sequence_id":1, "aa_sequence":1}'
	>>> L = p.db_query('find(' + query + ')')
	>>> for l in L:
	... 	print l['sequence_id'], l['aa_sequence']
	0 SSFTKDEFDCHILDEGFTAK
	1 SFTKDEFDCHILDEGFTAKD
	2 FTKDEFDCHILDEGFTAKDI
	3 TKDEFDCHILDEGFTAKDIL
	4 KDEFDCHILDEGFTAKDILD
	
	"""


if __name__ == '__main__':
	doctest.testmod()
