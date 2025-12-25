# 🚀 Radiosonde-Hunting Kurulum Rehberi

Bu rehber, radiosonde takip sistemini sıfırdan kurmak için gereken tüm adımları içerir.

---

## 📋 Gereksinimler

### Donanım
- **RTL-SDR Dongle:** RTL2832U chipset (RTL-SDR v3/v4 önerilir)
- **Anten:** 400-406 MHz için optimize edilmiş (Dipol, J-Pole veya Yagi)
- **Bilgisayar:** Windows, Linux veya macOS

### Yazılım
- **Python:** 3.8 veya üzeri
- **Git:** Versiyon kontrolü için

---

## 🛠️ Adım 1: RTL-SDR Sürücülerini Kurma

### Windows
1. [Zadig](https://zadig.akeo.ie/) uygulamasını indirin.
2. RTL-SDR dongle'ı takın.
3. Zadig'i açın ve **Options → List All Devices** seçeneğini etkinleştirin.
4. Listeden **Bulk-In, Interface (Interface 0)** seçin.
5. Sürücü olarak **WinUSB** seçip **Replace Driver** butonuna tıklayın.

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install rtl-sdr librtlsdr-dev
```

### macOS
```bash
brew install librtlsdr
```

**Test:**
```bash
rtl_test
```
Çıktıda "Found Rafael Micro R820T tuner" gibi bir mesaj görmelisiniz.

---

## 📡 Adım 2: Dekodlama Yazılımlarını Kurma

### RS41 Tracker (Önerilen)
```bash
git clone https://github.com/rs1729/RS.git
cd RS/rs41
gcc rs41mod.c -lm -o rs41mod
```

### Auto-RX (Otomatik Takip)
```bash
git clone https://github.com/projecthorus/radiosonde_auto_rx.git
cd radiosonde_auto_rx
./install.sh
```

---

## 🐍 Adım 3: Python Bağımlılıklarını Kurma

Bu projedeki scriptleri çalıştırmak için:

```bash
pip install requests
```

---

## 🎯 Adım 4: İlk Takip

### Manuel Takip (SDR++)
1. [SDR++](https://github.com/AlexandreRouma/SDRPlusPlus/releases) indirin ve kurun.
2. Frekansı **402.000 - 405.000 MHz** aralığına ayarlayın.
3. Modülasyon: **FM** (bant genişliği: ~12 kHz)
4. Sinyal bulduğunuzda, RS41 Tracker ile dekode edin:
   ```bash
   rtl_fm -f 402.7M -s 15k - | ./rs41mod --ecc --crc
   ```

### Otomatik Takip (Auto-RX)
```bash
cd radiosonde_auto_rx
python3 auto_rx.py
```

---

## 📊 Adım 5: SondeHub Entegrasyonu

Canlı verileri çekmek için:
```bash
python fetch_sonde_data.py
```

Tactical Dashboard'u başlatmak için:
```bash
python dashboard.py
```

---

## 🔧 Sorun Giderme

### "rtl_test" çalışmıyor
- **Windows:** Zadig ile sürücü yeniden yükleyin.
- **Linux:** `sudo` ile çalıştırın veya udev kuralları ekleyin:
  ```bash
  sudo usermod -aG plugdev $USER
  ```

### Sinyal bulamıyorum
- Salınım saatlerini kontrol edin (00Z ve 12Z UTC).
- Anteninizi açık alana yerleştirin.
- [SondeHub](https://sondehub.org) üzerinden yakınınızdaki aktif radiosonde'ları kontrol edin.

---

## 📚 Ek Kaynaklar
- [SondeHub Tracker](https://sondehub.org)
- [RTL-SDR Blog](https://www.rtl-sdr.com)
- [RS41 Protocol Documentation](https://github.com/rs1729/RS)

---

© 2025 Radiosonde-Hunting | Bahattin Yunus ÇETİN
