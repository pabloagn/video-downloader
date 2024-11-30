import yt_dlp
import os
from config_reader import get_config

def download_video(url, output_directory):
    config = {
        # Prioritize combined; fallback to separate
        "format": "bestvideo+bestaudio/best",
        # Clean filenames
        "outtmpl": os.path.join(output_directory, "%(title)s.%(ext)s"),
        # Ensure output is in MP4
        "merge_output_format": "mp4",
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
    }

    with yt_dlp.YoutubeDL(config) as ydl:
        try:
            ydl.download([url])
            print(f"Successfully downloaded: {url}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")