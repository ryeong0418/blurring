import os
import json

main_path="C:/Users/USER/Desktop/마도요3"

# 레디얼블러 RA

def data1():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_01=filename+"_"+"RA"+"_"+"01"


                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+1
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-1
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_01+".json"))
                    with open(os.path.join(path,RA_01+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data1()

def data2():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_02=filename+"_"+"RA"+"_"+"02"


                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+1.3
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-1.3
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_02+".json"))
                    with open(os.path.join(path,RA_02+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data2()

def data3():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_03=filename+"_"+"RA"+"_"+"03"


                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+1.6
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-1.6
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_03+".json"))
                    with open(os.path.join(path,RA_03+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data3()

def data4():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_04=filename+"_"+"RA"+"_"+"04"

                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+2
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-2
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_04+".json"))
                    with open(os.path.join(path,RA_04+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data4()

def data5():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_05=filename+"_"+"RA"+"_"+"05"

                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+2.5
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-2.5
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_05+".json"))
                    with open(os.path.join(path,RA_05+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data5()

def data6():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_06=filename+"_"+"RA"+"_"+"06"


                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+3
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-3
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_06+".json"))
                    with open(os.path.join(path,RA_06+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data6()

def data7():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_07=filename+"_"+"RA"+"_"+"07"

                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+3.5
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-3.5
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_07+".json"))
                    with open(os.path.join(path,RA_07+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data7()

def data8():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_08=filename+"_"+"RA"+"_"+"08"


                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+4
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-4
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_08+".json"))
                    with open(os.path.join(path,RA_08+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data8()

def data9():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_09=filename+"_"+"RA"+"_"+"09"


                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+4.5
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-4.5
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_09+".json"))
                    with open(os.path.join(path,RA_09+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data9()

def data10():
    filelist=[]
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                name=file.split(".")[0]
                if name.split("_")[-1] == "GT":
                    filename=name.split("_")[0]+"_"+name.split("_")[1]+"_"+name.split("_")[2]+"_"+name.split("_")[3]  

                    RA_10=filename+"_"+"RA"+"_"+"10"


                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                   
                        annot=json_data['Learning_Data_Info.']['Annotation']
                        jsonid=json_data["Learning_Data_Info."]["Json_Data_ID"]
                        print(annot)

                        for i in range(len(annot)):
                            annot_type=annot[i]["Type_value"]
                            for index, value in enumerate(annot_type):
                                if index==1 or index==2 or index==3 or index==4:
                                    value=value+5
                                    annot_type[index]=value
                                if index==0 or index==5 or index==6 or index==7:
                                    value=value-5
                                    annot_type[index]=value  

                        print(annot)
                        print(os.path.join(path,RA_10+".json"))
                    with open(os.path.join(path,RA_10+".json"), "w", encoding="utf-8") as json_file:
                        json.dump(json_data,json_file,indent= 4,ensure_ascii=False)            
                        print("{} meta 수정 완료".format(file))

if __name__ == '__main__':
    data10()
