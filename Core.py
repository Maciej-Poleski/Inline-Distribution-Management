from PyQt4.QtCore import *

class Model(QAbstractTableModel):
    def __init__(self, directory):
        QAbstractTableModel.__init__(self)
        self.header=None
        file=QFile(directory+'/template.xml')
        file.open(QIODevice.ReadOnly)
        xmlReader=QXmlStreamReader(file)
        while xmlReader.atEnd()==False:
            if xmlReader.readNext() == QXmlStreamReader.StartDocument:
                Model.__parse_template_document(self, xmlReader)
        if self.header==None:
            raise Exception('Podana ścieżka nie zawiera poprawnego szablonu!')
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        '''Prototyp funkcji zwracajcej nagłówek. Jedyna obsługiwana rola to Qt.DisplayRole'''
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]     # FIXME:Trzeba by sprawdzić, czy nie wychodzimy poza zakres
        return None
    
    def columnCount(self, parent=QModelIndex()):
        '''Prototyp funkcji zwracajcej liczbę kolumn. Parametr parent jest ignorowany'''
        return len(self.header)
    
    def rowCount(self, parent=QModelIndex()):
        '''Prototyp funkcji zwracajcej liczbę wierszy. Parametr parent jest ignorowany'''
        return 0    #FIXME: Prawdziwa implementacja musi użyć prawdziwej liczby wierszy!
    
    def parent(self, index):
        '''STUB. Nie wiem do czego ta metoda tak naprawdę służy.'''
        return QModelIndex()
    
    def data(self, index, role=Qt.DisplayRole):
        '''STUB. FIXME: Potrzebna jest implementacja.'''
        return None

    def __parse_template_document(self, xmlReader):
        while xmlReader.atEnd()==False:
            state=xmlReader.readNext()
            if state == QXmlStreamReader.StartElement and xmlReader.name() == 'header':
                Model.__parse_template_header(self, xmlReader)
            elif state == QXmlStreamReader.EndDocument:
                break

    def __parse_template_header(self, xmlReader):
        self.header=[]
        while xmlReader.atEnd()==False:
            state=xmlReader.readNext()
            if state == QXmlStreamReader.StartElement:
                self.header.append(xmlReader.name())
            elif state == QXmlStreamReader.EndElement and xmlReader.name() == 'header':
                break
