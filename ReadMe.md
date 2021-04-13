# Youtube Music Player 
Made with Python + Tkinter and a couple of other default modules (check [requirements.txt](https://github.com/s-aa-mmm/YoutubeMusicPlayer/blob/main/requirements.txt))

# Features:
1. Simple UI that contains basic music player functions such as pause, unpause, volume, previous/next song for videos/playlists on youtube
2. Global key binds which can be configured in "MusicPlayerConfig.txt" after running the main.py the config file will be created 
3. The volume and music entry are automatically saved after the program is closed

# To Do:
**Basic functionality reached, development of this project will be slowed**
> - [x] Improve code 
> - [x] Previous/Next song button
> - [x] Key bindings to next, previous, pause, play, etc buttons
> - [ ] Add played youtube video information to UI
> - [x] Load data from previous sessions / + configuration file
> - [ ] Download song being played
> - [ ] Slider to move to certain time on audio of video
> - [ ] Better UI

# Usage:
### Warning: all files must be in the same directory for the music player to work
1. Download [python](https://www.python.org/)
2. Download [VLC-player](https://www.videolan.org/vlc/index.en_GB.html)
3. Download the [repository](https://github.com/s-aa-mmm/YoutubeMusicPlayer)
4. Install modules listed in ['requirements.txt'](https://github.com/s-aa-mmm/YoutubeMusicPlayer/blob/main/requirements.txt)
5. Then from terminal you can do **'python3 main.py'** or you can double click the **'main.py'** [file](https://github.com/s-aa-mmm/YoutubeMusicPlayer/blob/main/main.py)
6. From there you can configure the MusicPlayerConfig.txt which stores all the key binds and is created after you run the file for the first time
7. The PlayerSession.session file stores volume and last user youtube url entry 
8. The keybinds configured in MusicPlayerConfig.txt are global and therefore work even without the music player interface in focus

# Image of UI:
![alt text](https://github.com/s-aa-mmm/YoutubeMusicPlayer/blob/main/screenshots/ui_screenshot.jpg)
