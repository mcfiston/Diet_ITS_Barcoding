import pandas
import re

print( "EXAMPLE FORMAT")
print( "HEADER LINE: H/S,Pro.Lang,otu.num,Seq.info" )
print("1ST LINE: S,0,1,A01_M00969_273_000000000-AY5TW_1_1101_17602_3601;size=234;|T|ITS2")
print("2ND LINE: H,0,1,A02_M00969_273_000000000-AY5TW_1_1101_9352_5615;size=305;|T|ITS2")

OUTfileTrimmedtoITS2 = input('Please enter name of OTU file, trimmed to ITS (example file is "OUTfileTrimmedtoITS2.csv"): ')

colnames = ['H_S', 'Pro_Lang', 'out_num', 'Seq_info']
data = pandas.read_csv( OUTfileTrimmedtoITS2 , names=colnames )
out_num = data.out_num.tolist()              #Reading column into list
Seq_info = data.Seq_info.tolist()              #Reading column into list
size = []              #For "Size=xxx" string
size_num = []              #For the xxx integer in the above string
ID = []              #ID part of the 4th column
uniques = 0
cumulative = 0

newlist_out_num = []
newlist_ID = []
newlist_sizenum = []
newlist_ref = []

size = [i.split( ';' )[1:2] for i in Seq_info]               #Parse 4th column by semi-colon

for k in range(0, len(size) ):              #Pull integer out of my size array
    current = str( size[k] )
    size_num.append( re.sub( "\D", "", current ) )              #regrex the digits from the string and append to new array

ID = [i.split( '_' )[0] for i in Seq_info]              #Parse by underscore and take first value (ID)

for k in range(2, len(size) ):              #loop through lines and check if ID and out_num are the same as the the previous
    if ID[k] != ID[k-1] or out_num[k] != out_num[k-1]:
        uniques = uniques + 1
        newlist_out_num.append( out_num[k-1] )
        newlist_ID.append( ID[k-1] )
        newlist_sizenum.append( int(size_num[k-1]) + int( cumulative ) )
        newlist_ref.append( uniques )
        cumulative = 0
    else:
        cumulative = cumulative + int( size_num[k-1] )              #if they're the same, make a cumulative total of the score
        

with open('unique.out','w') as csv_file:
    for j in range(0, len(newlist_ref) ):
        csv_file.write( '%s %s %s %s' % ( newlist_ref[j] , newlist_out_num[j] , newlist_ID[j] , newlist_sizenum[j] ) ) 
        csv_file.write( '\n' ) 


