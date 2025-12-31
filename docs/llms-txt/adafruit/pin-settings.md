# Source: https://learn.adafruit.com/fpga-rgb-matrix/pin-settings.md

# FPGA RGB Matrix

## Pin settings

## Pin settings
Now that the project has been created, you need to change two more settings before we can move on. Go to the Project Navigator panel in the top left area of Quartus and right click on the device ("Cyclone IV E: ..."). Select "Device" from the menu.![](https://cdn-learn.adafruit.com/assets/assets/000/000/912/medium800/led_matrix_pintristate.png?1396766996)

A window will open. Click "Device and Pin Options...". In the left hand side of the new window that comes up, open the "Unused Pins" category. Change the "Reserve all unused pins" settings to "As input tri-stated". This will essentially prevent the unused pins on the FPGA from doing anything unwanted on the DE0-Nano when we program the design.  
  
&nbsp;Now select the "Voltage" category. Change the "Default I/O standard" to "3.3-V LVTTL". This is essential to do because the panels will not recognize a signal below this voltage.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/911/medium800/led_matrix_voltage.png?1396766969)

Click OK, then click OK again.

- [Previous Page](https://learn.adafruit.com/fpga-rgb-matrix/new-project.md)
- [Next Page](https://learn.adafruit.com/fpga-rgb-matrix/pin-assignments.md)

## Featured Products

### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
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

- [Matrix Portal Sand Handles](https://learn.adafruit.com/matrix-portal-sand.md)
- [NextBus transit clock for Raspberry Pi](https://learn.adafruit.com/nextbus-transit-clock-for-raspberry-pi.md)
- [T³ Time Triangle Thing](https://learn.adafruit.com/t-time-triangle-thing.md)
- [Ultrasonic Ruler](https://learn.adafruit.com/ultrasonic-ruler.md)
- [DIY Pocket LED Gamer - Tiny Tetris!](https://learn.adafruit.com/diy-3d-printed-handheld-pocket-game-tiny-tetris-snake.md)
- [Moon Phase Clock for Adafruit Matrix Portal](https://learn.adafruit.com/moon-phase-clock-for-adafruit-matrixportal.md)
- [Lighting LED Nets with WLED and xLights](https://learn.adafruit.com/lighting-led-nets-with-wled-and-xlights.md)
- [MatrixPortal CircuitPython Animated Message Board](https://learn.adafruit.com/matrixportal-circuitpython-animated-message-board.md)
- [TIMESQUARE Watch Kit](https://learn.adafruit.com/timesquare-watch-kit.md)
- [Matrix Portal Scoreboard](https://learn.adafruit.com/matrix-portal-scoreboard.md)
- [Raspberry Pi LED Matrix Display](https://learn.adafruit.com/raspberry-pi-led-matrix-display.md)
- [Adafruit CharliePlex LED Matrix Bonnet](https://learn.adafruit.com/adafruit-charlieplex-bonnet.md)
- [LED Matrix Scoreboard](https://learn.adafruit.com/led-matrix-scoreboard.md)
- [SmartMatrix Remote Controlled LED Art Display](https://learn.adafruit.com/smartmatrix-remote-controlled-led-art-display.md)
- [Motion Controlled Matrix Bed Clock](https://learn.adafruit.com/motion-controlled-matrix-bed-clock.md)
