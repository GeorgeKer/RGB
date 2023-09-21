import datetime
import random
from decimal import *
import mido
from moviepy.editor import *


Clip_Selector_MidiFIle = mido.MidiFile('./20221213_Droner_Rander_[Clip_Selector]_test_03.mid', clip=True, ticks_per_beat=10000)
input_audio = AudioFileClip('./20230109_Droner_Rander 2023-01-09 2109.mp3')

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
    
# Get the total duration of the midi file
total_duration = mido.tick2second(Clip_Selector_MidiFIle.length, Clip_Selector_MidiFIle.ticks_per_beat, 120)

# Get the number of notes in the midi file
note_count = sum(1 for msg in Clip_Selector_MidiFIle if msg.type == 'note_on')


clips = []
for i, track in enumerate(Clip_Selector_MidiFIle.tracks):
    print(f'{i} \t {track}')
    
    for j, msg in enumerate(track):
        if msg.type == 'note_on' or msg.type =='note_off':
            start :float = 0 
            note = msg.note
            
            if msg.time==0: pass
            
            duration = msg.time * 0.0005
            end: float = start + duration
            
            clip = VideoFileClip(select_clip_with_notes(note, './INPUT_VIDEOS/'))
            subClip = clip.subclip(start, end)
            clips.append(subClip)
                
            print (f'i_track:{i} j_msg:{j}\t note:{note}\t duration:{duration}\t start:{start}\t end:{end}\t clip:{subClip.filename}\t {msg}')
                # print (f'output_video.duration - (end-start): {output_video.duration - (end-start)}')
            # start = end
        else:
            print(msg)

output_video = concatenate_videoclips(clips)
now = datetime.datetime.now()
output_video.audio = CompositeAudioClip([input_audio])
output_video.write_videofile(f'./{now}.mp4')

print('done')




# import mido
# from moviepy.editor import VideoFileClip, concatenate_videoclips

# # Read messages from midi file
# mid = mido.MidiFile('file.mid')

# # Initialize list to store video clips
# video_clips = []

# # Initialize starting time for video clips
# start_time = 0

# for msg in mid.play():
#     if msg.type == 'note_on':
#         # Get the duration of the note
#         duration = msg.time

#         # Get the subclip from the video
#         video_clip = VideoFileClip('video.mp4').subclip(start_time, start_time + duration)

#         # Append the subclip to the list of video clips
#         video_clips.append(video_clip)

#         # Update the starting time for the next clip
#         start_time += duration

# # Concatenate the video clips
# final_video = concatenate_videoclips(video_clips)

# # Write the final video to a file
# final_video.write_videofile('output.mp4')