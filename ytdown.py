from pytube import YouTube
import sys

link = sys.argv[1]
yt = YouTube(link)
print("Title:", yt.title)
print("View:", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download(r"C:\Users\p_a_u\Documents\videofolder")

