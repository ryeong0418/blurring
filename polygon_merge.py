#%%

import json
from shapely.ops import unary_union
import os
from shapely.geometry import Polygon


main_path="C:/Users/USER/Desktop/polygon"
poly_list=[]

for path,dir,files in os.walk(main_path):
    for file in files:
        if file.endswith(".json"):
            with open(os.path.join(path,file),"r",encoding="utf-8") as json_file:
                json_data=json.load(json_file)

                for i in json_data["Learning_Data_Info."]["Annotation"]:
                    for key,value in i.items():
                        # print(key)
                        # print("="*50)
                        # print(value)
                        if value=="F38":
                            poly_list.append(i["segmentation"])

#print(poly_list)

total=[]
baby_list=[]
old_list=[]


for index,i in enumerate(poly_list[0]):
    #print(index,i)
    #print(i)
    if (index+1)%2!=0: ###홀수일때
        total.append(i)
    
    else: ###짝수일때
        total.append(i)
        baby_list.append((total[0],total[1]))
        total=[]

#print(baby_list)

for index,i in enumerate(poly_list[1]):
    if (index+1)%2!=0:
        total.append(i)
    else:
        total.append(i)
        old_list.append((total[0],total[1]))
        total=[]

#print(old_list)

baby_polygon=Polygon(baby_list)
old_polygon=Polygon(old_list)
merge_polygon=[baby_polygon,old_polygon]
unary_union(merge_polygon)
unary_union(merge_polygon).boundary


# %%
