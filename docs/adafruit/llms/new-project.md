# Source: https://learn.adafruit.com/fpga-rgb-matrix/new-project.md

# FPGA RGB Matrix

## New Project

## User configuration

Once you are all set up and ready to begin, download the necessary files for this project from its [Github repository](https://github.com/adafruit/rgbmatrix-fpga) (click on the "ZIP" icon).   
  
Open the file vhdl/config.vhd in a text editor and change line 32 **(constant NUM\_PANELS...)** to indicate the total number of LED panels you have daisy-chained together in your display. For example, if you are using a 1x2 or 2x1 grid, you will want to change the line to:

> **constant NUM\_PANELS : integer := 2**

You may optionally edit line 33 **(constant PIXEL\_DEPTH...)** in a similar manner to indicate how many bits-per-pixel you want to use. This will affect the level of brightness control available to you later. Finally, save the file!

## Creating the Quartus II project

Start Quartus II and open the "New Project Wizard" from the "File" menu. On the first page, name the project **rgbmatrix-fpga** (or something similar) and name the top-level entity **top\_level**. Click Next.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/905/medium800/led_matrix_newproject1.png?1396766803)

Now we will add the source code files to the project. Click the "..." button to open the file browser and select the .vhd files in the vhdl folder you downloaded earlier (do not include the testbenches directory). Click "..." again and open the megawizard folder. Set the type drop-down menu to "All Files (\*.\*)" so you can select the .qip, .cmp, and megawizard\_vjtag.vhd files (do not include megawizard\_vjtag\_inst.vhd). Add them to the project and click Next.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/906/medium800/led_matrix_newproject2.png?1396766832)

The FPGA chip in use on the DE0-Nano is the Cyclone IV EP4CE22F17C6N. You can find it by setting the device family to "Cyclone IV E", package to "FBGA", pin count to 256, and speed grade to 6. Select the chip and click Next.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/907/medium800/led_matrix_newproject3.png?1396766863)

Set the "Simulation" tool name to "ModelSim-Altera" and the format to "VHDL". Leave everything else as "\<None\>" and click Next.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/908/medium800/led_matrix_newproject4.png?1396766889)

Click Finish to create the project!&nbsp;

- [Previous Page](https://learn.adafruit.com/fpga-rgb-matrix/overview.md)
- [Next Page](https://learn.adafruit.com/fpga-rgb-matrix/pin-settings.md)

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
