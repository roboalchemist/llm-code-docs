# Source: https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/connecting-the-cobbler-to-a-mcp3008.md

# Analog Inputs for Raspberry Pi Using the MCP3008

## Connecting the Cobbler to a MCP3008

# To follow this tutorial you will need

- [MCP3008 DIP-package ADC converter chip](https://www.adafruit.com/products/856 "Link: https://www.adafruit.com/products/856")
- [10K trimer](https://www.adafruit.com/products/356 "Link: https://www.adafruit.com/products/356") [or panel mount potentiometer](https://www.adafruit.com/products/562)
- [Adafruit T-Cobbler Plus](https://www.adafruit.com/product/2028) or for an older 26-pin Pi an&nbsp;[Adafruit Pi Cobbler](https://www.adafruit.com/products/914 "Link: https://www.adafruit.com/products/914")
- [Full-size breadboard](https://www.adafruit.com/products/239)&nbsp;
- [Breadboarding wires](https://www.adafruit.com/category/82 "Link: https://www.adafruit.com/category/82")

And of course a working Raspberry Pi.

# Why we need an ADC

The Raspberry Pi computer does not have a way to read analog inputs. It's a digital-only computer. Compare this to the Arduino, AVR or PIC microcontrollers that often have 6 or more analog inputs! Analog inputs are handy because many sensors are analog outputs, so we need a way to make the Pi analog-friendly.  
  
We'll do that by wiring up an [MCP3008 chip](https://www.adafruit.com/products/856) to it. The [MCP3008](https://www.adafruit.com/products/856) acts like a "bridge" between digital and analog. It has 8 analog inputs and the Pi can query it using 4 digital pins. That makes it a perfect addition to the Pi for integrating simple sensors like [photocells](http://learn.adafruit.com/photocells),&nbsp;[FSRs](http://learn.adafruit.com/force-sensitive-resistor-fsr) or&nbsp;potentiometers, [thermistors](http://learn.adafruit.com/thermistor), etc.!  
  
 [Let's check the datasheet of the MCP3008 chip.](http://www.adafruit.com/datasheets/MCP3008.pdf "Link: http://www.adafruit.com/datasheets/MCP3008.pdf")&nbsp;On the first page in the lower right corner there's a pinout diagram showing the names of the pins:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/222/medium800/raspberry_pi_mcp3008pin.gif?1447977143)

# Wiring Diagram

In order to read analog data we need to use the following pins:

**VDD** &nbsp;(power) and **DGND&nbsp;** (digital ground) to power the MCP3008 chip. We also need&nbsp;four "SPI" data&nbsp;pins:&nbsp; **DOUT** &nbsp;(Data Out from MCP3008),&nbsp; **CLK** &nbsp;(Clock pin),&nbsp; **DIN** &nbsp;(Data In from Raspberry Pi), &nbsp;and / **CS** &nbsp;(Chip Select). &nbsp;Finally of course, a source of analog data. We'll be using&nbsp;the basic&nbsp;10k trim pot.&nbsp;  
  
The MCP3008 has a few more pins we need to connect:&nbsp; **AGND** &nbsp;(analog ground, used sometimes in precision circuitry, which this is not) connects to&nbsp; **GND** , and&nbsp; **VREF** &nbsp;(analog voltage reference, used for changing the "scale" - we want the full scale, so tie it to&nbsp; **3.3V** ).  
  
Below is a wiring diagram. Connect the 3.3V cobbler pin to the left + rail and the GND pin to the right - rail. Connect the following pins for the MCP chip

- MCP3008 VDD -\> 3.3V (red)
- MCP3008 VREF -\> 3.3V&nbsp;(red)
- MCP3008 AGND -\> GND&nbsp;(black)
- MCP3008&nbsp;CLK -\> SCLK (yellow)
- MCP3008 DOUT -\> MISO (purple)
- MCP3008 DIN -\> MOSI (white)
- MCP3008 CS -\> #22 (green)
- MCP3008 DGND -\> GND&nbsp;(black)

Next connect up the potentiometer.

- Pin #1 (left) goes to 3.3v (red)
- Pin #2 (middle) connects to MCP3008&nbsp; **CH0** &nbsp;(analog input #0) with a purple wire
- Pin #3 (right) connects to GND (black)

Below we provide to wiring diagrams that will work with all versions of Raspberry Pi released so far (except the compute node which has no header). The first diagram is for the most recent Pi v3 and Pi Zero models which have a 40-pin GPIO header. The second is for the first two generations of Raspberry Pi which had a smaller 26-pin header. In both cases we are using the same GPIOs so the code will not be any different.&nbsp;

## T-Cobbler Plus Wiring 40-Pin Pi (v3, Zero)
![](https://cdn-learn.adafruit.com/assets/assets/000/071/321/medium800/learn_raspberry_pi_Analog_Inputs_for_Raspberry_Pi_Using_the_MCP3008-T-Cobbler-Plus_bb.png?1550268331)

## Pi Cobbler Wiring 26-Pin Pi (v1, v2)
![](https://cdn-learn.adafruit.com/assets/assets/000/071/320/medium800/learn_raspberry_pi_Analog_Inputs_for_Raspberry_Pi_Using_the_MCP3008-Pi-Cobbler_bb.png?1550268320)

- [Previous Page](https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/overview.md)
- [Next Page](https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/necessary-packages.md)

## Featured Products

### MCP3008 - 8-Channel 10-Bit ADC With SPI Interface

[MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://www.adafruit.com/product/856)
Need to add analog inputs? This chip will add 8 channels of 10-bit analog input to your microcontroller or microcomputer project. It's super easy to use and uses SPI so only 4 pins are required. We chose this chip as a great accompaniment to the Raspberry Pi computer because it's fun...

In Stock
[Buy Now](https://www.adafruit.com/product/856)
[Related Guides to the Product](https://learn.adafruit.com/products/856/guides)
### Breadboard trim potentiometer

[Breadboard trim potentiometer](https://www.adafruit.com/product/356)
These are our favorite trim pots, perfect for breadboarding and prototyping. They have a long grippy adjustment knob and with 0.1" spacing, they plug into breadboards or perfboards with ease.

This is the same pot that comes with our character LCDs and tutorial...

In Stock
[Buy Now](https://www.adafruit.com/product/356)
[Related Guides to the Product](https://learn.adafruit.com/products/356/guides)
### Full Sized Premium Breadboard - 830 Tie Points

[Full Sized Premium Breadboard - 830 Tie Points](https://www.adafruit.com/product/239)
This is a 'full-size' premium quality breadboard, 830 tie points. Good for small and medium projects. It's 2.2" x 7" (5.5 cm x 17 cm) with a standard double-strip in the middle and two power rails on both sides. You can pull the power rails off easily to make the...

In Stock
[Buy Now](https://www.adafruit.com/product/239)
[Related Guides to the Product](https://learn.adafruit.com/products/239/guides)
### Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM

[Raspberry Pi 3 - Model B+ - 1.4GHz Cortex-A53 with 1GB RAM](https://www.adafruit.com/product/3775)
The Raspberry Pi 3 Model B is the most popular Raspberry Pi computer made, and the Pi Foundation knows you can always make a good thing _better_! And what could make the Pi 3 better? How about a&nbsp;_faster_ processor, 5 GHz WiFi, and updated Ethernet chip with PoE capability?...

In Stock
[Buy Now](https://www.adafruit.com/product/3775)
[Related Guides to the Product](https://learn.adafruit.com/products/3775/guides)
### Assembled Pi T-Cobbler Plus - GPIO Breakout

[Assembled Pi T-Cobbler Plus - GPIO Breakout](https://www.adafruit.com/product/2028)
 **This is the assembled version of the Pi T-Cobbler Plus. &nbsp;It only works with the Raspberry Pi Model Zero, A+, B+, Pi 2, Pi 3 & Pi 4!** (Any Pi with 2x20 connector)  
  
The Raspberry Pi has landed on the Maker World like a 40-GPIO pinned, quad-USB ported, credit...

In Stock
[Buy Now](https://www.adafruit.com/product/2028)
[Related Guides to the Product](https://learn.adafruit.com/products/2028/guides)

## Related Guides

- [MCP3008 - 8-Channel 10-Bit ADC With SPI Interface](https://learn.adafruit.com/mcp3008-spi-adc.md)
- [Raspberry Pi E-mail Notifier Using LEDs](https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds.md)
- [Adafruit AMG8833 8x8 Thermal Camera Sensor](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Windows IoT Core Application Development: Headed Blinky](https://learn.adafruit.com/windows-iot-application-development-headed-blinky.md)
- [Single Channel LoRaWAN Gateway for Raspberry Pi](https://learn.adafruit.com/raspberry-pi-single-channel-lorawan-gateway.md)
- [LoRa and LoRaWAN Radio for Raspberry Pi](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi.md)
- [Adafruit's Raspberry Pi Lesson 12. Sensing Movement](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement.md)
- [Large Pi-based Thermometer and Clock](https://learn.adafruit.com/large-pi-based-thermometer-and-clock.md)
- [Playing sounds and using buttons with Raspberry Pi](https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi.md)
- [Windows IoT Core Application Development: Headless Blinky](https://learn.adafruit.com/windows-iot-application-development-headless-application.md)
- [Adafruit's Raspberry Pi Lesson 11. DS18B20 Temperature Sensing](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.md)
- [Node.js Embedded Development on the Raspberry Pi](https://learn.adafruit.com/node-embedded-development.md)
- [Adafruit's Raspberry Pi Lesson 10. Stepper Motors](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors.md)
- [CircuitPython Libraries on Linux and ODROID C2](https://learn.adafruit.com/circuitpython-libaries-linux-odroid-c2.md)
- [Adafruit's Raspberry Pi Lesson 4. GPIO Setup](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup.md)
