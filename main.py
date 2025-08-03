from yt_dlp import YoutubeDL #Youtube'dan ses ve video indirmek için kullancağımız kütüphane
import os #dosya işlemleri için

FFMPEG_PATH = r'C:\ffmpeg\bin\ffmpeg.exe' #kullancagımız ffmpeg in tam yolunu belirtiyoruz, kendinize göre ayarlayabilirsiniz ben C'ye kurmuştum. Ses ve video dosyalarını birleştirmek için gerekli

def video_indir(link : str):
    os.makedirs("Downloads", exist_ok=True) #indirilene kaydetmek için klasör oluşturuyoruz
    ydl_options = {
        'format': 'best',
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
        'ffmpeg_location': FFMPEG_PATH,
        'http_headers': { # YouTube bazen botlara izin vermez bu yüzden kendimizi Choreme tarayıcısı gibi gösteriyoruz
            'User_Agent': 'Mozilla/5.0 ...'
        }
    }

    with YoutubeDL(ydl_options) as ydl:
        ydl.download([link])
    print("Video Download.")

