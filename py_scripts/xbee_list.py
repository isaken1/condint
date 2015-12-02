# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xbee_list.ui'
#
# Created: Wed Aug 26 10:58:15 2015
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
        QtCore.QObject.connect(self.btn_fechar, QtCore.SIGNAL(
             _fromUtf8("clicked()")), Xbee_List.close)
        QtCore.QMetaObject.connectSlotsByName(Xbee_List)

        self.create_table()

    def retranslateUi(self, Xbee_List):
        Xbee_List.setWindowTitle(_translate("Xbee_List", "Dialog", None))
        self.btn_fechar.setText(_translate("Xbee_List", "Fechar", None))
        self.btn_atualizar.setText(_translate("Xbee_List", "Atualizar", None))

    def get_table_data(self):
        pass

    def create_table(self):
        #Inicializar dados e header
        #Colocar dados dos xbees no header
        header = []
        data = self.get_table_data()

        #Inicializar modelo
        tbl_model = MyTableModel(data, header, self)
        self.tbl_xbee.setModel(tbl_model)
        self.tbl_xbee.setShowGrid(True)

        #Esconder header vertical
        vertical_header = self.tbl_xbee.verticalHeader()
        vertical_header.setVisible(False)

        #Inicializar as propriedades do header horizontal
        horizontal_header = self.tbl_xbee.horizontalHeader()
        horizontal_header.setStretchLastSection(True)

        #Largura da coluna ocupar o conteudo
        self.tbl_xbee.resizeColumnsToContents()

        #Setar altura das linhas
        row_number = len(data)
        for row in xrange(row_number):
            self.tbl_xbee.setRowHeight(row, 18)

        #Habilitar ordenamento
        self.tbl_xbee.setSortingEnabled(True)