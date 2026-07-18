import whois

print("=== WHOIS Lookup Tool ===")

domain = input("Enter a domain (example: google.com): ")

try:
    info = whois.whois(domain)

    print("\nWHOIS Information")
    print("---------------------------")
    print("Domain Name:", info.domain_name)
    print("Registrar:", info.registrar)
    print("Creation Date:", info.creation_date)
    print("Expiration Date:", info.expiration_date)
    print("Name Servers:", info.name_servers)

except Exception as e:
    print("Error:", e)