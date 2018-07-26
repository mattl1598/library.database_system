<<<<<<< HEAD
import sqlite3
import books_api as books


def dbInputIn(input1):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("INSERT INTO input VALUES (\"")
	cmd += str(input1)
	cmd += str(chr(34))
	cmd += str(chr(41))
	#print(cmd)
	c.execute(cmd)
	conn.commit()
	conn.close()


def dbInputOutAll():
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	c.execute("SELECT * FROM input")
	data = c.fetchall()
	conn.close()
	#return data
	final = []
	for count in range(len(data)):
		value = str(data[count])
		real = value[2:len(value)-3]
		print(real)
		final.append(real)
	return final


def dbInputOut():
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	c.execute("SELECT * FROM input")
	data = c.fetchall()
	conn.close()
	# return data
	value = str(data[len(data)-1])
	real = value[2:len(value) - 3]
	return real


def checkBook(isbn):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("SELECT * FROM changed_books WHERE isbn = (\"")
	cmd += str(isbn)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	data = c.fetchall()
	conn.close()
	print(data)
	if data == "[]":
		return False
	else:
		return True

def addBook(isbn, a, b, c, d, e, f, g, h, i):
	#compare to google books then update sql
	a1, b1, c1, d1, e1, f1, g1, h1, i1 = books.getAll(isbn)
	if a == a1:
		a = "None"
	if b == b1:
		b = "None"
	elif b == "":
		b = "None"
	if c == c1:
		c = "None"
	elif c == "":
		c = "None"
	if d == d1:
		d = "None"
	if e == e1:
		e = "None"
	if f == f1:
		f = "None"
	if g == g1:
		g = "None"
	if h == h1:
		h = "None"
	if i == i1:
		i = "None"
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	cur = conn.cursor()
	if checkBook(isbn) == True:
		cur.execute("DELETE FROM changed_books WHERE isbn = ?", (isbn,))
	cur.execute("INSERT INTO changed_books (isbn, title, author, genre, released, binding, age, label, blurb) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (isbn, str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h),))
	conn.commit()
	conn.close()

def inDB(isbn):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("SELECT isbn FROM changed_books")
	c.execute(cmd)
	data = str(c.fetchall())
	conn.close()
	return str(isbn) in data


def getBook(isbn):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("SELECT * FROM changed_books WHERE isbn = (\"")
	cmd += str(isbn)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	data = str(c.fetchall())
	conn.close()
	# print(data)

	a = data[2:data.find(",")]
	data = data[data.find(",") + 3:]
	#print(data)
	b = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	c = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	d = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	e = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	f = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	g = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	h = data[:data.find(",") - 3]
	data = data[data.find(", \"") + 3:]
	#print("test")
	#print(data)
	i = data[:data.find("\",") - 2]
	data = data[data.find(",") + 3:]
	#print(data)
	j = data[:len(data) - 1]

	return a, b, c, d, e, f, g, h, i, j
=======
import sqlite3
import books_api as books


def dbInputIn(input1):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("INSERT INTO input VALUES (\"")
	cmd += str(input1)
	cmd += str(chr(34))
	cmd += str(chr(41))
	#print(cmd)
	c.execute(cmd)
	conn.commit()
	conn.close()


def dbInputOutAll():
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	c.execute("SELECT * FROM input")
	data = c.fetchall()
	conn.close()
	#return data
	final = []
	for count in range(len(data)):
		value = str(data[count])
		real = value[2:len(value)-3]
		print(real)
		final.append(real)
	return final


def dbInputOut():
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	c.execute("SELECT * FROM input")
	data = c.fetchall()
	conn.close()
	# return data
	value = str(data[len(data)-1])
	real = value[2:len(value) - 3]
	return real


def checkBook(isbn):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("SELECT * FROM changed_books WHERE isbn = (\"")
	cmd += str(isbn)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	data = c.fetchall()
	conn.close()
	print(data)
	if data == "[]":
		return False
	else:
		return True

def addBook(isbn, a, b, c, d, e, f, g, h, i):
	#compare to google books then update sql
	a1, b1, c1, d1, e1, f1, g1, h1, i1 = books.getAll(isbn)
	if a == a1:
		a = "None"
	if b == b1:
		b = "None"
	elif b == "":
		b = "None"
	if c == c1:
		c = "None"
	elif c == "":
		c = "None"
	if d == d1:
		d = "None"
	if e == e1:
		e = "None"
	if f == f1:
		f = "None"
	if g == g1:
		g = "None"
	if h == h1:
		h = "None"
	if i == i1:
		i = "None"
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	cur = conn.cursor()
	if checkBook(isbn) == True:
		cur.execute("DELETE FROM changed_books WHERE isbn = ?", (isbn,))
	cur.execute("INSERT INTO changed_books (isbn, title, author, genre, released, binding, age, label, blurb) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (isbn, str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h),))
	conn.commit()
	conn.close()

def inDB(isbn):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("SELECT isbn FROM changed_books")
	c.execute(cmd)
	data = str(c.fetchall())
	conn.close()
	return str(isbn) in data


def getBook(isbn):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("SELECT * FROM changed_books WHERE isbn = (\"")
	cmd += str(isbn)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	data = str(c.fetchall())
	conn.close()
	# print(data)

	a = data[2:data.find(",")]
	data = data[data.find(",") + 3:]
	#print(data)
	b = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	c = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	d = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	e = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	f = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	g = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]
	#print(data)
	h = data[:data.find(",") - 3]
	data = data[data.find(", \"") + 3:]
	#print("test")
	#print(data)
	i = data[:data.find("\",") - 2]
	data = data[data.find(",") + 3:]
	#print(data)
	j = data[:len(data) - 1]

	return a, b, c, d, e, f, g, h, i, j
>>>>>>> ade12e8163ce3463b78236abe5051e4cc8d5d57b
