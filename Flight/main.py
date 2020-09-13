import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj.save(filename)


def mergeAudios(audios) -> object:
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    audio = AudioSegment.from_mp3('flight.mp3')
    start = 98000
    finish = 100000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # flight number  name
    start = 5000
    finish = 7000
    audioProcessed = audio[start:finish]
    audioProcessed.export("2_hindi.mp3", format="mp3")

    # city name
    start = 8000
    finish = 15000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # thank you line
    start = 200000
    finish = 205000
    audioProcessed = audio[start:finish]
    audioProcessed.export("4_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # mayIhave your attention please
        textToSpeech(item['flight_no'], '2_hindi.mp3')
        # flight number  name
        textToSpeech(item['to'], '3_hindi.mp3')
        # city name

        # thank you line

        audios = [f"{i}_hindi.mp3" for i in range(1, 3)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['flight_no']}{index + 1}.mp3", format="mp3")


if __name__ == '__main__':
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now generating Announcement....")
    generateAnnouncement("announce_hindi.xlsx")
