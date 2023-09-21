from moviepy.editor import *
import easygui
import os

split_length :float = 15*60
INPUT_VIDEO = VideoFileClip(
    easygui.fileopenbox(default='/mnt/Double_Dragon/Videos/')
)
input_length :float = INPUT_VIDEO.duration
clip_start :float = 0.0

i :int = 1

if split_length < input_length:
    while clip_start < input_length:
        
        clip_end = clip_start + split_length
        if clip_end > input_length: clip_end = split_length
        clip :VideoClip= INPUT_VIDEO.subclip(clip_start, clip_end)
        clip.write_videofile(
            f'{str(INPUT_VIDEO.filename[:-4])}_{str(i)}.mp4',
            fps=INPUT_VIDEO.fps,
            preset= 'veryslow',
            threads= '4',
            logger='bar'
        )    
        clip_start = clip_end
        i+= 1
else:
    easygui.msgbox('"split_length" must be smaller than "input_length" to split')


print('Done!')