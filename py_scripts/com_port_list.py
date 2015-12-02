# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Com_port_list.ui'
#
# Created: Wed Sep  9 09:41:38 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from table_model import MyTableModel

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


class Com_port_list(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Com_port_list, self).__init__(parent)
        self.setupUi(self)
        self.port = ""
        self.create_table()

    def setupUi(self, Com_port_list):
        Com_port_list.setObjectName(_fromUtf8("Com_port_list"))
        Com_port_list.setWindowModality(QtCore.Qt.ApplicationModal)
        Com_port_list.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
             QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Com_port_list.sizePolicy().
             hasHeightForWidth())
        Com_port_list.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Com_port_list)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tbl_ports = QtGui.QTableView(Com_port_list)
        self.tbl_ports.setObjectName(_fromUtf8("tbl_ports"))
        self.verticalLayout.addWidget(self.tbl_ports)
        self.btn_atualizar = QtGui.QPushButton(Com_port_list)
        self.btn_atualizar.setObjectName(_fromUtf8("btn_atualizar"))
        self.verticalLayout.addWidget(self.btn_atualizar)
        self.btn_cancelar = QtGui.QPushButton(Com_port_list)
        self.btn_cancelar.setSizePolicy(sizePolicy)
        self.btn_cancelar.setObjectName(_fromUtf8("btn_cancelar"))
        self.verticalLayout.addWidget(self.btn_cancelar)

        self.retranslateUi(Com_port_list)
        self.btn_cancelar.clicked.connect(self.reject)
        self.btn_atualizar.clicked.connect(self.update_table_data)
        self.tbl_ports.doubleClicked.connect(self.doubleClicked_table)
        QtCore.QMetaObject.connectSlotsByName(Com_port_list)

    def retranslateUi(self, Com_port_list):
        Com_port_list.setWindowTitle(_translate("Com_port_list",
             "Lista de Portas COM", None))
        self.btn_atualizar.setText(_translate("Com_port_list",
             "Atualizar", None))
        self.btn_cancelar.setText(_translate("Com_port_list",
             "Fechar", None))

    def create_table(self):
        #Inicializar header
        self.header = ["Porta", "Dispositivo", "Informacoes"]

        #Inicializar modelo
        self.model = QtGui.QStandardItemModel()
        self.model.setColumnCount(3)
        self.model.setHorizontalHeaderLabels(self.header)
        self.tbl_ports.setModel(self.model)
        self.tbl_ports.setShowGrid(True)

        #Esconder header horizontal
        vertical_header = self.tbl_ports.verticalHeader()
        vertical_header.setVisible(False)

        #Inicializar dados
        self.update_table_data()

        ##Inicializar as propriedades do header horizontal
        #horizontal_header = self.tbl_xbee.horizontalHeader()
        #horizontal_header.setStretchLastSection(True)

        ##Largura da coluna ocupar o conteudo
        #self.tbl_xbee.resizeColumnsToContents()

        ##Setar altura das linhas
        #row_number = len(data)
        #for row in xrange(row_number):
            #self.tbl_xbee.setRowHeight(row, 18)

        ##Habilitar ordenamento
        #self.tbl_xbee.setSortingEnabled(True)

    def update_table_data(self):
        import serial.tools.list_ports

        self.tbl_ports.clearSpans()
        self.model.clear()

        tbl_data = list(serial.tools.list_ports.comports())
        column = 0
        for data in tbl_data:
            row = 0
            for d in data:
                item = QtGui.QStandardItem(d)
                item.setEditable(False)
                self.model.setItem(column, row, item)
                row = row + 1
            column = column + 1
        self.model.setHorizontalHeaderLabels(self.header)

    def doubleClicked_table(self):
        index = self.tbl_ports.selectedIndexes()[0]
        self.port = self.tbl_ports.model().data(index).toString()
        QtGui.QDialog.accept(self)

    def return_port(self):
        return self.port