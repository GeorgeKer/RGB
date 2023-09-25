# %%
import datetime
# import math
import random
from csv import reader

# import mido
import py_midicsv
from moviepy.editor import concatenate_videoclips, VideoFileClip, AudioFileClip, CompositeAudioClip

# %%
input_audio = AudioFileClip('20230925_MidiNote_Clip_Selector_b/input_audio.mp3')

csv_string = py_midicsv.midi_to_csv('./20230925_MidiNote_Clip_Selector_b/input_midi.mid', encoding='utf-8')
# with open("Droner_Rander_[Clip_Selector]_test_03.csv", "w") as f:
#     f.writelines(csv_string)

def select_clip_with_notes(note :int , dir :str) -> str:
    _note  :int = note
    _dir :str = dir
    assert _note >= 60 and _note <= 83, f'Note:{_note} is out of range'
    if _note == 60: return f'{_dir}001.mp4'
    if _note == 61: return f'{_dir}002.mp4'
    if _note == 62: return f'{_dir}003.mp4'
    if _note == 63: return f'{_dir}004.mp4'
    if _note == 64: return f'{_dir}005.mp4'
    if _note == 65: return f'{_dir}006.mp4'
    if _note == 66: return f'{_dir}007.mp4'
    if _note == 67: return f'{_dir}008.mp4'
    if _note == 68: return f'{_dir}009.mp4'
    if _note == 69: return f'{_dir}010.mp4'
    if _note == 70: return f'{_dir}011.mp4'
    if _note == 71: return f'{_dir}012.mp4'
    if _note == 72: return f'{_dir}013.mp4'
    if _note == 73: return f'{_dir}014.mp4'
    if _note == 74: return f'{_dir}015.mp4'
    if _note == 75: return f'{_dir}016.mp4'
    if _note == 76: return f'{_dir}017.mp4'
    if _note == 77: return f'{_dir}018.mp4'
    if _note == 78: return f'{_dir}019.mp4'
    if _note == 79: return f'{_dir}020.mp4'
    if _note == 80: return f'{_dir}021.mp4'
    if _note == 81: return f'{_dir}022.mp4'
    if _note == 82: return f'{_dir}023.mp4'
    if _note == 83: return f'{_dir}024.mp4'
    
# %%

# Initialize list to store video clips
subclips = []

# Initialize starting time for video clips
sub_startime = 0
concat_vid_duration = 0
concat_start_time = 0


with open("Droner_Rander_[Clip_Selector]_test_03.csv", "r") as f:
    csv_reader = reader(f, delimiter=',')
    for row in csv_reader:
        if row[2] == ' Note_off_c':
            
            note_off_time = float(row[1]) /1920  
            duration = note_off_time - concat_vid_duration
            clip = VideoFileClip(select_clip_with_notes(int(row[4]), './INPUT_VIDEOS/'), audio=False)
            sub_startime = random.random()*(clip.duration - 1)
            sub = clip.subclip(
                sub_startime,
                sub_startime + duration
                )
            
            # random_frame = clip.get_frame(
            #     random.randint(
            #         0, 10*int(clip.duration)
            #         )*10
            #                             )
            # clip = ImageClip(random_frame).set_duration(note_off_time-concat_vid_duration)
            
            # if start_time + clip_duration > 0
            # Append the subclip to the list of video clips
            subclips.append(sub)

            concat_vid_duration = note_off_time
            print (f'concat_duration:{concat_vid_duration}\t clips_length:{len(subclips)}\t')

# Concatenate clips
final_video = concatenate_videoclips(subclips).set_fps(60)

now = datetime.datetime.now()
final_video.audio = CompositeAudioClip([input_audio])
final_video.write_videofile(f'./{now}.mp4',)