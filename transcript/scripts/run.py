# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import whisper
import os


os.chdir('C:\\Users\\51027\\Documents\\GitHub\\whisper_transcription\\transcript\\raw_data')
file_names=os.listdir()
audio_files=[];

for i in file_names:
    if i[len(i)-3:len(i)] =='wav':
        audio_files.append(i)

    

model = whisper.load_model("small")
os.chdir('C:\\Users\\51027\\Documents\\GitHub\\whisper_transcription\\transcript')
i=1
for s in audio_files:
    result = model.transcribe('raw_data\\'+s)
    tmp_file='text_data\\'+s[0:-4]+'_whisper.txt'
    f = open(tmp_file , 'w' )
    f.write(result['text'])
    f.close()
    

    print('No.'+str(i)+' Aduio:')
    print(result["text"])
    i=i+1