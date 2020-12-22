#!/bin/bash

body() {     IFS= read -r header;     printf '%s\n' "$header";     "$@"; }

python 01_ReadNumberOTU.py
python 02_CleanData.py
sed -i -e 's/ /,/g' sc2.out
rm sc2.out-e
python 03a_AdjustPool.py
sed 's/,$//g' out_3-1.out > out_3-1-f1.out
cat out_3-1-f1.out | body sort --field-separator=',' --key=2 > out_3-1-formatted.out
python 03b_CollapseMatrix.py 
sed 's/,$//g' out_3-2.out > out_3-2-f1.out
cat out_3-2-f1.out | body sort --field-separator=',' --key=2 > out_3-2-formatted.out
python 03c_CollapseMatrix2.py
sed 's/,$//g' out_3-3.out > out_3-3-f1.out
cat out_3-3-f1.out | body sort -n --field-separator=',' --key=1 > 00_Final_Matrix.out
rm out_3-3-f1.out out_3-2-f1.out out_3-1-f1.out out_3-3.out out_3-2.out out_3-1.out