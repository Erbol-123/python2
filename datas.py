import sqlite3


db = sqlite3.connect(database='users.db')
cursor = db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               id INTEGER,
               name TEXT,
               username TEXT)
''')


async def add_to_db(id,name,username):
    cursor.execute('''
INSERT INTO users(id,name,username)
                VALUES(?,?,?)
''',(id,name,username))
    db.commit()
async def show_user():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()
    

    


