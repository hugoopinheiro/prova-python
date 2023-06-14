def createNote(notebook_conn, title, note, usuarioId, sectionId):
    cursor = notebook_conn.cursor()
    sql = f'INSERT INTO notas(titulo, conteudoNotas, NotasUsuarioId, blocoDeNotas_secao_id) VALUES (?, ?, ?, ?)'
    cursor.execute(sql, [title, note, int(usuarioId), sectionId])
    notebook_conn.commit()
    return 'Inserido com sucesso.'

def isAllowed(notebook_conn, noteId):
    cursor = notebook_conn.cursor()
    sql = 'SELECT NotasUsuarioId FROM notas WHERE notasId = ?'
    cursor.execute(sql, [noteId])
    return cursor.fetchall()

def editNotes(notebook_conn, change, noteId, opc):
    cursor = notebook_conn
    match opc:
        case 1: 
            sql = 'UPDATE Notas SET titulo = ? WHERE notasId= ?'
            cursor.execute(sql, [change, noteId])
        case 2: 
            sql = 'UPDATE Notas SET conteudo = ? WHERE notasId = ?'
            cursor.execute(sql, [change, noteId])
    notebook_conn.commit()
    
def listOfNotes(notebook_conn, selectedSection, usuarioId):
    cursor = notebook_conn.cursor()
    sql = 'SELECT * FROM notas WHERE blocoDeNotas_secao_id = ? AND NotasUsuarioId = ?'
    cursor.execute(sql, [selectedSection, usuarioId])
    notebook_conn.commit()
    return cursor.fetchall()

def displayer(notes, usuarioId):
    for row in notes:
        if row[4] == usuarioId:
            print('==================')
            print('ID:', row[0])
            print('Titulo:', row[1])
            print('Conteudo:', row[2])
            print('bloco de notas:', row[3])
            print('usuario id:', row[4])
            print('==================')

def searchProduct(connection, noteId):
    cursor = connection.cursor()
    sql = 'SELECT * FROM Notas WHERE notasId = ?'
    cursor.execute(sql, [noteId])
    return cursor.fetchall()

def deletedNote(notebook_conn, noteId, usuarioId):
    sql = 'DELETE FROM blocoDeNotas WHERE notasId = ? AND NotasUsuarioId = usuarioId'
    cursor = notebook_conn.cursor()
    cursor.execute(sql, [noteId, usuarioId])
    notebook_conn.commit()
    return 'Excluido com sucesso.'