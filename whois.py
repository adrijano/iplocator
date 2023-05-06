import whois


while True:
    domain = input("Enter domain name: ")

    try:
        w = whois(domain)
        print(w)
    except Exception as e:
        print("Error: An error occurred while performing the WHOIS lookup:", str(e))
