def validateName(usersConn, name):
    cursor = usersConn.cursor()
    sql = f'SELECT * FROM usuarios WHERE usuario_name = ?'
    cursor.execute(sql, [name])
    return cursor.fetchall()

def sign_user(usersConn, nome, senha):
    cursor= usersConn.cursor()
    sql = f'INSERT INTO usuarios(usuario_name, usuario_password) VALUES (?, ?)'
    cursor.execute(sql,[nome, senha])
    usersConn.commit()

def user_login(usersConn, nome, senha):
    cursor = usersConn.cursor()
    sql = f'SELECT * FROM usuarios WHERE usuario_name = ? and usuario_password = ?'
    cursor.execute(sql, [nome, senha])
    usersConn.commit()

def getUserId(usersConn, name):
    cursor = usersConn.cursor()
    sql = 'SELECT usuario_id FROM usuarios WHERE usuario_name LIKE ?'
    cursor.execute(sql, [name])
    return cursor.fetchall()[0][0]

def listOf_users(usersConn):
     cursor = usersConn.cursor()
     sql = 'select * from usuarios'
     cursor.execute(sql)
     usersConn.commit()
     return cursor.fetchall()