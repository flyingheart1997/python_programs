# ****** Download Single Video ******

from pytube import YouTube

link = "https://www.youtube.com/watch?v=oUjb0V4XOW4"
# link = input("Enter video link : ")

youtube = YouTube(link)
# print(youtube.title)
# print(youtube.thumbnail_url)

video = youtube.streams.all()
vid = list(enumerate(video))
for i in vid:
    print(i)

stream = int(input("Enter : "))
video[stream].download()
print("successful")

# ****** Download Playlist Video ******

# from pytube import Playlist
# link = "https://www.youtube.com/playlist?list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl"
# # link = input("Enter video link : ")
#
# youtube = Playlist(link)
#
#
# for video in youtube.videos:
#     videos = video.streams.all()
#     vid = list(enumerate(videos))
#     for i in vid:
#         print(i)
#     stream = int(input("Enter : "))
#     videos[stream].download()
#     print("successful")
