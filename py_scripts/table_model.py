from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MyTableModel(QAbstractTableModel):

    def __init__(self, datain, headerdata, parent=None, *args):
        #datain = uma lista de listas
        #headerdata = uma lista de strings
        super.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        from QtCore import *
        from QtGui import *
        if not index.isValid():
            return QVariant()
        elif role != QtGui.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        from QtCore import *
        from QtGui import *
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, col_number, order):
        from QtCore import *
        from QtGui import *

        #Ordenar tabela pelo numero de coluna fornecido
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata,
             key=operator.itemgetter(col_number))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))