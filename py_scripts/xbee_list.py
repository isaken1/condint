#! -*- coding: utf-8 -*-
#!/usr/bin/env python

# Form implementation generated from reading ui file 'xbee_list.ui'
#
# Created: Wed Aug 26 10:58:15 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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


class Xbee_List(QtGui.QDialog):
    def __init__(self):
        super(Xbee_List, self).__init__()
        self.setupUi(self)

    def setupUi(self, Xbee_List):
        Xbee_List.setObjectName(_fromUtf8("Xbee_List"))
        Xbee_List.resize(393, 581)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
             QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Xbee_List.sizePolicy().hasHeightForWidth())
        Xbee_List.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Xbee_List)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tbl_xbee = QtGui.QTableView(Xbee_List)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
             QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_xbee.sizePolicy().
             hasHeightForWidth())
        self.tbl_xbee.setSizePolicy(sizePolicy)
        self.tbl_xbee.setAutoFillBackground(False)
        self.tbl_xbee.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tbl_xbee.setFrameShadow(QtGui.QFrame.Raised)
        self.tbl_xbee.setLineWidth(2)
        self.tbl_xbee.setMidLineWidth(0)
        self.tbl_xbee.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_xbee.setAlternatingRowColors(True)
        self.tbl_xbee.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tbl_xbee.setObjectName(_fromUtf8("tbl_xbee"))
        self.verticalLayout.addWidget(self.tbl_xbee)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_fechar = QtGui.QPushButton(Xbee_List)
        self.btn_fechar.setObjectName(_fromUtf8("btn_fechar"))
        self.horizontalLayout.addWidget(self.btn_fechar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.
             MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_atualizar = QtGui.QPushButton(Xbee_List)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
             QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_atualizar.sizePolicy().
             hasHeightForWidth())
        self.btn_atualizar.setSizePolicy(sizePolicy)
        self.btn_atualizar.setDefault(True)
        self.btn_atualizar.setObjectName(_fromUtf8("btn_atualizar"))
        self.horizontalLayout.addWidget(self.btn_atualizar)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Xbee_List)
        self.btn_atualizar.clicked.connect(self.update_table_data)
        QtCore.QObject.connect(self.btn_fechar, QtCore.SIGNAL(
             _fromUtf8("clicked()")), Xbee_List.close)
        QtCore.QMetaObject.connectSlotsByName(Xbee_List)

        self.create_table()

    def retranslateUi(self, Xbee_List):
        Xbee_List.setWindowTitle(_translate("Xbee_List", "Listar XBees", None))
        self.btn_fechar.setText(_translate("Xbee_List", "Fechar", None))
        self.btn_atualizar.setText(_translate("Xbee_List", "Atualizar", None))

    def create_table(self):
        self.header = ["Source Addr", "Source Addr Long", "Node",
             "Parent Addr", "Device", "Status", "Profile", "Manufacturer"]

        #Inicializar modelo
        self.model = QtGui.QStandardItemModel()
        self.model.setColumnCount(8)
        self.model.setHorizontalHeaderLabels(self.header)
        self.tbl_xbee.setModel(self.model)
        self.tbl_xbee.setShowGrid(True)

        #Modelo de selecao
        self.tbl_xbee.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tbl_xbee.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)

        #Esconder header horizontal
        vertical_header = self.tbl_xbee.verticalHeader()
        vertical_header.setVisible(False)

        #Inicializar dados
        self.update_table_data()


    def toHex(self, data):
        lst = []
        for char in lst:
            hv = hex(ord(ch).replace('0x', ''))
            if len(hv) == 1:
                hv = '0' + hv
            hv = '0x' + hv
            lst.append(hv)

    def update_table_data(self):
        from serial import Serial
        from xbee import ZigBee

        dialog = Com_port_list()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            port = str(dialog.return_port())

        serial_port = Serial(port, 9600)

        xbee = ZigBee(serial_port)

        xbee.at(command="ND")

        tbl_data = xbee.wait_read_frame()
        print tbl_data

        self.tbl_xbee.clearSpans()
        self.model.clear()

        column = 0
        for data in tbl_data['parameter']:
            row = 0
            #for decodeData(toHex(d)) in data:
                #item = QtGui.QStandardItem(d)
                #item.setEditable(False)
                #self.model.setItem(column, row, item)
                #row = row + 1
            column = column + 1
        self.model.setHorizontalHeaderLabels(self.header)

    def decodeData(self, data):
        source_addr_long = toHex(data['source_addr_long'])
        source_addr = toHex(data['source_addr'])
        id = data['id']
        status = toHex(data['status'])
        samples = data['samples']
        options = toHex(data['options'])
        return [id, status]