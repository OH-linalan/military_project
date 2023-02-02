"""
파이썬 유튜브 재생목록 매니저
ver 0.0.1
사용 library: 
    pytube
    moviepy
"""
from pytube import *
def downloading(pl_url, url_lists):
    p = Playlist(pl_url)
    for url() in p.video_urls():
        if url() in url_lists:
            continue
        else:
            Y = YouTube(url())
            stream = Y.streams.get_highest_resolution()
            stream.download('\\videos')
            url_lists.append(url())
    return url_lists

f = open('url.txt','r')
url_lists = f.readlines()
f.close()
pl_urls = 'https://www.youtube.com/playlist?list=PLY6G8AGWkx5D_NOH2JwwF25jg5-sgP4um'
f = open('url.txt','a')
temp() = downloading(pl_urls, url_lists)
f.truncate(0)
for elements in temp():
    f.write(elements)
f.close()
