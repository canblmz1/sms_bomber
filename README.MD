# 📱 SMS Bomber (Eğitim Amaçlı)

> **UYARI:** Bu proje tamamen eğitim ve kişisel geliştirme amaçlıdır. Gerçek SMS gönderimi için bir servis sağlayıcısına (Twilio, Turkcell vb.) API entegrasyonu yapılması gerekmektedir. Kötüye kullanım veya yasal olmayan işlemlerden geliştirici sorumlu değildir!

---

## 🚀 Özellikler

- 📲 Belirtilen numaraya toplu SMS gönderme (simülasyon)
- 📊 Canlı gönderim durumu ve istatistikler (başarılı/başarısız)
- 🖥️ Kullanıcı dostu arayüz
- 🕵️‍♂️ Flask ile kolay kurulum ve çalışma

## ⚙️ Kurulum

```bash
# 1. Projeyi klonla
git clone https://github.com/yourusername/sms-bomber.git
cd sms-bomber

# 2. Gerekli paketleri yükle
pip install -r requirements.txt

# 3. Çalıştır
python app.py
```

---

## 📝 Kullanım

1. Tarayıcıda `http://localhost:5000` adresine git.
2. Telefon numarası, mesaj ve SMS adedini gir.
3. **Başlat** butonuna tıkla.
4. Gönderim durumunu panelden takip et.

---

## 🛠️ Gerçek SMS Göndermek İçin

> **Not:** Proje şu anda gerçek SMS göndermez, sadece simülasyon yapar.
>
> Gerçek SMS için:
>
> - Twilio, Turkcell, Vodafone veya başka bir API entegrasyonu gerekir.
> - `send_sms` fonksiyonunu sağlayıcının dökümantasyonuna göre güncellemelisin.

---

## 🌟 Katkıda Bulunmak

PR’lar ve öneriler memnuniyetle karşılanır!  
Lütfen önce bir issue açmayı unutma.

---

## 📄 Lisans

MIT Lisansı

---

<div align="center">
  <img src="https://img.shields.io/github/stars/canblmz1/sms_bomber?style=social">
  <img src="https://img.shields.io/github/forks/canblmz1/sms_bomber?style=social">
  <br>
  <b>🚫 Sorumluluk Reddi: Yasal olmayan kullanım tamamen kullanıcının sorumluluğundadır.</b>
</div>
