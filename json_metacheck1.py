import os
import json

main_path="D:/blurring-Json/Final_Json/6m2w_1"
jsonArr=[]
jsonCount=0
# 딕셔너리 key, value값 존재여부

def data():
    for path,dir,files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):

                error_json={}
                annot_key=[]
                annot_value=[]
                filename=file.split(".")[0]

                try:
                    with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                        json_data=json.load(json_file)                       
                        #syn_list=["AV_01","","","",]
                        raw_key_list=["Raw_Data_ID","Copyrighter","Location","Lux_Level","Object_ID","Date","Length","Resolution","FPS","F-Stop","Exposure_Time","Angle","File_Extension"]
                        source_key_list=["Source_Data_ID","Noise_type","Synthesis_type","Center_coordinate","File_Extension"]
                        learning_key_list=["Path","File_Extension","Json_Data_ID","Annotations"]
                        annot_list=['Class_ID','Type','Type_value','Class_size']
                        annotations=json_data["Learning_Data_Info."]["Annotations"]

                        error_json[os.path.join(path, file)] = ""

                        #raw_data key값 확인하기
                        for i in raw_key_list:
                            if i not in json_data["Raw_Data_Info."].keys():
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +i+"에러"+","

                        #source_data key값 확인하기
                        for i in source_key_list:
                            if i not in json_data["Source_Data_Info."].keys():
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +i+"에러"+","
                        
                        #learning_data key값 확인하기
                        for i in learning_key_list:
                            if i not in json_data["Learning_Data_Info."].keys():
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +i+"에러"+","
                        
                        #raw_data value값이 ""이면 확인하기
                        for key,value in json_data["Raw_Data_Info."].items():
                            if len(value)==0:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)]+key+"에러"+","
                        
                        #learning_data value값이 ""이면 확인하기
                        for key,value in json_data["Learning_Data_Info."].items():
                            if len(value)==0:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +key+"에러"+","
                                               
                        #annotations key, value값 없는거 확인하기
                        for i in range(len(annotations)):
                            for key,value in annotations[i].items():
                                annot_key.append(key)
                                annot_value.append(value)

                        for i in annot_list:
                            if i not in annot_key:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +i+"에러"+","

                        for value in annot_value:
                            if len(value)==0:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +"annotation value 에러:"+","

                        #syntehsis 없는거 check
                        if len(filename) ==26:
                            if len(json_data["Source_Data_Info."]["Synthesis_type"])==0:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +"synthesis value 에러:"+","

                        #noise 없는거 check
                        if len(filename) ==23:
                            if len(json_data["Source_Data_Info."]["Noise_type"])==0:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +"noise value 에러:"+","
                        
                        #source_data_id 없는거 check
                        if len(json_data["Source_Data_Info."]["Source_Data_ID"])==0:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +"source_data_id value 에러:"+","

                        #file_extension 없는거 check
                        if len(json_data["Source_Data_Info."]["File_Extension"])==0:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +"File_Extension value 에러:"+","

                        #center_coordinate 없는 거 check
                        if len(json_data["Source_Data_Info."]["Center_coordinate"])==0:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] +"Center_coordinate 에러:"+","

                                
                    if error_json[os.path.join(path,file)] == "":
                        pass
                    else:
                        print(error_json)

                except Exception as ex:
                    print(ex)
                    pass


if __name__ == '__main__':
    data()


def data_type():

    for (path, dirs, files) in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                error_json = {}
                try:

                    with open(os.path.join(path, file), "r", encoding="utf-8") as json_file:
                        json_data = json.load(json_file)
                        error_json[os.path.join(path, file)] =""

                        annot=json_data["Learning_Data_Info."]["Annotations"]

                        #raw_data value값 string 확인하기
                        for i in json_data["Raw_Data_Info."].values():
                            if type(i) != str:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Raw_Data_ID 타입 에러, "

                        #source_data value값 string 확인하기
                        for i in json_data["Source_Data_Info."].values():
                            if type(i) != str:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Raw_Data_ID 타입 에러, "

                        #learning_data value값 type 확인하기
                        if "Path" in json_data["Learning_Data_Info."] and type(json_data["Learning_Data_Info."]["Path"])!=str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Raw_Data_ID 타입 에러, "

                        if "File_Extension" in json_data["Learning_Data_Info."] and type(json_data["Learning_Data_Info."]["File_Extension"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "json 타입 에러, "

                        if "Json_Data_ID" in json_data["Learning_Data_Info."] and type(json_data["Learning_Data_Info."]["Json_Data_ID"]) != str:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Json_Data_ID 타입 에러, "

                        if "Annotations" in json_data["Learning_Data_Info."] and type(json_data["Learning_Data_Info."]["Annotations"]) != list:
                            error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "annotations 타입 에러, "

                        
                        for i in range(len(annot)):

                            class_id=annot[i]["Class_ID"]
                            b_box=annot[i]["Type"]
                            type_value=annot[i]["Type_value"]
                            class_size=annot[i]["Class_size"]
    

                            if "Class_ID" in annot[i] and type(class_id) != str:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "class_id 타입 에러, "

                            if "Type" in annot[i] and type(b_box) != str:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "b_box 타입 에러, "

                            if "Type_value" in annot[i] and type(type_value) != list:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "Type_value 타입 에러, "

                            if "Class_size" in annot[i] and type(class_size) != str:
                                error_json[os.path.join(path, file)] = error_json[os.path.join(path, file)] + "class_size 타입 에러, "



                    if error_json[os.path.join(path, file)] == "":
                        pass

                    else :
                        print(error_json)

                except:
                    error_json[os.path.join(path, file)] = "json 타입 에러"


if __name__ == '__main__':
    data_type()


def duplicate():
    global jsonCount

    for path, dir, files in os.walk(main_path):
        for file in files:
            if file.endswith(".json"):
                if file not in jsonArr:
                    jsonArr.append(file)
                    jsonCount += 1
                else:
                    print("json중복 파일 : {}".format(file))
    print("총 json 수량 : {}".format(jsonCount))

if __name__ == '__main__':
    duplicate()
