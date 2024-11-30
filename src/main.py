import os
import time
import tomli
from url_reader import read_urls
from video_downloader import download_video
from output_writer import write_log
from config_reader import get_config

def main():
    try:
        config = get_config()
        input_file = config["directories"]["input_file"]
        output_dir = config["directories"]["output_dir"]
        log_file = os.path.join(output_dir, "download_log.txt")

        urls = read_urls(input_file)
        for url in urls:
            try:
                write_log(log_file, f"Processing URL: {url}\n")
                download_video(url, output_dir)
                write_log(log_file, f"Successfully downloaded: {url}\n")
            except Exception as e:
                write_log(log_file, f"Failed to process URL {url}: {e}\n")

            # Avoid sending too many requests too quickly
            time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()