# 🛰️ Radiosonde Hardware Deep Dive

Bu döküman, atmosfere salınan radiosonde cihazlarının teknik özelliklerini ve bu sinyalleri yakalamak için gereken donanım optimizasyonlarını içerir.

## 🛠️ Yaygın Radiosonde Modelleri

### 1. Vaisala RS41-SG / RS41-SGP
- **Frekans Aralığı:** 400 - 406 MHz
- **Modülasyon:** GFSK (4800 baud)
- **Özellikler:** Günümüzde en yaygın kullanılan modeldir. Yüksek hassasiyetli GPS ve sıcaklık sensörlerine sahiptir.
- **Batarya:** 2x AA Lityum.

### 2. Vaisala RS92-SGP
- **Frekans Aralığı:** 400 - 406 MHz
- **Modülasyon:** GFSK / FSK (Eski modellerde analog FM)
- **Özellikler:** Daha eski bir teknolojidir, dijital olanları dekodlamak RS41'e göre biraz daha karmaşıktır.

### 3. Graw DFM (DFM-06 / DFM-09 / DFM-17)
- **Frekans Aralığı:** 400 - 406 MHz
- **Modülasyon:** FSK (2500 baud)
- **Özellikler:** Alman yapımıdır. RS41'e göre daha dar bant genişliği kullanır.

---

## 📡 SDR Optimizasyonu ve Anten Seçimi

Radiosonde avcılığında sinyal kalitesi (SNR) hayati önem taşır. Cihaz 30km yüksekteyken sinyali almak kolaydır, ancak inişe geçtiğinde ve ufuk çizgisinin altına düştüğünde işler zorlaşır.

### 🚀 RTL-SDR Ayarları
- **Gain (Kazanç):** Genellikle 30-40 dB arası idealdir. Aşırı kazanç gürültü tabanını yükseltir.
- **PPM Correction:** Eski RTL-SDR cihazlarda sıcaklık değişimine bağlı frekans kaymasını düzeltmek için gereklidir (v3/v4 modellerinde genellikle 0-1 PPM'dir).

### 📐 Anten Tavsiyeleri
1. **Vertical Dipole:** En basit ve etkili başlangıç anteni.
2. **Turnstile Anten:** Gökyüzünden gelen sinyalleri (zirve noktasına yakınken) yakalamak için mükemmeldir.
3. **Yagi (3-5 Element):** Sadece cihazın düştüğü son anlarda, sinyalin zayıfladığı durumlarda yönlü takip için kullanılır.

---

## 💻 Dekodlama Algoritmaları

| Cihaz | Protokol | Baud Rate | Durum |
| :--- | :--- | :--- | :--- |
| **RS41** | Digital GFSK | 4800 | Tam Destek |
| **DFM** | Digital FSK | 2500 | Tam Destek |
| **M10/M20** | Digital | 9600 | Kısmi Destek |

> [!IMPORTANT]
> Sinyal yakalarken **Center Frequency**'nin tam ortalandığından emin olun. GFSK modülasyonunda frekans kayması (offset) dekodlamayı bozabilir.

---
© 2025 Radiosonde-Hunting | Bahattin Yunus ÇETİN
