from stream_urls import playlist_urls, stream_url
from random import choice
from sys import exit as exit_program
from time import sleep
import vlc
import tkinter as tk
import threading

class MusicPlayer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.entry1 = tk.Entry(self)
        self.entry1["text"] = "Playlist or video url"
        self.entry1.pack(side="top")


        self.getinput = tk.Button(self, text="Stream video or Playlist(randomly)", fg="blue", command=self.get_entry1_input)
        self.getinput.pack(side="bottom")

        self.scale = tk.Scale(orient="vertical", from_=120, to=0, command=self.update_player)
        self.scale.pack(side="bottom")
        self.scale.set(30)

        self.pauseButton = tk.Button(text="Pause", bg="red", fg="white", command=self.pause)
        self.pauseButton.pack(side="left")

        self.unpauseButton = tk.Button(text="Unpause", bg="green", fg="white", command=self.unpause)
        self.unpauseButton.pack(side="right")

    def update_player(self, _value):
        try:
            _value = self.scale.get()
            player.audio_set_volume(_value)
        except:
            pass
    
    def pause(self):
        try:
            player.pause()
        except:
            pass

    def unpause(self):
        try:
            player.play()
        except:
            pass

    def get_entry1_input(self):
        entry1_input = self.entry1.get()
        print(entry1_input)
        threading.Thread(target=self.play_video, args=(entry1_input,), daemon=True).start()

    def play_video(self, youtube_url):
        Instance = vlc.Instance()
        Instance.log_unset()
        global player
        player = Instance.media_player_new()
        try:
            videos = playlist_urls(youtube_url)
            for i in range(len(videos)):
                video = choice(videos)
                print(video)
                videos.remove(video)
                streaming_url, info = stream_url(video)             
                Media = Instance.media_new(streaming_url)
                player.set_media(Media)
                player.play()
                while True:
                    if player.get_state() == 6:
                        break
                    else:
                        sleep(2)
                    
        except:
            streaming_url, info = stream_url(youtube_url)
            Media = Instance.media_new(streaming_url)
            Media.get_mrl()
            player.set_media(Media)
            player.play()
            while True:
                if player.get_state() == 6:
                    break
                else:
                    sleep(2)
            

if __name__ == "__main__":
    root = tk.Tk()
    Music_Player = MusicPlayer(master=root)

    root.title("Youtube Music Player")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 200
    height = 300
    root.geometry(f"{width}x{height}+{int(screen_width/2-width/2)}+{int(screen_height/2-height/2)}")

    Music_Player.mainloop()
    exit_program()
