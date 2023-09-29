# %%
import datetime
# import math
import random
from csv import reader
import easygui
# import mido
import py_midicsv
from moviepy.editor import concatenate_videoclips, VideoFileClip, AudioFileClip, CompositeAudioClip

# %%
input_audio_path = easygui.fileopenbox('../', filetypes=['*.mp3'], multiple=False, title='Select Audio File')
input_audio = AudioFileClip(input_audio_path)

midi_file_path = easygui.fileopenbox('../', filetypes=['*.mid'], multiple=False, title='Select Midi File')
csv_string = py_midicsv.midi_to_csv(midi_file_path)

with open('auto_saved.csv', 'w', encoding='UTF8') as f:
    csv_with_no_header = csv_string[5:]
    f.writelines(csv_with_no_header)
    

# %%
def select_clip_with_notes(note: int, dir: str) -> str:
    assert 36 <= note <= 63, f'Note: {note} is out of range'
    video_number = note - 35  # Calculate video number
    print(f'note: {note}\tvideo_number: {video_number}')
    return f'{dir}{video_number:03d}.MP4'

    
# %%
# Initialize list to store video clips
subclips = []
# Initialize starting time for video clips
sub_startime = 0
concat_vid_duration = 0
concat_start_time = 0

# %%
with open('auto_saved.csv', 'r', encoding='UTF8') as f:
    csv_reader = reader(f, delimiter=',')
    for row in csv_reader:
        if row[0]=='4' and row[2] == ' Note_off_c':
            print(f'{row}')
            note_off_time = float(row[1]) /1920  
            duration = note_off_time - concat_vid_duration
            clip = VideoFileClip(select_clip_with_notes(int(row[4]), '/media/user7/Double_Dragon/Videography/My_Python_Video_Projects/RGB/INPUT_VIDEOS/'), audio=False)
            sub_startime = random.random()*(clip.duration - 1)
            sub = clip.subclip(
                sub_startime,
                sub_startime + duration
                )

            subclips.append(sub)

            concat_vid_duration = note_off_time
            print (f'concat_vid_duration:{concat_vid_duration}\t clips_length:{len(subclips)}\t')

# Concatenate clips
final_video = concatenate_videoclips(subclips).set_fps(60)

clip.close()
sub.close()
now = datetime.datetime.now()
final_video.audio = CompositeAudioClip([input_audio])
final_video.write_videofile(f'./{now}.MP4',)
# %%
