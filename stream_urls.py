from pytube import Playlist, YouTube
from pytube.exceptions import VideoPrivate, VideoRegionBlocked, VideoUnavailable, RegexMatchError
from streamer_exceptions import InvalidPlaylist



def playlist_urls(_playlist: str):
    try:
        plist = Playlist(_playlist)
        return plist.video_urls
    except KeyError:
        raise InvalidPlaylist(_playlist)


def get_stream_url(_video: str, info=False):
    """
    Returns streaming url
    _video = url to youtube video from which you want the streaming url
    info = True refers to returning dictionary styled data about url as well
    """
    try:
        yt_video = YouTube(_video)
        _stream_url = yt_video.streams.get_audio_only()
        if not info:
            return _stream_url.url  
        _video_info = {
            "title": yt_video.title,
            "author": yt_video.author,
            "description": yt_video.description,
            "length": yt_video.length,
            "publish_date": yt_video.publish_date,
            "rating": yt_video.rating,
            "thumbnail_url": yt_video.thumbnail_url,
            "views": yt_video.views,
            }
        return _stream_url.url, _video_info

    except RegexMatchError:
        print(f"\n'{_video}' --> Invalid Url")
    except VideoRegionBlocked:
        print(F"\n'{_video}' --> Region Blocked Video")
    except VideoPrivate:
        print(f"\n'{_video}' --> Private Video")
    except VideoUnavailable:
        print(f"\n'{_video}' --> Video Unavailable")
