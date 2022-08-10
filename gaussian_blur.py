import os
from pathlib import Path
from PIL import Image
from PIL import ImageFilter


main_path="C:/Users/USER/Desktop/7월3주차"

for path,dir,files in os.walk(main_path):
    for file in files:
        if file.endswith(".jpg"):
            filename=file.split(".")[0]
            if filename.split("_")[-1] == "GT":
                f_name=filename.split("_")[0]+"_"+filename.split("_")[1]+"_"+filename.split("_")[2]+"_"+filename.split("_")[3]
                #print(f_name)
                img=Image.open(path+"/"+file)
                i=0
                while i<10:
                    i=i+1
                    # print(i) 1,2,3,4,5,6,7,8,9,10
                    blur_img=img.filter(ImageFilter.GaussianBlur(i))
                    print(path+"/"+f_name+"_GA"+"_"+str(i).zfill(2)+".jpg")
                    blur_img.save(path+"/"+f_name+"_GA"+"_"+str(i).zfill(2)+".jpg")

print("가우시안블러 생성 완료")
