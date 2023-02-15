# WiF-based Device Locator

                                                                                           
                                                                    ,██   ██▄              
                                                                                           
                                                                    ███   ███              
                                                                                           
                  W i F i    b a s e d -- l o c a t i o n          ███▌  ▐███              
                                                                                           
             ███████████ ██████    ┌████████   ██████████    ███    ███   ███   ▐████████   
                                                                                           
               ████   ████   ███⌂  ▄███    ███  ██▌  ███▀     ███   ███   ███▀  ▀▀▀   ███▌   
                                                                                           
               ███▌   ███▌   ███   ███    ███▌    ███▀        ███   ██▌   ███   ▄████████▌   
                                                                                           
               ███▌   ███▌  ███▌  ███,    ▄███  ████,  ██▌    ███  ███   ███   ▐███  ,███▌  
                                                                                           
             ██████▌ █████  █████   ▀██████▀   ▀█████████   ███  ███   ▐██▌    █████▀└███▌ 
             powered by:                                 l o c a t i o n   s e r v i c e s 
                                                                                           
            ________________________________________________________________________________ 

##  Introduction

This script uses the Mozilla Location Services API to determine the location of a device based on the Wi-Fi access points in its vicinity. The script has a menu-driven interface that allows users to input the information of multiple Wi-Fi access points and obtain their location information. Accuracy of the output relays in the amount of users offer as input for the script to call the Mozilla API, results are printed as coordinates to use as input in any map services out there. 

## Installation & Usage 

	   
- Clone repository: 

		git clone https:github.com/e-m3din4/wifi-based-device-locator

- Install library:

        pip3 install requests

- Run the script:

		python3 wifi-based=device-locator.py

- Follow the on-screen instructions to enter the details of the Wi-Fi access points.
		
		-------------------------------
		1. Get location information
		2. Quit
		-------------------------------
		
		Enter your choice [1-2]: 1
	
- Enter the MAC address of the Wi-Fi access point, addtional data will increase accuracy in the results (optional: signal strenght, channel, addtional access points) 

		
		-------------------------------
		1. Get location information
		2. Quit
		-------------------------------
		Enter your choice [1-2]: 1
		Enter the MAC address of the Wi-Fi access point: 
		Enter the signal strength of the Wi-Fi access point (in dBm) [optional]: 
		Enter the channel of the Wi-Fi access point [optional]: 
		Add another Wi-Fi access point? (y/n):
		WiFi Access Point:
			         {
			         macAddress : 01:a1:02:b2:03:c3
			         signalStrenght : -45 dbm
			         channel : 8
			         Latitude : 10,XXXXXX
			         Longitude : 10,XXXXXX
			         Location Accuracy : 86%
			         }
	
- The script will then make a POST request to the API endpoint and return the location information if the request was successful.


- If the request was not successful, the script will return None. The script provides the option to obtain the location information for multiple Wi-Fi access points or quit the program.

## Limitations

This script is limited by the accuracy and availability of Wi-Fi access points in the vicinity of the device. The accuracy of the location information also depends on the number of Wi-Fi access points provided and the quality of their signals. Location of specific wifi-devices such as mobile phones, tablets, etc, it is required it has been, at least once, working as wifi AP, as a tether for certain area and has been captured for it to appears in the database. 

### Only for research and educational purposes, respect people privacy.
### Author: Edgar Medina   
    
