# Source: https://learn.sparkfun.com/tutorials/humidity-sensing-led-flower

## Introduction

This tutorial will show you how to make your own LED flower that senses humidity, just like the one in this week\'s episode of ElectriCute! In case you missed it, here\'s the video explaining exactly how this circuit works:

ReplaceMeOpen

ReplaceMeClose

This is a pretty versatile project. It lives in my terrarium, and could reasonably go pretty much anywhere, including a garment or accessory. The only reason I didn\'t go that route is our location: Colorado is a *very* boring place to sense humidity!

[![Humidity-sensing flower in terrarium](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/9/Terrarium_Action_Shot-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/9/Terrarium_Action_Shot-02.jpg)

Continue reading to learn how to make your own.

### Suggested Reading

Before getting started with this tutorial, there are a few concepts with which you should be familiar. Consider reading some of the tutorials below, before continuing on with this one.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/working-with-wire)

### Working with Wire 

How to strip, crimp, and work with wire.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/i2c)

### I2C 

An introduction to I2C, one of the main embedded communications protocols in use today.

## Materials

Here\'s what you\'re going to need for this circuit. The RGB LED flower is exclusive to the [21st Century Fashion Kit](https://www.sparkfun.com/products/11817), but you can substitute a [standard RGB LED](https://www.sparkfun.com/products/105) if you\'d rather!

## The Circuit

Here\'s your circuit, in all its glory:

[![circuit diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/9/flowers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/9/flowers.jpg)

*Click image for a closer look.*

The Fritzing diagram makes it look nearly impossible to tell the pins of the RGB LED apart, but it really isn\'t! The longest leg is ground. The single pin to one side of ground is red, and the other two pins, moving out from ground, are green, then blue.

If you\'re using the flower, rather than a standard RGB LED, be very careful if you use heatshrink over the connections \-- it\'s very easy to melt the flower petals with a hot-air gun!

## The Code

Not sure how to upload code to your Arduino? No problem! Take a look [our tutorial](https://learn.sparkfun.com/tutorials/installing-arduino-ide) explaining everything in detail. Remember to select the correct board and port for your application.

Copy and paste the code below into the IDE, and click Upload:

    language:c
     /*********************************************************
    ElectriCute: Humidity Sensing LED Flower
    Dia Campbell
    SparkFun Electronics
    Oct. 29, 2014
    Based off of the code found on bildr.org,
    http://bildr.org/2012/11/sht15-arduino/
    which in turn was based of the wiring code at
    http://wiring.org.co/learning/basics/humiditytemperaturesht15.html
    With a few additions from Arduino example code 
    Basically, if this code was a dog, you'd have gotten it from the pound.

    Development environment specifics:
    Arduino IDE 1.0+
    Arduino Pro 5V 16MHz

    This code is beerware; if you see us at the local pub, 
    and you've found our code helpful, please buy us a round!
    *********************************************************/

     int SHT_clockPin = 3;  // pin used for clock
     int SHT_dataPin  = 2;  // pin used for data
     int redPin = 4; // Define RGB pins
     int bluePin = 6;
     int greenPin = 5;

    void setup()
     void loop() 
      else  
      }

    float getTemperature()

    float getHumidity()

    void SHT_sendCommand(int command, int dataPin, int clockPin)

    void SHT_waitForResult(int dataPin)

      if (ack == HIGH) Serial.println("ACK error 2");
       }

     int SHT_getData(int dataPin, int clockPin)

    void SHT_skipCrc(int dataPin, int clockPin) 

Once the code is uploaded, open the [Serial Monitor](https://learn.sparkfun.com/tutorials/terminal-basics/arduino-serial-monitor-windows-mac-linux). This should open a window which is scrolling numbers. The right column is temperature, the left column is humidity. Take a look at the number your humidity is hovering around, and use that to determine what you\'d like your ideal humidity to be.

The line addressing humidity threshold is commented, and pretty close to the top, so look for that and make adjustments as needed. I set mine to just a hair above ambient humidity, because I wanted it to be easy to demo. You may want yours to be a bit less sensitive. In that same section, you can make changes to the way the lights react to those changes!

When the sensor is reading below that threshold, the LED blinks red, like so:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/9/Terrarium_Action_Shot-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/9/Terrarium_Action_Shot-01.jpg)

And, when it\'s above the threshold, a nice, white glow is emitted:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/1/9/Terrarium_Action_Shot-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/1/9/Terrarium_Action_Shot-02.jpg)

Once you\'ve got your reactivity and behavior where you\'d like them, you\'re all set! Unhook the board from the computer, plug the battery into the Arduino, and put your new humidity sensing device in your favorite terrarium, buttonhole, [fascinator](http://en.wikipedia.org/wiki/Fascinator), or whatever you choose!