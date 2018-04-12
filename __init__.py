import psycopg2

class db:
	def __init__(self, dbname, user):
		self.dbname = dbname
		self.user = user
		self.conn = psycopg2.connect("dbname=%s user=%s" %(dbname,user))
		self.cur = self.conn.cursor()

	def read(self, command, args=(), flat=True):
		self.cur.execute(command, args)
		f = self.cur.fetchall()
		if not flat:
			return f
		else:
			if len(f[0]) == 1:
				f = [i[0] for i in f]
			if len(f) == 1:
				f = f[0]
			return f
	
	def write(self, command, args=()):
		self.cur.execute(command, args)
		self.conn.commit()

	def clear(self): # Reconnect if transaction error
		self.__init__(self.dbname, self.user)
	
	def __del__(self):
		self.cur.close()
		self.conn.close()
