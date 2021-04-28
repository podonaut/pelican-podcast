import os
from urllib import request
from io import BytesIO
from datetime import timedelta
#import mutagen
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.wave import WAVE
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
#from mutagen.oggtheora import OggTheora
from mutagen import MutagenError

class AudioResolve:
    def __init__(self, item):
        self.item = item
        self.r = None
        
        self.file = self.item.podcast
        self.ext = self.file.split('.')[-1].lower()
        
        self._audio = None
        
        if os.path.isfile(self.file):
            self.r = None
        elif self.file.startswith('http'):
            self.r = request.urlopen(self.file)
    
    def matchAudio(self, f):
        if 'wav' == self.ext or 'wave' == self.ext:
            return WAVE(f)
        elif 'mp3' == self.ext:
            return MP3(f)
        elif 'm4a' == self.ext:
            return MP4(f)
        elif 'flac' == self.ext:
            return FLAC(f)
        #elif 'ogg' == self.ext:
        #    return OggVorbis(f)
        else:
            raise Exception(f'Unsupported ext "{self.ext}"')
    
    def get_audio(self):
        if self.r is None:
            return self.matchAudio(self.file)
        else:
            try:
               size = 128
               filelike = BytesIO()
               while 1:
                   data = self.r.read(size)
                   size *= 2
                   filelike.seek(0, 2)
                   filelike.write(data)
                   filelike.seek(0)
                   try:
                       return self.matchAudio(filelike)
                   except MutagenError:
                       if not data:
                           raise
                       pass
            finally:
                self.r.close()
    
    @property
    def headers(self):
        return self.r.headers
    
    @property
    def audio(self):
        if self._audio is None:
            self._audio = self.get_audio()
        return self._audio                 

    @property
    def duration(self):
        return str(timedelta(seconds=round(self.audio.info.length)))     
    
    @property
    def length(self):
        if hasattr(self.item, 'length'):
            return self.item.length
        elif self.r is None:
            return os.stat(self.file).st_size
        else:
            return self.headers["Content-Length"]
            
    @property
    def mimetype(self):
        if hasattr(self.item, 'mimetype'):
            return self.item.mimetype
        elif self.r is None:
            if 'mp3' == self.ext or 'm4a' == self.ext:
                return 'audio/mpeg'
            elif 'wav' == self.ext or 'wave' == self.ext:
                return 'audio/x-wav'
            elif 'flac' == self.ext:
                return 'audio/flac'
            else:
                raise Exception(f'Unsupported ext "{self.ext}"')
        else:
            return self.headers["Content-Type"]
            
class itemss:
    def __init__(self, file):
        self.podcast = file
        #self.length = 12345
        #self.mimetype = 'audio/xmpeg'

items = itemss('https://archive.org/download/test_audio_20210428/test_audio.mp3')
a = AudioResolve(items)
print(a.length)
print(a.mimetype)
print(a.duration)

items = itemss('https://archive.org/download/test_audio_20210428/test_audio.wav')
a = AudioResolve(items)
print(a.length)
print(a.mimetype)
print(a.duration)

items = itemss('https://archive.org/download/test_audio_20210428/test_audio.flac')
a = AudioResolve(items)
print(a.length)
print(a.mimetype)
print(a.duration)

items = itemss('https://archive.org/download/test_audio_20210428/test_audio.m4a')
a = AudioResolve(items)
print(a.length)
print(a.mimetype)
print(a.duration)

# items = itemss('https://archive.org/download/test_audio_20210428/test_audio.ogg')
# a = AudioResolve(items)
# print(a.length)
# print(a.mimetype)
# print(a.duration)

items = itemss('pelican_podcast/tests/audio/test_audio.MP3')
a = AudioResolve(items)
print(a.length)
print(a.mimetype)
print(a.duration)


items = itemss('pelican_podcast/tests/audio/test_audio.wav')
a = AudioResolve(items)
print(a.length)
print(a.mimetype)
print(a.duration)

items = itemss('pelican_podcast/tests/audio/test_audio.flac')
a = AudioResolve(items)
print(a.length)
print(a.mimetype)
print(a.duration)

items = itemss('pelican_podcast/tests/audio/test_audio.m4a')
a = AudioResolve(items)
print(a.length)
print(a.mimetype)
print(a.duration)

# items = itemss('pelican_podcast/tests/audio/test_audio.ogg')
# a = AudioResolve(items)
# print(a.length)
# print(a.mimetype)
# print(a.duration)

# items = itemss('goc01.mp3')
# a = AudioResolve(items)
# print(a.length)
# print(a.mimetype)
# print(a.duration)
# 
# items = itemss('https://archive.org/download/gurucomedy/goc02.mp3')
# a = AudioResolve(items)
# print(a.length)
# print(a.mimetype)
# print(a.duration)
# 
# items = itemss('3342247-episode-i.mp3')
# a = AudioResolve(items)
# print(a.length)
# print(a.mimetype)
# print(a.duration)
# 
