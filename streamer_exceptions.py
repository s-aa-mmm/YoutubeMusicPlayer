class InvalidPlaylist(Exception):
    """Exception raised when invalid playlist url is passed through.

    Attributes:
        playlist -- the invalid playlist input
        message -- explanation of the error
    """

    def __init__(self, _playlist, message="Invalid Playlist"):
        self._playlist = _playlist
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'\n"{self._playlist}" -> {self.message}'
