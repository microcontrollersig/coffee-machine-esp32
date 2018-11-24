# An Esp32 controlled coffee machine

### Step 1

Take apart a coffee machine (Sunbeam EM4800)

![Sunbeam EM4800](https://github.com/microcontrollersig/coffee-machine-esp32/raw/master/EM4800C_primary_1.jpg)

Get at its electronics

![EM4800 pcb](https://github.com/microcontrollersig/coffee-machine-esp32/raw/master/coffee-machine_bb.jpg)

Microcontroller voltage (3.3V) not enough to trigger solid-state relay (SSR-25DA), so use this circuit

![pic6](https://github.com/microcontrollersig/coffee-machine-esp32/raw/master/IMG_20181124_204517.jpg)

![Relay microcontroller](https://github.com/microcontrollersig/coffee-machine-esp32/raw/master/relay-microcontroller.jpg)

Use 3.3kohms as pullup and 1K to base of NPN transistor (PN2222A Emitter-Base-Collector)

### Pictures

![pic1](https://raw.githubusercontent.com/microcontrollersig/coffee-machine-esp32/master/IMG_20181124_194302.jpg)

![pic2](https://raw.githubusercontent.com/microcontrollersig/coffee-machine-esp32/master/IMG_20181124_194315.jpg)

![pic3](https://raw.githubusercontent.com/microcontrollersig/coffee-machine-esp32/master/IMG_20181124_192732.jpg)

![pic4](https://raw.githubusercontent.com/microcontrollersig/coffee-machine-esp32/master/IMG_20181124_192812.jpg)

![pic5](https://raw.githubusercontent.com/microcontrollersig/coffee-machine-esp32/master/IMG_20181124_194257.jpg)

