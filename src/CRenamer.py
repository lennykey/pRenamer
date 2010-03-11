import os
import commands
 
 
class CRenamer(object):
    ''' Der Renamer als objektorientierte Version: CRenamer '''
    
    def __init__(self, zielPath, neuerName, dateiEndung):
        self.__zielPath= zielPath
        self.__neuerName= neuerName
        self.__dateiEndung= dateiEndung
 
        
    def dateienUmbenennen(self):
        ''' Benennt die Dateien um '''
        command= 'ls ' + self.__zielPath
        string= commands.getoutput(command)
        
        listeDateien= str.split(string)
        anzahlDateien= len(listeDateien)
        anzahlStellen= len(str(anzahlDateien))
        
        maximaleLaengeNeuerName= len(self.__neuerName) + len(self.__dateiEndung)+ anzahlStellen + 1 # +1 Wegen Punkt
        
        counter= 1
        for eintrag in listeDateien:
            zeroTimes= maximaleLaengeNeuerName - len(self.__neuerName + str(counter) + '.' + self.__dateiEndung)
            
            zero= '0' * zeroTimes
            
            newString= self.__neuerName + zero + str(counter) + '.' + self.__dateiEndung
            os.rename(self.__zielPath+eintrag, self.__zielPath+newString)
            
            counter += 1
        
        
        
    def __del__(self):
        print 'Klasse geloescht'