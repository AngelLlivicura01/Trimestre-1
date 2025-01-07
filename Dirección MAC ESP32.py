import network


wlan = network.WLAN(network.STA_IF)

wlan.active(True)



if wlan.active():
    
    mac_address = wlan.config("mac")
    print(mac_address)
    print("Device MAC Address:", ";".join(["{:02x}".format(byte) for byte in mac_address]))
else:
    print("WI-FI is not active.")