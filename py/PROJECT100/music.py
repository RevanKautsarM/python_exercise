import pygame, sys, time
from threading import Thread, Lock

lock = Lock()


def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("In my dream", 0.18),
        ("You with me", 0.13),
        ("\n""Will be everything i want us to be", 0.09),
        ("And from there... who knows?", 0.12), 
        ("Maybe this will be the night that we kiss", 0.12),
        ("For the first time", 0.13),
        ("Or it was just me and my", 0.15),
        ("Imagination", 0.2),



    ]
    delays = [0.3, 2.5, 2.8, 3.0, 3.4, 3.6, 4.0, 4.3]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()

sound = pygame.mixer.Sound('imagination.wav')
sound.play()