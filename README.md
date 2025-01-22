# whisper_audio_translate
Input: folder with wav files  
Output: the txt files of the audios


## Step 1
Crawl the data from [Broadcastify](https://github.com/ChiShengChen/broadcastify_mp3_crawler).
> python firefox_craw_data_v3.py

## Step 2
Pre-process the audio to filter the non-silent part.
> python pick_tri_all10s.py

## Step 3
Translate the audio into transcription.
