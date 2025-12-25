#!/usr/bin/env python3
"""
Radiosonde-Hunting Live Data Fetcher
SondeHub API entegrasyonu ile canlı radiosonde verilerini çeker.
"""

import json
import sys
from datetime import datetime

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("[WARN] 'requests' modülü bulunamadı. Simülasyon modunda çalışılacak.")

# Terminal Renkleri
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

SONDEHUB_API = "https://api.v2.sondehub.org/sondes"

def fetch_live_data():
    """SondeHub API'den canlı radiosonde verilerini çeker."""
    if not REQUESTS_AVAILABLE:
        return simulate_data()
    
    try:
        print(f"{CYAN}[+] SondeHub API'ye bağlanılıyor...{RESET}")
        response = requests.get(SONDEHUB_API, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"{GREEN}[✓] {len(data)} radiosonde verisi alındı.{RESET}\n")
            return data
        else:
            print(f"{RED}[!] API Hatası: {response.status_code}{RESET}")
            return simulate_data()
    except Exception as e:
        print(f"{RED}[!] Bağlantı hatası: {e}{RESET}")
        return simulate_data()

def simulate_data():
    """API erişimi yoksa simüle edilmiş veri döndürür."""
    print(f"{YELLOW}[i] Simülasyon modunda çalışılıyor...{RESET}\n")
    return {
        "RS41-V12345": {
            "lat": 41.0082,
            "lon": 28.9784,
            "alt": 15420,
            "vel_v": -12.4,
            "temp": -45.2,
            "datetime": datetime.utcnow().isoformat()
        },
        "DFM-09-X999": {
            "lat": 39.9334,
            "lon": 32.8597,
            "alt": 28900,
            "vel_v": 5.8,
            "temp": -58.1,
            "datetime": datetime.utcnow().isoformat()
        }
    }

def display_data(sondes):
    """Radiosonde verilerini formatlı şekilde gösterir."""
    print(f"{BOLD}{'SONDE ID':<20} {'LAT':<12} {'LON':<12} {'ALT (m)':<12} {'V.SPD (m/s)':<15} {'TEMP (°C)':<10}{RESET}")
    print("-" * 90)
    
    for sonde_id, data in list(sondes.items())[:10]:  # İlk 10 sonuç
        lat = data.get('lat', 0.0)
        lon = data.get('lon', 0.0)
        alt = data.get('alt', 0)
        vel_v = data.get('vel_v', 0.0)
        temp = data.get('temp', 0.0)
        
        status_icon = "🎈" if vel_v > 0 else "🪂"
        color = GREEN if alt > 10000 else YELLOW
        
        print(f"{status_icon} {sonde_id:<18} {lat:<12.4f} {lon:<12.4f} {color}{alt:<12,}{RESET} {vel_v:<15.1f} {temp:<10.1f}")

def main():
    print(f"""
{BOLD}{CYAN}
╔══════════════════════════════════════════════════════════╗
║     RADIOSONDE-HUNTING LIVE DATA INTELLIGENCE SYSTEM     ║
╚══════════════════════════════════════════════════════════╝
{RESET}
    """)
    
    sondes = fetch_live_data()
    
    if sondes:
        display_data(sondes)
        print(f"\n{GREEN}[✓] Veri çekme işlemi tamamlandı.{RESET}")
    else:
        print(f"{RED}[!] Veri alınamadı.{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] İşlem kullanıcı tarafından iptal edildi.{RESET}")
        sys.exit(0)
