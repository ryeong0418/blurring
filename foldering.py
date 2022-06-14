import os
import json
import glob
import shutil


main_path="C:/Users/USER/Desktop/jpg_test"

def makedir():
    path_list=[]

    for path,dirs,files in os.walk(main_path):
        path_list.append(path)

    for i in range(1,len(path_list)):
        os.makedirs(path_list[i]+"/"+"합성블러",exist_ok=True)
        print(path_list[i]+"/"+"합성블러")


makedir()


#blur_move

def blur_move():
    p_list=[]
    synthesis_list=["AV","BO","FD","GA","IR","LS","RA","SH","SM","TI"]

    for path,dir,files in os.walk(main_path):
        p_list.append(path)

    for i in p_list:
        syn_path=i.split("\\")[-1]
        if syn_path=="합성블러":
            start_path=i.split("\\")[0]+"/"+i.split("\\")[1]
            filename=glob.glob(start_path+"/*.jpg")
            for file in filename:
                #print(file) C:/Users/USER/Desktop/jpg_test/D2_220602_OH15_E0001\D2_220602_OH15_E0001_AV_01.jpg
                #print(file.split("\\")) #['C:/Users/USER/Desktop/jpg_test/D2_220602_OH15_E0001', 'D2_220602_OH15_E0001_AV_01.jpg']
                #print(len(file.split("\\")[1])) 30 ,D2_220602_OH15_H0002_SH_09.jpg
                syn_name=file.split("\\")[1].split("_")[4]

                if syn_name in synthesis_list:
                    src=file.split("\\")[0]+"/"+file.split("\\")[1]
                    dst= file.split("\\")[0]+"/"+"합성블러"+"/"+file.split("\\")[1]
                    #print(src,dst)
                    shutil.move(src,dst)

    print("폴더 이동 완료")

blur_move()
