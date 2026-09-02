"""
PortPulse - A lightweight TCP and UDP port scanner built in Python.
"""

import socket

def scan_tcp(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        s.close()
        return result == 0
    except socket.error:
        return False

def scan_udp(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        # Надсилаємо порожній пакет для перевірки UDP
        s.sendto(b"", (target_ip, port))
        s.close()
        return True
    except socket.error:
        return False

def main():
    target = input("Введи IP-адресу або домен для сканування (наприклад, 127.0.0.1): ").strip()
    
    # Популярні TCP та UDP порти
    tcp_ports = [21, 22, 80, 443, 3306]
    udp_ports = [53, 123, 5353] # DNS, NTP, mDNS
    
    print(f"\n[+] Починаємо сканування цілі: {target}")
    print("=" * 40)
    
    print("--- TCP Порти ---")
    for port in tcp_ports:
        if scan_tcp(target, port):
            print(f" Порт {port}: ВІДКРИТИЙ")
        else:
            print(f" Порт {port}: закритий")
            
    print("\n--- UDP Порти ---")
    for port in udp_ports:
        if scan_udp(target, port):
            print(f" Порт {port}: ДОСТУПНИЙ / ВІДКРИТИЙ")
        else:
            print(f" Порт {port}: закритий")
            
    print("=" * 40)
    print("[+] Сканування завершено!")

if __name__ == "__main__":
    main()
