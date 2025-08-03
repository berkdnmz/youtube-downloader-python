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
            'User-Agent': 'Mozilla/5.0 ...'
        }
    }

    with YoutubeDL(ydl_options) as ydl:
        ydl.download([link])
    print("Video Downloaded.")

def ses_indir(link : str):
    os.makedirs("Downloads", exist_ok=True)
    ydl_options = {
        'format': 'bestaudio/best',
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
        'ffmpeg_location': FFMPEG_PATH,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 ...'
        }
    }

    with YoutubeDL(ydl_options) as ydl:
        ydl.download([link])
    print("Audio Downloaded.")

def link_sor():
    link = input("İndirmek istediğiniz YouTube linki: ")
    return link


def menu_goster():
    print("\n****************")
    print("1.Video Download")
    print("2.Audio Download")
    print("****************\n")

def menu_secimi_yap():
    secim = input("Yapmak istediginiz islemi seciniz : ")
    return secim

def baslat():
    while True:
        menu_goster()
        menu_secimi = menu_secimi_yap()

        try:
            link = link_sor()
            if menu_secimi == "1":
                video_indir(link)
            elif menu_secimi == '2':
                ses_indir(link)
            else:
                print("Hatali bir giris yaptiniz. Tekrar Deneyin")
                continue
        except Exception as e :
            print(f"bilinmeyen bir hata oluştu : {type(e).__name__}{e}. Tekrar deneyin.")
            continue
        break


if __name__ == '__main__':
    baslat()


