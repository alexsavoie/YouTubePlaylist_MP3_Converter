from pytube import YouTube, Playlist
import os

dir = './songs'

print("\n" + "= "*19 + "\nALEX'S YOUTUBE PLAYLIST MP3 CONVERTER\n" + "= "*19 + "\n")
#Import the playlist:
print("Enter the playlist URL:")
url = input(">> ")


#Import the playlist:
print("Do you wish to remove all songs currently in the songs directory? (Y or N):")
choice = input(">> ")

while(True):
    
    if(choice.lower() == "y"):
        #Deleting all the files in the songs directory
        print("Clearing the songs folder...")
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        break
    
    elif(choice.lower() == "n"):
        break
    
    else:
        print("Wrong input! Press Y or N")
        choice = input(">> ")

    

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
    
    path = dir + './' + video.title+ '.mp3'
    if(os.path.exists(path)):
        print(f'{video.title} already exist!')
        it +=1
        continue
    
    
    print(f"Downloading -> {video.title}")
    
    stream = video.streams.filter(only_audio=True, mime_type='audio/mp4').order_by('abr').desc().first()
    try:
        out_file = stream.download(output_path='./songs')
    except:
        print(f'{video.title} download has failed...')
        it +=1
        k=input("Press the enter button to close the window") 
        continue

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(f"{it}/{len(p.videos)} songs downloaded")
    it += 1 
    
print("\nThe playlist has been successfully downloaded!\n")
k=input("Press the enter button to close the window") 
