def createNotebook(notebook_conn, titleNotebook, usuarioId):
    cursor = notebook_conn.cursor()
    sql = f'INSERT INTO blocoDeNotas(tituloBlocoDeNotas, blocoDeNotas_UsuarioId)  VALUES(?, ?)'
    cursor.execute(sql, [titleNotebook, usuarioId])
    notebook_conn.commit()
    return 'Criado com sucesso com sucesso.'

def listAllNotebook(notebook_conn, usuarioId):
    cursor = notebook_conn.cursor()
    sql = f'SELECT * FROM blocoDeNotas WHERE blocoDeNotas_UsuarioId = ?'
    cursor.execute(sql, [usuarioId])
    notebook_conn.commit()
    return cursor.fetchall()

def deleteNotebook(notebook_conn, sectionId):
    sql = 'DELETE FROM blocoDeNotas WHERE  blocoDeNotas_id  = ?'
    cursor = notebook_conn.cursor()
    cursor.execute(sql, [sectionId])
    notebook_conn.commit()
    return 'Excluido com sucesso.'

def displayNotebook(products, userId):
    for row in products:
        if row[2] == userId:
            print('==================')
            print('ID:', row[0])
            print('Titulo:', row[1])
            print('Id do usuario:', row[2])
            print('==================')