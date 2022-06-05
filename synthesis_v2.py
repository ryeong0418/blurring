import os
main_path="C:/Users/USER/Desktop/synthesis_test"
path_list=[]


def synthesis(s):
    key_list=["AV","BO","FD","GA","IR","LS","RA","SH","SM","TI"]


    syndic={"AV_01":0,"AV_02":0,"AV_03":0,"AV_04":0,"AV_05":0,"AV_06":0,"AV_07":0,"AV_08":0,"AV_09":0,"AV_10":0,
            "BO_01":0,"BO_02":0,"BO_03":0,"BO_04":0,"BO_05":0,"BO_06":0,"BO_07":0,"BO_08":0,"BO_09":0,"BO_10":0,
            "GA_01":0,"GA_02":0,"GA_03":0,"GA_04":0,"GA_05":0,"GA_06":0,"GA_07":0,"GA_08":0,"GA_09":0,"GA_10":0,
            "LS_01":0,"LS_02":0,"LS_03":0,"LS_04":0,"LS_05":0,"LS_06":0,"LS_07":0,"LS_08":0,"LS_09":0,"LS_10":0,
            "FD_01":0,"FD_02":0,"FD_03":0,"FD_04":0,"FD_05":0,"FD_06":0,"FD_07":0,"FD_08":0,"FD_09":0,"FD_10":0,
            "RA_01":0,"RA_02":0,"RA_03":0,"RA_04":0,"RA_05":0,"RA_06":0,"RA_07":0,"RA_08":0,"RA_09":0,"RA_10":0,
            "SH_01":0,"SH_02":0,"SH_03":0,"SH_04":0,"SH_05":0,"SH_06":0,"SH_07":0,"SH_08":0,"SH_09":0,"SH_10":0,
            "SM_01":0,"SM_02":0,"SM_03":0,"SM_04":0,"SM_05":0,"SM_06":0,"SM_07":0,"SM_08":0,"SM_09":0,"SM_10":0,
            "IR_01":0,"IR_02":0,"IR_03":0,"IR_04":0,"IR_05":0,"IR_06":0,"IR_07":0,"IR_08":0,"IR_09":0,"IR_10":0,
            "TI_01":0,"TI_02":0,"TI_03":0,"TI_04":0,"TI_05":0,"TI_06":0,"TI_07":0,"TI_08":0,"TI_09":0,"TI_10":0}

    for path,dir,files in os.walk(s):
        for filename in files:
            a=filename.split(".")[0]
            synthesis_name=a.split("_")[-2]+"_"+a.split("_")[-1]   
            try:
                if len(filename)==30 and synthesis_name[0:2] in key_list: #Synthesis_name=AV_01, AV_02, AV_03 ,,       
                    syndic[synthesis_name]+=1
                if len(filename)==30 and synthesis_name[0:2] not in key_list:
                    print("키오류파일",filename)
                if len(filename)!=30 and len(filename)!=27:
                    print("자릿수 오류파일",filename)
            except:
                print("오류파일",filename)

    for path,dir,files in os.walk(s):          
        for i in syndic.items():
            if i[1]!=1:
                print("합성오류누락파일",path.split("\\")[-1]+"_"+i[0])

    return s


for path,dirs,files in os.walk(main_path):
    path_list.append(path)


for i in range(1,len(path_list)):
    synthesis(path_list[i])









                    





