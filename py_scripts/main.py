# -*- coding: utf-8 -*-
#!/usr/bin/env python

from frm_main import Main_Window
from login import Login
from PyQt4 import QtGui, QtCore

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    if Login().exec_() == QtGui.QDialog.Accepted:
        main_window = Main_Window()
        main_window.show()
        sys.exit(app.exec_())
    else:
        QtCore.QCoreApplication.instance().quit()