# Source: https://learn.adafruit.com/fpga-rgb-matrix/synthesize-and-upload.md

# FPGA RGB Matrix

## Synthesize and Upload

## Synthesizing the design

To synthesize the design, go to the "Processing" menu and select "Start Compilation", or click on the purple arrow icon in the toolbar. Synthesis should be quite fast since the design is small. After compilation is successful, you should have a new .sof file in your Quartus project directory. It should be 703,642 bytes long.

## Uploading the bitfile

Plug in your DE0-Nano board via the USB connector. Now, go to the "Tools" menu and select "Programmer".

![](https://cdn-learn.adafruit.com/assets/assets/000/000/917/medium800/led_matrix_nohardware.png?1396767077)

In the top left of the window that appears, you should see "USB-Blaster [USB-0]". If instead you see "No Hardware", click on "Hardware Setup..." and (re-)select your device.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/918/medium800/led_matrix_hardwaresetup.png?1396767093)

Now, select the **.sof** file in the list, ensure "Program/Verify" is checked, and click "Start"! This should take about a second.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/919/medium800/led_matrix_programmer.png?1396767112)

The FPGA is now programmed with your design! (This only programmed the SRAM though, not the onboard EEPROM — so the design is only stored until power is turned off.)

Note: In the future, you can use the command script **de0-nano/program.cmd** to quickly program the FPGA's SRAM with your **.sof** file (it uses the Quartus command line programming utility).

- [Previous Page](https://learn.adafruit.com/fpga-rgb-matrix/pin-assignments.md)
- [Next Page](https://learn.adafruit.com/fpga-rgb-matrix/demos.md)

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
