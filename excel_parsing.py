import os
from openpyxl import load_workbook
from fractions import Fraction

excel_path="D:/blurring-linkflow/6m1w-/7-2_링크플로우_RawData_촬영일정_6월 1주차_220602.xlsx"

load_excel=load_workbook(excel_path,data_only=True)
load_sheet=load_excel["7-2 촬영시트(수집)"]

object_total=["('01','화분')","('02','시계')","('03','스마트폰')","('04','공기청정기')","('05','메뉴판')","('06','책표지')","('07','사과')","('08','칠판')","('09','달력')","('10','커피/케이크')",
"('11','리코더')","('12','자전거')","('13','실외기')","('14','휴대용게임기')","('15','음료수')","('16','전자레인지')","('17','안내표지판')","('18','자동차')","('19','그네')","('20','우산')",
"('21','카메라')","('22','야구배트')","('23','미끄럼틀')","('24','데스크탑')","('25','스노우보드')","('26','가방')","('27','라켓')","('28','헬멧')","('29','유모차')","('30','간판')",
"('31','안경')","('32','모자')","('33','테이블')","('34','프라이팬')","('35','피자')","('36','스탠드조명')","('37','가로등')","('38','오토바이')","('39','TV')","('40','거울')",
"('41','공')","('42','사람')","('43','고양이')","('44','개')","('45','RC카')","('46','야구글러브')","('47','풍선')","('48','휴지통')","('49','주전자')","('50','소화기')",
"('51','벤치')","('52','시소')","('53','근력운동기구(덤벨/바벨)')","('54','노트북')","('55','구두')","('56','보온병')","('57','피망')","('58','세탁기')","('59','체스판')","('60','프린터기')",
"('61','소파')","('62','냄비')","('63','칼')","('64','냉장고')","('65','피아노')","('66','자판기')","('67','수박')","('68','다리미')","('69','와인병')","('70','선풍기')",
"('71','국자')","('72','기타')","('73','신문')","('74','리모컨')","('75','포도')","('76','에어컨')","('77','토스터기')","('78','의자')","('79','모니터')","('80','침대')"]

filename_cell=load_sheet["B4":"B21"]
copyrighter_cell=load_sheet["C4":"C21"]
location_cell=load_sheet["D4":"D21"]
object_cell=load_sheet["F4":"F21"]
filedate_cell=load_sheet["G4":"G21"]
resolution_cell=load_sheet["I4":"I21"]
fileextension_cell=load_sheet["N4":"N21"]
fps_cell=load_sheet["J4":"J21"]
fstop_cell=load_sheet["K4":"K21"]
exposuretime_cell=load_sheet["L4":"L21"]
angle_cell=load_sheet["M4":"M21"]


objectnumberlist=[]

#파일명과 실내,실외 비교
for i in range(0,len(filename_cell)):   
    if filename_cell[i][0].value.split("_")[2][0] !=location_cell[i][0].value:
        print("파일명과 실내,실외 오류", filename_cell[i][0],location_cell[i][0] )

#copyrighter 비교
for i in copyrighter_cell:
    if i[0].value != "㈜미디어그룹사람과숲":
        print("copyrighter 오류", i[0])

#1920, 1080
for i in resolution_cell:
    if i[0].value != "1920, 1080":
        print("resolution 오류", i[0])

#FPS 체크
for i in fps_cell:
    if i[0].value != 30:
        print("fps 오류",i[0])

#mp4 체크
for i in fileextension_cell:
    if i[0].value != "mp4":
        print("mp4 오류", i[0])

#파일명과 촬영날짜 체크
for i in range(0,len(filename_cell)):  
    filename_date=filename_cell[i][0].value.split("_")[1]
    filename_m="20"+filename_date[:2]+"-"+filename_date[2:4]+"-"+filename_date[4:]
    date=str(filedate_cell[i][0].value)[:10]
    if filename_m != date:
        print("date 오류",filename_cell[i][0],filedate_cell[i][0])


#fstop 체크
for i in fstop_cell:
    fstop=i[0].value #F/12
    if fstop[0]=="F" and fstop[1]=="/" and "1.8"<=fstop[2:5]<="12":
        pass
    else:
        print("fstop오류",i[0])

#exposuretime 체크
for i in exposuretime_cell:
    ex_date=i[0].value #1/1000

    if ex_date[0]=="1" and ex_date[1]=="/" and 40<=int(ex_date[2:])<=1043:
        pass
    else:
        print("exposuretime오류",i[0])

#filename과 angle 체크
for i in range(0,len(filename_cell)):
    file_angle=filename_cell[i][0].value.split("_")[3][0]
    angle=angle_cell[i][0].value[0]
    if file_angle != angle:
        print("angle 오류",filename_cell[i][0],angle_cell[i][0])
    

#rawdataID와 객체ID 체크
for i in range(0,len(filename_cell)):
    key=filename_cell[i][0].value.split("_")[2][2:4] #파일명 객체ID
    value=object_cell[i][0].value
    kv="("+"'"+ key +"'"+","+"'"+value+"'"+")"
    #print(kv) #('15','음료수')
    objectnumberlist.append(kv)

for i in objectnumberlist:
    if i in object_total:
        pass
    else:
        print("raw_data_ID와 객체ID 불일치",i)

