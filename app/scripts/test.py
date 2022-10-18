from re import S
from turtle import speed
import av
import os
import shutil
import argparse
import cv2
import numpy as np
import glob
import Searching
import args_parser
import time

#args.demo = 'image'


def ArgParse():
    try:
        tmp_args = args_parser.make_parser().parse_args()
        try:
            
            tmp_args.frames = tmp_args.frames.split(",")
            
        except:
          tmp_args.frames = "all"
        
        tmp_args.ckpt = '../YOLOX/assets/yolox_s.pth'
        tmp_args.exp_file = '../YOLOX/exps/default/yolox_s.py'
        tmp_args.path = "../YOLOX/assets/"
        tmp_args.save_result = True
        return tmp_args
    except:
        print("Arguments Error")
        raise SystemExit
    
def ClearDir():
    shutil.rmtree("test/")
    os.mkdir("test/")

def SplitVideo(video):
    try:
        current_video = av.open(video)
        frames_list = []
        for frame in current_video.decode():
            frames_list.append(frame.to_image())
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

def SearchObjects(type, frames):
    if type == False:
        os.system(f"python ../YOLOX/tools/Searching.py \
        image -f ../YOLOX/exps/default/yolox_s.py -c ../YOLOX/assets/yolox_s.pth \
        --path test/ --conf 0.25 --nms 0.45 --tsize 640 \
        --save_result --device [cpu/gpu]")
    else:
        for frame in frames:
            if os.path.exists(f"processed_frames/frame_{(frame, frame.index)[type == True]}.jpg"):
                continue
            else:
                os.system(f"python Searching.py \
            image -f ../YOLOX/exps/default/yolox_s.py -c ../YOLOX/assets/yolox_s.pth \
            --path test/frame_{(frame, frame.index)[type == True]}.jpg --conf 0.25 --nms 0.45 --tsize 640 \
            --save_result --device [cpu/gpu]")
                

def WriteVideo(video_frames, type='not_all'):
    out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 20, (1920, 1080))
    i = 0

    for frame in video_frames:


        # filename = f"processed_frames/frame_{(frame, i)[type == 'all']}.jpg"

        i += 1

      
        image = Searching.main_search(Searching.get_exp(args.exp_file), args, f'test/frame_{i}.jpg')
        # img = cv2.imread(filename)
        
        out.write(image)
        self._frames += 1
    out.release()

def upload_speed(self):
    _frames_speed = 0
    
  
    _frames = 0
    time.sleep(2) 
    _frames_speed = _frames/2
    print(f'current_speed: {_frames_speed}')

    def addFrame():
        frames += 1

    #upload_speed()

def Start():

    frame_list = []

    global args 
    args = ArgParse()
    if (args.frames != "all"):
        for param in args.frames:
            param = int(param)
            frame_list.append(param)

    # ClearDir()
    
    # splited_video = SplitVideo(args.video)
    # if (args.frames != "all"):
    #     SaveFrames(frame_list, splited_video)
    # else: 
    #     SaveFrames("all", args.video)
    self.upload_speed()
    # SearchObjects(True, splited_video)
    if (args.frames != "all"):
        WriteVideo(frame_list)
    else: 
        WriteVideo(splited_video, 'all')
    

Start()

#/app/resources/develop_streem.ts
