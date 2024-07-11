import network
import espnow
import time

while True:
    
    try:
        # A WLAN interface must be active to send()/recv()
        sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
        sta.active(True)
        sta.disconnect()      # For ESP8266

        e = espnow.ESPNow()
        e.active(True)
        peer = b'0\xae\xa4\xd4}\x04'   # MAC address of peer's wifi interface
        e.add_peer(peer)      # Must add_peer() before send()

        e.send(peer, "Starting...")

        for i in range(60):
            e.send(peer, str(i) + "a"*200, True)
            print(i)
            time.sleep(1)

        e.send(peer, b'end')
        e.active(False)
        sta.active(False)
    
        time.sleep(60)
    except Exception as e:
        f = open("error.log", "a")
        f.write(str(e))
        f.write("\n")
        f.close()
	e.active(False)
        sta.active(False)
