02#! -*- encoding: utf-8 -*-
#!/usr/bin/env python

# Form implementation generated from reading ui file 'frm_cadastro.ui'
#
# Created: Tue Aug 11 10:07:07 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import database, sys, glob, serial
from com_port_list import Com_port_list

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


class Cadastro_Morador(QtGui.QDialog):
    def __init__(self):
            super(Cadastro_Morador, self).__init__()
            self.dbm = database.DB_Manager('Morador')
            self.setupUi(self)
            self.lbl_porta.setText("Selecionar porta -->")

    def setupUi(self, Cadastro_Morador):
        Cadastro_Morador.setObjectName(_fromUtf8("Cadastro_Morador"))
        Cadastro_Morador.resize(393, 282)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,
             QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Cadastro_Morador.sizePolicy().
            hasHeightForWidth())
        Cadastro_Morador.setSizePolicy(sizePolicy)
        Cadastro_Morador.setMaximumSize(QtCore.QSize(393, 282))
        self.verticalLayout = QtGui.QVBoxLayout(Cadastro_Morador)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_nome = QtGui.QLabel(Cadastro_Morador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,
            QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_nome.sizePolicy().
            hasHeightForWidth())
        self.lbl_nome.setSizePolicy(sizePolicy)
        self.lbl_nome.setObjectName(_fromUtf8("lbl_nome"))
        self.horizontalLayout.addWidget(self.lbl_nome)
        self.edt_nome = QtGui.QLineEdit(Cadastro_Morador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
             QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_nome.sizePolicy().
            hasHeightForWidth())
        self.edt_nome.setSizePolicy(sizePolicy)
        self.edt_nome.setObjectName(_fromUtf8("edt_nome"))
        self.horizontalLayout.addWidget(self.edt_nome)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lbl_porta = QtGui.QLabel(Cadastro_Morador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
             QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_porta.sizePolicy().
            hasHeightForWidth())
        self.lbl_porta.setSizePolicy(sizePolicy)
        self.lbl_porta.setObjectName(_fromUtf8("lbl_porta"))
        self.horizontalLayout_4.addWidget(self.lbl_porta)
        self.btn_atualizar = QtGui.QPushButton(Cadastro_Morador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_atualizar.sizePolicy().
            hasHeightForWidth())
        self.btn_atualizar.setSizePolicy(sizePolicy)
        self.btn_atualizar.setObjectName(_fromUtf8("btn_atualizar"))
        self.horizontalLayout_4.addWidget(self.btn_atualizar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.edt_tag = QtGui.QLineEdit(Cadastro_Morador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_tag.sizePolicy().
            hasHeightForWidth())
        self.edt_tag.setSizePolicy(sizePolicy)
        self.edt_tag.setToolTip(_fromUtf8(""))
        self.edt_tag.setStatusTip(_fromUtf8(""))
        self.edt_tag.setWhatsThis(_fromUtf8(""))
        self.edt_tag.setInputMask(_fromUtf8(""))
        self.edt_tag.setText(_fromUtf8(""))
        self.edt_tag.setMaxLength(32767)
        self.edt_tag.setReadOnly(True)
        self.edt_tag.setPlaceholderText(_fromUtf8(""))
        self.edt_tag.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.edt_tag.setObjectName(_fromUtf8("edt_tag"))
        self.horizontalLayout_5.addWidget(self.edt_tag)
        self.btn_tag = QtGui.QPushButton(Cadastro_Morador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tag.sizePolicy().
            hasHeightForWidth())
        self.btn_tag.setSizePolicy(sizePolicy)
        self.btn_tag.setObjectName(_fromUtf8("btn_tag"))
        self.horizontalLayout_5.addWidget(self.btn_tag)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btn_cancelar = QtGui.QPushButton(Cadastro_Morador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancelar.sizePolicy().
            hasHeightForWidth())
        self.btn_cancelar.setSizePolicy(sizePolicy)
        self.btn_cancelar.setObjectName(_fromUtf8("btn_cancelar"))
        self.horizontalLayout_3.addWidget(self.btn_cancelar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_cadastrar = QtGui.QPushButton(Cadastro_Morador)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cadastrar.sizePolicy().
            hasHeightForWidth())
        self.btn_cadastrar.setSizePolicy(sizePolicy)
        self.btn_cadastrar.setObjectName(_fromUtf8("btn_cadastrar"))
        self.horizontalLayout_3.addWidget(self.btn_cadastrar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Cadastro_Morador)
        self.btn_atualizar.clicked.connect(self.get_port)
        QtCore.QObject.connect(self.btn_cadastrar,
            QtCore.SIGNAL(_fromUtf8("clicked()")), self.add_user)
        QtCore.QObject.connect(self.btn_cancelar,
            QtCore.SIGNAL(_fromUtf8("clicked()")), Cadastro_Morador.close)
        QtCore.QMetaObject.connectSlotsByName(Cadastro_Morador)

    def retranslateUi(self, Cadastro_Morador):
        Cadastro_Morador.setWindowTitle(_translate("Cadastro_Morador",
            "Cadastrar Usuario", None))
        self.lbl_nome.setText(_translate("Cadastro_Morador",
            "Nome do Morador:", None))
        self.btn_atualizar.setText(_translate("Cadastro_Morador",
            "Atualizar portas", None))
        self.btn_tag.setText(_translate("Cadastro_Morador",
            "Inserir tag RFID", None))
        self.btn_cancelar.setText(_translate("Cadastro_Morador",
            "Cancelar", None))
        self.btn_cadastrar.setText(_translate("Cadastro_Morador",
            "Cadastrar", None))

    def get_tag(self, port):
        self.used_tag = '00 00 00 00'
        #str(self.dbm.get_rfid(str(self.combo_porta.currentText())))
        self.edt_tag.setText(self.used_tag)

    def get_port(self):
        self.lbl_porta.setText(Com_port_list.return_port(self))

    def add_user(self):
        self.dbm.Add_Entry_Morador(self.used_tag, self.edt_nome.text())
        print "User added succesfully!"

    def closeEvent(self, event):
        if self.edt_nome.text() != '' or self.edt_tag.text() != '':
            reply = QtGui.QMessageBox.question(self, 'Confirmacao',
                'Certeza que deseja sair? Ainda ha texto na janela!',
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def __del__(self):
        Cadastro_Morador = None