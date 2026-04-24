import socket
import requests
import dns.resolver

# -------------------------
# PORT SCANNER
# -------------------------
def port_scanner(target):
    print(f"\n[+] Scanning ports on {target}")
    ports = [21, 22, 80, 443, 3306, 8080]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")
        s.close()


# -------------------------
# IP LOOKUP
# -------------------------
def ip_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n[+] Domain: {domain}")
        print(f"[+] IP Address: {ip}")
    except:
        print("[-] Unable to resolve domain")


# -------------------------
# SUBDOMAIN FINDER (basic brute force)
# -------------------------
def subdomain_finder(domain):
    print(f"\n[+] Finding subdomains for {domain}")

    subdomains = ["www", "mail", "ftp", "test", "dev", "api"]

    for sub in subdomains:
        full = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full)
            print(f"[FOUND] {full} -> {ip}")
        except:
            pass


# -------------------------
# HTTP HEADER CHECKER
# -------------------------
def header_check(url):
    print(f"\n[+] Checking headers for {url}")

    try:
        res = requests.get(url, timeout=3)
        headers = res.headers

        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Strict-Transport-Security"
        ]

        for h in security_headers:
            if h in headers:
                print(f"[OK] {h} is present")
            else:
                print(f"[MISSING] {h} not found")

    except:
        print("[-] Request failed")


# -------------------------
# MENU
# -------------------------
def menu():
    print("\n===== SECURITY TOOL =====")
    print("1. Port Scanner")
    print("2. IP Lookup")
    print("3. Subdomain Finder")
    print("4. Header Security Check")
    print("5. Exit")


def main():
    while True:
        menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            target = input("Enter IP: ")
            port_scanner(target)

        elif choice == "2":
            domain = input("Enter domain: ")
            ip_lookup(domain)

        elif choice == "3":
            domain = input("Enter domain: ")
            subdomain_finder(domain)

        elif choice == "4":
            url = input("Enter URL (http/https): ")
            header_check(url)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
