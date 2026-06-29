import os

MUSIC_FOLDER = r"D:\Music"

def play_music():

    songs = os.listdir(MUSIC_FOLDER)

    if songs:
        os.startfile(os.path.join(MUSIC_FOLDER, songs[0]))
    else:
        print("No Songs Found")

if __name__ == "__main__":
    print("Music module started...")
    play_music()