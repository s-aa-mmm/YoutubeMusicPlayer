import random
import sys
import tkinter as tk
import threading
from stream_urls import playlist_urls, get_stream_url
from time import sleep
from music_player import MusicPlayer



class MusicPlayerUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg="black")
        self.master = master
        self.master.configure(bg="black")
        self.music_player = MusicPlayer()
        self.thread_count = 0
        self.pack(pady=10)
        self.create_widgets()


    def create_widgets(self):
        self.entry1 = tk.Entry(self, width=60)
        self.entry1.insert(0, "Enter URL to playlist or video")
        self.entry1.pack(side="top")

        self.play_button = tk.PhotoImage(file=r"ui_images/playButton.png").subsample(15, 15)
        self.getinput = tk.Button(self,
        image=self.play_button,
        highlightthickness=1,
        bd=1,
        background="blue", 
        activebackground="red", 
        command=lambda: self.controller("play_button"))
        self.getinput.pack(side="top")

        self.shuffle_button = tk.PhotoImage(file=r"ui_images/shuffleButton.png").subsample(15, 15)
        self.shuffle = tk.Button(self,
        image=self.shuffle_button,
        highlightthickness=1,
        bd=1,
        background="blue",
        activebackground="red",
        command=lambda: self.controller("shuffle"))
        self.shuffle.pack(side="top")

        self.volume_scale = tk.Scale(self, 
        fg="white", 
        orient="vertical", 
        from_=120, 
        to=0, 
        background="blue", 
        highlightthickness=0, 
        bd=0,
        activebackground="red",
        command=lambda vol_value: self.music_player.change_volume(int(vol_value)))
        self.volume_scale.pack(side="top")
        self.volume_scale.set(30)

        self.pauseButton = tk.Button(self, 
        text=" Pause ", 
        height=3,
        bg="red", 
        fg="white", 
        command=self.music_player.pause_song)
        self.pauseButton.pack(side="left")

        self.unpauseButton = tk.Button(self, 
        text="Unpause", 
        height=3,
        bg="green", 
        fg="white", 
        command=self.music_player.unpause)
        self.unpauseButton.pack(side="right")

        self.next_button = tk.PhotoImage(file=r"ui_images/nextButton.png").subsample(12, 12)
        self.next = tk.Button(self, 
        image=self.next_button,
        highlightthickness=1,
        bd=3,
        background="blue",
        activebackground="red", 
        command=lambda: self.controller("next"))
        self.next.pack(side="right")

        self.previous_button = tk.PhotoImage(file=r"ui_images/previousButton.png").subsample(12, 12)
        self.prev = tk.Button(self, 
        image=self.previous_button,
        highlightthickness=1,
        bd=3,
        background="blue",
        activebackground="red",
        command=lambda: self.controller("previous"))
        self.prev.pack(side="left")


    def controller(self, _commmand: str):
        self.cmd = _commmand
        if self.cmd == "next":
            self.music_player.stop_song()
            self.skip = True
        elif self.cmd == "previous":
            self.music_player.stop_song()
            self.previous = True
        elif self.cmd == "shuffle":
            threading.Thread(target=self.play_input, args=(True,), daemon=True).start()
            self.thread_count += 1
        elif self.cmd == "play_button":
            threading.Thread(target=self.play_input, args=(False,), daemon=True).start()
            self.thread_count += 1

    def play_input(self,  _shuffle: bool):
        self.source = self.entry1.get()
        self.shuffle_choice = _shuffle
        self.music_player.stop_song()
        self.urls_from_source = []
        if "playlist" in self.source:
            self.urls_from_source = self.urls_from_source + playlist_urls(self.source)
        else:
            self.urls_from_source.append(self.source)
        
        if self.shuffle_choice:
            self.playlist_order = random.sample(self.urls_from_source, len(self.urls_from_source))
        else:
            self.playlist_order = self.urls_from_source

        self.play_the_music(self.playlist_order)


    def play_the_music(self,  the_urls):
        if self.thread_count > 1:
            while not self.thread_count == 1: 
                sleep(0.55) 
        self.music_player.stop_song()
        self.future_songs = the_urls
        self.song_position = 0
        while not self.song_position > len(self.future_songs):
            try:
                self.song = self.future_songs[self.song_position]
            except:
                self.thread_count -= 1
                return
                # there are no more songs in the list!!!!!!!!!!!!!!!!!!!!!!!
            self.skip = False
            self.previous = False
            self.stream_url = get_stream_url(self.song)
            self.music_player.play_song(self.stream_url)
            while True:
                if self.skip:
                    break
                elif self.previous:
                    if self.song_position == 0:
                        self.song_position += 1
                    self.song_position -= 2
                    break
                elif self.music_player.musicplayer_state() == 6:
                    break
                elif self.thread_count > 1:
                    self.thread_count -= 1
                    return
                else:
                    sleep(0.5)
            self.song_position += 1


def main():
    root = tk.Tk()
    Music_Player = MusicPlayerUI(master=root)
    
    root.title("Youtube Music Player")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 400
    height = 290
    root.geometry(f"{width}x{height}+{int(screen_width/2-width/2)}+{int(screen_height/2-height/2)}")
    root.iconbitmap(r"ui_images/yt_player_ico.ico")
    root.resizable(False, False)

    Music_Player.mainloop()
    return


if __name__ == "__main__":
    main()
    sys.exit()
