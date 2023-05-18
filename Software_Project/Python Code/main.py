import os
import random
import pygame
import sys
import select

songs_dir = "./Playlist"


song_files = os.listdir(songs_dir)
 

while True:

 
 random.shuffle(song_files)
 pygame.mixer.init()

 for item in song_files:

    song_path = os.path.join(songs_dir, item)

   
    pygame.mixer.music.load(song_path)

    pygame.mixer.music.play()

    is_paused = False
    song_timer = 0
    max_timer = 30

    print("Enter :")
    print("1 to Pause")
    print("2 to Resume")
    print("3 for Next Song")
    print("4 to Quit the Playlist")

    while pygame.mixer.music.get_busy() or is_paused:
       
        if sys.stdin in select.select([sys.stdin], [], [], max_timer-song_timer)[0]:
           

            choice = input(" ")

            if choice == "1":
                if not is_paused:
                    # Pause the song
                    pygame.mixer.music.pause()
                    song_timer=pygame.mixer.music.get_pos()//1000
                    is_paused = True

            elif choice == "2":
                if is_paused:
                    # Unpause the song
                    pygame.mixer.music.unpause()
                    is_paused = False

            elif choice == "3":
            # Stop the current song and move to the next one
                pygame.mixer.music.stop()
                break
                
            elif choice == "4":
                # Stop the music and quit the program
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                exit()
           
        else :
            break
    print("Playing next song")
    print("")        
 pygame.mixer.quit()

     