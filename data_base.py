import sqlite3


def reg(name, password):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    info = cursor.execute('''SELECT * from users WHERE username=?''', (name,)).fetchone()
    if info is not None:
        return 'Этот логин уже занят!'
    else:
        cursor.execute('''INSERT INTO users (username,password) VALUES(?,?)''', (name, password))
        conn.commit()
        conn.close()
        return name


def login(name, password):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    res = cursor.execute('''SELECT username from users WHERE username = ? and password = ?''',
                         (name, password)).fetchone()
    conn.close()
    if not res:
        return
    else:
        return name
