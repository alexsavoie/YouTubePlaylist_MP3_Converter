import os
import pytube
from pydub import AudioSegment
from tqdm import tqdm

def download_video(url):
    # Use pytube to download the video
    yt = pytube.YouTube(url)
    video = yt.streams.first()
    
    # Use tqdm to show the progress of the download
    with tqdm(total=video.filesize, unit="B", unit_scale=True, desc="Downloading") as pbar:
        # Download the video in chunks of 1024 bytes
        video.download(chunk_size=1024)
        pbar.update(1024)
    print("Video downloaded!")

def convert_to_mp3(video_name, mp3_name):
    # Use pydub to convert the video file to an mp3 file
    video_format = video_name.split(".")[-1]
    sound = AudioSegment.from_file(video_name, video_format)

    # Use tqdm to show the progress of the conversion
    with tqdm(total=len(sound), unit="B", unit_scale=True, desc="Converting") as pbar:
        sound.export(mp3_name, format="mp3", progress_callback=lambda x, y: pbar.update(y - x))
    print("Converted to MP3!")

def download_and_convert(url, mp3_name):
    # Download the video and convert it to an mp3 file
    video_name = url.split("/")[-1] + ".mp4"
    download_video(url)
    convert_to_mp3(video_name, mp3_name)

def main():
    # Get the YouTube url from the user
    url = input("Enter the YouTube url: ")

    # Create the mp3 file name
    mp3_name = input("Enter the name for the mp3 file: ") + ".mp3"

    # Download and convert the video
    download_and_convert(url, mp3_name)

if __name__ == "__main__":
    main()