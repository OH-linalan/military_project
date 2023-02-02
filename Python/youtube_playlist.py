"""
파이썬 유튜브 재생목록 매니저
ver 0.0.1
사용 library: 
    pytube
    moviepy
"""
from pytube import YouTube
Download_folder = '\\workspace\\mili\Python\\videos'
yt = YouTube('https://www.youtube.com/watch?v=K4TOrB7at0Y')

titles = yt.title
stream = yt.streams.get_highest_resolution()
stream.download(Download_folder)