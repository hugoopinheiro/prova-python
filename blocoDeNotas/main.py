import sqlite3
import os

from functions.usuario_db import user_login, sign_user, validateName, getUserId
from menu.menu import menu

database_conn = sqlite3.connect('blocoDeNotas_database')

option = 0
def main():
    global option
    while(option != 3):
        option = int(input("Bem-vindo a seu bloco de notas.\nDigite 1 para fazer login\nDigite 2 para se cadastrar\ndigite 3 para sair do sistema\n "))
        os.system("cls")
        if option == 1:
            print('------LOGIN------')
            for attempts in range(0, 3):
                nome = str(input('Digite seu nome de usuario: '))
                senha = str(input('Digite sua senha: '))
                
                validateLogin = user_login(database_conn, nome, senha)
                if not validateLogin:
                    print('Senha ou usuario digitados errados!')
                else:
                    os.system("cls")
                    menu(getUserId(database_conn, nome))
        elif option == 2:
            print('------CADASTRO------')
            nome = str(input('Digite seu nome de usuario: '))
            for attempts in range(0, 3):
                if len(nome) <= 3:
                    print('Nome de usuario deve ter 4 letras ou mais!')
                    nome = str(input('Digite outro nome de usuario: '))
                if nome != ' ':
                    usernameValid = validateName(database_conn, nome)
                    if not usernameValid:
                        print('Nome de usuario valido!')
                        break
                    else:
                        print('Nome de usuario invalido')
                        nome = str(input('Digite outro nome de usuario: '))
            senha = str(input('Digite sua senha: '))
            if len(senha) <= 7:
                for attempts in range(3, 0, -1):
                    print (f'Sua senha deve ter mais de 8 caracteres.\nVocê tem mais {attempts} tentativas')
                    senha = str(input('Digite sua senha: '))
                    if len(senha) > 7:
                        print('Senha aceita')
                        break
                    if attempts == 0:
                        print('você excedeu suas tentativas! ):')
                        break
            sign_user(database_conn, nome, senha)
        elif option == 3:
            print('Até mais!')
            break
        else:
            print('Digite alguma opção valida!')
main()