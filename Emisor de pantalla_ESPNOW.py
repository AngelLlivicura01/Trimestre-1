import network
import espnow
import time
from machine import Pin


wlan = network.WLAN(network.STA_IF)
wlan.active(True)  


e = espnow.ESPNow()
e.active(True) 


peer_mac = b'\xb0\xb2\x1c\xa8K,'

e.add_peer(peer_mac)



text1 = "Franklin Simbaña"
text2 = "Angel llivicura"


mensaje_completo = text1 + "|" + text2


e.send(peer_mac, mensaje_completo)
print(f"Mensajes enviados: {text1} y {text2}")


time.sleep(5)