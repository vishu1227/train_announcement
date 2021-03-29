import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    mytext=str(text)
    langunage='hi'
    myobj=gTTS(text=mytext,lang=langunage,slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined=AudioSegment.empty()

    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)

    return combined

def genrateSkeleton():
    audio=AudioSegment.from_mp3('railway.mp3')

    #1. Kripys dyan dijiya.....
    start=87200  # starting timein milli second
    finish=90000
    audioProcessed=audio[start:finish]
    audioProcessed.export('1_hindi.mp3',format='mp3')

    #2. From city 

    #3. sai chalkar.....
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    #4. is via-city
     
    #5. ke rastai
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    #6. to-city
     
    #7. Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    #8. is train no and name
     
    #9. kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11 - par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")


def genrateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)

    for index,item in df.iterrows():
        # 2 from City
        textToSpeech(item['from'],'2_hindi.mp3')

        # 4 via-city
        textToSpeech(item['via'],'4_hindi.mp3')

        # 6 to-city
        textToSpeech(item['to'],'6_hindi.mp3')

        # 8 train no and name
        textToSpeech(item['train_no']+' '+item['train_name'],'8_hindi.mp3')

        # 10 plateform number
        textToSpeech(item['plateform'],'10_hindi.mp3')

        audios=[f'{i}_hindi.mp3' for i in range(1,12)]

        announcement=mergeAudios(audios) 
        announcement.export(f'announcement_{index+1}.mp3',format='mp3')


if __name__=='__main__':
    print('Genrating Skeleton...')
    genrateSkeleton()
    genrateAnnouncement('announce_hindi.xlsx')

