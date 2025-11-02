# 📥 PDF Toplu İndirici

**Muhammet Baykara'nın web sitesi için özel olarak tasarlanmış PDF indirme aracı.**

Bu araç, [muhammetbaykara.com](https://muhammetbaykara.com) sitesindeki ders dökümanlarını otomatik olarak tespit edip toplu halde indirmenizi sağlar.

> ⚠️ **Önemli Not:** Bu script özellikle muhammetbaykara.com'un WordPress yapısına göre optimize edilmiştir. Diğer sitelerde çalışmayabilir.

## 🎯 Özellikler

- ✅ Otomatik PDF linki algılama
- ✅ Toplu indirme
- ✅ Düzenli dosya isimlendirme
- ✅ İndirme ilerlemesi takibi
- ✅ Hata yönetimi

## 📋 Gereksinimler

- Python 3.6 veya üzeri
- `requests` kütüphanesi
- `beautifulsoup4` kütüphanesi

## 🚀 Kurulum

### 1. Python'u Kurun

[Python'un resmi web sitesinden](https://www.python.org/downloads/) işletim sisteminize uygun sürümü indirip kurun.

### 2. Gerekli Kütüphaneleri Kurun

Terminal veya Komut İstemi'ni açın ve şu komutu çalıştırın:

```bash
pip install requests beautifulsoup4
```

### 3. Script'i İndirin

`pdf_indirici.py` dosyasını bilgisayarınıza kaydedin.

## 💻 Kullanım

### Yöntem 1: Doğrudan URL'den İndirme

```python
python pdf_indirici.py
```

Script çalıştırıldığında varsayılan olarak belirtilen URL'den PDF'leri indirir.

### Yöntem 2: Farklı Bir URL İçin

Script içindeki bu satırı düzenleyin:

```python
url = 'https://muhammetbaykara.com/2025/09/28/yazilim-kalite-guvencesi-ve-testi-2025-2026-guz/'
```

Veya Python kod içinde:

```python
from pdf_indirici import pdf_indir

# URL ile
pdf_indir('https://istediginiz-url.com')
```

### Yöntem 3: Bilgisayarınızdaki HTML Dosyasından

Eğer sayfayı HTML olarak kaydettiyseniz:

```python
from pdf_indirici import pdf_indir

pdf_indir('sayfa.html')
```

## 📁 Dosya Yapısı

İndirilen dosyalar şu şekilde organize edilir:

```
proje_klasoru/
├── pdf_indirici.py
└── indirilen_pdfler/
    ├── 1-Hafta-KaliteKonseptleri.pdf
    ├── 1-Yazilim-Muhendisliginde-Kalite.pdf
    ├── 2CevikYazilim.pdf
    └── ...
```

## 🔧 Özelleştirme

### İndirme Klasörünü Değiştirme

Script içinde bu satırı bulun ve değiştirin:

```python
download_folder = 'indirilen_pdfler'  # İstediğiniz klasör adını yazın
```

### İndirmeler Arasındaki Bekleme Süresini Ayarlama

Sunucuyu yormamak için varsayılan olarak her indirme arasında 1 saniye beklenir:

```python
time.sleep(1)  # Saniye cinsinden bekleme süresi
```

## ⚠️ Sorun Giderme

### "Module not found" Hatası

```bash
pip install requests beautifulsoup4
```

### "Permission Denied" Hatası

Windows'ta:
- Komut İstemi'ni Yönetici olarak çalıştırın

Linux/Mac'te:
```bash
sudo python3 pdf_indirici.py
```

### İndirme Başarısız Oluyor

- İnternet bağlantınızı kontrol edin
- URL'nin doğru olduğundan emin olun
- Bazı siteler bot erişimini engelleyebilir

## 🌐 Alternatif Yöntem: Tarayıcı Konsolu

Python kullanmak istemiyorsanız, tarayıcınızın konsolunu kullanabilirsiniz:

1. Sayfayı açın
2. **F12** tuşuna basın
3. **Console** sekmesine gidin
4. Şu kodu yapıştırın:

```javascript
document.querySelectorAll('a.pdfemb-viewer').forEach((link, index) => {
    setTimeout(() => {
        const a = document.createElement('a');
        a.href = link.href;
        a.download = link.textContent.trim() || `dokuman_${index + 1}.pdf`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }, index * 2000);
});
```

5. **Enter** tuşuna basın

## 📝 Örnek Çıktı

```
Toplam 8 PDF bulundu.
1/8 - İndiriliyor: 1-Hafta-KaliteKonseptleri.pdf
✓ İndirildi: 1-Hafta-KaliteKonseptleri.pdf
2/8 - İndiriliyor: 1-Yazilim-Muhendisliginde-Kalite.pdf
✓ İndirildi: 1-Yazilim-Muhendisliginde-Kalite.pdf
3/8 - İndiriliyor: 2CevikYazilim.pdf
✓ İndirildi: 2CevikYazilim.pdf
...
İşlem tamamlandı! Dosyalar 'indirilen_pdfler' klasöründe.
```

## ⚖️ Yasal Uyarı

Bu araç yalnızca eğitim amaçlıdır. İndirdiğiniz içeriklerin telif haklarına saygı gösterin ve yalnızca erişim izniniz olan kaynakları indirin.

## 🤝 Katkıda Bulunma

Geliştirme önerileri ve hata bildirimleri için lütfen iletişime geçin.

## 📞 Destek

Herhangi bir sorun yaşarsanız:
- Script'in en son sürümünü kullandığınızdan emin olun
- Hata mesajını tam olarak kopyalayın
- URL'nin erişilebilir olduğunu kontrol edin

## 📜 Lisans

Bu proje eğitim amaçlı geliştirilmiştir ve özgürce kullanılabilir.

---

**Son Güncelleme:** 2025
**Versiyon:** 1.0
