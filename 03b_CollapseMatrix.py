import csv

Pool1MatrixForPuzzle3_noHead = input( 'Please re-enter poolfilename (original file was "Pool1MatrixForPuzzle3_noHead.csv"): ' )
pool = list(csv.reader(open( Pool1MatrixForPuzzle3_noHead )))

poolfile2 = 'out_3-1-formatted.out'
pool2 = list(csv.reader(open(poolfile2)))

new_pool2 = [[[] for i in range( len( pool[0] ) )] for i in range( len( pool ) )]

row_index = 0

for firstline in range(0, len( pool[0] ) ):
    new_pool2[0][firstline] = pool2[0][firstline]

for row in range(1, len( pool ) ):
    if pool2[row][1] == pool2[row-1][1]:
        new_pool2[row_index][0] = pool2[row][0]
        new_pool2[row_index][1] = pool2[row][1]
        for col in range(2, len( pool[0] ) ):
            new_pool2[row_index][col] = ( int( new_pool2[row_index][col] ) + int( pool2[row][col] ) )
    else:
        row_index = row_index + 1
        for col in range(0, len( pool[0] ) ):
            new_pool2[row_index][col] = pool2[row][col]

count = 0

for row in range(0, len( new_pool2 ) ):
    if new_pool2[row][0] == []:
        break
    else:
        count = count + 1


with open('out_3-2.out','w') as csv_file:
    for rowprint in range(0, count ):
        for val in range(0, len( pool[0] ) ):
            csv_file.write( '%s,' %new_pool2[rowprint][val] )
        csv_file.write( '\n' )

