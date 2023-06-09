def createNote(notebook_conn, title, note, usuarioId):
    cursor = notebook_conn.cursor()
    sql = f'INSERT INTO blocoDeNotas(titulo, conteudoNotas, NotasUsuarioId) VALUES (?, ?, ?)'
    cursor.execute(sql, [title, note, int(usuarioId)])
    notebook_conn.commit()
    return 'Inserido com sucesso.'

def isAllowed(notebook_conn, noteId):
    cursor = notebook_conn.cursor()
    sql = 'SELECT NotasUsuarioId FROM blocoDeNotas WHERE notasId = ?'
    cursor.execute(sql, [noteId])
    return cursor.fetchall()

def editNotes(notebook_conn, change, noteId, opc):
    cursor = notebook_conn
    match opc:
        case 1: 
            sql = 'UPDATE blocoDeNotas SET titulo = ? WHERE notasId= ?'
            cursor.execute(sql, [change, noteId])
        case 2: 
            sql = 'UPDATE blocoDeNotas SET conteudo = ? WHERE notasId = ?'
            cursor.execute(sql, [change, noteId])
    notebook_conn.commit()
    
def listOfNotes(notebook_conn):
    cursor = notebook_conn.cursor()
    sql = 'select * from blocoDeNotas'
    cursor.execute(sql)
    notebook_conn.commit()
    return cursor.fetchall()

def displayer(products, userId):
    for row in products:
        if row[3] == userId:
            print('==================')
            print('ID:', row[0])
            print('Titulo:', row[1])
            print('Conteudo:', row[2])
            print('==================')

def searchProduct(connection, noteId):
    cursor = connection.cursor()
    sql = 'SELECT * FROM blocoDeNotas WHERE notasId = ?'
    cursor.execute(sql, [noteId])
    return cursor.fetchall()

def deletedNote(notebook_conn, noteId):
    sql = 'DELETE FROM blocoDeNotas WHERE notasId = ?'
    cursor = notebook_conn.cursor()
    cursor.execute(sql, [noteId])
    notebook_conn.commit()
    return 'Excluido com sucesso.'