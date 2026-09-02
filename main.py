"""
PortPulse - A lightweight and simple TCP port scanner built in Python.
"""

import socket
import sys

def scan_port(target_ip, port):
    try:
        # Створюємо сокет
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        
        # Спробуємо підключитися до порту
        result = s.connect_ex((target_ip, port))
        s.close()
        
        return result == 0
    except socket.error:
        return False

def main():
    target = input("Введи IP-адресу або домен для сканування (наприклад, 127.0.0.1): ").strip()
    
    # Базовий список найпопулярніших портів для перевірки
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 443, 8080, 3306]
    
    print(f"\n[+] Починаємо сканування цілі: {target}")
    print("-" * 40)
    
    open_ports = []
    
    for port in ports_to_scan:
        if scan_port(target, port):
            print(f" Порт {port}: ВІДКРИТИЙ")
            open_ports.append(port)
        else:
            print(f" Порт {port}: закритий")
            
    print("-" * 40)
    print(f"[+] Сканування завершено. Знайдено відкритих портів: {len(open_ports)}")

if __name__ == "__main__":
    main()
