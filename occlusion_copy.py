import os
import shutil

new_jpg_path=r'C:\Users\USER\Desktop\D_NEW'

list_01=[]

for path,dir,files in os.walk(new_jpg_path):
    for file in files:
        if file.endswith(".jpg"):
            if file.split(".")[0].split("_")[-1]=="0001":
                # print(file) D1_221009_ISS02_E0008_0001.jpg
                list_01.append(file)
                src=os.path.join(path,file)
                print("0001 파일 ",src)
                new_filename=file.split("_")[0]+"_"+file.split("_")[1]+"_"+file.split("_")[2]+"_"+file.split("_")[3]+"_"+"0000"+".jpg"
                dst=os.path.join(path,new_filename)
                print("0000 파일 ",dst)
                shutil.copy(src,dst)



                
                