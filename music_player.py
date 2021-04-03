import vlc
from time import sleep


class MusicPlayer:
    def __init__(self):
        self.vlc_instance = vlc.Instance("--no-xlib", "--input-repeat=-1")
        self.vlc_instance.log_unset()
        self.player = self.vlc_instance.media_player_new()

    def get_audio_delay(self):
        return self.player.audio_get_delay()

    def play_song(self, _song):
        self.song = self.vlc_instance.media_new(_song)
        self.player.set_media(self.song)
        self.player.play()

    def musicplayer_state(self):
        return self.player.get_state()

    def change_volume(self, _volume):
        self.player.audio_set_volume(_volume)    
    
    def pause_song(self):
        self.player.pause()

    def unpause(self):
        self.player.play()
    
    def stop_song(self):
        self.player.stop()
