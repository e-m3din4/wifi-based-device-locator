import requests

def get_location(wifi_access_points):
    # Define the API endpoint
    endpoint = "https://location.services.mozilla.com/v1/geolocate"
    
    # Define the request payload with the Wi-Fi access points
    payload = {
        "wifiAccessPoints": wifi_access_points
    }
    
    # Make a POST request to the API endpoint
    response = requests.post(endpoint, json=payload)
    
    # Check the status code of the response
    if response.status_code == 200:
        # If the request was successful, return the location information
        return response.json()
    else:
        # If the request was not successful, return None
        return None

def display_menu():
    print("                                                                                ")
    print("                                                         ,██   ██▄              ")
    print("                                                                                ")
    print("                                                         ███   ███              ")
    print("                                                                                ")
    print("       W i F i    b a s e d -- l o c a t i o n          ███▌  ▐███              ")
    print("                                                                                ")
    print("  ███████████ ██████    ┌████████   ██████████   ███    ███   ███   ▐████████   ")
    print("                                                                                ")
    print("    ████   ████   ███⌂  ▄███    ███  ██▌  ███▀    ███  ███   ███▀  ▀▀▀   ███▌   ")
    print("                                                                                ")
    print("    ███▌   ███▌   ███   ███     ███▌    ███▀           ▄██▌  ███   ▄████████▌   ")
    print("                                                                                ")
    print("     ███▌   ███▌  ███▌  ███,  ▄███  ████,  ██▌    ███  ███   ███   ▐███  ,███▌  ")
    print("                                                                                ")
    print("  ██████▌ █████  █████   ▀██████▀   ▀█████████   ███  ███   ▐██▌    █████▀└███▌ ")
    print("  powered by:                                 l o c a t i o n   s e r v i c e s ")
    print("                                                                                ")
    print("  _____________________________________________________________________________ ")
    print("                         1. Get location information                            ")
    print("  _____________________                                ________________________ ")
    print("                         2.Quit                                                 ")
    print("  ----------------------------------------------------------------------------- ")
    print("                                                                                ")
    choice = input("Enter your choice [1-2]: ")
    return int(choice)

def get_wifi_access_points():
    wifi_access_points = []
    more = True
    while more:
        mac_address = input("Enter the MAC address of the Wi-Fi access point: ")
        signal_strength = int(input("Enter the signal strength of the Wi-Fi access point (in dBm) [optional]: ") or -120)
        channel = int(input("Enter the channel of the Wi-Fi access point [optional]: ") or 1)
        wifi_access_point = {
            "macAddress": mac_address,
            "signalStrength": signal_strength,
            "channel": channel
        }
        wifi_access_points.append(wifi_access_point)
        more = input("Add another Wi-Fi access point? (y/n): ") == "y"
    return wifi_access_points

# Main loop
choice = 0
while choice != 2:
    choice = display_menu()
    if choice == 1:
        wifi_access_points = get_wifi_access_points()
        location = get_location(wifi_access_points)
        if location:
            print("Latitude:", location["location"]["lat"])
            print("Longitude:", location["location"]["lng"])
            print("Accuracy:", location["accuracy"])
        else:
            print("Location could not be determined.")
    elif choice == 2:
        print("Exiting program.")
    else:
        print("Invalid choice.")
