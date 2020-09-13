 # generate attention.
    start = 182000
    finish = 186000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")
    # 2 flight number
    start = 0
    finish = 7000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")
    # kha ki flight h
    start = 7000
    finish = 10000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # you can use your mobile phones
    start = 93000
    finish = 103000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # reaching out destination
    start = 48000
    finish = 54000
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    pass


if __name__ == "__main__":
    print("Generating Skeleton....")
    generateSkeleton()
    print("Now Generating Annoucement...")
    generateAnnouncement("announce_hindi.xlsx")