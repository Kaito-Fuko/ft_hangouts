import sqlite3

# le coeur
DB_NAME = "hangouts.db"

def connect():
	return sqlite3.connect(DB_NAME)

# cration des table
def create_table():
	conn = connect()
	cursor = conn.cursor()

	cursor.execute("""
	CREATE TABLE IF NOT EXISTS contact(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT,
        address TEXT,
        note TEXT
	)""")

	cursor.execute("""
	CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_id INTEGER,
        sender TEXT,
        content TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

	conn.commit()
	conn.close()

# contact CRUD Create Read Update Delete   (? = sécurité SQL (important))
def add_contact(name, phone, email, address, note):
	conn = connect()
	cursor = conn.cursor()

	cursor.execute("""
	INSERT INTO contact(name, phone, email, addres, note)
	VALUE (?,?,?,?,?)
	""", (name, phone, email, address, note))

	conn.commit()
	conn.close()

# read
def get_contact():
	conn = connect()
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM contact")
	data = cursor.fetchall()

	conn.close()
	return data