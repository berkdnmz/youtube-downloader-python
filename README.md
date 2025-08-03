# 🎵 YouTube Video & Ses İndirici (Python + yt-dlp)

Bu proje, kullanıcıdan alınan bir YouTube bağlantısını kullanarak **video** veya **ses** formatında indirme işlemi gerçekleştiren bir komut satırı uygulamasıdır. Kullanıcıya indirme öncesi **kalite seçimi** sunar (video için çözünürlük, ses için bitrate).  
`yt-dlp` ve `ffmpeg` araçlarını kullanır.

## 🚀 Özellikler

- 📽️ YouTube videosu indirme (kalite seçilebilir: en iyi, 720p, 480p)
- 🎧 YouTube ses dosyası (MP3) indirme (kalite seçilebilir: 192 kbps, 128 kbps)
- 🗂️ Otomatik olarak `Downloads` klasörüne kaydeder
- ❌ Hatalı linklerde kullanıcı dostu hata mesajı verir
- ✅ `ffmpeg` ile dönüştürme işlemleri

## 🛠️ Gereksinimler

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/download.html) (örn: `C:\ffmpeg\bin\ffmpeg.exe` gibi bir path verilmelidir)

### Kurulum

```bash
pip install yt-dlp
```

### ffmpeg kurulumu

1. ffmpeg'i [buradan](https://ffmpeg.org/download.html) indirin.
2. `ffmpeg.exe` yolunu `FFMPEG_PATH` sabitine uygun şekilde belirtin:
   ```python
   FFMPEG_PATH = r'C:\ffmpeg\bin\ffmpeg.exe'
   ```

## 📦 Kullanım

Terminalde çalıştırın:

```bash
python main.py
```

### Adımlar:

1. Video mu ses mi indireceğinizi seçin.
2. Kalite seçimi yapın (örneğin 720p veya 192 kbps).
3. YouTube linkini girin.
4. Dosya `Downloads` klasörüne indirilir.

## 📁 Dosya Yapısı

```
.
├── Downloads/              # İndirilen dosyaların kaydedildiği klasör
├── main.py                 # Uygulama ana Python dosyası
├── .gitignore
└── README.md
```

## 📌 Notlar

- Video formatları ve kalite seçenekleri, `yt-dlp`’nin desteklediği formatlara göre ayarlanmıştır.
- Ses dosyaları `.mp3` formatında indirilir.

## 🧠 Öğrenilenler

- `yt-dlp` kullanımı ve özel `format` kodlarıyla kalite belirleme
- `ffmpeg` kullanarak ses dönüştürme
- `try-except` ile hataları yönetme
- `dict` ve kullanıcı menüleriyle Python CLI tasarımı

## 🪪 Lisans

Bu proje [Apache License 2.0](LICENSE) altında lisanslanmıştır.
Kodları kullanabilir, değiştirebilir ve ticari projelerde bile kullanabilirsiniz ancak kaynak belirtmeniz gerekmektedir.
Detaylar için LICENSE dosyasına bakabilirsiniz.


## 👤 Proje Sahibi

**Berk DÖNMEZ**

GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

Projeyle ilgili her türlü soru ve öneri için bana ulaşabilirsiniz.
