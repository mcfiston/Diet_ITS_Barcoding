import pandas
import re
import csv

print( "EXAMPLE FORMAT")
print( "NO HEADER" )
print("1ST LINE: 1	120")
print("2ND LINE: 3	43")
print("2ND LINE: 7	11")
print("....")

OTU_ReadNo_Negatives = input( 'Please enter negatives (tab separated; example file is "OTU_ReadNo_Negatives.txt"): ' )

colnames = ['ref_ID', 'OTU', 'ID', 'depth']
colnamesNEG = ['OTU_neg', 'depth_neg']
data = pandas.read_table("unique.out", names=colnames, sep=r"\s+")
data_negs = pandas.read_table( OTU_ReadNo_Negatives , names=colnamesNEG, sep=r"\s+")

ref_ID = data.ref_ID.tolist()              #Reading column into list
OTU = data.OTU.tolist()              #Reading column into list
ID = data.ID.tolist()              #Reading column into list
depth = data.depth.tolist()              #Reading column into list

OTU_neg = data_negs.OTU_neg.tolist()              #Reading column into list
depth_neg = data_negs.depth_neg.tolist()              #Reading column into list

with open('sc2.out','w') as csv_file:
    for k in range(0, len(OTU_neg) ):
        for j in range(0, len(OTU) ):
            if int( OTU[j] ) == int( OTU_neg[k] ) and int( depth[j] ) <= int( depth_neg[k] ):
                csv_file.write( '%s,%s,0' % ( OTU[j], ID[j] ) )
                csv_file.write( '\n' ) 


