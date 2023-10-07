## Python YouTube Video and Audio Downloader

This is a simple Python script for downloading YouTube videos and audio.

### How to use:

1. Install the `pytube` library: `pip install pytube`
2. Clone this repository: `git clone https://github.com/your-username/youtube-video-audio-downloader.git`
3. Navigate to the project directory: `cd youtube-video-audio-downloader`
4. Run the script: `python youtube_video_audio_downloader.py`

You will be prompted to enter the link to the YouTube video or audio that you want to download. Then, you will be prompted to select whether you want to download the video or audio.

### Selecting the video or audio stream:

Once you have selected the video or audio, you will be shown a list of available streams. Each stream has a different resolution or audio quality. You can select the stream that you want by entering its number.

### Downloading the video or audio:

Once you have selected the stream, the script will start downloading the video or audio. You will be able to see the progress of the download in the console.

### Example:

```python
Enter your link: https://www.youtube.com/watch?v=your_video_id
For Video enter 0
For Audio enter 1: 0
0 - <VideoStream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
1 - <VideoStream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">
Enter your choise: 1
Downloading ---------> Video Title.
Successful
```

### Note:

This script is for educational purposes only. Please do not download copyrighted material without permission.


To save this code as a README.md file, you can simply open a new text editor and paste the code into it. Then, save the file as `README.md` in the root directory of your project.
