import csv


allonesfile = 'out_3-2-formatted.out'
allones = list(csv.reader(open(allonesfile)))


for i in range( 1, len( allones ) ):
    for j in range( 2, len( allones[0] ) ):
        if int( allones[i][j] ) > 1:
            allones[i][j] = 1
            
            
            
with open('out_3-3.out','w') as csv_file:
    for rowprint in range(0, len( allones ) ):
        for val in range(0, len( allones[0] ) ):
            csv_file.write( '%s,' %allones[rowprint][val] )
        csv_file.write( '\n' )
        
        
