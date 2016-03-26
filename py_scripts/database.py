#! -*- coding: utf-8 -*-
#!/usr/bin/env python

import mysql.connector
from mysql.connector import errorcode
import serial
from datetime import datetime
import sys


class DB_Manager:

    #Construtor do objeto da classe DB_Manager
    def __init__(self, tableName):
        self.dbase = "condominio"
        self.username = "root"
        self.passwrd = "jkgs1234"
        self.table_name = tableName

        self.connection = mysql.connector.connect(user=self.username,
             password=self.passwrd, host='127.0.0.1')
        self.cursor = self.connection.cursor()

        self.connect_db()
        self.create_table_morador()
        self.create_table_usuario()
    
    #Função de conexão com o BD
    def connect_db(self):
        try:
            self.connection.database = self.dbase
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print ('Something is wrong with yout username and password.')
                return False
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print ('Database does not exist, attempting to create it...')
                self.create_database()
                return True
            else:
                print (err)
                return False

        else:
            print ('Connected')
            return True
    #Função de criação do DB
    def create_database(self):
        try:
            self.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".
                    format(self.dbase))
        except mysql.connector.Error as err:
            print ('Failed creating database: {}'.format(err))
            exit(1)
    
    #Função de criação da tabela morador
    def create_table_morador(self):
        table_morador = ("CREATE TABLE IF NOT EXISTS Morador ("
                "idMorador INTEGER UNSIGNED NOT NULL AUTO_INCREMENT, "
                #"Casa_numCasa INTEGER UNSIGNED NOT NULL,"
                "tagMorador VARCHAR(8) NOT NULL, "
                "nomeMorador VARCHAR(50) NOT NULL, "
                "emCasa BIT NULL, "
                "dataCadastro DATETIME NOT NULL, "
                "ultimaSaida DATETIME NULL, "
                "ultimaEntrada DATETIME NULL, "
                "PRIMARY KEY (idMorador)"
                # "FOREIGN KEY (Casa_numCasa)"
                # "    REFERENCES Casa(numCasa)"
                # "        ON UPDATE NO ACTION"
                # "        ON DELETE NO ACTION"
                ")ENGINE=InnoDB;")
        self.RunCommand(table_morador)
    
    #Função de criação da tabela usuário
    def create_table_usuario(self):
        table_usuario = ("CREATE TABLE IF NOT EXISTS Usuario ("
                 "idUsuario INT NOT NULL AUTO_INCREMENT, "
                 "login VARCHAR(20) NOT NULL, "
                 "nome VARCHAR(40) NOT NULL, "
                 "senha VARCHAR(32) NOT NULL, "
                 "CONSTRAINT Login_pk PRIMARY KEY (idUsuario)"
                 ")ENGINE=InnoDB;")
        self.RunCommand(table_usuario)
    #Função de verificação de conexão
    def connected(self):
        if (self.connection.is_connected()):
            print 'Connected'
        else:
            print 'Not connected'

    #Função (de autoria do MIT) de conexão com o módulo RFID
    def get_rfid(self, port):
        #lint:disable
        ################################################################################
        # MIT License - Share/modify/etc, but please keep this notice.
        #
        # Copyright (c) 2010 Matt Williamson, App Delegate Inc
        #
        # Permission is hereby granted, free of charge, to any person obtaining a copy
        # of this software and associated documentation files (the "Software"), to deal
        # in the Software without restriction, including without limitation the rights
        # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        # copies of the Software, and to permit persons to whom the Software is
        # furnished to do so, subject to the following conditions:
        #
        # The above copyright notice and this permission notice shall be included in
        # all copies or substantial portions of the Software.
        #
        # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
        # THE SOFTWARE.
        ################################################################################
        #lint:enable
        print 'Starting connection'
        try:
            com = serial.Serial(port, 9600)
            print 'Connected to Arduino module. Awaiting RFiD scans.'
            chars = []
            while True:
                char = com.read()

                #Read characters until hit line endings
                if char != '\r' and char != '\n' and len(chars) <= 10:
                    chars.append(char)

                    #If we have 10 characters, then we have an RFID tag
                    if len(chars) >= 10:
                        tag_id = ''.join(chars[:10])
                        print 'Tag: ', tag_id
                        return tag_id
                else:
                    #Reset buffer
                    chars = []
                    return 0
        except serial.SerialException:
            print '*ERROR'
            print 'Could not open serial port'
            sys.exit('Edit database.py and make sure you'
                ' define serial_port properly')
            return 0

    #Função de execução de scripts SQL no BD
    def RunCommand(self, cmd):
        print ("RUNNING COMMAND: " + cmd)
        try:
            self.cursor.execute(cmd)
        except mysql.connector.Error as err:
            print ("\nError Message: " + str(err.msg))
            print ("WITH " + cmd)
        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()
        return msg
    
    #Função de adição de registros na tabela morador
    def Add_Entry_Morador(self, name, tag):
        entry_time = datetime.now.strftime("%y-%m-%d %H:%M:%S")

        command = ("INSERT INTO " + self.table + " (nomeMorador,"
            " tagMorador, dataCadastro)")
        command += " VALUES ('%s', '%s', '%s');" % (name, tag, entry_time)

        self.RunCommand(command)
    
    #Função de adição de registros na tabela Usuário
    def Add_Entry_Usuario(self, login, nome, senha):
        command = "INSERT INTO Morador (login, nome, senha)"
        command += " VALUES ('%s', '%s', '%s');" % (login, nome, senha)
        self.RunCommand(command)
        
    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
