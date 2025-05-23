import argparse
import os
import time
import tomli
from url_reader import read_urls
from video_downloader import download_video
from output_writer import write_log
from config_reader import get_config
from playlist_downloader import download_playlist, read_playlist_urls

def get_project_root():
    """Get the root directory of the project."""
    # Since main.py is in src/, go up one level to get to project root
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    parser = argparse.ArgumentParser(description='Download videos from URLs or playlists')
    parser.add_argument('--mode', choices=['single', 'playlist'], required=True,
                      help='Download mode: single videos or playlist')
    args = parser.parse_args()

    try:
        # Get the absolute path to the project root (video-downloader directory)
        project_root = get_project_root()
        config = get_config()
        output_dir = config["directories"]["output_dir"]
        log_file = os.path.join(output_dir, "download_log.txt")

        if args.mode == 'single':
            input_file = os.path.join(project_root, "inputs", "target_videos.txt")
            urls = read_urls(input_file)
            for url in urls:
                try:
                    write_log(log_file, f"Processing URL: {url}\n")
                    download_video(url, output_dir)
                    write_log(log_file, f"Successfully downloaded: {url}\n")
                except Exception as e:
                    write_log(log_file, f"Failed to process URL {url}: {e}\n")
                time.sleep(5)
        
        elif args.mode == 'playlist':
            playlist_file = os.path.join(project_root, "inputs", "target_playlists.txt")
            playlists = read_playlist_urls(playlist_file)
            for playlist_url in playlists:
                try:
                    write_log(log_file, f"Processing playlist: {playlist_url}\n")
                    success = download_playlist(playlist_url, output_dir)
                    if success:
                        write_log(log_file, f"Successfully processed playlist: {playlist_url}\n")
                    else:
                        write_log(log_file, f"Failed to process playlist: {playlist_url}\n")
                except Exception as e:
                    write_log(log_file, f"Failed to process playlist {playlist_url}: {e}\n")
                time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()