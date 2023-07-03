#YoutubeVideoDowloader
from pytube import YouTube
from sys import argv



class video:
    
    def __init__(self,name,views):
        self.name=name
        self.views=views

def main():
    link = argv[1]
    yt=YouTube(link)
    print(yt.name,yt.views)
if __name__ == '__main__':
    main()