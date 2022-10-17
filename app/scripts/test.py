import av
import os
import shutil
import argparse
import cv2
import numpy as np
import glob




def AddArgParser():
    
    global argParser
    argParser = argparse.ArgumentParser(description='')
        
    argParser.add_argument("--frames", default=100, help="Frames")
        
    argParser.add_argument("--video", help="Video")
      

def ArgParse():
    try:
        args = argParser.parse_args()
        try:
            
            frames_list = args.frames.split(",")
            
        except:
            frames_list = "all"
        video = args.video
        return [frames_list, video]
    except:
        print("Arguments Error")
        raise SystemExit
    
def ClearDir():
    shutil.rmtree("test/")
    os.mkdir("test/")

def SplitVideo(video):
    try:
        current_video = av.open(video)
        frames_list = list(current_video.decode())
        return frames_list
    except:
        VideoError()

def SaveFrames(frames_list, splited_video):
    if (frames_list != "all"):
        for frame in frames_list:
            try:
                splited_video[frame].to_image().save("test/frame_%d.jpg" % splited_video[frame].index)
            except: 
                continue
    else:
        for frame in av.open(splited_video).decode():
            frame.to_image().save("test/frame_%d.jpg" % frame.index)


def VideoError():
    print("Video Error")
    raise SystemExit

def SearchObjects():
    os.system(f"python ../YOLOX/tools/Searching.py \
    image -f ../YOLOX/exps/default/yolox_s.py -c ../YOLOX/datasets/yolox_s.pth \
    --path test/ --conf 0.25 --nms 0.45 --tsize 640 \
    --save_result --device [cpu/gpu]")

def WriteVideo(video_frames):
    out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 20, (1920, 1080))

    for frame in video_frames:
        filename = f"processed_frames/frame_{frame}.jpg"
        print(filename)
        img = cv2.imread(filename)
        out.write(img)

    out.release()

def Start():

    AddArgParser()

    frame_list = []

    params = ArgParse()
    if (params[0] != "all"):
        for param in params[0]:
            param = int(param)
            frame_list.append(param)

    ClearDir()
    
    splited_video = SplitVideo(params[1])
    if (params[0] != "all"):
        SaveFrames(frame_list, splited_video)
    else: 
        SaveFrames("all", params[1])

    SearchObjects()
    if (params[0] != "all"):
        WriteVideo(frame_list)
    else: 
        WriteVideo(splited_video)
    

Start()

#/app/resources/develop_streem.ts