Here's how the code works:

The script prompts the user to enter an IP address.

The script reads in the GeoIP2 database file "GeoLite2-City.mmdb".

The script attempts to retrieve the geolocation information for the specified IP address by passing the IP address as a string to the GeoIP2 Reader object.

If the IP address is found in the database, the script formats the geolocation information into a dictionary object and prints it to the console in JSON format.
If the IP address is not found in the database, the script outputs an error message indicating that the address information could not be found.

If any other errors occur during the retrieval of the IP address information, the script outputs an error message with the details of the error.

This script can be useful for anyone who needs to retrieve and display geolocation information for a specific IP address. It can be used for a variety of purposes, such as analyzing website traffic, identifying the location of network attacks, and more.

Unpack GeoLite2-City.part1 and GeoLite2-City.part2

pip -r requirements.txt 

python iplocator.py
