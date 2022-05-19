import os
from openpyxl import load_workbook

excel_path="C:/Users/USER/Desktop/excel/parsing.xlsx"

#excel parsing

load_excel=load_workbook(excel_path,data_only=True)
load_sheet=load_excel["Sheet1"]

filename_cell=load_sheet["B2":"B44"]
fileextension_cell=load_sheet["C2":"C44"]
location_cell=load_sheet["D2":"D44"]
filedate_cell=load_sheet["F2":"F44"]
copyrighter_cell=load_sheet["O2":"O44"]
resolution_cell=load_sheet["E2":"E44"]

filenamearr=[]
locationarr=[]
filename_placearr=[]

#파일명과 촬영장소 비교
for i in range(0,len(filename_cell)):   
    if filename_cell[i][0].value.split("_")[1] != location_cell[i][0].value:
        print("파일명과 촬영장소 오류", filename_cell[i][0] )

#copyrighter 비교
for i in copyrighter_cell:
    if i[0].value != "":
        print("copyrighter 오류", i[0])
   
#mp4 체크
for i in fileextension_cell:
    if i[0].value != "mp4":
        print("mp4 오류", i[0])



# mp4