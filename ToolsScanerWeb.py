import socket
import requests
import re
import time
import os

# Clear the terminal
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Define color codes
RESET = "\x1b[0m"
HEADER = "\x1b[38;5;33m"  # Blue
HIGHLIGHT = "\x1b[38;5;196m"  # Red
SUCCESS = "\x1b[38;5;46m"  # Green
INFO = "\x1b[38;5;220m"  # Yellow
DIM = "\x1b[38;5;240m"  # Dim Grey

# Print header logo
print(INFO + "━" * 60 + RESET)
logo = f"""
{HEADER}88888888888 .d88888b.   .d88888b.  888      .d8888b.        .d8888b.   .d8888b.        d8888 888b    888 
    888    d88P" "Y88b d88P" "Y88b 888     d88P  Y88b      d88P  Y88b d88P  Y88b      d88888 8888b   888 
    888    888     888 888     888 888     Y88b.           Y88b.      888    888     d88P888 88888b  888 
    888    888     888 888     888 888      "Y888b.         "Y888b.   888           d88P 888 888Y88b 888 
    888    888     888 888     888 888         "Y88b.          "Y88b. 888          d88P  888 888 Y88b888 
    888    888     888 888     888 888           "888            "888 888    888  d88P   888 888  Y88888 
    888    Y88b. .d88P Y88b. .d88P 888     Y88b  d88P      Y88b  d88P Y88b  d88P d8888888888 888   Y8888 
    888     "Y88888P"   "Y88888P"  88888888 "Y8888P"        "Y8888P"   "Y8888P" d88P     888 888    Y888 

{SUCCESS}Y88b   d88P  .d8888b.            .d8888b.   .d8888b.  888             
 Y88b d88P  d88P  Y88b          d88P  Y88b d88P  Y88b 888             
  Y88o88P   Y88b.               888    888 888    888 888             
   Y888P     "Y888b.    .d8888b 888    888 888    888 888888 88888888 
   d888b        "Y88b. d88P"    888    888 888    888 888       d88P  
  d88888b         "888 888      888    888 888    888 888      d88P   
 d88P Y88b  Y88b  d88P Y88b.    Y88b  d88P Y88b  d88P Y88b.   d88P    
d88P   Y88b  "Y8888P"   "Y8888P  "Y8888P"   "Y8888P"   "Y888 88888888 

{RESET}"""
print(logo)
print(INFO + "━" * 60 + RESET)

print(f"{HIGHLIGHT}[+] Facebook: XSc00tz{RESET}")
print(f"{HIGHLIGHT}[+] GitHub: https://github.com/The1975z{RESET}")
print(f"{SUCCESS}[+] VERSION: 1.2{RESET}")
print(f"{INFO}[+] This Tool extracts sensitive information like IP addresses, open ports, DNS records, etc.{RESET}")
print(DIM + "-" * 60 + RESET)

# Pause before proceeding
time.sleep(2)

# Define color variables for later use
xxh = "\x1b[38;5;208m"  # Orange
C = SUCCESS
B = HIGHLIGHT
D = INFO
E = HEADER
F = RESET
m1 = HIGHLIGHT

# Map of common ports and services
PORT_SERVICE_MAP = {
    20: "FTP Data", 21: "FTP Control", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 8080: "HTTP Alt",
}

def get_open_ports(target_ip):
    open_ports = []
    for port in range(1, 1024):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((target_ip, port)) == 0:
                open_ports.append(port)
                print(f"{C}Port: {port} - Service: {get_port_service(port)}{F}")
    return open_ports

def get_port_service(port):
    return PORT_SERVICE_MAP.get(port, "Unknown Service")

def get_dns_info(target_ip):
    try:
        hostname = socket.gethostbyaddr(target_ip)[0]
        dns_servers = socket.gethostbyname_ex(hostname)[2]
        return {"hostname": hostname, "ip_address": target_ip, "dns_servers": dns_servers}
    except Exception as e:
        return {"error": f"Failed to get DNS info: {str(e)}"}

def get_whois_info(target_ip):
    try:
        response = requests.get(f"https://whois.domaintools.com/{target_ip}")
        whois_info = re.findall(r"(\+): (.+)", response.text)
        return dict(whois_info)
    except Exception as e:
        return {"error": f"Failed to get WHOIS info: {str(e)}"}

def get_geoip_info(target_ip):
    try:
        response = requests.get(f"https://ipinfo.io/{target_ip}/json")
        geo_info = response.json()
        return {
            "ip": geo_info.get('ip', 'N/A'),
            "city": geo_info.get('city', 'N/A'),
            "region": geo_info.get('region', 'N/A'),
            "country": geo_info.get('country', 'N/A'),
            "location": geo_info.get('loc', 'N/A'),
            "org": geo_info.get('org', 'N/A')
        }
    except Exception as e:
        return {"error": f"Failed to get GeoIP info: {str(e)}"}

def get_domain_registration_info(domain):
    try:
        response = requests.get(f"https://api.whoisxmlapi.com/v1/whoisserver/WhoisService?domainName={domain}&apiKey=YOUR_API_KEY&outputFormat=JSON")
        data = response.json()
        registrar = data.get('WhoisRecord', {}).get('registrarName', 'N/A')
        registrant_country = data.get('WhoisRecord', {}).get('registryData', {}).get('registrant', {}).get('country', 'N/A')
        return {"registrar": registrar, "country": registrant_country}
    except Exception as e:
        return {"error": f"Failed to get domain registration info: {str(e)}"}

def get_additional_info(target_ip):
    try:
        response = requests.get(f"https://api.hackertarget.com/whoisapi/?q={target_ip}")
        additional_info = response.json()
        return {
            "creation_date": additional_info.get('created', 'N/A'),
            "programming_language": additional_info.get('language', 'N/A'),
            "server_info": additional_info.get('server', 'N/A'),
        }
    except Exception as e:
        return {"error": f"Failed to get additional info: {str(e)}"}

def check_waf(target_url):
    try:
        response = requests.get(target_url)
        headers = response.headers
        if 'Server' in headers and 'WAF' in headers['Server']:
            print(f"{C}✅ WAF Detected: {headers['Server']}{F}")
        else:
            print(f"{B}❌ No WAF Detected{F}")
    except Exception as e:
        print(f"{B}Error checking WAF: {str(e)}{F}")

def check_sql_injection(target_url): # and payload
    payload = "' OR '1'='1"
    try:
        response = requests.get(f"{target_url}/?id={payload}")
        if "SQL" in response.text or "error" in response.text.lower():
            print(f"{C}✅ Potential SQL Injection vulnerability detected on {target_url}{F}")
        else:
            print(f"{B}❌ No SQL Injection vulnerability found on {target_url}{F}")
    except Exception as e:
        print(f"{B}Error checking SQL Injection: {str(e)}{F}")

def main():
    target_url = input(xxh + "Enter the Website URL: " + C)
    print(m1 + "Fetching information, please wait...")
    time.sleep(1)

    # replace https และ http
    domain = target_url.replace("http://", "").replace("https://", "").strip("/")
    target_ip = socket.gethostbyname(domain)

    print(f"{D}--- Open Ports ---{F}")
    open_ports = get_open_ports(target_ip)

    print(f"\n{D}--- DNS Information ---{F}")
    dns_info = get_dns_info(target_ip)
    if "error" in dns_info:
        print(f"{B}{dns_info['error']}{F}")
    else:
        print(f"{C}Hostname: {dns_info['hostname']}{F}")
        print(f"{C}IP Address: {dns_info['ip_address']}{F}")
        print(f"{C}DNS Servers: {', '.join(dns_info['dns_servers'])}{F}")

    print(f"\n{D}--- WHOIS Information ---{F}")
    whois_info = get_whois_info(target_ip)
    if "error" in whois_info:
        print(f"{B}{whois_info['error']}{F}")
    else:
        for key, value in whois_info.items():
            print(f"{C}{key}: {value}{F}")

    print(f"\n{D}--- Domain Registration Information ---{F}")
    registration_info = get_domain_registration_info(domain)
    if "error" in registration_info:
        print(f"{B}{registration_info['error']}{F}")
    else:
        print(f"{C}Registrar: {registration_info['registrar']}{F}")
        print(f"{C}Registrant Country: {registration_info['country']}{F}")

    print(f"\n{D}--- Additional Information ---{F}")
    additional_info = get_additional_info(target_ip)
    if "error" in additional_info:
        print(f"{B}{additional_info['error']}{F}")
    else:
        print(f"{C}Creation Date: {additional_info['creation_date']}{F}")
        print(f"{C}Programming Language: {additional_info['programming_language']}{F}")
        print(f"{C}Server Info: {additional_info['server_info']}{F}")

    print(f"\n{D}--- Checking WAF ---{F}")
    check_waf(target_url)

    print(f"\n{D}--- Checking SQL Injection ---{F}")
    check_sql_injection(target_url)

if __name__ == "__main__":
    main()

print(' ')
print(' ')
print(' ')
print(E + '\t\t BY XSc00tz')
