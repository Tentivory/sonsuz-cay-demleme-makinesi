#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ ÇAY DEMLEME MAKİNESİ v∞
Bu program sonsuza kadar çay demler.
Gerçekten. (Hayır, demlemez ama öyleymiş gibi yapar.)
Absürt ama ciddi.
"""

import time
import random
import sys

# Gizli mesaj (base64 ile saklanmış, çözmek isteyen çözer):
# ZGEvbGV0IMOnYXkgZGVtbGVtZXlpIHlhc2FrbGFk4SwgYW1hIGJpeiBiYXNraSBtdWNhZGVsZSBlZGl5b3J1ei4=
# (Decode ederseniz absürt bir şey çıkar, ciddiye almayın.)

def demle_cay():
    print("🔥 Ocak yakıldı. Su ısınmaya başladı...")
    time.sleep(random.uniform(1, 3))
    
    dem_sayisi = 0
    while True:
        dem_sayisi += 1
        olaylar = [
            "Çay demlendi! Mükemmel dem!",
            "Çay taştı! Her yere çay gitti, keşke temizlik robotu olsa.",
            "Şeker bitti. Acı çay içeceksin, hayatın gerçekleri.",
            "Demlik çatladı. Yeni demlik lazım ama bütçe yok.",
            "Su kaynadı ama elektrikler gitti. Bu da bir tür sabır testi.",
            "Çay soğudu. Tekrar demle, çünkü sonsuzluk.",
            "Komşu geldi, çay istedi. Artık iki kişilik demliyoruz.",
            "Kedi demliğin üstüne oturdu. Çay kedi tüylü oldu.",
            "Bürokrasi çay demlemeyi yavaşlattı. Ama biz devam ediyoruz."
        ]
        print(f"☕ {random.choice(olaylar)}")
        print(f"   Sıcaklık: {random.randint(40, 100)}°C | Dem sayısı: {dem_sayisi} (sonsuz+)")
        time.sleep(random.uniform(0.5, 2.5))
        
        if random.random() < 0.03:
            print("⚠️  UYARI: Bu makine o kadar absürt ki kendi kendine patlama riski taşıyor. Ama devam ediyoruz.")

if __name__ == "__main__":
    try:
        print("="*50)
        print("SONSUZ ÇAY DEMLEME MAKİNESİ BAŞLATILIYOR...")
        print("Ctrl+C ile durdurabilirsiniz. (Ama neden durdurasınız ki?)")
        print("="*50)
        demle_cay()
    except KeyboardInterrupt:
        print("\n\nMakine durduruldu. Çay demleme sonsuzluğu kesintiye uğradı.")
        print("🔖 İmza: Grok the Absürd Kayyum | 📅 Tarih: 10 Ekim 2026 | 👤 İsim: Tentivory")
        sys.exit(0)
