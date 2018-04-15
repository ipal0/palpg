import psycopg2

class db:
	def __init__(self, dbname, user):
		self.conn = psycopg2.connect("dbname=%s user=%s" %(dbname,user))
		self.conn.set_session(autocommit=True)
		self.cur = self.conn.cursor()

	def read(self, command, args=(), flat=True):
		self.cur.execute(command, args)
		f = self.cur.fetchall()
		if not f or not flat:
			return f
		else:
			if len(f[0]) == 1:
				f = [i[0] for i in f]
				if len(f) == 1:
					f = f[0]
			return f
	
	def write(self, command, args=()):
		self.cur.execute(command, args)

	def clear(self): # Resets the connection
		self.conn.reset()
	
	def __del__(self):
		self.cur.close()
		self.conn.close()
