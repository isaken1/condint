# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_usuario.ui'
#
# Created: Wed Aug 19 09:29:47 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from database import DB_Manager

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


class Cadastro_Usuario(QtGui.QDialog):
    def __init__(self):
        super(Cadastro_Usuario, self).__init__()
        self.setupUi(self)
        self.dbm = DB_Manager('Usuario')
        self.dbm.connection.raise_on_warnings = True

    def setupUi(self, Cadastro_Usuario):
        Cadastro_Usuario.setObjectName(
            _fromUtf8("Cadastro_Usuario"))
        Cadastro_Usuario.setWindowModality(QtCore.Qt.ApplicationModal)
        Cadastro_Usuario.resize(350, 216)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
             QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Cadastro_Usuario.sizePolicy()
            .hasHeightForWidth())
        Cadastro_Usuario.setSizePolicy(sizePolicy)
        Cadastro_Usuario.setMinimumSize(QtCore.QSize(350, 216))
        Cadastro_Usuario.setMaximumSize(QtCore.QSize(350, 216))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cantarell"))
        font.setPointSize(12)
        Cadastro_Usuario.setFont(font)
        Cadastro_Usuario.setAutoFillBackground(True)
        self.verticalLayout = QtGui.QVBoxLayout(Cadastro_Usuario)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
             QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_login = QtGui.QLabel(Cadastro_Usuario)
        self.lbl_login.setObjectName(_fromUtf8("lbl_login"))
        self.horizontalLayout.addWidget(self.lbl_login)
        self.edt_login = QtGui.QLineEdit(Cadastro_Usuario)
        self.edt_login.setText(_fromUtf8(""))
        self.edt_login.setMaxLength(20)
        self.edt_login.setObjectName(_fromUtf8("edt_login"))
        self.horizontalLayout.addWidget(self.edt_login)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
             QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
             QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(Cadastro_Usuario)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.edt_senha = QtGui.QLineEdit(Cadastro_Usuario)
        self.edt_senha.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase |
            QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhPreferLowercase)
        self.edt_senha.setMaxLength(15)
        self.edt_senha.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.edt_senha.setObjectName(_fromUtf8("edt_senha"))
        self.horizontalLayout_2.addWidget(self.edt_senha)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
             QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.layout_cadastro = QtGui.QHBoxLayout()
        self.layout_cadastro.setObjectName(_fromUtf8("layout_cadastro"))
        self.lbl_nome = QtGui.QLabel(Cadastro_Usuario)
        self.lbl_nome.setObjectName(_fromUtf8("lbl_nome"))
        self.layout_cadastro.addWidget(self.lbl_nome)
        self.edt_nome = QtGui.QLineEdit(Cadastro_Usuario)
        self.edt_nome.setMaxLength(40)
        self.edt_nome.setObjectName(_fromUtf8("edt_nome"))
        self.layout_cadastro.addWidget(self.edt_nome)
        self.verticalLayout_2.addLayout(self.layout_cadastro)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btn_cancelar = QtGui.QPushButton(Cadastro_Usuario)
        self.btn_cancelar.setObjectName(_fromUtf8("btn_cancelar"))
        self.horizontalLayout_3.addWidget(self.btn_cancelar)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
             QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btn_cadastrar = QtGui.QPushButton(Cadastro_Usuario)
        self.btn_cadastrar.setObjectName(_fromUtf8("btn_cadastrar"))
        self.horizontalLayout_3.addWidget(self.btn_cadastrar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Cadastro_Usuario)
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)
        QtCore.QObject.connect(self.btn_cancelar, QtCore.SIGNAL(
            _fromUtf8("clicked()")), Cadastro_Usuario.reject)
        QtCore.QObject.connect(self.btn_cancelar, QtCore.SIGNAL(
            _fromUtf8("clicked()")), Cadastro_Usuario.close)
        QtCore.QMetaObject.connectSlotsByName(Cadastro_Usuario)

    def retranslateUi(self, Cadastro_Usuario):
        Cadastro_Usuario.setWindowTitle(_translate(
            "Cadastro_Usuario", "Cadastrar Usuario", None))
        self.lbl_login.setText(_translate(
            "Cadastro_Usuario", "Login:", None))
        self.edt_login.setPlaceholderText(_translate(
            "Cadastro_Usuario", "Login", None))
        self.label_3.setText(_translate(
            "Cadastro_Usuario", "Senha:", None))
        self.edt_senha.setPlaceholderText(_translate(
            "Cadastro_Usuario", "Senha", None))
        self.lbl_nome.setText(_translate(
            "Cadastro_Usuario", "Nome do Usuario:", None))
        self.edt_nome.setPlaceholderText(_translate(
            "Cadastro_Usuario", "Nome de usuario", None))
        self.btn_cancelar.setText(_translate(
            "Cadastro_Usuario", "Cancelar", None))
        self.btn_cadastrar.setText(_translate(
            "Cadastro_Usuario", "Cadastrar", None))

    def __del__(self):
        self = None

    def cadastrar_usuario(self):
        login = self.edt_login.text()
        senha = self.edt_senha.text()
        nome = self.edt_nome.text()
        command = ("INSERT INTO Usuario (login, senha, nome) VALUES"
            "(%s, MD5(%s), %s)")
        self.dbm.cursor.execute(command, (str(login), str(senha), str(nome)),
            multi=False)