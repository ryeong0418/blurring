import os
import json
import pandas as pd
import glob

raw_source_path="C:/Users/USER/Desktop/jso/raw_source"
learning_path="C:/Users/USER/Desktop/jso/crowdworks"
result_path="C:/Users/USER/Desktop/jso"

raw_source_list=[]
learning_list=[]

raw_source_list=glob.glob(raw_source_path+"/*/*.json")
learning_list=glob.glob(learning_path+"/*/*.json")


for raw_source, learning in zip(raw_source_list,learning_list):
    with open(raw_source,"r",encoding="utf-8") as json_files:
        data1=json.load(json_files)
    with open(learning,"r",encoding="utf-8") as json_files:
        data2=json.load(json_files)

        raw_id=data1['Raw_Data_Info.']['Raw_Data_ID']
        source_id=data1['Source_Data_Info.']['Source_Data_ID']
        learning_id=data2['Learning_Data_Info.']['Json_Data_ID']
   
        os.makedirs(result_path+"/"+raw_id,exist_ok=True) # 최종 json 파일 들어갈 폴더 생성

        if source_id == learning_id:
            data1.update(data2) # json merge

            with open(os.path.join(result_path+"/"+raw_id,source_id+".json"),"w",encoding="utf-8") as json_file:
                json.dump(data1,json_file,indent=4,ensure_ascii=False,default=str)
