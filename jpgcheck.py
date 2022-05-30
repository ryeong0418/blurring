import os
main_path="C:/Users/USER/Desktop/blurtest"
path_list=[]



def total_count(p):    
    total_count=0
    
    for path,dir,files in os.walk(p):
        for i in files:
            if i.endswith(".jpg"):
                total_count+=1
    return total_count

def gt_count(g):
    gt_count=0
    for path,dir,files in os.walk(g):
        for i in files:
            a=i.split(".")
            if len(i)==27 and a[0].split("_")[4]=="GT":
                gt_count+=1
    
    return gt_count

def noise_count(n):
    noise_list=["FF", "RF", "RL","UD","LE","DU","SC","FI","LB","RB"]
    noise_count=0
    for path,dir,files in os.walk(n):
        for i in files:
            a=i.split(".")
            if len(i)==27 and a[0].split("_")[4]!="GT"and (a[0].split("_")[4] in noise_list):
                noise_count+=1
    return noise_count


for path,dirs,files in os.walk(main_path):
    path_list.append(path)

for i in range(1,len(path_list)):

    filename=path_list[i].split("\\")[1]
    if total_count(path_list[i])!=103:
        print(filename,"파일수량 103장 아닙니다")
    
    if gt_count(path_list[i])!=1:
        print(filename, "GT수량 오류")

    if noise_count(path_list[i])!=2:
        print(filename,"Noise수량 오류")
