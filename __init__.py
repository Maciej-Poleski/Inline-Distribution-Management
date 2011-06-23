if __name__ == "__main__":
    from Core import *
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    app=QApplication([])
    view=QTableView()
    view.setModel(Model('C:\\Users\\evil\\Projekty\\Inline Distribution Management'))
    view.show();
    app.exec_()
