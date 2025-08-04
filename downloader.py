# MIT License
# Copyright (c) 2025 Necati Berk DÖNMEZ

import sys #hatalı çıkışları yakalamak için

from yt_dlp import YoutubeDL #Youtube'dan ses ve video indirmek için kullancağımız kütüphane
import os #dosya işlemleri için

FFMPEG_PATH = r'C:\ffmpeg\bin\ffmpeg.exe' #kullancagımız ffmpeg in tam yolunu belirtiyoruz, kendinize göre ayarlayabilirsiniz ben C'ye kurmuştum. Ses ve video dosyalarını birleştirmek için gerekli

def video_indir(link : str, kalite : str):
    os.makedirs("Downloads", exist_ok=True) #indirilene kaydetmek için klasör oluşturuyoruz
    ydl_options = {
        'format': kalite,
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
        'ffmpeg_location': FFMPEG_PATH,
        'http_headers': { # YouTube bazen botlara izin vermez bu yüzden kendimizi Choreme tarayıcısı gibi gösteriyoruz
            'User-Agent': 'Mozilla/5.0 ...'
        }
    }

    with YoutubeDL(ydl_options) as ydl:
        ydl.download([link])
    print("Video başarıyla indirildi.")

def ses_indir(link : str, kalite : str, bitrate : str):
    os.makedirs("Downloads", exist_ok=True)
    ydl_options = {
        'format': kalite,
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
        'ffmpeg_location': FFMPEG_PATH,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': bitrate,
        }],
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 ...'
        }
    }

    with YoutubeDL(ydl_options) as ydl:
        ydl.download([link])
    print("Ses başarıyla indirildi.")

def link_sor():
    link = input("İndirmek istediğiniz YouTube linki: ")
    return link


def menu_goster():
    print("\n****************")
    print("1.Video Download")
    print("2.Audio Download")
    print("****************\n")

def menu_secimi_yap():
    secim = input("Yapmak istediginiz islemi seciniz : ").strip()
    return secim

def kalite_secim_menu(type : str):

    if type == "video":
        print("** Video kalitesini seçiniz **")
        print("1. En iyi (default)")
        print("2. 720p (Orta kalite)")
        print("3. 480p (Düşük kalite)")
        while True:
            try:
                secim = int(input("Seçiminiz (1-3): "))
                if 1 == secim:
                    return "best"
                elif 2 == secim:
                    return "bestvideo[height<=720]+bestaudio/best[height<=720]"
                elif 3 == secim:
                    return "bestvideo[height<=480]+bestaudio/best[height<=480]"
                else:
                    print("Hatalı Seçim. Tekrar deneyin")
                    continue
            except ValueError:
                print("Lütfen sadece rakam tuşlayınız.")
                continue
            except Exception as e:
                print(f"Bilinmeyen bir hata oluştu {type.__name__} - {e}")
                sys.exit(1)


    if type == "ses" :
        print("\n** Ses kalitesini seçiniz **")
        print("1. En iyi (default)")
        print("2. 192 kbps (Orta kalite)")
        print("3. 128 kbps (Düşük kalite)")

        kalite_map = {
            1: ("bestaudio/best", "192"),
            2: ("bestaudio[abr<=192]/bestaudio", "192"),
            3: ("bestaudio[abr<=128]/bestaudio", "128")
        }
        while True:
            try:
                secim = int(input("Seçiminiz (1-3): "))
                if secim in kalite_map:
                    return kalite_map[secim]
                else:
                    print("Hatalı Seçim. Tekrar deneyin")
            except ValueError:
                print("Lütfen sadece rakam tuşlayınız.")
            except Exception as e:
                print(f"Bilinmeyen bir hata oluştu {type(e).__name__} - {e}")


def video_kalitesi():
    kalite = kalite_secim_menu("video")
    return kalite

def ses_kalitesi():
    kalite, bitrate = kalite_secim_menu("ses")
    return kalite, bitrate

def baslat():
    while True:
        menu_goster()
        menu_secimi = menu_secimi_yap()

        try:
            link = link_sor()
            if menu_secimi == "1":
                kalite = video_kalitesi()
                video_indir(link, kalite)
            elif menu_secimi == '2':
                kalite, bitrate = ses_kalitesi()
                ses_indir(link, kalite, bitrate)
            else:
                print("Hatali bir giris yaptiniz. Tekrar Deneyin")
                continue
        except Exception as e :
            print(f"bilinmeyen bir hata oluştu : {type(e).__name__}{e}. Tekrar deneyin.")
            continue
        break


if __name__ == '__main__':
    baslat()


