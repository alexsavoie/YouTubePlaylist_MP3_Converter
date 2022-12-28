from pytube import YouTube, Playlist
import os

#Clearing the songs folder to avoid duplicate error
dir = './songs'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))


print("\n" + "= "*19 + "\nALEX'S YOUTUBE PLAYLIST MP3 CONVERTER\n" + "= "*19 + "\n")
#Import the playlist:
print("Enter the playlist URL:")
url = input(">> ")

try:
    p = Playlist(url)
    print(f'Downloading: {p.title}\n')
except KeyError:
    print("You the url you entered is invalid!")
    exit()
except Exception:
    print("Error - Problem with the app!")
    exit()






it = 1
#Download every video in the YouTube playlist
for video in p.videos:
    
    print(f"Downloading -> {video.title}")
    
    stream = video.streams.filter(only_audio=True, mime_type='audio/mp4').order_by('abr').desc().first()
    try:
        out_file = stream.download(output_path='./songs')
    except:
        print(f'{video.title} download has failed...')
        it +=1
        continue

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(f"{it}/{len(p.videos)} songs downloaded")
    it += 1 
    
print("\nThe playlist has been successfully downloaded!")
k=input("Press the enter button to close the window") 
