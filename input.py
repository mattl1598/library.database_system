import entrysmall
import entrysmall_support
import book
import book_support
import tkinter
import sqlite3
import entry
import sql
import books_api as books
import book2


def isbn():
	root = tkinter.Tk()
	#entrysmall_support.set_Tk_var("Enter the ISBN:")
	top = entrysmall.Entry_Form(root, entry = str("isbn:"))
	entrysmall_support.init(root, top)
	root.mainloop()

def bookDeets(j, k, l, m, n, o, p, q, r, isbn):
	'''
	root = tkinter.Tk()
	top = book.New_Toplevel(root, j, k, l, m, n, o, p, q, r)
	book_support.init(root, top)
	root.resizable(False, False)
	root.mainloop()
	'''
	book2.Book(j, k, l, m, n, o, p, q, r, isbn)


def isbn2book():
	entry.App("isbn here:")
	isbn = sql.dbInputOut()
	#print(len(isbn))
	if len(isbn) == 13 or len(isbn) == 10:
		if sql.inDB(isbn) == True:
			j, k, l, m, n, o, p, q, r, s = sql.getBook(isbn)
		else:
			j, k, l, m, n, o, p, q, r = books.getAll(books.getBook(isbn))
		bookDeets(j, k, l, m, n, o, p, q, r, isbn)
	else:
		print("error")