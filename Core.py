from PyQt4.QtCore import *

class Model(QAbstractTableModel):
    def __init__(self, directory):
        self.header=None
        file=QFile(directory+'/template.xml')
        file.open(QIODevice.ReadOnly)
        xmlReader=QXmlStreamReader(file)
        while xmlReader.atEnd()==False:
            if xmlReader.readNext() == QXmlStreamReader.StartDocument:
                Model.__parse_template_document(self, xmlReader)
        if self.header==None:
            raise Exception('Podana ścieżka nie zawiera poprawnego szablonu!')
    
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
            
