import sys
import CRenamer


''' Ausfuehrung der CRenamer-Klasse '''

ziel= sys.argv[1]
neuerName= sys.argv[2]
endung= sys.argv[3]

myRenamer= CRenamer.CRenamer(ziel, neuerName, endung) 
myRenamer.dateienUmbenennen()

