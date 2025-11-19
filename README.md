# mp3-downloader-from-youtube
A small proyect i made to get an audio from youtube and convert it into an mp3. To use it you must install:
pip install mutagen
pip install pytubefix
pip install python-ffmpeg

# How to use it
To use the program, place YouTube links in a text file inside the `data` folder. Each link should be on its own line (separate links with a newline / press Enter after each link). For example, create a file called `data/links.txt` and add one URL per line:

- https://www.youtube.com/watch?v=example1
- https://www.youtube.com/watch?v=example2

The program will read that file and download/convert each link to an MP3.
To use the program execute the main.py file.
Also, it works with youtube links and youtube music links.