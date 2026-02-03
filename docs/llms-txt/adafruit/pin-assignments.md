# Source: https://learn.adafruit.com/fpga-rgb-matrix/pin-assignments.md

# FPGA RGB Matrix

## Pin Assignments

## Making pin assignments

Go to the "Assignments" menu and select "Import Assignments...". Import the&nbsp; **de0-nano/rgbmatrix-fpga.qsf** &nbsp;file. After you do this, a message should appear in the "System" console tab at the bottom of Quartus: "Import completed. 14 assignments were written (of of 14 read)."

![](https://cdn-learn.adafruit.com/assets/assets/000/000/913/medium800/led_matrix_importassignments.png?1396767009)

You can (optionally) customize the pin assignments that were imported by going to the "Assignments" menu and selecting "Assignment Editor". Additional information on the GPIO headers can be found in the [DE0-Nano PDF manual](http://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=139&No=593&PartNo=4) (pages 18-20). A mapping of FPGA pins to GPIO headers can also be found in the de0-nano/DE0\_Nano.qsf file (open it with a text editor).

![](https://cdn-learn.adafruit.com/assets/assets/000/000/914/medium800/led_matrix_assignmenteditor.png?1396767026)

Save any changes. Now we are ready to connect the pins on the FPGA to the pins on the RGB LED matrix panel!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/915/medium800/led_matrix_gpio0diagram.png?1396767052)

Please refer to the [Adafruit guide for wiring details](http://learn.adafruit.com/32x16-32x32-rgb-led-matrix/) on the panel side.  
  
[You may want to use female-female jumper wires to make the connections between the IDC pins!](https://www.adafruit.com/products/266)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/916/medium800/led_matrix_ffjumpersentire_LRG.jpg?1396767059)

Info: 

- [Previous Page](https://learn.adafruit.com/fpga-rgb-matrix/pin-settings.md)
- [Next Page](https://learn.adafruit.com/fpga-rgb-matrix/synthesize-and-upload.md)

## Featured Products

### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

In Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### Medium 16x32 RGB LED matrix panel - 6mm Pitch

[Medium 16x32 RGB LED matrix panel - 6mm Pitch](https://www.adafruit.com/product/420)
Bring a little bit of Times Square into your home with this 16 x 32 RGB LED matrix panel. These panels are normally used to make video walls, here in New York we see them on the sides of busses and bus stops, to display animations or short video clips. We thought they looked really cool so we...

In Stock
[Buy Now](https://www.adafruit.com/product/420)
[Related Guides to the Product](https://learn.adafruit.com/products/420/guides)
### DE0-Nano - Altera Cyclone IV FPGA starter board

[DE0-Nano - Altera Cyclone IV FPGA starter board](https://www.adafruit.com/product/451)
For every day projects, microcontrollers are low-cost and easy to use. But when you have a project that needs raw power and high speed you may want to check out FPGAs (Field Programmable Gate Arrays). FPGAs are like raw chips that you can design by hand. They run very fast and very...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/451)
[Related Guides to the Product](https://learn.adafruit.com/products/451/guides)

## Related Guides

- [Smart Bathroom App](https://learn.adafruit.com/smart-bathroom-app.md)
- [NeoTrellis Light Painting](https://learn.adafruit.com/neotrellis-light-painting.md)
- [TIMESQUARE Wordclock](https://learn.adafruit.com/timesquare-wordclock.md)
- [MatrixPortal S3 Flight Proximity Tracker](https://learn.adafruit.com/matrixportal-s3-flight-proximity-tracker.md)
- [MicroPython Displays: Drawing Shapes](https://learn.adafruit.com/micropython-displays-drawing-shapes.md)
- [Adafruit Protomatter RGB Matrix Library](https://learn.adafruit.com/adafruit-protomatter-rgb-matrix-library.md)
- [Adafruit Microphone Amplifier Breakout](https://learn.adafruit.com/adafruit-microphone-amplifier-breakout.md)
- [16x16 NeoPixel Matrix Square Pixel Display](https://learn.adafruit.com/16x16-neopixel-matrix-square-pixel-display.md)
- [Shake Away 2021 with MatrixPortal](https://learn.adafruit.com/matrixportal-shake-away-2020.md)
- [NeoTrellis Feather Case Assembly](https://learn.adafruit.com/neotrellis-feather-case-assembly.md)
- [RGB LED Matrices with CircuitPython](https://learn.adafruit.com/rgb-led-matrices-matrix-panels-with-circuitpython.md)
- [Scroll an SMS Text Message on your RGB Matrix](https://learn.adafruit.com/scroll-an-sms-text-message-on-your-rgb-matrix.md)
- [Adafruit LED Backpacks](https://learn.adafruit.com/adafruit-led-backpack.md)
- [Raspberry Pi LED Matrix Display](https://learn.adafruit.com/raspberry-pi-led-matrix-display.md)
- [Sino:bit with Arduino](https://learn.adafruit.com/sino-bit-with-arduino.md)
