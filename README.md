# Diet_ITS_Barcoding
Pipeline for processing ITS barcoding data from "Moorhouse-Gann et al. Impacts of Herbivory by Ecological Replacements on an Island Ecosystem"

Please note - this is NOT a finished program, but just a set of scripts used for processing one particular dataset. We have not tested how generalisable they are to other datasets so use at your own risk. 

## Pipeline:
(i) fill in the presence/absence matrix with the plant taxa assigned from the DNA barcode library, 
(ii) calculate the number of reads of each unique sequence in each sample 
(iii) extract read numbers found in PCR and DNA extraction negatives in addition to unpooled samples, and 
(iv) remove plant species detections from those samples where the read number did not exceed that found in negative or unpooled samples; and finally 
(v) collapse the matrix to combine all ITS2 haplotypes corresponding to a single taxon.

## Scipts

### Run_all.sh
Runs all the appropriate scripts and intermediate formatting steps. You should be able to run all steps by navigating to the containing directory and typing:
./Run_all.sh
Just enter the 

### 01_ReadNumberOTU.py

Takes an input file (“OUTfileTrimmedtoITS2.csv”) of four columns, the third being the OTU number and the fourth being sequence information for the samples which have sequences that fall into that OTU. Outputs the total read number for each sample within each OUT (“unique.out”)

### 02_CleanData.py

This script cleans the data to remove possible contamination/sequencing artefacts. It takes the output from 01_ReadNumberOTU.py and a second file (“OTU_ReadNo_Negatives.txt”) that contains a list of OTUs which appear in the negatives alongside the maximum read number of that OTU for any given negative. The script searches through file1 and locate all samples where the read number for each OTU is not equal to or greater than the “negative” value from file2. For all of those samples, it prints to a new file (“sc2.out”) the OTU number, the sample number and a new read number of 0.

### 03a_AdjustPool.py

This script reads a matrix of OTU number and then the taxa that it has been assigned to (“Pool1MatrixForPuzzle3.csv”). It uses the output from 02_CleanData.py to correct those samples from present (1) to absent (0) into “out_3-1.out”.

### 03b_CollapseMatrix.py
### 03c_CollapseMatrix2.py

Collapses instances when there are multiple haplotypes per species (in a formatted version of  “out_3-1.out”) into in a single record per species and formats table to present (1) and absent (0).
