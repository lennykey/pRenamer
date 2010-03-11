'''
Created on 19.02.2010
 
@author: sonne
 
usage: python pRenamer.py Verzeichnis neuerName dateiEndung
 
Wichtig: Die Dateien, die umbenannt werden sollen, muessen bereits in der richtigen Reihenfolge im Verzeichnis vorliegen
 
'''
 
import os
import commands
import sys
 
 
 
def main(zielPath, neuerName, dateiEndung):
    ''' Main Funktion, mit allen erforderlichen Anweisungen'''
    command= 'ls ' + zielPath
    string= commands.getoutput(command)
    
    #print list(string)
    #print string
    
    listeDateien= str.split(string)
    anzahlDateien= len(listeDateien)
    anzahlStellen= len(str(anzahlDateien))
    
    maximaleLaengeNeuerName= len(neuerName) + len(dateiEndung)+ anzahlStellen + 1 # +1 Wegen Punkt
    
    #print listeDateien
    
    #aktuellerPath= os.getcwd() + '/' + path + '/'
    
    
    counter= 1
    for eintrag in listeDateien:
        zeroTimes= maximaleLaengeNeuerName - len(neuerName + str(counter) + '.' + dateiEndung)
        
        #print 'ZeroTimes:' + str(zeroTimes)
        zero= '0' * zeroTimes
        #print 'Zero: ' + str(zero)
        #print 'Eintrag: ' + str(eintrag)
        
        newString= neuerName + zero + str(counter) + '.' + dateiEndung
        #print 'New String: '+ str(newString)
        os.rename(zielPath+eintrag, zielPath+newString)
        
        counter += 1
 
 
if len(sys.argv) < 4:
    print 'Sie haben nicht genug Argumente uebergeben'
    print 'Beispiel: ' + 'pRenamer' + ' ' + 'zielVerzeichnis neuerName Dateiendung'
    sys.exit()
else:
    try:
        neuerName= sys.argv[2]
        dateiEndung= sys.argv[3]
        zielPath= sys.argv[1]
 
        main(zielPath, neuerName, dateiEndung)
    except OSError, e:
        print 'Datei bzw. Verzeichnis existiert nicht'
        
 