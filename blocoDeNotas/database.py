import sqlite3

database_conn = sqlite3.connect('blocoDeNotas_database') 
c = database_conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_name VARCHAR(25) UNIQUE,
            usuario_password VARCHAR(25)
        );
    ''')
database_conn.commit()

c.execute('''
        CREATE TABLE IF NOT EXISTS blocoDeNotas(
            blocoDeNotas_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tituloBlocoDeNotas VARCHAR(30) NOT NULL,
            blocoDeNotas_UsuarioId int,
            FOREIGN KEY (blocoDeNotas_UsuarioId) REFERENCES usuario(usuarioId)
        );
        ''')
database_conn.commit()

c.execute('''
        CREATE TABLE IF NOT EXISTS Notas(
            notasId INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo VARCHAR(30) NOT NULL,
            conteudoNotas VARCHAR(170) NOT NULL,
            blocoDeNotas_secao_id int,
            NotasUsuarioId INT,
            FOREIGN KEY (blocoDeNotas_secao_id) REFERENCES blocoDeNotas(blocoDeNotas_id)
            FOREIGN KEY (NotasUsuarioId) REFERENCES usuario(usuarioId)
        );
        ''')
database_conn.commit()

# notas_conn = sqlite3.connect('notas_database') 
# c = notas_conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS notas(
#             notasId int PRIMARY KEY,
#             usuarioId int,
#             titulo varchar(30) NOT NULL,
#             conteudoNotas varchar(170) NOT NULL,
#             FOREIGN KEY (usuarioId) REFERENCES usuario(usuarioId)
#         );''')
# notas_conn.commit()