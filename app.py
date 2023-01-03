
while(True):
    print("What do you wish to convert?\n\n1. Youtube song\n2. Youtube playlist")
    choice = input(">> ")
    if(choice =="1"):
        print("Nothing for noww")
        break
    elif(choice =="2"):
        from lib.youtube_playlist import converter as yt_playlist_converter
        yt_playlist_converter()
        break
    else:
        print("Wrong input Try Again")
        