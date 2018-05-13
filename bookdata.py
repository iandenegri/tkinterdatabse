import sqlite3

class Database:

#db allows the user to pass what database (.db file) they want to use when they edit the gui file.
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')
        self.conn.commit()

    def insert_data(self,title,author,year,isbn):
        self.cur.execute('INSERT INTO book VALUES (NULL,?,?,?,?)',(title,author,year,isbn))
        self.conn.commit()

    def view_data(self):
        self.cur.execute('SELECT * FROM book')
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?',(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete_data(self,id):
        self.cur.execute('DELETE FROM book WHERE id=?',(id,))
        self.conn.commit()

    def update_data(self,id,title='',author='',year='',isbn=''):
        self.cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?',(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
