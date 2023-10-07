import pytube
from pytube import YouTube 

# YouTube link

link = input("Enter your link: ")
yt_video = YouTube(link)
# yt_chanel = Channel(link)
# YouTube file type
type_of_video = int(input("For Video enter 0\nFor Audio enter 1: "))

if type_of_video == 0:
    yt_streams = yt_video.streams.filter(only_video=True)
    yt_strms_list = list(enumerate(yt_streams))
    for i in yt_strms_list:
        print(i)
    
    # chose streams
    stream_sel = int(input("Enter your choise: "))
    print(f"Downloading ---------> {yt_video.title}. ")
    yt_streams[stream_sel].download()
    print("Successful")

elif type_of_video == 1:
    yt_streams = yt_video.streams.filter(only_audio=True)
    yt_strms_list = list(enumerate(yt_streams))
    for i in yt_strms_list:
        print(i)
    
    # chose streams
    stream_sel = int(input("Enter your choise: "))

    print(f"Downloading ---------> {yt_video.title}.")
    yt_streams[stream_sel].download()
    print("Successful")

