# Source: https://learn.adafruit.com/webide/using-the-debugger.md

# Adafruit WebIDE

## Using the Debugger

The python debugger in the WebIDE can be quite useful for many situations. &nbsp;The debugger allows you to step through your python program in realtime. &nbsp;This is in contrast to the visualizer, which runs the program fully, and then allows you to step through it.  
  
When would you use the debugger? &nbsp;One scenario would be if you're just not getting the right values returned out of your functions. &nbsp;Or your variables aren't being set to the values you'd expect. &nbsp;You could then debug it, set a breakpoint to where you think it's broken, and see exactly what the values are at that given moment in your program. &nbsp;Also, you could use the GPIO pins to light various LED's. &nbsp;As you step through your program, you'll see them turn on and off as you'd expect.  
  
To use the debugger, open a python file, and click the "Debug" link in the toolbar:

![](https://cdn-learn.adafruit.com/assets/assets/000/003/466/medium800/adafruit_products_debug_link.png?1396796915)

Once you've clicked the link, the toolbar will change with a new debugging bar. &nbsp;It should open within a couple of seconds. &nbsp;The editor will still display, and you can make changes to your code while debugging.  
  
Once the debugger is ready, you'll see the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/003/467/medium800/adafruit_products_debug_screen.png?1396796938)

There is quite a bit more to the debugger than just running a program, or even than using&nbsp;the visualizer.  
  
The first think you'll notice is the toolbar (#1) has new buttons available:

1. Save/Restart allows you to save your file, and&nbsp;restart the debugger for that file in one click. &nbsp;You can initiate that by hitting control-s, or command-s (on OS X). &nbsp;
2. The Exit link will exit the debugger. &nbsp;
3. The Run link will continue execution of your program either to the end, or to the next breakpoint you have enabled. &nbsp;If there is a breakpoint enabled (clicking in the gutter (#6)), it will stop there, and wait for your instruction.  
4. Step Over will step through your program line-by-line until it hits the end. &nbsp;This option will skip any function calls. &nbsp;So, if you have a function called foo(), it will just run the entire function, and move to the next line.
5. Step In will step through your program as well, but it will jump into many of the functions, instead of skipping over them.

The editor is also displayed (#2). &nbsp;You can edit your file at any time. &nbsp;If you do change your file, you'll need to click the Save/Restart link in the toolbar in order to let the debugger pick up any of the changes you've made.  
  
At the bottom two panels, you'll see the Debug Output (#3), and the Debug Variables (#4). &nbsp;The Debug Output displays anything from stdout or stderr that your program would output (such as print statements). &nbsp;The Debug Variables displays the live variables as they're being assigned.  
  
The red line in the editor (#5) moves as you step through your program. &nbsp;It is the line that will execute next, and will stay centered in the editor window as you step through your program.  
  
At the far left of the editor (#6), there is a blank space to the left of the line numbers. &nbsp;This is called the gutter. &nbsp;If you click in the gutter when the debugger is in a "Ready" state, you can add breakpoints. &nbsp;A breakpoint is useful for many situations, such as if you have a longer script, and there is a certain troubling section that is buggy. &nbsp;Instead of slowly stepping through your program you would set the breakpoint (a red square will appear in the gutter), and then click "Run". &nbsp;The script will execute to the breakpoint, and the red line will stop, and wait for you to continue stepping through it.  
  
The last feature you'll want to be aware of is the debug status messages (#7). &nbsp;These will show you what the debugger is doing. &nbsp;For example, when it initially loads, or when you click "Save/Restart", it will be in an "Initializing..." state. &nbsp;When it's ready for your input, it will be "Ready". &nbsp;Some parts of your script will cause it to appear locked up, but it's really waiting for the server to return a response from your script (a long sleep() statement could cause this, for example).![](https://cdn-learn.adafruit.com/assets/assets/000/003/468/medium800/adafruit_products_debug_populated.png?1396796962)

In the screen shot above, you can see what the debugger looks like in the middle of running a program. &nbsp;The debugger is currently one step after the breakpoint that was set on line #13. &nbsp;You can see the 'print "Bonjour, World"' in the Debug Output, and the variables as they are in that given state of the program execution.  
  
At this point in the debug cycle, you could edit your file, and Save/Restart. &nbsp;You could continue stepping through the program, or you could Exit the debugger.

- [Previous Page](https://learn.adafruit.com/webide/use.md)
- [Next Page](https://learn.adafruit.com/webide/using-the-visualizer.md)

## Featured Products

### Raspberry Pi Model B 512MB RAM

[Raspberry Pi Model B 512MB RAM](https://www.adafruit.com/product/998)
Adafruit ships the **Raspberry Pi Model B 512MB RAM** as of 10/18/2012.  
  
The Raspberry Pi® is a single-board computer developed in the UK by the Raspberry Pi Foundation with the intention of stimulating the teaching of basic computer science in schools. The Raspberry...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/998)
[Related Guides to the Product](https://learn.adafruit.com/products/998/guides)
### BeagleBone Black - Rev B

[BeagleBone Black - Rev B](https://www.adafruit.com/product/1278)
**[Adafruit is no longer shipping the BeagleBone Black Rev B, it has been replaced with the Rev C as of 5/12/14](https://www.adafruit.com/products/1876) - the Rev C now has 4G flash and also comes with Debian, it also costs slightly more. There are no exchanges or...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1278)
[Related Guides to the Product](https://learn.adafruit.com/products/1278/guides)
### Adafruit Pi Box -  Enclosure for Raspberry Pi Model A or B

[Adafruit Pi Box -  Enclosure for Raspberry Pi Model A or B](https://www.adafruit.com/product/859)
 **Discontinued** - you can grab&nbsp;[Adafruit Pi Box Plus - Enclosure for RasPi Model B+/Pi 2/ Pi 3](https://www.adafruit.com/product/1985) instead!&nbsp;

**We're still selling this classic Adafruit case for those who specifically want it but <a...></a...>**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/859)
[Related Guides to the Product](https://learn.adafruit.com/products/859/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)

## Related Guides

- [Trellis Python Library](https://learn.adafruit.com/trellis-python-library.md)
- [Adafruit DVI Sock for Pico](https://learn.adafruit.com/adafruit-dvi-sock-for-pico.md)
- [Introducing Adafruit ItsyBitsy M4](https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4.md)
- [SMT Breadboard Prototyping Using Breakout PCBs](https://learn.adafruit.com/smt-prototyping-using-breakout-pcbs.md)
- [Getting Started with RTL-SDR and SDR-Sharp and CubicSDR](https://learn.adafruit.com/getting-started-with-rtl-sdr-and-sdr-sharp.md)
- [Adafruit STEMMA Reflective Photo Interrupt Sensor](https://learn.adafruit.com/adafruit-stemma-reflective-photo-interrupt-sensor.md)
- [Adafruit 9-DOF Orientation IMU Fusion Breakout - BNO085](https://learn.adafruit.com/adafruit-9-dof-orientation-imu-fusion-breakout-bno085.md)
- [Adafruit I2C to 8 Channel Solenoid Driver](https://learn.adafruit.com/adafruit-i2c-to-8-channel-solenoid-driver.md)
- [Controlling Motors using the Raspberry Pi and RasPiRobot Board V2](https://learn.adafruit.com/controlling-motors-using-the-raspberry-pi-and-raspirobot-board-v2.md)
- [Adafruit Feather 32u4 FONA](https://learn.adafruit.com/adafruit-feather-32u4-fona.md)
- [Adafruit Pi Stemma QT Breakout](https://learn.adafruit.com/adafruit-pi-stemma-qt-breakout.md)
- [Adafruit's Raspberry Pi Lesson 8. Using a Servo Motor](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor.md)
- [IoT Bird Feeder with Camera](https://learn.adafruit.com/iot-window-bird-feeder-with-camera.md)
- [Using the BMP085/180 with Raspberry Pi or Beaglebone Black](https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi.md)
- [AR1100 Resistive Touch Screen Controller Guide](https://learn.adafruit.com/ar1100-resistive-touch-screen-controller-guide.md)
