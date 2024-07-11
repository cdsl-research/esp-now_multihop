import network
import espnow
import time

while True:
    try:
        # A WLAN interface must be active to send()/recv()
        sta = network.WLAN(network.STA_IF)
        sta.active(True)
        sta.disconnect()   # Because ESP8266 auto-connects to last Access Point

        e = espnow.ESPNow()
        e.active(True)

        while True:
            host, msg = e.recv()
            if msg:             # msg == None if timeout in recv()
                print(host, msg)
                if msg == b'end':
                    break
            
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