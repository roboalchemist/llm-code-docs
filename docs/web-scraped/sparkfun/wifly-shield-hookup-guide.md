# Source: https://learn.sparkfun.com/tutorials/wifly-shield-hookup-guide

## Introduction 

The [WiFly Shield](https://www.sparkfun.com/products/9954) allows you to easily connect your Arduino to a wireless network, serve up data, act as a client, create an ad-hoc network for your Internet of things devices, and get data such as data and time from your network. This hookup guide will show you how get started, how to configure the WiFly module, and how to set up some simple sketches using the WiFly Shield.

[![WiFly Shield](https://cdn.sparkfun.com/r/500-500/assets/9/2/a/d/8/52015a3f757b7f031f7b5446.jpg)](https://cdn.sparkfun.com/assets/9/2/a/d/8/52015a3f757b7f031f7b5446.jpg)

### Covered in This Tutorial

This guide will show you:

- How to connect the WiFly Shield to the Arduino
- How to communicate with the WiFly Shield through the terminal
- How to connect the WiFly to a WiFi network
- Simple communication over a network
- How to create a simple server
- How to update the firmware on the WiFly module

All of the functions and commands used in this tutorial can be found in the RN131 documentation:

- [RN131 Product Page](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en558369)
- [RN131 Reference Guide](http://ww1.microchip.com/downloads/en/DeviceDoc/50002230A.pdf)
- \[RN131 Datasheet\]([link text](http://ww1.microchip.com/downloads/en/DeviceDoc/rn-131-ds-v3.2r.pdf)
- [SC16IS750 SPI to UART Bridge Datasheet](//cdn.sparkfun.com/assets/c/f/6/9/7/511552e6ce395fbe3f000004.pdf)

### Suggested Reading

If you're new to electronics or wireless communication, you may also want to check out these other concepts first:

- [Installing an Arduino Library](https://learn.sparkfun.com/tutorials/installing-an-arduino-library)
- [What is a Shield?](https://learn.sparkfun.com/tutorials/arduino-shields)
- [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [SPI Communication](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi)
- [Serial Terminal Basics](https://learn.sparkfun.com/tutorials/terminal-basics)
- [How to Solder](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering)

You should also have a basic understanding of simple networking terms such as:

- [802.11](http://en.wikipedia.org/wiki/IEEE_802.11)
- [TCP/IP](http://en.wikipedia.org/wiki/Internet_protocol_suite)
- [FTP](http://en.wikipedia.org/wiki/Ftp)
- [Telnet](http://en.wikipedia.org/wiki/Telnet)
- [SSH](http://en.wikipedia.org/wiki/Secure_Shell)
- [HTTP](http://en.wikipedia.org/wiki/Http)
- [DNS](http://en.wikipedia.org/wiki/Dns)
- [DHCP](http://en.wikipedia.org/wiki/Dhcp)
- [WLAN](http://en.wikipedia.org/wiki/Wlan)

## Hardware Overview

[![WiFly Shield](https://cdn.sparkfun.com/r/500-500/assets/5/c/1/f/1/52015b36757b7f541c5f5dbd.jpg)](https://cdn.sparkfun.com/assets/5/c/1/f/1/52015b36757b7f541c5f5dbd.jpg)

The [WiFly Shield](https://www.sparkfun.com/products/9954) consists of two major components:

- An [SC16IS750 SPI-to-UART bridge chip](http://www.sparkfun.com/datasheets/Components/SMD/SC16IS740_750_760.pdf)
- An [RN-131C WiFly Module](https://www.sparkfun.com/products/10004)

The WiFly module communicates via its UART to the SC16IS750 bridge chip, which in turn communicates with the Arduino via SPI.

[![Communication diagram](//cdn.sparkfun.com/r/600-600/assets/d/c/6/f/2/51154f35ce395f6540000004.png)](//cdn.sparkfun.com/assets/d/c/6/f/2/51154f35ce395f6540000004.png)

This allows the WiFly module to communicate with the Arduino at high speed without using the Arduino's UART so that the Arduino can still communicate with a serial terminal. Any communication from the WiFly to the Arduino (or vice versa) must be sent through the SC16IS50.

The WiFly module is connected to four indicator LEDs through its I/O pins. These indicator LEDs will blink at different rates depending on the state of the module. They can provide a lot of information to the user about the state of the module without the user having to connect the device to a serial terminal. For more information on the behavior of the LEDs, see the [RN-131 Reference Guide](http://ww1.microchip.com/downloads/en/DeviceDoc/50002230A.pdf).

[![LED Status Table](//cdn.sparkfun.com/r/600-600/assets/3/a/4/a/b/511524c9ce395f2240000002.jpg)](//cdn.sparkfun.com/assets/3/a/4/a/b/511524c9ce395f2240000002.jpg)

The WiFly module is also connected to four jumpers. The jumper PIO9 is a special jumper and is used to put the module into adhoc mode. If you would like to communicate directly with the WiFly from a computer in an adhoc fashion, short the PIO9 jumper with solder.

Last, the WiFly has a small prototyping area to connect any other components you\'d like. You could add additional LEDs, sensors, motors, or other bits to make your project come alive.

### WiFly Breakout Board

You can also use the information in this tutorial to use the [WiFly GSX Breakout](https://www.sparkfun.com/products/10050). However, since the breakout board does not include an SPI-to-UART IC, you will have to either use a [separate conversion chip](https://www.sparkfun.com/products/9981) or communicate directly to the WiFly module over the UART. Keep in mind that if you do use the Arduino\'s UART to communicate to the module, you will not be able to send back repsonses to the termial window unless you use a seperate UART (The Arduino mega has several UARTs or you can you the SoftwareSerial library on an Uno).

## Connecting the WiFly Shield to the Arduino

### What You Will Need

To get the WiFly Shield up and networking, you'll need the following things:

- [WiFly Shield](https://www.sparkfun.com/products/9954)
- [Arduino UNO](https://www.sparkfun.com/products/11021?) or [similar Arduino compatible boards](https://learn.sparkfun.com/tutorials/arduino-comparison-guide)
- [Stackable Headers](https://www.sparkfun.com/products/10007) or another way to connect the shield to the Arduino
- [USB A-to-B Cable](https://www.sparkfun.com/products/512) or whichever USB cable your Arduino board needs
- A Computer
- A WiFi Access Point

### Assembly

Connecting the WiFly Shield to the Arduino is easy. Solder on the headers, and attach the shield to the Arduino board. You can use [male headers](https://www.sparkfun.com/products/116) or [stackable headers](https://www.sparkfun.com/search/results?term=stackable+headers&what=products), depending on how you intend to use your WiFly. For detailed instructions on how to connect headers to the WiFly shield, please see the [Arduino Shields tutorial](https://learn.sparkfun.com/tutorials/arduino-shields/installing-headers-preparation).

[![wifly shield with headers](https://cdn.sparkfun.com/r/600-600/assets/2/3/c/5/1/5201615a757b7f3f2066205b.jpg)](https://cdn.sparkfun.com/assets/2/3/c/5/1/5201615a757b7f3f2066205b.jpg)

*WiFly Shield with standard [strait male headers](https://www.sparkfun.com/products/116).*

Next, connect the Arduino to the computer through the USB cable. Some of the LEDs on the WiFly shield should now be blinking. You should see the yellow LED blinking quickly and the green LED blinking slowly. This indicates that the WiFly is open for new connections.

## WiFly Library and the Terminal Sketch

### WiFly Shield Library

To aid in the use of the WiFly shield, several authors have contributed to making a WiFly library. It has gone through several iterations, and, although it is not perfect, it allows the end user to easily get the WiFly up and running.

Interaction with the WiFly Shield will be done via the Arduino Serial monitor or a terminal program of your choice. In order to do this, we'll need an example sketch called SpiUartTerminal from the WiFly Shield github page. Use the following steps to install the library and sketch in the Arduino environment.

1.  Download the library code as a zip file from the [WiFly Shield github page](https://github.com/sparkfun/WiFly-Shield).
2.  Unzip the downloaded file into your \.../arduino/libraries/ folder
3.  Rename the unzipped folder "WiFly". This must be done because the Arduino environment does not accept library folder names with dashes in them.
4.  Start the Arduino IDE (or restart if it is open).

### The Terminal Sketch

Once you've installed the library, navigate to the example sketch

File-\>Examples-\>WiFlyShield-\>SpiUartTerminal

Load the sketch in tot he Arduino IDE. This sketch allows the user to communicate with the WiFly Shield directly through the Arduino serial monitor or any other terminal emulator.

Upload the sketch to the Arduino board, and open the Arduino serial monitor (or terminal emulator of your choice). Make sure the baud rate is set to 9600, 8-N-1-NONE.

[![alt text](//cdn.sparkfun.com/assets/b/f/e/d/8/51152676ce395f633f000002.jpg)](//cdn.sparkfun.com/assets/b/f/e/d/8/51152676ce395f633f000002.jpg)

The Arduino should now print out an info menu with instructions on how to use the sketch. We're now ready to configure the WiFly to connect to a network.

Please note that you will need to use this sketch a lot when working with your WiFly Shield. Anytime this tutorial references talking to the WiFly module, assume that it is referring to using this sketch to do so.

### Troubleshooting

- If you are experiencing problems with you WiFly Shield, make sure you are using the most up to date version of the library from GitHub. The Arduino IDE is constantly evolving, and, occasionally, the newest version might not work with existing libraries. If you can\'t get the WiFly shield to work with the latest version of the Arduino IDE, you may have to revert to an older version of the IDE. If you are using Arduino 0023 or older, you will want to use the [pre-Arduino 1.0 version](https://cdn.sparkfun.com/assets/5/0/a/5/0/52f00ca8ce395f82558b4568.zip) of the library.

- If you are seeing data that looks mostly right but is jumbled in places when you use the terminal sketch, the problem is most likely related to not having the correct library matched up with the correct version of the IDE.

## Connecting to a Network

The WiFly module is configured by sending it commands through its UART. To do this, the user must first place the module in command mode. For a complete list of configuration commands, please see the [RN-131 Reference Guide](http://ww1.microchip.com/downloads/en/DeviceDoc/50002230A.pdf).

To begin, put the module in command mode by typing the command

    $$$

into the Arduino Serial Monitor and pressing enter. (Make sure the serial monitor is set to **\"No line ending\"** when you type in the \$\$\$). The module will respond with the letters "CMD", indicating that it is in command mode. From this point on, commands that we send must be ended with a carriage return, so in the dropdown menu next to the baud rate menu, select **"Carriage return"**. This will ensure that the serial monitor sends a carriage return after every command you type in the send box.

[![alt text](//cdn.sparkfun.com/assets/4/0/c/b/c/51152752ce395fbb4f000000.jpg)](//cdn.sparkfun.com/assets/4/0/c/b/c/51152752ce395fbb4f000000.jpg)

Next, we need to scan for wifi networks. To do this type the command

    scan

You can skip this step if you already know the credentials of your wireless network. The WiFly module will scan for any networks and print the results to the terminal. We are concerned with the columns labeled "SSID" and "Sec". These are the name of the access point and the security protocol of the access point, respectively. We will need them to configure the WiFly to connect to the access point.

At this point, we'll need to tell the WiFly what security protocol to use. The security protocols have set values listed in the [RN131 reference guide](http://ww1.microchip.com/downloads/en/DeviceDoc/50002230A.pdf) on page 65.

[![alt text](https://cdn.sparkfun.com/assets/3/5/e/8/d/52f13d15ce395ff8328b4567.jpg)](https://cdn.sparkfun.com/assets/3/5/e/8/d/52f13d15ce395ff8328b4567.jpg)

Find the value that corresponds to the security protocol on your access point. Then, in the serial monitor, send the command

    set wlan auth <value>

where \\ is the number that corresponds to the access point's security protocol. This tells the WiFly to use that security protocol when connecting.

If your access point is using a security protocol, you will need to tell the WiFly your passphrase. To do this, send the command

    set wlan phrase <passphrase>

where \\ is the password to connect to the access point.

Now our module should be configured and ready to connect to the access point. Tell it to join by sending the command

    join <ssid>

Where \\ is the name of the access point you found during the scan. The WiFly module should now connect and print out information about your connection, such as the IP address.

[![alt text](//cdn.sparkfun.com/assets/8/1/3/d/7/51152c34ce395f573d000004.jpg)](//cdn.sparkfun.com/assets/8/1/3/d/7/51152c34ce395f573d000004.jpg)

Congrats, you are now networking from the Arduino!

### Autoconnect to a Network

If you would like the WiFly module to automatically connect to a network upon power up, follow the above directions. Instead of using the join command, you can store the SSID and tell the module to connect to that SSID by default.

Do so by using this command

    set wlan ssid <ssid>

where \\ is the name of the access point you\'d like to connect to automatically. Then use the command

    set wlan join 1

This tells the module to try and connect to the SSID stored in memory automatically.

The last thing is to store these settings in the WiFly\'s config file. We\'ll talk about this more in depth in the Configuration Files and Firmware Upgrade section, but, for now, just know that is where the WiFly stores all its settings. To do this, simply type

    save

Now, whenever you power up your WiFly, it should connect to that network without having to issue it any commands. To join to the network you just stored in memory without reseting the Arduino, issue just the `join` command without an parameters.

### Static IP

If you want your WiFly Shiled to have a static IP address instead of having one assigned via DHCP, you must first turn of DHCP and then set the IP address you want if it hasn\'t been set already. Using the Terminal sketch, enter command mode. Issue this command to turn of DHCP:

    set ip dhcp 0

Next you can assign the IP address you want using this command:

    set ip address <address>

### Troubleshooting

- If you already used the WiFly shield with DHCP on, there may already be an IP address stored in the WiFly\'s memory. You can keep this IP address as you static IP address, and you know that it will be available.

- If you upload any of the default example sketches that come with the WiFly library, you may overwrite the settings you just configured. If you are using an example sketch with a static IP, comment out the following lines in the Setup() function.

  if (!WiFly.join(ssid, passphrase))  }

This will prevent the sketch from overwriting your settings.

Also, check out the [Configuration Files](https://learn.sparkfun.com/tutorials/wifly-shield-hookup-guide/configuration-files-and-upgrading-the-firmware) section of this tutorial to see how you can save and load different settings profiles in case you do accidentally overwrite your settings.

- You may also need to change this line in any example sketch, if you plan on using a port other than 80.

  WiFlyServer server(80);

## Communicating with the Network

Now that the WiFly is connected, we'd like to communicate with the network. But how? What do we send? Where do we send it? The WiFly will transmit anything it's sent, the trick to successful networking is knowing where the data is going and how to package it.

When the WiFly connects to an access point, it communicates through a *port*. Ports are like sub-addresses, they indicate what type of information is being sent or received so that devices know how to use the sent data. For example, when trying to reach a website, a browser communicates on port 80, which is the HTTP port (hence the "http://" at the beginning of most URLs). The server "listens" on port 80, and when a browser request comes in, it sends the requested information back on port 80. There are thousands of port numbers, each with a different standardized protocol.

By default, the WiFly transmits and listens on port 2000. We can change the port by sending the command

    set ip local <port>

Where \\ is the port on which the WiFly will listen. To listen for HTTP requests from a browser, we send the command

    set ip local 80

Now, any computer that is also connected to the same access point as the WiFly can query the WiFly through a browser. Simply open a browser and attempt to navigate to

    http://<IP of WiFly>

The IP address of the WiFly is always printed when it joins a network, and you can always find it by sending the command

    get ip

when the device is in command mode.

When the WiFly receives a request from a browser, it will print the incoming data to the terminal. For example:

[![alt text](//cdn.sparkfun.com/assets/5/d/1/d/b/51154351ce395fe23f000001.jpg)](//cdn.sparkfun.com/assets/5/d/1/d/b/51154351ce395fe23f000001.jpg)

The browser is now waiting for data, the WiFly can send sensor values, serve web pages, or any other data straight back to the browser! In this case, the browser is waiting for a web page. If the WiFly responds with an HTML-formatted page, the browser will display it. The next section will show you exactly how to do that.

## Setting Up a Simple Server

In this example, you will create a simple server with your WiFly module. The functionallity will be simple, but you can take what you learn with this example to create more complex projects.

### Materials Needed

If you\'ve been following along, you should already have a WiFly shield attached to an Arduino. For this example, the only other items you will need are an [RGB LED](https://www.sparkfun.com/products/105) and three [330Ω resistors](https://www.sparkfun.com/products/8377). You will also need some wire or other means to connect the LED to the WiFly Shield.

### Assembly

In this example, the LED and resistors will be soldered directly to the shield. If you need a refresher on soldering, check out our [tutorial](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering). For those who don\'t want to solder to their shield, you can use a [breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard) to build the circuit.

Connect the LED and resistors to the shield like the image below. When working with a prototyping surface, don\'t forget that none of the through-holes are connected to one another. You must make solder connections on the underside of the shield to complete the circuit.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/2/6/a/0/7/52af8164757b7f83618b4568.jpg)](https://cdn.sparkfun.com/assets/2/6/a/0/7/52af8164757b7f83618b4568.jpg)

*Don\'t forget that the RGB LED has [polarity](https://learn.sparkfun.com/tutorials/polarity) and must be placed in the correct orientation.*

### Firmware

Once the hardware is wired up, it\'s time to upload the code. Copy the code below, and upload it to your Arduino, or you can download the sketch [here](https://cdn.sparkfun.com/assets/0/d/7/e/c/52f1857ece395f8f028b4569.zip). **Note:** Keep in mind that you must have gone through the previous steps to configure your WiFly module to connect to your network automatically.

    language:c
    /*********************************************************
    WiFi LED Controller
    Joel Bartlett
    SparkFun Electronics
    August 1, 2013

    This code uses an Arduino Uno with a SparkFun WiFly shield attached
    to act as a webserver cabable of controlling an RGB LED

    To use this code with Arduino 1.0+, it is recommended that you use
    the latest version of the WiFLy Library found here:
    https://github.com/sparkfun/WiFly-Shield
    Many thanks to Philip Lindsay (aka Follower) for creating this library
    and many thanks to jmr13031 for updating the library for Arduino 1.0+

    This code borrows heavily from the code found from Upverter.com
    https://gist.github.com/1201213
    Many thanks to Emmanuel DeVries for doing a lot of the heavy lifting.

    This also borrows from the Sparkfun Speakjet Wifly Example by Chris Taylor
    https://www.sparkfun.com/tutorials/158
    ***********************************************************/
    //I took out the credentials.h file as well as the code that 
    //tells the wifly server the ssid and the parephrase since
    //this info was setup manually on the WiFly shield.
    //The IP address is also set maually instead of being assigned. 

    #include <SPI.h>
    #include "WiFly.h" //include the WiFly experimental library

    char msg[128];//variables for reading in the html responses
    int letterCount = 0; 

    int redPin = 3; 
    int greenPin = 5; 
    int bluePin = 6; 

    WiFlyServer server(80);// This is set manually but this line is needed to initialize server()
                      //Port 80 is the default HTTP port

    ///////////////////////////////////////////////////////////////////
    void setup() 
    
    ///////////////////////////////////////////////////////////////////
    void loop() 
     else if (c == '\n')  else if (c != '\r') 

            //this is where the message that the user entered is going so this is where
            //we record it into a char array
            if (msgIsolator == 1) 
            

            if ((c == '\n' && current_line_is_blank && !client.available()) || endOfCode) 
            

            //if you want to see all data comming in and going out uncomment the line below
            //Serial.print(c);

            //We detect where the actual post data is in other words what the user entered
            //once we isolate it we can parse it and use it
            if (c =='%')
            
              if (dataFlag == 1)
              
              }
          }
        }

      // give the web browser time to receive the data
      delay(100);//delay is very important 
      client.flush();
      client.stop();
      }
    }
    ///////////////////////////////////////////////////////////////////////

    char recordMessage (char incomingMsg)
    
    ///////////////////////////////////////////////////////////////////////
    void checkAction() 
    // the first two or three letters of each message are read to determine which button was clicked on the webage
    
      //-------------------------------------------------------
      else if (msg[0] == 'G' && msg[1] == 'r' && msg[2] == 'e')//Turn on GREEN LED
      
      //-------------------------------------------------------
      else if (msg[0] == 'B' && msg[1] == 'l' && msg[2] == 'u')//Turn on BLUE LED
      

    }//end checkAction()

Once the code is uploaded, open the [Serial Terminal](https://learn.sparkfun.com/tutorials/terminal-basics) set to 9600. After a few seconds, the WiFly should print out its IP address. This will vary depending on if you are using DHCP or if you assigned a static IP.

[![alt text](https://cdn.sparkfun.com/assets/e/e/a/0/8/52af9475757b7f586f8b4567.jpg)](https://cdn.sparkfun.com/assets/e/e/a/0/8/52af9475757b7f586f8b4567.jpg)

In your browser, type the IP address that was printed out in the Terminal into the address bar. After a few seconds, you should see a web page with these three buttons load.

[![alt text](https://cdn.sparkfun.com/assets/d/6/f/e/a/52af9489757b7f36738b456f.jpg)](https://cdn.sparkfun.com/assets/d/6/f/e/a/52af9489757b7f36738b456f.jpg)

As long as everything is connected correctly, each button on the website should light up the corresponding LED when clicked. The change will not be instantaneous as the commands need to propagate from the browser, through the network, and to your WiFly shield.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/2/9/1/0/7/52af9843757b7f2a0e8b456c.jpg)](https://cdn.sparkfun.com/assets/2/9/1/0/7/52af9843757b7f2a0e8b456c.jpg)

You can even control it from your smart phone as long as it\'s connected to the same wireless network as the WiFly shield.

[![iphone screenshot](https://cdn.sparkfun.com/r/500-500/assets/f/8/5/b/f/52f181a6ce395f97518b4567.png)](https://cdn.sparkfun.com/assets/f/8/5/b/f/52f181a6ce395f97518b4567.png)

#### Troubleshooting

- Please note that data transmission of the wireless network is NOT instantaneous. It may take up to several seconds for your request to be sent to and processed by the Wifly shield depending on the size and configuration of your wireless network. If you are experiencing problems, there are many links in the chain to investigate.

It is also worth noting that the sketch prints data to the terminal by default. This will add some time to this delay. You can change this by commenting/uncommenting line 88.

    if (client.available()) 
          {
            c = client.read();
            delay(10);
            //Uncomment this line to see the HTTP respone
            //Serial.print(c);

- When you click any of the HTML buttons, you should see the green LED on the WiFly shield go solid while it processes the request. If you see that the LED is just hanging and never returns to blinking, then the WiFly shield is getting hung up on the HTML request. This could be the result of a firmware issue or a network/browser issue.

- If the red or yellow LED on the WiFly shield are blinking continuously, it is having a problem connecting to your wireless network. See the datasheet for more info on LED statuses.

- If you have a steady blinking green LED and your Arduino is printing out a valid IP address but you are not seeing a webpage load, then the problem is most likely in the code or in your wireless network settings. Makes sure you selected the correct security settings and make sure you **save** your settings to the WiFly config file after you have set all the necessary settings.

### Going Further

Try changing up the code to add different colors and more buttons. You can also take a look at the server example that comes with the WiFly library. This example reads the analog inputs on the Arduino and posts them to a webpage. See if you can add digital inputs and analog outputs to the same webpage. You could also replace the single RGB LED with a strip of RGB LEDS controlled via some MOSFETs. Then you could create an Internet controlled [LED Light Cube](https://www.sparkfun.com/news/1210)

## Configuration Files and Upgrading the Firmware

The firmware for the WiFly module is updated occasionally. Luckily for you, there is a simple way to update your module to the latest version.

The WiFly module sold by SparkFun Electronics currently ships with firmware **version 2.38**. To check which version of the firmware your WiFly shield is running, upload the Terminal sketch, enter command mode, and enter this command:

    ver

Note: The version is usually displayed after each command issued in command mode as well.

Before we update the firmware, let\'s go over the configuration files stored within the WiFly and how to add other config files.

### Storing Separate Configuration Files

Using the terminal sketch mentioned on the [WiFly Library page](https://learn.sparkfun.com/tutorials/wifly-shield-hookup-guide/wifly-library), create a connection to the module, and enter command mode.

Now issue the command

    ls

to list all the files on the module. Depending on what firmware version you have, you should see something like this:

[![ls config files](https://cdn.sparkfun.com/assets/0/7/6/4/b/52016cab757b7f37599dadff.jpg)](https://cdn.sparkfun.com/assets/0/7/6/4/b/52016cab757b7f37599dadff.jpg)

You\'ll notice the **WiFly_GSX-2.21** file is the current firmware version and the **config** file is where all of the settings are stored.

One great feature of the WiFly is its ability to store multiple configuration files. For instance, if you wanted to use the WiFly at both your home and your work, you could create two separate config files, each with the correct settings for both locations. To do so, set all the settings for one location such as SSID, pasphrase, security. etc. Then use the **save** command followed by the name you want to call that configuration.

[![alt text](https://cdn.sparkfun.com/assets/5/4/c/6/d/52016f7d757b7f7e35ca9b04.jpg)](https://cdn.sparkfun.com/assets/5/4/c/6/d/52016f7d757b7f7e35ca9b04.jpg)

*Notice that there is now two config files named home and work.*

Now, to use one of those config files, simply issue the **load** command followed by the name of the file. It\'s impotant to note that even though there are separate config files, the WiFly always uses what is stored in the default config file, so after you load a config file, it\'s best to save it to the default config file using just the **save** command.

[![alt text](https://cdn.sparkfun.com/assets/f/7/4/c/2/520171a0757b7f2c3cfcbaf1.jpg)](https://cdn.sparkfun.com/assets/f/7/4/c/2/520171a0757b7f2c3cfcbaf1.jpg)

Now, even after a firmware update, you should be able to load all of the settings you had before. (Note: Firmware updates will often include new features/settings, so there is no guarantee that your previous settings will work on a new version of the firmware.) You can delete a config file using the **del** command.

### Updating the Firmware

Directions on how to update the firmware can be found on [Microchip site](http://www.microchip.com/support/KBArticle.aspx?KBID=KB100349), but we will also go over the process here.

Again, use the terminal sketch to enter command mode. You must be connected to the Internet in order to get the firmware update from Roving Networks, so follow the directions on the [Connecting to a Network page](https://learn.sparkfun.com/tutorials/wifly-shield-hookup-guide/connecting-to-a-network) to connect to your wireless network.

While you are connected, you should still be able to issue commands. We now need to set the FTP settings on the module and point it to the correct website from which to retrieve the new firmware. Depending on 1) how old your module is and 2) how many settings you have changed, you may need to change several settings.

The first thing to check/change is the FTP settings. Issue the command

    get f

to see your current FTP settings.

[![ftp settings](https://cdn.sparkfun.com/assets/c/0/f/e/8/5201763e757b7f3759990684.jpg)](https://cdn.sparkfun.com/assets/c/0/f/e/8/5201763e757b7f3759990684.jpg)

To get the update, you must make sure the FTP address is the correct one. The Roving Networks page say the the firmware must be pulled from **rn.microchip.com**. Pinging this URL gives the correct IP address.

[![ping](https://cdn.sparkfun.com/assets/3/3/c/8/3/520176ec757b7f671e997ea5.jpg)](https://cdn.sparkfun.com/assets/3/3/c/8/3/520176ec757b7f671e997ea5.jpg)

Now, set the FTP address to the one returned during the ping, if it does not match the one stored in memory. Also make sure the user name and password match the ones in the image below. These should be the default values unless you changed them in your configuration.

[![set ftp](https://cdn.sparkfun.com/assets/c/9/f/5/a/520177a3757b7fdb1b5b1773.jpg)](https://cdn.sparkfun.com/assets/c/9/f/5/a/520177a3757b7fdb1b5b1773.jpg)

With all the correct settings, issue this command

    ftp update

You should see something like this:

[![ftp update](https://cdn.sparkfun.com/assets/c/3/1/f/b/520178cf757b7faf1caec7d0.jpg)](https://cdn.sparkfun.com/assets/c/3/1/f/b/520178cf757b7faf1caec7d0.jpg)

*Notice how the Ver is now 4.00*

Once the update has finished, you need to reboot the module, give it a factory RESET, and then reboot it again.

[![alt text](https://cdn.sparkfun.com/assets/0/d/3/6/5/520178cf757b7fcd1dc2daed.jpg)](https://cdn.sparkfun.com/assets/0/d/3/6/5/520178cf757b7fcd1dc2daed.jpg)

Failing to issue the factory RESET will result in config files not being saved correctly.

Now, using the **ls** command, we can see the new firmware. The old firmware is still stored in the module in case you need to revert back to an older version.

[![ls 2](https://cdn.sparkfun.com/assets/d/3/f/4/8/520179c6757b7fb61c301101.jpg)](https://cdn.sparkfun.com/assets/d/3/f/4/8/520179c6757b7fb61c301101.jpg)

To boot from an older firmware version, use the **boot image** command. In the image above, you can see that the older firmware (2.21) is stored in FL# 11. So we issue the boot image 11 command to get back to that version.

[![alt text](https://cdn.sparkfun.com/assets/9/6/4/4/f/52017f9b757b7f771cbf5504.jpg)](https://cdn.sparkfun.com/assets/9/6/4/4/f/52017f9b757b7f771cbf5504.jpg)

Again, it\'s best to reboot, RESET, and reboot after changing the firmware.

As of this writing, the most up to date version of the firmware that will be downloaded with this process is Ver 4.41.

### Troubleshooting

If you can\'t get the firmware to update, check the following:

- Make sure you are actually connected to the Internet.
- Make sure the FTP address is correct (198.175.253.161).
- Make sure the FTP port is correct (21).
- Make sure the FTP User=roving and the Pass=Pass123
- If all else fails, issue a factory RESET and then try updating the firmware.