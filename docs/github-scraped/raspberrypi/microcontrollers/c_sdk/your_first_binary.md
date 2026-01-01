## Your First Binaries

### Blink an LED

The first program anyone writes when using a new microcontroller is to blink an LED on and off. The Raspberry Pi Pico comes with a single LED on-board. The LED is connected to `GP25` on the board's Raspberry Pi RP2040 for Pico, and `WL*GPIO0` on the Infineon 43439 wireless chip for Pico W.

video: images/Blink-an-LED.webm[width="80%"]

You can blink this on and off by,

1. Download the Blink UF2 https://datasheets.raspberrypi.com/soft/blink.uf2[for Raspberry Pi Pico], or https://datasheets.raspberrypi.com/soft/blink*picow.uf2[for Pico W].
1. Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer.
1. It will mount as a Mass Storage Device called RPI-RP2.
1. Drag and drop the Blink UF2 binary onto the RPI-RP2 volume. Pico will reboot.

You should see the on-board LED blinking.

You can see the code on Github for the https://github.com/raspberrypi/pico-examples/blob/master/blink/blink.c[Raspberry Pi Pico] and https://github.com/raspberrypi/pico-examples/blob/master/pico*w/wifi/blink/picow*blink.c[Pico W] versions.

### Say "Hello World"

The next program anyone writes is to say 'Hello World' over a USB serial connection.

video: images/Hello-World.webm[width="80%"]

1. Download the https://datasheets.raspberrypi.com/soft/hello*world.uf2['Hello World' UF2].
1. Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer.
1. It will mount as a Mass Storage Device called RPI-RP2.
1. Drag and drop the 'Hello World' UF2 binary onto the RPI-RP2 volume. Pico will reboot.
1. Open a Terminal window and type:
+
[source,console]
------
$ sudo apt install minicom
$ minicom -b 115200 -o -D /dev/ttyACM0
------

You should see 'Hello, world!' printed to the Terminal.

You can see the code https://github.com/raspberrypi/pico-examples/blob/master/hello*world/usb/hello_usb.c[on Github]