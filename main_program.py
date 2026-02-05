import time
import machine

led = machine.Pin(2, machine.Pin.OUT)

def loop():
    print("test2")

    led.off()   # mati
    time.sleep(1)

    led.on()    # hidup
    time.sleep(1)
