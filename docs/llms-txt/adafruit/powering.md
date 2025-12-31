# Source: https://learn.adafruit.com/36mm-led-pixels/powering.md

# Source: https://learn.adafruit.com/20mm-led-pixels/powering.md

# Source: https://learn.adafruit.com/36mm-led-pixels/powering.md

# Source: https://learn.adafruit.com/20mm-led-pixels/powering.md

# 20mm LED Pixels

## Powering

When running a lot of LEDs, it’s important to keep track of power usage.&nbsp;Individual LEDs don't get very hot or use tons of power, but they add up fast!

Each single 20mm RGB LED pixel can draw up to 60mA from a 5V supply. That means a strand of 20 can use up to 1.2 Amps.&nbsp;That’s a peak rate, which assumes that all the LEDs are on at full brightness. If most of the LEDs are kept dim or off (as when animating patterns), the average power usage can be 1/3 this or less.

Info: 

Connect ground to both your power supply and microcontroller. Then connect the 5V line from the power supply to the red wire on the LED strand. A large capacitor (1000uF or so) between 5V and ground is a nice addition to keep ripple down.  
  
We suggest a nice switching supply for driving LED pixels:

Our&nbsp;[5 Volt,&nbsp;2 Amp power supply](http://adafruit.com/products/276)&nbsp;is ideal for one strand of pixels.![led_pixels_5v2A_LRG.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/128/medium640/led_pixels_5v2A_LRG.jpg?1396769041)

For larger projects using multiple strands of pixels, our&nbsp;[5 Volt&nbsp;10 Amp power supply](http://adafruit.com/products/658)&nbsp;is good for up to 8 strands (160 pixels total).![led_pixels_ID658_LRG.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/129/medium640/led_pixels_ID658_LRG.jpg?1396769051)

The&nbsp;[female DC power adapter](http://adafruit.com/products/368)&nbsp;mates with either of the above power supplies. Screw terminals clamp down on the power leads at the end of a strand, reducing the amount of soldering required.  
  
Note the embossed polarity markings. Connect the&nbsp; **red wire** &nbsp;to the&nbsp; **+** &nbsp;terminal and the&nbsp; **blue wire** &nbsp;to the&nbsp; **-** &nbsp;terminal.  
![led_pixels_dc-jack.jpg](https://cdn-learn.adafruit.com/assets/assets/000/001/130/medium640/led_pixels_dc-jack.jpg?1396769057)

# Tips for powering pixel strands:

- When linking multiple strands together, power should be split and&nbsp;applied to&nbsp;_each_&nbsp;strand. If you try to power too many LEDs from just one end of the strand, they’ll start to “brown out” the further they are from the power supply.
- Strands can be powered from&nbsp;_either_&nbsp;end — “input” and “output” doesn’t apply to power, only the data signals from the microcontroller.  
- If the 10 Amp power supply isn’t large enough for your project, a&nbsp;[slightly modified ATX computer power supply](http://www.instructables.com/pages/search/search.jsp?ie=ISO-8859-1&q=ATX)&nbsp;can provide 30 Amps to power upwards of 500 pixels!
- Generally speaking, you should not try to&nbsp;power an LED strand from the Arduino’s 5V line. This is okay if just a few pixels are lit, but is not adequate for driving a full strand.  
- For a standalone application (not USB connected to a computer), you can power the Arduino from the same regulated 5V supply as the LEDs — connect to the 5V pin on the Arduino,&nbsp;_not_&nbsp;Vin, and don’t use the DC jack on the Arduino.
- Remember to insulate or trim&nbsp;any unused, exposed power wires!

- [Previous Page](https://learn.adafruit.com/20mm-led-pixels/wiring.md)
- [Next Page](https://learn.adafruit.com/20mm-led-pixels/code.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Female DC Power adapter - 2.1mm jack to screw terminal block

[Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
If you need to connect a DC power wall wart to a board that doesn't have a DC jack - this adapter will come in very handy! There is a 2.1mm DC jack on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/368)
[Related Guides to the Product](https://learn.adafruit.com/products/368/guides)
### 5V 10A switching power supply

[5V 10A switching power supply](https://www.adafruit.com/product/658)
This is a beefy switching supply, for when you need a lot of power! It can supply 5V DC up to 10 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard computer/appliance...

In Stock
[Buy Now](https://www.adafruit.com/product/658)
[Related Guides to the Product](https://learn.adafruit.com/products/658/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)

## Related Guides

- [WiFi Controlled Mobile Robot](https://learn.adafruit.com/wifi-controlled-mobile-robot.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [TTL Serial Camera](https://learn.adafruit.com/ttl-serial-camera.md)
- [Adafruit Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps.md)
- [Ladyada's Learn Arduino - Lesson #1](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-1.md)
- [OLED TRON Clock](https://learn.adafruit.com/oled-tron-clock.md)
- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [WiFi Weather Station](https://learn.adafruit.com/wifi-weather-station-arduino-cc3000.md)
- [Circuit Playground: D is for Diode](https://learn.adafruit.com/circuit-playground-d-is-for-diode.md)
- [Wave Shield Talking Clock](https://learn.adafruit.com/wave-shield-talking-clock.md)
- [How to program a Zumo Robot with Simulink](https://learn.adafruit.com/zumo-robot-control-with-simulink.md)
- [8BitBox](https://learn.adafruit.com/8bitbox.md)
- [Arduino "Hunt The Wumpus"](https://learn.adafruit.com/arduino-hunt-the-wumpus.md)
- [36mm LED Pixels](https://learn.adafruit.com/36mm-led-pixels.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
