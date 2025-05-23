# playlist_downloader.py

import yt_dlp
import os
import re
from config_reader import get_config

def sanitize_filename(filename):
    """Remove special characters and normalize filename."""
    # Replace spaces and special chars with underscore
    filename = re.sub(r'[^\w\s-]', '', filename)
    # Replace multiple spaces/underscores with single underscore
    filename = re.sub(r'[-\s]+', '_', filename)
    return filename.strip('_')

def download_playlist(url, output_directory):
    config = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
        'merge_output_format': 'mkv',
        'ignoreerrors': True,  # Skip unavailable videos
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv',
        }],
        'outtmpl_na_placeholder': 'NA',  # For unavailable videos
        'extract_flat': False,  # Extract full info
        'quiet': False,
        'no_warnings': False,
        # Custom filename sanitization
        'outtmpl_na_placeholder': 'NA',
        'restrictfilenames': True,
        # Process each video in playlist
        'noplaylist': False,
        'yes_playlist': True
    }

    with yt_dlp.YoutubeDL(config) as ydl:
        try:
            # Download playlist
            result = ydl.download([url])
            print(f"Successfully processed playlist: {url}")
            return True
        except Exception as e:
            print(f"Error processing playlist {url}: {e}")
            return False

def read_playlist_urls(file_path):
    """Read playlist URLs from file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Playlist file not found: {file_path}")
    
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]