# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_main.ui'
#
# Created: Wed Aug 19 10:04:21 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from cadastro_morador import Cadastro_Morador
from cadastro_usuario import Cadastro_Usuario
from xbee_list import Xbee_List

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Main_Window(QtGui.QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.cadastro_usuario = None
        self.cadastro_morador = None
        self.xbee_list = None

    def setupUi(self, Main_Window):
        Main_Window.setObjectName(_fromUtf8("Main_Window"))
        Main_Window.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Main_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPrograma = QtGui.QMenu(self.menubar)
        self.menuPrograma.setObjectName(_fromUtf8("menuPrograma"))
        self.menuCadastrar_novo = QtGui.QMenu(self.menuPrograma)
        self.menuCadastrar_novo.setObjectName(_fromUtf8("menuCadastrar_novo"))
        Main_Window.setMenuBar(self.menubar)
        self.actionUsuario = QtGui.QAction(Main_Window)
        self.actionUsuario.setObjectName(_fromUtf8("actionUsuario"))
        self.actionMorador = QtGui.QAction(Main_Window)
        self.actionMorador.setObjectName(_fromUtf8("actionMorador"))
        self.actionFechar = QtGui.QAction(Main_Window)
        self.actionFechar.setObjectName(_fromUtf8("actionFechar"))
        self.actionListarXbees = QtGui.QAction(Main_Window)
        self.actionListarXbees.setObjectName(_fromUtf8("actionListarXbees"))
        self.menuCadastrar_novo.addAction(self.actionUsuario)
        self.menuCadastrar_novo.addAction(self.actionMorador)
        self.menuPrograma.addAction(self.menuCadastrar_novo.menuAction())
        self.menuPrograma.addSeparator()
        self.menuPrograma.addAction(self.actionListarXbees)
        self.menuPrograma.addSeparator()
        self.menuPrograma.addAction(self.actionFechar)
        self.menubar.addAction(self.menuPrograma.menuAction())

        self.retranslateUi(Main_Window)
        self.actionMorador.activated.connect(self.abrir_cadastro_morador)
        self.actionUsuario.activated.connect(self.abrir_cadastro_usuario)
        self.actionListarXbees.activated.connect(self.abrir_lista_xbees)
        QtCore.QObject.connect(self.actionFechar, QtCore.SIGNAL(
            _fromUtf8("activated()")), Main_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(_translate("Main_Window", "CONDINT", None))
        self.menuPrograma.setTitle(_translate("Main_Window", "Programa", None))
        self.menuCadastrar_novo.setTitle(_translate("Main_Window",
             "Cadastrar novo...", None))
        self.actionUsuario.setText(_translate("Main_Window", "Usuario", None))
        self.actionMorador.setText(_translate("Main_Window", "Morador", None))
        self.actionFechar.setText(_translate("Main_Window", "Fechar", None))
        self.actionListarXbees.setText(_translate("Main_Window",
             "Listar XBees", None))

    def abrir_cadastro_morador(self):
        if self.cadastro_morador is None:
            self.cadastro_morador = Cadastro_Morador()
            self.cadastro_morador.show()
        else:
            print "Erro ao abrir"

    def abrir_cadastro_usuario(self):
        if self.cadastro_usuario is None:
            self.cadastro_usuario = Cadastro_Usuario()
            self.cadastro_usuario.show()
        else:
            print "Erro ao abrir"

    def abrir_lista_xbees(self):
        if self.xbee_list is None:
            self.xbee_list = Xbee_List()
            self.xbee_list.show()
        else:
            print "Erro ao abrir"