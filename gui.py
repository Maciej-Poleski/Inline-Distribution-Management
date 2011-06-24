if __name__ == '__main__':
    from PyQt4.QtGui import *
    import Core
    app=QApplication([])
    model=Core.Model('C:\\Users\\evil\\Projekty\\Inline Distribution Management')
    view=QTableView()
    view.setModel(model)
    view.show()
    quit(app.exec_())
    
