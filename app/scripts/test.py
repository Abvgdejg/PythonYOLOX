import av
import os
import shutil
import argparse




def AddArgParser():
    
    global argParser
    argParser = argparse.ArgumentParser(description='')
        
    argParser.add_argument("--frames", default=100, help="Frames")
        
    argParser.add_argument("--video", help="Video")
      

def ArgParse():
    try:
        args = argParser.parse_args()
        frames_list = args.frames.split(",")
        video = args.video
        return [frames_list, video]
    except:
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
    for frame in frames_list:
        try:
            frame = int(frame)
            splited_video[frame].to_image().save("test/frame_%d.jpg" % splited_video[frame].index)
        except: 
            continue

def VideoError():
    print("Video Error")
    raise SystemExit

def Start():

    AddArgParser()

    params = ArgParse()

    ClearDir()
    
    splited_video = SplitVideo(params[1])
    SaveFrames(params[0], splited_video)

Start()

#/app/resources/develop_streem.ts