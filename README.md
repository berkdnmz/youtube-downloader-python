# 🎬 YouTube Video / MP3 Downloader (Python + yt-dlp)

Bu proje, YouTube videolarını hem video formatında hem de sadece ses (MP3) formatında indirmek için geliştirilmiştir.  
Kullanıcıdan bağlantı alır, isteğe göre video veya sadece ses indirir.  
Basit ama güçlü bir araçtır.

## 🚀 Özellikler

- 📥 YouTube'dan **video** veya **sadece ses** (MP3) indirme
- ⚙️ `yt-dlp` ve `ffmpeg` entegrasyonu
- 📁 İndirilenler otomatik olarak `Downloads` klasörüne kaydedilir
- ✅ Hatalı bağlantılara karşı `try-except` kontrolü
- 👨‍💻 Komut satırı üzerinden kullanıcı dostu arayüz

## 🛠️ Gereksinimler

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/) (sisteme kurulu ve `PATH`'e ekli)

### Kurulum (Windows için örnek)

```bash
pip install yt-dlp
```

- ffmpeg'i [buradan](https://www.gyan.dev/ffmpeg/builds/) indirip `C:\ffmpeg` gibi bir klasöre çıkartın.
- `ffmpeg.exe` yolunu `.py` dosyasındaki `FFMPEG_PATH` değişkenine belirtin:
  ```python
  FFMPEG_PATH = r'C:\ffmpeg\bin\ffmpeg.exe'
  ```

## 📦 Dosya Yapısı

```
youtube_downloader/
│
├── downloader.py         # Ana Python scripti
├── .gitignore            # Gereksiz dosyaları hariç tutar
└── Downloads/            # İndirilen videolar ve mp3'ler
```

## ⚙️ Kullanım

```bash
python downloader.py
```

### Program akışı:

1. Kullanıcıdan bağlantı alınır
2. Menüden video mu, ses mi indirileceği seçilir
3. Dosya `Downloads/` klasörüne kaydedilir

## 💡 Örnek Ekran

```
****************
1.Video Download
2.Audio Download
****************

Yapmak istediginiz islemi seciniz : 2
İndirmek istediğiniz YouTube linki: https://www.youtube.com/watch?v=abc123

Audio Downloaded.
```

## 🧠 Öğrenim Notları

Bu proje aşağıdaki konuları pekiştirir:

- Fonksiyonel Python yazımı
- Kütüphane kullanımı (`yt_dlp`, `os`, `ffmpeg`)
- Hata yönetimi (`try-except`)
- Kullanıcıdan veri alma ve akış kontrolü

## Proje Sahibi

**Berk DÖNMEZ**

GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

Projeyle ilgili her türlü soru ve öneri için bana ulaşabilirsiniz.
