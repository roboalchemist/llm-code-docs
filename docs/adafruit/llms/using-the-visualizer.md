# Source: https://learn.adafruit.com/webide/using-the-visualizer.md

# Adafruit WebIDE

## Using the Visualizer

The visualizer is a feature designed to help understand how a Python program is working at&nbsp;a more basic level. &nbsp;It let's you see what the python interpreter is doing as it steps&nbsp;through your program, such as&nbsp;variables being assigned, objects being created, etc.  
  
Generally, the visualizer is a good tool to use if you have simpler scripts that you'd like to understand. &nbsp;Some of the questions it will help you with are: "How does recursion work?", "How does a function call work?", "How do various methods, such as append,&nbsp;work when working with lists?".

## Starting the visualizer
  
In order to start the visualizer, open a python script that you're able to run. &nbsp;In the menu, there will be a link with the title "Visualize". &nbsp;Click the "Visualize" link.  
![](https://cdn-learn.adafruit.com/assets/assets/000/003/437/medium800/adafruit_products_visualizer_link.png?1396796569)

Once you've clicked the link, it will take from a couple of seconds, to a few minutes to load, depending on what your python script is doing. &nbsp;Something simple, like lighting a few LED's, or printing out a few lines will load very quickly. &nbsp;One thing to watch out for is that you don't have any infinite loops in your code, such as if you have a script that is designed to just keep running while periodically checking the temperature.  
  
The next screen you'll see is the following:

![](https://cdn-learn.adafruit.com/assets/assets/000/003/438/medium800/adafruit_products_visualizer_screen.png?1396796598)

The toolbar (#1) allows you to step through your program. &nbsp;You can navigate any way you'd like, forward, back, and jump to the start, or end.  
  
The code (#2) is listed to the left. &nbsp;As you step through your program, you'll see two arrows in the left gutter that will show you what line has just executed (green), and what will be executing once you click "Forward" (red).  
  
The right column displays the stack (#3)&nbsp;as your program executes. &nbsp;You'll see your variables getting assigned, objects being created, etc.  
  
The bottom pane is your program output (#4). &nbsp;Anytime you have a print statement, or any other type of output, you'll see it displayed in this section.  
  
Here is a screen shot of how it looks while stepping through&nbsp;a program:

![](https://cdn-learn.adafruit.com/assets/assets/000/003/439/medium800/adafruit_products_visualizer_running.png?1396796626)

One thing to note about the visualizer is that it runs your entire script on the server, then sends the playback of your script to the WebIDE. &nbsp;It's not a real-time debugger (but the WebIDE has one of those as well!). &nbsp;For example,&nbsp;if you have an LED that lights up in your program,&nbsp;it will light up quick and then send back the response, and when you step through your program, the LED won't light up as it has already run.  
  
Credit to the visualizer is given to Philip Guo at&nbsp;[pythontutor.com](http://pythontutor.com). We forked, tweaked, converted,&nbsp;and&nbsp;modified his open source creation to work as a streamlined feature within the WebIDE.

- [Previous Page](https://learn.adafruit.com/webide/using-the-debugger.md)
- [Next Page](https://learn.adafruit.com/webide/faq.md)

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
