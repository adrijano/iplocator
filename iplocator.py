import geoip2.database
import ipaddress
import json

while True:
    ip_str = input("Enter IP address: ")
    ip = ipaddress.ip_address(ip_str)

    database_path = 'GeoLite2-City.mmdb'

    try:
        with geoip2.database.Reader(database_path) as reader:
            response = reader.city(str(ip))
            formatted_response = {
                'ip_address': response.traits.ip_address,
                'country': response.country.name,
                'region': response.subdivisions.most_specific.name,
                'city': response.city.name,
                'latitude': response.location.latitude,
                'longitude': response.location.longitude
            }

            print(json.dumps(formatted_response, indent=4))
    except geoip2.errors.AddressNotFoundError:
        print("Error: Could not find address information for the given IP address.")
    except Exception as e:
        print("Error: An error occurred while retrieving IP address information:", str(e))
