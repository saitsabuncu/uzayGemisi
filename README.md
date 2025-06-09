# 🚀 Uzaylı İstilası - Pygame Projesi

Bu proje, Python ve Pygame kullanılarak geliştirilen 2D klasik bir uzaylı istilası oyunudur. Oyuncu, uzay gemisini kontrol ederek gelen uzaylıları vurmaya çalışır. Seviye geçişleri, skor takibi ve görsel arayüz ile zenginleştirilmiş eğlenceli bir mini oyun.

---

## 🎮 Ekran Görüntüsü

![Oyun Ekranı](assets/screenshot.png) <!-- Görsel eklemediysen bunu sonra ekleyebilirsin -->

---

## 🔧 Özellikler

- 👾 Uzaylı filosu oluşturma ve çarpışma algılama
- 🚀 Oyuncu gemisi hareketleri (yukarı, aşağı, sağ, sol)
- 💥 Üç mermiyle ateş etme (orta, sağ, sol)
- 📈 Skor, seviye ve can bilgisi (Scoreboard)
- 🟥 Oyun başlatma ("Play") ve bitiş ("Game Over") butonları
- 🔁 Her seviye sonrası zorluk artışı
- ⌨️ P tuşuyla oyunu başlatma, Q ile çıkış

---

## 🛠️ Kurulum

### Gereksinimler
- Python 3.8+ (sen Python 3.13.1 kullanmışsın)
- Pygame kütüphanesi

### Kurulum Adımları
```bash
git clone https://github.com/saitsabuncu/uzayGemisi.git
cd uzayGemisi
pip install pygame
python alien_invasion.py
uzayGemisi/
### Dosya Yapısı

uzayGemisi/
│
├── alien.py
├── alien_invasion.py
├── bullet.py
├── button.py
├── game_stats.py
├── scoreboard.py
├── settings.py
├── ship.py
├── images/
│   ├── ship.png
│   └── alien.png
└── README.md
└── difficulty.py


###  Lisans

Bu proje kişisel öğrenim ve gelişim amacıyla yapılmıştır. Dilersen kaynak kodu inceleyebilir ve kendi oyunlarını geliştirmek için kullanabilirsin ✌️
### İlham

Bu proje, Eric Matthes'in Python Crash Course kitabındaki "Alien Invasion" oyun örneğinden ilham alınarak geliştirilmiştir.
