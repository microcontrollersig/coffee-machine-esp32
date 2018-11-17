import network
from time import sleep

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sleep(5)
sta_if.connect('MelbPC-NUE', 'peachspeak38')

