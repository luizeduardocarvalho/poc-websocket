import sqlite3
from datetime import datetime
from json import dumps

class DataInitializer:
    @staticmethod
    def initialize():
        conn = sqlite3.connect('memory.db')
        c = conn.cursor()

        print('- [INFO] - initializing tables')
        
        c.execute('DROP TABLE IF EXISTS COMMAND')
        c.execute('CREATE TABLE IF NOT EXISTS COMMAND(NAME VARCHAR2(250), DATE TIMESTAMP)')
        c.execute('INSERT INTO COMMAND VALUES("nome", CURRENT_TIMESTAMP)')
        conn.commit()

        for row in c.execute('SELECT * FROM COMMAND'):
            print(row)

        c.close()
        conn.close()

class DataController:
    @staticmethod
    def insertCommand(command):
        conn = sqlite3.connect('memory.db')
        c = conn.cursor()

        sql = 'INSERT INTO COMMAND(NAME, DATE) VALUES(?,?)'
        c.execute(sql, (command.name, command.date))
        conn.commit()

        c.close()
        conn.close()
    
    @staticmethod
    def getCommands():
        conn = sqlite3.connect('memory.db')
        c = conn.cursor()

        commandLine = []

        for row in c.execute('SELECT * FROM COMMAND'):
            commandLine.append(row)

        c.close()
        conn.close()

        return commandLine

    @staticmethod
    def deleteCommands():
        conn = sqlite3.connect('memory.db')
        c = conn.cursor()

        c.execute('DELETE FROM COMMAND')
        conn.commit()

        c.close()
        conn.close()


    @staticmethod
    def printCommand():
        conn = sqlite3.connect('memory.db')
        c = conn.cursor()

        print('\n')
        print('--Fila de comandos:')
        for row in c.execute('SELECT * FROM COMMAND'):
            print('----comando:' + row[0] + 'data de criacao:' + row[1])
        print('\n')

        c.close()
        conn.close()
   