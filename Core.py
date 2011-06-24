from PyQt4.QtCore import *
from PyQt4.QtXml import *

class Model(QAbstractTableModel):
    def __init__(self, directory):
        QAbstractTableModel.__init__(self)
        self.header=QDomDocument('template')
        self.data=[]
        file=QFile(directory+'/template.xml')
        if file.open(QIODevice.ReadOnly) == False:
            raise Exception('W podanym katalogu nie ma pliku szablonu')
        if self.header.setContent(file) == False:
            file.close()
            raise Exception('Parsowanie szablonu nie powiodło się - plik jest uszkodzony')
        file.close()
        # Tutaj rozpoczyna się czytanie pojedyńczych wpisów (każdy z osobnego pliku)
        
        for i in range(0x7fffffff): # TODO: Zrobić to ładniej (mamy do dyspozycji 2Gi - 1 plików)
            file=QFile(str(i)+'.xml')
            if file.open(QIODevice.ReadOnly) == False:
                break
            self.data.append(QDomDocument(str(i)));
            if self.data[i].setContent(file) == False:
                file.close()
                continue    # Plik istnieje, ale jest uszkodzony
            file.close()
            # Dany plik powinien być odczytany na tyle na ile jest to możliwe
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        '''Prototyp funkcji zwracajcej nagłówek. Jedyna obsługiwana rola to Qt.DisplayRole'''
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header.documentElement().childNodes().at(section).nodeName()
        return None
    
    def columnCount(self, parent=QModelIndex()):
        '''Prototyp funkcji zwracajcej liczbę kolumn. Parametr parent jest ignorowany'''
        return self.header.documentElement().childNodes().size()
    
    def rowCount(self, parent=QModelIndex()):
        '''Prototyp funkcji zwracajcej liczbę wierszy. Parametr parent jest ignorowany'''
        return len(self.data)
    
    def parent(self, index):
        '''STUB. Nie wiem do czego ta metoda tak naprawdę służy.'''
        return QModelIndex()
    
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if index.row() >= len(self.data):
                return None
            columnName = self.header.documentElement().childNodes().at(index.column()).nodeName()
            for i in range(self.data[index.row()].documentElement().childNodes().size()):
                if self.data[index.row()].documentElement().childNodes().at(i).nodeName() == columnName:
                    textToReturn=''
                    for j in range(self.data[index.row()].documentElement().childNodes().at(i).childNodes().size()):
                        if self.data[index.row()].documentElement().childNodes().at(i).childNodes().at(j).isText():
                            textToReturn += self.data[index.row()].documentElement().childNodes().at(i).childNodes().at(j).nodeValue()
                    return textToReturn
        return None
