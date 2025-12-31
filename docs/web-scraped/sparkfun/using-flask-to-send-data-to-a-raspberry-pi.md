# Source: https://learn.sparkfun.com/tutorials/using-flask-to-send-data-to-a-raspberry-pi

## Introduction

In this tutorial, we\'ll show you how to send data from cheap WiFi nodes to a Raspberry Pi over an internal WiFi network. It relies on the Flask framework for [Python](https://www.sparkfun.com/python), which is a relatively simple-to-use method of creating a web application that can execute Python scripts.

[![Glamour shot of two boards from tutorial](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/6/main_image.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/6/main_image.png)

We\'ll use a [Raspberry Pi 3](https://www.sparkfun.com/products/13825) and [SparkFun ESP8266 Thing](https://www.sparkfun.com/products/13231) to demonstrate. We\'re going to send a very simple signal from the Thing board to the RasPi - just a signal to turn an attached LED on or off. Hopefully, it\'ll be obvious from the example how to send more complex signals and run more complex scripts upon receipt.

### Suggested Reading

Before you tackle this project, there are a few other tutorials you may want to check out.

[](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

### How to Solder: Through-Hole Soldering 

This tutorial covers everything you need to know about through-hole soldering.

[](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide)

### ESP8266 Thing Hookup Guide 

An overview of SparkFun\'s ESP8266 Thing - a development board for the Internet of\...Things. This tutorial explains the circuitry driving the board, and how to get it up and running in an Arduino environment.

[](https://learn.sparkfun.com/tutorials/raspberry-gpio)

### Raspberry gPIo 

How to use either Python or C++ to drive the I/O lines on a Raspberry Pi.

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

### Required Materials

You\'ll need the items on this wishlist to complete this tutorial. Substitutions can be made; a [Raspberry Pi Zero W](https://www.sparkfun.com/products/14277) can be substituted for the Pi 3, for instance, and individual components can be sourced instead of the full starter kit.

### Required Tools

No special tools are required to follow this tutorial. You will need a soldering iron, solder, and general soldering accessories.

[![Solder Lead Free - 15-gram Tube](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/8/7/09162-02-L.jpg)](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html)

### [Solder Lead Free - 15-gram Tube](https://www.sparkfun.com/solder-lead-free-15-gram-tube.html) 

[ TOL-09163 ]

This is your basic tube of unleaded (Pb-free) solder with a no clean, water soluble resin core. 0.031\" gauge and 15 grams

[ [\$4.95] ]

[![Soldering Iron - 30W (US, 110V)](https://cdn.sparkfun.com/r/140-140/assets/parts/3/2/4/3/09507-01.jpg)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html)

### [Soldering Iron - 30W (US, 110V)](https://www.sparkfun.com/soldering-iron-30w-us-110v.html) 

[ TOL-09507 ]

This is a very simple fixed temp, quick heating, 30W 110/120 VAC soldering iron. We really enjoy using the more expensive iro...

[ [\$11.50] ]

## Hardware Hookup

You\'ll need to do some basic breadboarding to prepare for this tutorial. Don\'t worry, we\'ll walk you through all of it.

### Raspberry Pi Connections

The connections for the Pi are simple: we\'re just connecting one LED to GPIO pin 2. See the Fritzing diagram below for information on how to do that.

[![Raspberry Pi connection diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/6/raspi_fritzing.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/6/raspi_fritzing.png)

### ESP8266 Thing Connections

Hook up two of the buttons as seen in the Fritzing diagram below.

[![Thing connection diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/7/0/6/ThingButton_bb4.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/6/ThingButton_bb4.png)

One of the buttons will turn the remote LED on, the other will turn it off. We\'re going to assume that you\'re capable of soldering the headers onto the ESP8266 Thing board yourself, but if you need some help, check out our [soldering tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering).

This is also where you\'ll use the [long, centered breakaway headers](https://www.sparkfun.com/products/12693). A six-pin group of them inserted into the breadboard aligned with the programming pins on the Thing will give you a place to plug in the [FTDI board](https://www.sparkfun.com/products/13746).

## Raspberry Pi Software

Let\'s get down to business and program the Raspberry Pi to serve a web app that we can use for data connection. This tutorial assumes that you have some familiarity with Linux and Python to follow along.

### Installing Flask

The first step is adding support for Flask to the RasPi. Python is already installed and support for using GPIO through Python, so we don\'t need to worry about that.

All of these commands can be run either on a [serial terminal](https://learn.sparkfun.com/tutorials/terminal-basics) opened on the Raspberry Pi directly with the Pi hooked up to a monitor, or remotely with a Pi via an SSH connection. However, we\'re not going to get into how to set up and run a Pi without a monitor.

The first thing you need to do is install the Flask framework. There are a lot of additional packages that can be used with Flask, but we only need the basic package for this tutorial.

    sudo pip install flask

Next, we\'re going to create the directory within which the app will run. These commands will create the directory and ensure that you\'re working inside that directory.

    mkdir FlaskTutorial
    cd FlaskTutorial

The next step is to create a blank Python file in the directory called \"app.py\". This is the file that we\'re going to put our code into. Open that file in your favorite text editor (the Pi has vi, nano, and a textpad).

    touch app.py

Then put the following code into it.

    language:python
    #!/usr/bin/python

    from flask import Flask
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)  # Sets up the RPi lib to use the Broadcom pin mappings
                            #  for the pin names. This corresponds to the pin names
                            #  given in most documentation of the Pi header
    GPIO.setwarnings(False) # Turn off warnings that may crop up if you have the
                            #  GPIO pins exported for use via command line
    GPIO.setup(2, GPIO.OUT) # Set GPIO2 as an output

    app = Flask(__name__)   # Create an instance of flask called "app"

    @app.route("/")         # This is our default handler, if no path is given
    def index():
        return "hello"

    # The magic happens here. When some http request comes in with a path of
    #  gpio/x/y, the Flask app will attempt to parse that as x=pin and y=level.
    #  Note that there is no error handling here! Failure to properly specify the
    #  route will result in a 404 error.
    @app.route('/gpio/<string:id>/<string:level>')
    def setPinLevel(id, level):
        GPIO.output(int(id), int(level))
        return "OK"

    # If we're running this script directly, this portion executes. The Flask
    #  instance runs with the given parameters. Note that the "host=0.0.0.0" part
    #  is essential to telling the system that we want the app visible to the 
    #  outside world.
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)

There are comments in the code to cover most questions but I want to highlight three things:

- First, there\'s no error checking here. The message is passed as the path requested via an HTTP request, and that request can contain just about anything. A request of the format `GET /gpio/2/0` will set the pin low, for instance. However, `GET /bats/are/bugs` is equally valid, it just won\'t do anything and the app will return a \"404 error.\"

- Second, the parameter `host='0.0.0.0'` is required to let the app know that you want the application visible to external clients. If you omit this, you\'ll still be able to test the app by visiting `localhost:5000` in a web browser on the Pi, it just won\'t be visible externally.

- Third, the most commonly used port number is 5000, but you can use any port you want.

## ESP8266 Thing Firmware

Now we\'ll need to program the Thing. This portion assumes that you\'ve followed the [SparkFun ESP8266 Thing hookup guide](https://learn.sparkfun.com/tutorials/esp8266-thing-hookup-guide) and can program the ESP8266.

### Example Code

**Note:** This example assumes you are using the latest version of the Arduino IDE on your desktop. If this is your first time using Arduino, please review our tutorial on [installing the Arduino IDE.](https://learn.sparkfun.com/tutorials/installing-arduino-ide) If you have not previously installed an Arduino library, please check out our [installation guide.](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)

Here\'s the firmware that I\'ve written to send the proper page requests to the Raspberry Pi.

    language:cpp
    #include <Arduino.h>
    #include <ESP8266WiFi.h>
    #include <ESP8266WiFiMulti.h>
    #include <ESP8266HTTPClient.h>

    ESP8266WiFiMulti WiFiMulti;

    void setup() 
    

      // Add the WiFi access point information
      WiFiMulti.addAP("SSID", "PASSWORD");

      // Set our buttons pins to inputs with pullup resistors enabled
      pinMode(12, INPUT_PULLUP);
      pinMode(13, INPUT_PULLUP);

    }

    void loop() 
    
        // Repeat the process for pin 13.
        if (digitalRead(13) == LOW)
        
      }
      else
      
    }

Hopefully, the code and comments make it clear what\'s going on. Two quick reminders:

- First, the IP address and port number in the functions `http.begin()` are mine from development. You\'ll have to change them to match the IP address and port number used on your Raspberry Pi.

- Second, don\'t forget to put in your `SSID` and `PASSWORD` for your wireless network.

### Try It Out!

By now, you ought to have everything ready to go. You\'ll need to start the script on the Raspberry Pi. Enter these commands in the subdirectory where you created the *\'app.py\'* file:

    chmod a+x app.py
    ./app.py

You should see a message, then, like the one below.

[![Output of the script run on the Raspberry Pi](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/6/app_launch.png)](https://cdn.sparkfun.com/assets/learn_tutorials/7/0/6/app_launch.png)

As you can see, I pressed the buttons a couple of times to show you what it looks like when a client makes an HTTP request. Flask reports the IP address of the client, the date and time stamp of the request, the contents of the request, and the result of the request (in this case, 200, or \"success\"). This is a useful tool to make sure that your requests are actually making it through to the Flask server and not disappearing into the ether somewhere.