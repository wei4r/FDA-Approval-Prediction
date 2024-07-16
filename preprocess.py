# READ WHOLE FILE
import csv
from rdkit import Chem

f = open('drugbank_output_20220104.txt', 'r')
lines = f.readlines()
col_select = ['DrugBank ID', 'approved' , 'SMILES']
select = []
output = []
output.append(col_select)
for i, value in enumerate(lines):
    input = value.split("\t")
    output_line = []
    if i ==0:
        for j, string in enumerate(input):
            if string in col_select:
                select.append(j)
                #print("check Drugbank ID")
    else:
        for j, string in enumerate(input):
            if j in select:
                output_line.append(string)
        if len(output_line)>2:
            if output_line[2]!='':
                m = Chem.MolFromSmiles(output_line[2])
                if m is None:
                    print("Invalid: ",output_line[2])
                else:
                    output.append(output_line)

#print("output: ", output)
with open('input_smiles.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile,delimiter=',')
    writer.writerows(output)