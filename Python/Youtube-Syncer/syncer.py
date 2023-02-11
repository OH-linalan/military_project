"""
파이썬 유튜브 재생목록 매니저
ver 0.0.1
사용 library: 
    pytube
이름 규칙
    변수명은 앞글자 대문자
    함수명은 2글자 대문자(앞,중간)
    상수명은 전체 앞문자 대문자(단어 사이에는_이용)
"""
import pytube
import shutil
import os

Video_File_Path = './audio'
Config_File_Path = './config'

def DownLoad(Urls):
    pl=pytube.Playlist('https://www.youtube.com/playlist?list=PLY6G8AGWkx5D_NOH2JwwF25jg5-sgP4um')
    Updatedurls = pl.video_urls
    print('update checking...')
    i= len(Updatedurls)
    j=len(Urls)
    if(i==j):
        for Item in Updatedurls:
            if(Item in Urls==True):
                continue
            else:
                print('update video available...')
                break
        print('already synced...')
        CliInput()
    else:
        print('update video available...')
    print('update starting...')
    DirRmv()
    for Elements in Updatedurls:
        Y = pytube.YouTube(Elements)
        St = Y.streams.get_audio_only()
        print('downloading: '+Elements)
        St.download(Video_File_Path)
    print('sync complete!')
    ListWrite(Updatedurls)
def DirRmv():
    if(os.path.isdir(Video_File_Path)==True):
        shutil.rmtree(Video_File_Path)
        os.mkdir(Video_File_Path)
    else:
        os.mkdir(Video_File_Path)
def ListWrite(Urllist):
    f=open(Config_File_Path+'/urls.txt', 'w')
    for i in Urllist:
        f.write(i+'\n')
    f.close()
def ListRead():
    f=open(Config_File_Path+'/urls.txt', 'r')
    Naiveurls = f.readlines()
    Urls = list()
    for i in Naiveurls:
        Str = i.replace('\n',"")
        Urls.append(Str)
    f.close()
    return Urls
def CliInput():
    Cmd = input('$->')
    if(Cmd == 'sync'):
        DownLoad(ListRead())
print('Youtube playlist sync manager')
CliInput()