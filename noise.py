import os


main_path="D:/blurring-linkflow/6m2w_220610/6월 2주차_220610(정제데이터)"

FF_RF=[]
RL_UD=list(range(17,33))
LE_DU=list(range(33,49))
SC_FI=list(range(49,65))
LB_RB=list(range(65,81))

n=0
while n<16:
    n+=1
    number=str(n).zfill(2)
    FF_RF.append(number)

for path,dir,files in os.walk(main_path):
    for file in files:
        if file.endswith(".jpg"):
            #print(file)
            filename=file.split(".")[0]
            real_blur=filename.split("_")[4]
            #print(real_blur)
            object_id=filename.split("_")[2][2:4]

                
            if (real_blur == "FF" or real_blur =="RF") and not (object_id in FF_RF):
                print("FF/RF오류",file)
            if (real_blur == "RL" or real_blur =="UD") and not (int(object_id) in RL_UD):
                print("RL/UD오류",file)

            if (real_blur == "LE" or real_blur =="DU") and not (int(object_id) in LE_DU):
                print("LE/DU오류",file)

            if (real_blur == "SC" or real_blur =="FI") and not (int(object_id) in SC_FI):
                print("SC/FI오류",file)

            if (real_blur == "LB" or real_blur =="RB") and not (int(object_id) in LB_RB):
                print("LB/RB오류",file)


                
                    
                
    


