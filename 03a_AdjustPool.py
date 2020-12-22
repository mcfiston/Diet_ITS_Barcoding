import pandas
import re
import csv
import numpy

print( "EXAMPLE FORMAT")
print( "OUT.no,taxon.name,A01,A02,A03,A04,A05,A06,A07....")
print( "1,Leucaena_leucocephala,1,2,1,2,1,1,1....")
print( "2,Ipomoea_macrantha,1,1,1,0,1,1,1,1,1....")


Pool1MatrixForPuzzle3_noHead = input( 'Please enter poolfile (original file was "Pool1MatrixForPuzzle3_noHead.csv"): ' )


sc2out = 'sc2.out'
sc2 = list(csv.reader(open(sc2out)))


pool = list(csv.reader(open( Pool1MatrixForPuzzle3_noHead )))


for taxon in range( 0, len( pool[0] ) ):
    for k in range( 0, len( sc2 ) ):
        if pool[0][taxon] == sc2[k][1]: 
            for j in range(1, len( pool ) ):
                if int( pool[j][0] ) == int( sc2[k][0] ):
                    pool[j][taxon] = sc2[k][2]


with open('out_3-1.out','w') as csv_file:
    for rowprint in range(0, len( pool ) ):
        for val in range(0, len( pool[0] ) ):
            csv_file.write( '%s,' %pool[rowprint][val] )
        csv_file.write( '\n' )




