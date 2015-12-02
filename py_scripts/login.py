# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Form implementation generated from reading ui file 'frm_login.ui'
#
# Created: Wed Aug 12 11:07:55 2015
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
    def _translate(context, text, disambig):  # lint:ok
        return QtGui.QApplication.translate(context, text, disambig)


class Login(QtGui.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.dbm = DB_Manager('Usuario')
        self.setupUi(self)

    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.setWindowModality(QtCore.Qt.ApplicationModal)
        Login.resize(274, 159)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QtCore.QSize(274, 159))
        Login.setMaximumSize(QtCore.QSize(274, 159))
        Login.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Login)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_usuario = QtGui.QLabel(Login)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_usuario.sizePolicy().
            hasHeightForWidth())
        self.lbl_usuario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.lbl_usuario.setFont(font)
        self.lbl_usuario.setObjectName(_fromUtf8("lbl_usuario"))
        self.horizontalLayout.addWidget(self.lbl_usuario)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum,
             QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.edt_login = QtGui.QLineEdit(Login)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
             QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_login.sizePolicy().
            hasHeightForWidth())
        self.edt_login.setSizePolicy(sizePolicy)
        self.edt_login.setObjectName(_fromUtf8("edt_login"))
        self.horizontalLayout.addWidget(self.edt_login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lbl_senha = QtGui.QLabel(Login)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,
             QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_senha.sizePolicy().
            hasHeightForWidth())
        self.lbl_senha.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.lbl_senha.setFont(font)
        self.lbl_senha.setObjectName(_fromUtf8("lbl_senha"))
        self.horizontalLayout_2.addWidget(self.lbl_senha)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum,
             QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.edt_senha = QtGui.QLineEdit(Login)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
             QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_senha.sizePolicy().
            hasHeightForWidth())
        self.edt_senha.setSizePolicy(sizePolicy)
        self.edt_senha.setInputMethodHints(QtCore.Qt.ImhHiddenText |
            QtCore.Qt.ImhNoAutoUppercase |
            QtCore.Qt.ImhNoPredictiveText |
            QtCore.Qt.ImhPreferLowercase | QtCore.Qt.ImhPreferNumbers)
        self.edt_senha.setEchoMode(QtGui.QLineEdit.Password)
        self.edt_senha.setObjectName(_fromUtf8("edt_senha"))
        self.horizontalLayout_2.addWidget(self.edt_senha)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(Login)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel |
            QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Login)
        QtCore.QObject.connect(self.buttonBox,
            QtCore.SIGNAL(_fromUtf8("accepted()")), Login.get_login)
        QtCore.QObject.connect(self.buttonBox,
            QtCore.SIGNAL(_fromUtf8("rejected()")), Login.reject)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login", None))
        self.lbl_usuario.setText(_translate("Login", "Usuario:", None))
        self.edt_login.setPlaceholderText(_translate("Login",
            "Nome de usuario", None))
        self.lbl_senha.setText(_translate("Login", "Senha:", None))
        self.edt_senha.setPlaceholderText(_translate("Login", "Senha", None))

    def get_login(self):
        self.login = self.edt_login.text()
        self.senha = self.edt_senha.text()
        command = ("SELECT idUsuario FROM Usuario WHERE"
            " login=%s AND senha=MD5(%s)")
        self.dbm.cursor.execute(command, (str(self.login), str(self.senha)),
             multi=False)
        self.dbm.cursor.fetchall()
        #for (idUsuario, login, nome) in self.dbm.cursor: TESTE (SUCESSO)
        #    print("%s, %s, %s!" % (idUsuario, login, nome))
        if self.dbm.cursor.rowcount != 1:
            QtGui.QMessageBox.warning(self, 'Erro',
                 'Usuário ou senha incorretos', QtGui.QMessageBox.Retry,
                  QtGui.QMessageBox.Retry)
        else:
            self.accept()