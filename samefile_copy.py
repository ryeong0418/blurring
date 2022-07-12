import os
from distutils.dir_util import copy_tree

json_path="C:\\Users\\USER\\Desktop\\test\\json"
jpg_path="C:\\Users\\USER\\Desktop\\test\\jpg"
new_jpg="C:\\Users\\USER\\Desktop\\test\\new_jpg"

json_path_list=[]
json_dir_list=[]

jpg_path_list=[]
jpg_dir_list=[]
copy_jpg_list=[]

for path,dir,files in os.walk(json_path):
    json_path_list.append(path)

for file in json_path_list:
    if len(file.split("\\")[-1])==20:
        json_dir_list.append(file.split("\\")[-1])


for path,dir,files in os.walk(jpg_path):
    jpg_path_list.append(path)


for file in jpg_path_list:
    if len(file.split("\\")[-1])==20:
        jpg_dir_list.append(file.split("\\")[-1])


for i in json_dir_list: 
    if i in jpg_dir_list:  
        copy_jpg_list.append(i)  ### json_dir와 jpg_dir 공통인 것들 뽑아서 copy_jpg_list에 넣기 ###

        
for i in jpg_path_list:
    total_jpg=i.split("\\")[-1]
    for j in copy_jpg_list:
        if total_jpg==j:
            copy_tree(i,new_jpg+"/"+total_jpg) ### copytree의 경우 이미 폴더가 존재하면 에러 발생->이미 존재하는 폴더에 복사를 하고 싶은 경우 copy_tree이용하기


