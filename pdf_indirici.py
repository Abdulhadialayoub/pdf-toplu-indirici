import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import time

def pdf_indir(html_dosya_yolu_veya_url):
    """
    Muhammet Baykara'nın web sitesinden PDF dosyalarını bulup indirir
    Özel olarak muhammetbaykara.com için tasarlanmıştır
    """
    
    # HTML içeriğini oku
    if html_dosya_yolu_veya_url.startswith('http'):
        # Site kontrolü
        if 'muhammetbaykara.com' not in html_dosya_yolu_veya_url:
            print("⚠️  UYARI: Bu script sadece muhammetbaykara.com için optimize edilmiştir!")
            devam = input("Yine de devam etmek istiyor musunuz? (e/h): ").strip().lower()
            if devam != 'e':
                print("❌ İşlem iptal edildi.")
                return
        
        try:
            response = requests.get(html_dosya_yolu_veya_url, timeout=10)
            response.raise_for_status()
            html_content = response.text
            base_url = html_dosya_yolu_veya_url
        except Exception as e:
            print(f"❌ Sayfa yüklenirken hata: {str(e)}")
            return
    else:
        try:
            with open(html_dosya_yolu_veya_url, 'r', encoding='utf-8') as f:
                html_content = f.read()
            base_url = 'https://muhammetbaykara.com'
        except Exception as e:
            print(f"❌ Dosya okunamadı: {str(e)}")
            return
    
    # BeautifulSoup ile parse et
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Farklı yöntemlerle PDF linklerini bul (muhammetbaykara.com'a özel)
    pdf_links = []
    
    # Yöntem 1: pdfemb-viewer class'ı ile (siteye özel)
    pdf_links.extend(soup.find_all('a', class_='pdfemb-viewer'))
    
    # Yöntem 2: href'i .pdf ile biten tüm linkler
    all_links = soup.find_all('a', href=True)
    for link in all_links:
        href = link.get('href', '')
        if href.endswith('.pdf') and link not in pdf_links:
            pdf_links.append(link)
    
    # Yöntem 3: wp-content/uploads içindeki PDF'ler (WordPress'e özel)
    for link in all_links:
        href = link.get('href', '')
        if 'wp-content/uploads' in href and '.pdf' in href.lower():
            if link not in pdf_links:
                pdf_links.append(link)
    
    if not pdf_links:
        print("❌ Hiç PDF linki bulunamadı!")
        print("\n📝 Olası sebepler:")
        print("  • Sayfada PDF dosyası bulunmuyor olabilir")
        print("  • Sayfanın yapısı farklı olabilir")
        print("  • JavaScript ile yükleniyor olabilir")
        print("\nSayfadaki ilk birkaç link:")
        for link in all_links[:5]:
            print(f"  - {link.get('href', 'N/A')}")
        return
    
    # İndirme klasörü oluştur
    download_folder = 'indirilen_pdfler'
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    print(f"✅ Toplam {len(pdf_links)} PDF bulundu.")
    print()
    
    basarili = 0
    basarisiz = 0
    
    # Her PDF'i indir
    for i, link in enumerate(pdf_links, 1):
        try:
            pdf_url = link.get('href', '')
            
            # Tam URL oluştur
            if not pdf_url.startswith('http'):
                pdf_url = urljoin(base_url, pdf_url)
            
            # Dosya adını belirle
            dosya_adi = link.get_text(strip=True)
            if not dosya_adi:
                # URL'den dosya adını çıkar
                dosya_adi = pdf_url.split('/')[-1]
                if not dosya_adi.endswith('.pdf'):
                    dosya_adi = f"dokuman_{i}.pdf"
            elif not dosya_adi.endswith('.pdf'):
                dosya_adi = dosya_adi + '.pdf'
            
            # Geçersiz karakterleri temizle
            dosya_adi = "".join(c for c in dosya_adi if c.isalnum() or c in (' ', '-', '_', '.'))
            dosya_adi = dosya_adi.strip()
            
            dosya_yolu = os.path.join(download_folder, dosya_adi)
            
            # Dosya zaten varsa atla
            if os.path.exists(dosya_yolu):
                print(f"[{i}/{len(pdf_links)}] ⏭️  Zaten var: {dosya_adi}")
                basarili += 1
                continue
            
            print(f"[{i}/{len(pdf_links)}] 📥 İndiriliyor: {dosya_adi}")
            
            # PDF'i indir
            response = requests.get(pdf_url, stream=True, timeout=30)
            response.raise_for_status()
            
            with open(dosya_yolu, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            dosya_boyutu = os.path.getsize(dosya_yolu) / 1024
            print(f"     ✓ İndirildi ({dosya_boyutu:.1f} KB)")
            basarili += 1
            
            # Sunucuyu yormamak için kısa bir bekleme
            time.sleep(1)
            
        except Exception as e:
            print(f"     ✗ Hata: {str(e)}")
            basarisiz += 1
    
    print()
    print("=" * 60)
    print(f"🎉 İşlem tamamlandı!")
    print(f"   ✅ Başarılı: {basarili}")
    print(f"   ❌ Başarısız: {basarisiz}")
    print(f"   📁 Konum: '{download_folder}' klasörü")
    print("=" * 60)

# KULLANIM ÖRNEKLERİ:

# 1. Doğrudan URL'den indir
# pdf_indir('https://muhammetbaykara.com/2025/09/28/yazilim-kalite-guvencesi-ve-testi-2025-2026-guz/')

# 2. Bilgisayarınızdaki HTML dosyasından indir
# pdf_indir('sayfa.html')

if __name__ == "__main__":
    print("=" * 60)
    print("📥 PDF Toplu İndirici")
    print("=" * 60)
    print()
    print("Lütfen PDF'leri indirmek istediğiniz kaynağı seçin:")
    print("1. Web sitesi URL'si")
    print("2. Bilgisayarımdaki HTML dosyası")
    print()
    
    secim = input("Seçiminiz (1/2): ").strip()
    
    if secim == "1":
        url = input("\nWeb sitesi URL'sini girin: ").strip()
        if url:
            pdf_indir(url)
        else:
            print("❌ Geçerli bir URL girmediniz!")
    
    elif secim == "2":
        dosya_yolu = input("\nHTML dosyasının yolunu girin: ").strip()
        if dosya_yolu and os.path.exists(dosya_yolu):
            pdf_indir(dosya_yolu)
        else:
            print("❌ Dosya bulunamadı!")
    
    else:
        print("❌ Geçersiz seçim!")
