import mido
import datetime
import random
import math
from csv import reader
import py_midicsv
from moviepy.editor import *

# mid = mido.MidiFile('20221213_Droner_Rander_[Clip_Selector]_test_03.mid', )
input_audio = AudioFileClip('./20230109_Droner_Rander 2023-01-09 2109.mp3')


# csv_string = py_midicsv.midi_to_csv("20221213_Droner_Rander_[Clip_Selector]_test_03.mid",)

# with open("Droner_Rander_[Clip_Selector]_test_03.csv", "w") as f:
#     f.writelines(csv_string)

def select_clip_with_notes(note :int , dir :str) -> str:
    _note  :int = note
    _dir :str = dir
    if _note == 60:
        return f'{_dir}001.mp4'
    elif _note == 61:
        return f'{_dir}002.mp4'
    elif _note == 62:
        return f'{_dir}003.mp4'
    elif _note == 63:
        return f'{_dir}004.mp4'
    elif _note == 64:
        return f'{_dir}005.mp4'
    elif _note == 65:
        return f'{_dir}006.mp4'
    elif _note == 66:
        return f'{_dir}007.mp4'
    elif _note == 67:
        return f'{_dir}008.mp4'
    else:
        return (f'Note:{_note} is out of range')
    

# Initialize list to store video clips
clips = []

# Initialize starting time for video clips
start_time = 0

# Get the total duration of the midi file
# midi_total_duration = mido.tick2second(mid.length, 1000000, mid.tempo)
# midi_total_time = mid.length

# Get the number of notes in the midi file
# note_count = sum(1 for msg in mid if msg.type == 'note_off' and msg.time > 0)

concat_vid_duration = 0


with open("Droner_Rander_[Clip_Selector]_test_03.csv", "r") as f:
    csv_reader = reader(f, delimiter=',')
    for row in csv_reader:
        if row[2] == ' Note_off_c':
            
        
    # for msg in mid.play():
    #     print(msg)
    #     if msg.time == True and concat_vid_duration < midi_total_time:
            # if msg.note = 
        # if msg.type == 'note_off' and msg.time > 0 or msg.type == 'note_on' and msg.time > 0:
            # Get the duration of the note
            clip_duration = float(row[1]) /1920.031           
            # Get the subclip from the video
            clip = VideoFileClip(select_clip_with_notes(int(row[4]), './INPUT_VIDEOS/'), audio=False).subclip(start_time, start_time + clip_duration)
            # clip = VideoFileClip(select_clip_with_notes(msg.note, './INPUT_VIDEOS/'), audio=False)
            
            # random_frame = clip.get_frame(random.randint(0, int(clip.duration)))
            # clip = ImageClip(random_frame).set_duration(clip_duration)

            # if start_time + clip_duration > 0
            # Append the subclip to the list of video clips
            clips.append(clip)

            # Update the starting time for the next clip
            # start_time += concat_vid_duration
            concat_vid_duration += clip_duration
            print (f'clip_duration:{clip_duration}\t concat_duration:{concat_vid_duration}\t clips_length:{len(clips)}\t')

# Concatenate the video clips
final_video = concatenate_videoclips(clips).set_fps(24)

now = datetime.datetime.now()
final_video.audio = CompositeAudioClip([input_audio])
final_video.write_videofile(f'./{now}.mp4',)