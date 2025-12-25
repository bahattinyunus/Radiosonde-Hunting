import time
import random
import os
import sys

# Terminal Renk Kodları
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_header():
    header = f"""
{BLUE}{BOLD}
    ==========================================================
    |       RADIOSONDE-HUNTING TACTICAL COMMAND CENTER       |
    |                   STATUS: OPERATIONAL                  |
    ==========================================================
{RESET}"""
    print(header)

def simulate_data():
    sondes = [
        {"id": "RS41-V123", "alt": 28450, "lat": 41.0082, "lon": 28.9784, "rate": -4.2},
        {"id": "DFM-09-X2", "alt": 12400, "lat": 39.9334, "lon": 32.8597, "rate": -15.8},
        {"id": "RS41-W999", "alt": 32000, "lat": 40.6970, "lon": 39.5630, "rate": 5.1}
    ]
    
    while True:
        clear_screen()
        draw_header()
        
        print(f"{CYAN}{BOLD}[+] SCANNING FREQUENCIES (400.000 - 406.000 MHz)...{RESET}\n")
        
        print(f"{BOLD}{'SONDE ID':<15} {'ALTITUDE (m)':<15} {'LATITUDE':<12} {'LONGITUDE':<12} {'V. SPEED':<10}{RESET}")
        print("-" * 68)
        
        for sonde in sondes:
            # Rastgele dalgalanma simülasyonu
            sonde["alt"] += int(sonde["rate"] * 10)
            sonde["lat"] += random.uniform(-0.0001, 0.0001)
            sonde["lon"] += random.uniform(-0.0001, 0.0001)
            
            color = GREEN if sonde["alt"] > 5000 else RED
            status_icon = "🎈" if sonde["rate"] > 0 else "🪂"
            
            print(f"{status_icon} {BOLD}{sonde['id']:<12}{RESET} {color}{sonde['alt']:<15,}{RESET} {sonde['lat']:<12.4f} {sonde['lon']:<12.4f} {sonde['rate']:<10.1f} m/s")

        print(f"\n{BLUE}[i] Press Ctrl+C to exit Command Center.{RESET}")
        
        # Log simülasyonu
        print(f"\n{BOLD}[LOGS]{RESET}")
        logs = [
            "[INFO] RS41-V123: Burst detected at 32,450m",
            "[WARN] DFM-09-X2: Signal to Noise Ratio (SNR) dropping...",
            "[INFO] Station TR-OF: Telemetry synchronized."
        ]
        for log in logs:
            print(f"> {log}")
            
        time.sleep(2)

if __name__ == "__main__":
    try:
        simulate_data()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Command Center Terminated.{RESET}")
        sys.exit()
