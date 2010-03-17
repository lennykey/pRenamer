
import sys
from PyQt4 import QtGui, QtCore

from dialog import Ui_Dialog as Dlg
from CRenamer import CRenamer




class MeinDialog(QtGui.QDialog, Dlg, CRenamer):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        #Das ist auch moeglich 
        #Dlg.setupUi(self,self)
        
        #Slots einrichten
        self.connect(self.dAusfuehren, QtCore.SIGNAL("clicked()"), self.startRename )
        self.connect(self.dAbbrechen, QtCore.SIGNAL("clicked()"), self.onAbbrechen)
    
    def startRename(self):
        ''' Uebergebenen Pfad auslesen und Renamer starten '''
        
        CRenamer.__init__(self, str(self.dPfad.text()), str(self.dNeuerName.text()), str(self.dDateiEndung.text()))
        print str(self.dPfad.text())
        print str(self.dNeuerName.text())
        print str(self.dDateiEndung.text())
        
        #if str(self.dPfad.text()) == '' or (str(self.dNeuerName.text() == '') or str(self.dNeuerName.text() == 'Neuer Name')) or (str(self.dDateiEndung.text()) == '' or str(self.dDateiEndung.text()) == 'Dateiendung' ):
        if (str(self.dNeuerName.text()) == 'Neuer Name' or len(str(self.dNeuerName.text())) == 0) or (str(self.dPfad.text()) == '') or (str(self.dDateiEndung.text()) == 'Dateiendung' or len(str(self.dNeuerName.text())) == 0) :
            print 'Gleich null'
            pass
        else:
            #print 'Umbennant'
            self.dateienUmbenennen()
            
            #self.close()
        
        
    def onAbbrechen(self): 
        self.close()
        
        

app= QtGui.QApplication(sys.argv)
dialog= MeinDialog()
dialog.show()
#sys.exit(app.exec_())

sys.exit(app.exec_())
