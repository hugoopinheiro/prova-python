# aqui é onde o usuario depois de fazer login vai poder interagir com o bloco de notas
import sqlite3
import os

from functions.notes_db import createNote, listOfNotes, editNotes, deletedNote, isAllowed, displayer, searchProduct
from functions.notebook_db import createNotebook, listAllNotebook, displayNotebook, deleteNotebook
database_conn = sqlite3.connect('blocoDeNotas_database') 

option = 0

def menu(usuarioId):
    print(usuarioId)
    global option
    print('Olá, bem vindo ao seu bloco de notas!') 
    print('O bloco de notas é dividido em seções onde voce pode dividir suas anotações por temas')
    print('Aqui você podera criar ou alterar essas seções.') 
    while option != 4:
        option = int(input('1- Para adicionar uma seção\n2- Para listar seçôes\n3- Para excluir seção\n4- Ir administrar as notas  '))
        if option == 1:
            titleNotebook = str(input('Dê um titulo para sua seção: '))
            if titleNotebook != '':
                createNotebook(database_conn, titleNotebook, usuarioId)
            else:
                print('O titulo nao pode ficar em branco!')
        if option == 2:
            allNotebook = (listAllNotebook(database_conn, usuarioId))
            displayNotebook(allNotebook, usuarioId)
        if option == 3:
            seeSections = 'S'
            while seeSections not in 'SN':
                print('Você ira apagar a seção atraves do id da mesma.\nResponda a proxima pergunta com s ou n')
                seeSections = str(input('Deseja rever a lista de seções?(caso tenha esquecido o id): ')).upper()
                if seeSections == 'N':
                    deletSection_id = int(input('Digite aqui o id da seção que deseja excluir: ')) 
                    deleteNotebook(database_conn, deletSection_id )  
                elif seeSections == 'S':
                    allNotebook = (listAllNotebook(database_conn, usuarioId))
                    displayNotebook(allNotebook)
                    deletSection_id = int(input('Digite aqui o id da seção que deseja excluir: '))
                    deleteNotebook(database_conn, deletSection_id ) 
                else:
                    print('DiAgite uma opção valida!')
        if option == 4:
            selectedSection = int(input('Digite o id da seção que voce deseja alterar: '))
    while (option != 6):
        option = int(input('1- Para adicionar nota\n2- Para editar notas\n3- Para listar notas\n4- Para excluir nota\n5- Para mostrar um produto\n6- Sair do programa '))
        # os.system("cls")
        if option == 1:
            print('Adicione uma nota, voce pode escrever ate 170 caracteres!')
            title = str(input('Dê um titulo para sua nota(maximo de 30 caracter):  '))
            note = str(input('Digite aqui suas anotações:  '))
            createNote(database_conn, title, note, usuarioId, selectedSection)
        elif option == 2:
            notes = listOfNotes(database_conn, selectedSection, usuarioId)
            print(notes)
            id_note = int(input('Essas são suas notas, qual você deseja editar?[indique pelo id]'))
            allowed = (isAllowed(database_conn, id_note)[0][0] == usuarioId)
            if allowed:
                opc = 0
                while(opc != 3):
                    os.system("cls")
                    displayer(searchProduct(database_conn, id_note), usuarioId)
                    print('1 - Mudar o titulo da nota')
                    print('2 - Mudar o conteudo da nota')
                    print('3 - Voltar ao Menu\n')
                    opc = int(input('Digite a opção: '))
                    match opc:
                        case 1:
                            newTitle = input('Insira o novo titulo: ')
                            editNotes(database_conn, newTitle, id_note, opc)
                        case 2:
                            newContent = str(input('Insira o novo conteudo:  ')) 
                            editNotes(database_conn, newContent, id_note, opc)
                    os.system("cls")
            else:
                os.system("cls")
                print('Você não pode editar a nota de outro usuário')
            os.system("cls")
        elif option == 3:
            notes = listOfNotes(database_conn, selectedSection, usuarioId)
            # all_notes = listOfNotes(database_conn, selectedSection, usuarioId)
            # os.system("cls")
            notes = displayer(notes, usuarioId)
            # print(notes)
        elif option == 4:
            id_note = int(input('Através do id qual nota você quer deletar? '))
            deletedNote(database_conn, id_note, usuarioId)
        elif option == 5:
            seeAllNotes = str(input('Quer ver toda a lista de notas de novo(caso tenha esquecido o id: [S/N]')).upper
            if seeAllNotes == 'S':
                all_notes = listOfNotes(database_conn)
                displayer(all_notes, usuarioId)
            else:
                id_note = int(input('Informe o ID do produto: '))
                selectedNote = searchProduct(database_conn, id_note)
                os.system("cls")
                print(selectedNote)
        elif option == 6:
            os.system("cls")
            break
        