from moviepy.editor import VideoFileClip
import os

old_path="D:/blurring-linkflow"
new_path="D:/20s_mp4"


## 20초 초과하는 영상 파일명 추출
def get_duration():

    for path,dir,files in os.walk(old_path):
        for file in files:
            if file.endswith(".mp4"):
                clip=VideoFileClip(path+"/"+file)
                mp4_second=clip.duration # 7.83
                s=str(mp4_second).split(".")[0] #7

                if int(s)>20:
                    print(str(file)+"//"+str(mp4_second))
                    #clip=clip.cutout(0,20) # 뒤에 20초 잘림
                    clip=clip.subclip(0,20) # 영상길이 20초로 만듦 (앞에서부터 20초)
                    clip.write_videofile(new_path+"/"+file)

                else:
                    pass

                clip.close()


if __name__ == "__main__":
    get_duration()
