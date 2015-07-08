# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frm_cadastro.ui'
#
# Created: Tue Jul  7 23:28:17 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import database, sys, glob, serial

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

class Ui_Form_Cadastro(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.dbm = database.DB_Manager('Morador')
        self.setupUi(self)
        self.init_combobox()

    def setupUi(self, Form_Cadastro):
        Form_Cadastro.setObjectName(_fromUtf8("Form_Cadastro"))
        Form_Cadastro.resize(393, 282)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_Cadastro.sizePolicy().hasHeightForWidth())
        Form_Cadastro.setSizePolicy(sizePolicy)
        Form_Cadastro.setMaximumSize(QtCore.QSize(393, 282))
        self.verticalLayout = QtGui.QVBoxLayout(Form_Cadastro)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_nome = QtGui.QLabel(Form_Cadastro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_nome.sizePolicy().hasHeightForWidth())
        self.lbl_nome.setSizePolicy(sizePolicy)
        self.lbl_nome.setObjectName(_fromUtf8("lbl_nome"))
        self.horizontalLayout.addWidget(self.lbl_nome)
        self.edt_nome = QtGui.QLineEdit(Form_Cadastro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_nome.sizePolicy().hasHeightForWidth())
        self.edt_nome.setSizePolicy(sizePolicy)
        self.edt_nome.setObjectName(_fromUtf8("edt_nome"))
        self.horizontalLayout.addWidget(self.edt_nome)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.combo_porta = QtGui.QComboBox(Form_Cadastro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_porta.sizePolicy().hasHeightForWidth())
        self.combo_porta.setSizePolicy(sizePolicy)
        self.combo_porta.setObjectName(_fromUtf8("combo_porta"))
        self.horizontalLayout_4.addWidget(self.combo_porta)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.edt_tag = QtGui.QLineEdit(Form_Cadastro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_tag.sizePolicy().hasHeightForWidth())
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
        self.btn_tag = QtGui.QPushButton(Form_Cadastro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tag.sizePolicy().hasHeightForWidth())
        self.btn_tag.setSizePolicy(sizePolicy)
        self.btn_tag.setObjectName(_fromUtf8("btn_tag"))
        self.horizontalLayout_5.addWidget(self.btn_tag)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btn_cancelar = QtGui.QPushButton(Form_Cadastro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancelar.sizePolicy().hasHeightForWidth())
        self.btn_cancelar.setSizePolicy(sizePolicy)
        self.btn_cancelar.setObjectName(_fromUtf8("btn_cancelar"))
        self.horizontalLayout_3.addWidget(self.btn_cancelar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_cadastrar = QtGui.QPushButton(Form_Cadastro)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cadastrar.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar.setSizePolicy(sizePolicy)
        self.btn_cadastrar.setObjectName(_fromUtf8("btn_cadastrar"))
        self.horizontalLayout_3.addWidget(self.btn_cadastrar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form_Cadastro)
        QtCore.QObject.connect(self.btn_tag, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_tag(self.combo_porta.currentText))
        QtCore.QObject.connect(self.btn_cadastrar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.add_user)
        QtCore.QObject.connect(self.btn_cancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form_Cadastro.close)
        QtCore.QMetaObject.connectSlotsByName(Form_Cadastro)

    def retranslateUi(self, Form_Cadastro):
        Form_Cadastro.setWindowTitle(_translate("Form_Cadastro", "Cadastrar Usuário", None))
        self.lbl_nome.setText(_translate("Form_Cadastro", "Nome do Morador:", None))
        self.btn_tag.setText(_translate("Form_Cadastro", "Inserir tag RFID", None))
        self.btn_cancelar.setText(_translate("Form_Cadastro", "Cancelar", None))
        self.btn_cadastrar.setText(_translate("Form_Cadastro", "Cadastrar", None))


    def get_tag(self, port):  
        self.used_tag = str(self.dbm.get_rfid(str(self.combo_porta.currentText())))
        self.edt_tag.setText(self.used_tag)

    def get_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM' + str(i + 1) for i in range(256)]

        elif sys.platform.startswith('linux'):
            temp_list = glob.glob('/dev/tty[A-Za-z]*')
            result = []

            for a_port in temp_list:
                try:
                    s = serial.Serial(a_port)
                    s.close()
                    result.append(a_port)
                except serial.SerialException:
                    pass
                return result

        elif sys.platform.startswith('darwin'):
            ports = glob.glob('dev/tty.*')

        else:
            raise EnvironmentError('Unsuported platform')

        result = []

        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
            return result

    def init_combobox(self):
        ports = self.get_ports()
        for port in ports:
            self.combo_porta.addItem(str(port))

    def add_user(self):
        self.dbm.Add_Entry(self.used_tag, self.edt_nome.text())
        print "User added succesfully!"

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form_Cadastro()
    ex.show()

    x = app.exec_()

    sys.exit(x)

def get_ports():
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux'):
        temp_list = glob.glob('/dev/tty[A-Za-z]*')
        result = []

        for a_port in temp_list:
            try:
                s = serial.Serial(a_port)
                s.close()
                result.append(a_port)
            except serial.SerialException:
                pass
            return result

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('dev/tty.*')

    else:
        raise EnvironmentError('Unsuported platform')

    result = []

    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
        return result