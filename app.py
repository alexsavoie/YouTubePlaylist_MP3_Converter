
while(True):
    print("What do you wish to convert?\n\n1. Youtube song\n2. Youtube playlist")
    choice = input(">> ")
    if(choice =="1"):
        #from lib.youtube_song import converter
        #converter()
        break
    elif(choice =="2"):
        from lib.youtube_playlist import converter
        converter()
        break
    else:
        print("Wrong input Try Again")
        