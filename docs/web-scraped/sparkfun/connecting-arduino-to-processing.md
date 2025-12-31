# Source: https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing

## Introduction

So, you\'ve blinked some LEDs with [Arduino](http://arduino.cc), and maybe you\'ve even drawn some pretty pictures with [Processing](http://processing.org) - what\'s next? At this point you may be thinking, \'I wonder if there\'s a way to get Arduino and Processing to communicate to each other?\'. Well, guess what - there is! - and this tutorial is going to show you how.

In this tutorial we will learn:

- How to send data from Arduino to Processing over the serial port
- How to receive data from Arduino in Processing
- How to send data from Processing to Arduino
- How to receive data from Processing in Arduino
- How to write a serial \'handshake\' between Arduino and Processing to control data flow
- How to make a \'Pong\' game that uses analog sensors to control the paddles

Before we get started, there are a few things you should be certain you\'re familiar with to get the most out of this tutorial:

- [What\'s an Arduino?](https://learn.sparkfun.com/tutorials/what-is-an-arduino)
- [How to use a breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [Working with wire](https://learn.sparkfun.com/tutorials/working-with-wire)
- [What is serial communication?](https://learn.sparkfun.com/tutorials/serial-communication)
- Some basic familiarity with [Processing](http://processing.org) will be useful, but not strictly necessary.

## Looking for the right Arduino?

Check out our **[Arduino Comparison Guide](https://www.sparkfun.com/standard_arduino_comparison_guide)**! We\'ve compiled every Arduino development board we carry, so you can quickly compare them to find the perfect one for your needs.

[Take me there!](https://www.sparkfun.com/standard_arduino_comparison_guide)

![Arduino Comparison](https://cdn.sparkfun.com/assets/learn_tutorials/5/0/arduino-comparison.jpg)

## From Arduino\... 

Let\'s start with the Arduino side of things. We\'ll show you the basics of how to set up your Arduino sketch to send information over serial.

- First things first. If you haven\'t done so yet, [download and install the Arduino software](http://arduino.cc/en/Main/Software) for your operating system. [Here\'s a tutorial](https://learn.sparkfun.com/tutorials/installing-arduino) if you get stuck.
- You\'ll also need an Arduino-compatible microcontroller and an appropriate way to connect it to your computer (an A-to-B USB cable, micro USB, or FTDI breakout). Check [this comparison guide](https://learn.sparkfun.com/tutorials/arduino-comparison-guide) if you\'re not sure what\'s right for you.

Ok. You should by this point have the Arduino software installed, an Arduino board of some kind, and a cable. Now for some coding! Don\'t worry, it\'s quite straightforward.

- Open up the Arduino software. You should see something like this:

[![alt text](https://cdn.sparkfun.com/assets/e/5/d/d/0/51894727ce395fe854000000.png)](https://cdn.sparkfun.com/assets/e/5/d/d/0/51894727ce395fe854000000.png)

The nice big white space is where we are going to write our code. Click in the white area and type the following (or copy and paste if you feel lazy):

    language:cpp
    void setup() 
    

This is called our setup method. It\'s where we \'set up\' our program. Here, we\'re using it to start serial communication from the Arduino to our computer at a baud rate of 9600. For now, all you need to now about baud rate is that (basically) it\'s the rate at which we\'re sending data to the computer, and if we\'re sending and receiving data at different rates, everything goes all gobbledy-gook and one side can\'t understand the other. This is bad.

After our `setup()` method, we need a method called `loop()`, which is going to repeat over and over as long as our program is running. For our first example, we\'ll just send the string \'Hello, world!\' over the serial port, over and over (and over). Type the following in your Arduino sketch, below the code we already wrote:

    language:cpp
    void loop()
    

That\'s all we need for the Arduino side of our first example. We\'re setting up serial communication from the Arduino and telling it to send data every 100 milliseconds. Your Arduino sketch should now look something like this:

[![alt text](https://cdn.sparkfun.com/assets/b/3/c/f/b/51895ebece395f3b55000001.png)](https://cdn.sparkfun.com/assets/b/3/c/f/b/51895ebece395f3b55000001.png)

All that\'s left to do is to plug in your Arduino board, select your board type (under Tools -\> Board Type) and your Serial port (under Tools -\> Serial Port) and hit the \'upload\' button to load your code onto the Arduino.

Now we\'re ready to see if we can magically (or through code) detect the \'Hello, world!\' string we\'re sending from Processing.

## \...to Processing

Our task now is to find a way to listen in on what our Arduino sketch is sending. Luckily, Processing comes with a Serial library designed for just this kind of thing! If you don\'t have a version of Processing, make sure you go to [Processing.org](http://processing.org) and download the latest version for your operating system. Once Processing is installed, open it up. You should see something like this:

[![alt text](https://cdn.sparkfun.com/assets/4/b/8/6/b/518961ffce395f9d54000000.png)](https://cdn.sparkfun.com/assets/4/b/8/6/b/518961ffce395f9d54000000.png)

Looks a lot like Arduino, huh? The Arduino software was actually based in part off of Processing - that\'s the beauty of open-source projects. Once we have an open sketch, our first step is to import the Serial library. Go to Sketch-\>Import Library-\>Serial, as shown below:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/d/2/e/5/b/5189644fce395fc86e000000.png)](https://cdn.sparkfun.com/assets/d/2/e/5/b/5189644fce395fc86e000000.png)

You should now see a line like `import processing.serial.*;` at the top of your sketch. Magic! Underneath our import statement we need to declare some global variables. All this means is that these variables can used anywhere in our sketch. Add these two lines beneath the import statement:

    language:java
    Serial myPort;  // Create object from Serial class
    String val;     // Data received from the serial port

In order to listen to any serial communication we have to get a Serial object (we call it `myPort` but you can it whatever you like), which lets us listen in on a serial port on our computer for any incoming data. We also need a variable to recieve the actual data coming in. In this case, since we\'re sending a String (the sequence of characters \'Hello, World!\') from Arduino, we want to receive a String in Processing. Just like Arduino has `setup()` and `loop()`, Processing has `setup()` and `draw()` (instead of loop).

For our `setup()` method in Processing, we\'re going to find the serial port our Arduino is connected to and set up our Serial object to listen to that port.

    language:java
    void setup()
    

Remember how we set `Serial.begin(9600)` in Arduino? Well, if we don\'t want that gobbledy-gook I was talking about, we had better put 9600 as that last argument in our Serial object in Processing as well. This way Arduino and Processing are communicating at the same rate. Happy times!

In our `draw()` loop, we\'re going to listen in on our Serial port and we get something, stick that something in our `val` variable and print it to the console (that black area at the bottom of your Processing sketch).

    language:java
    void draw()
     
    println(val); //print it out in the console
    }

Ta-Da! If you hit the \'run\' button (and your Arduino is plugged in with the code on the previous page loaded up), you should see a little window pop-up, and after a sec you should see \`Hello, World!\' appear in the Processing console. Over and over. Like this:

[![alt text](https://cdn.sparkfun.com/assets/4/4/6/9/4/51ae08bace395f6f1b000000.png)](https://cdn.sparkfun.com/assets/4/4/6/9/4/51ae08bace395f6f1b000000.png)

Excellent! We\'ve now conquered how to send data from Arduino to Processing. Our next step is figure out how go the opposite way - sending data from Processing to Arduino.

## From Processing\... 

So we\'ve sent data from Arduino to Processing, but what if we want to send data the other way - from Processing to Arduino? Piece of cake!

Let\'s start with the Processing side of things. It starts out much like our last sketch: we import the Serial library and declare a global Serial object variable for our port up top, and in our `setup()` method we find our port and initialize Serial communication on that port with our Serial variable at 9600 baud. We\'re also going to use the `size()` command, to give us a little window to click in, which will trigger our sketch to send something over the Serial port to Arduino.

    language:java
    import processing.serial.*;

    Serial myPort;  // Create object from Serial class

    void setup() 
    

In our `draw()` loop, we send whatever we want over the serial port by using the `write` method from the Processing Serial library. For this sketch, we will send a \'1\' whenever we click our mouse in the Processing window. We\'ll also print it out on the console, just to see that we\'re actually sending something. If we aren\'t clicking we\'ll send a \'0\' instead.

    language:java
    void draw()  else 
         
    }

This is what your code should look like at this point:

[![alt text](https://cdn.sparkfun.com/assets/5/2/c/b/5/51a51ac5ce395f2a24000001.png)](https://cdn.sparkfun.com/assets/5/2/c/b/5/51a51ac5ce395f2a24000001.png)

If you run this code, you should see a bunch of 1\'s appear in the console area whenever you click your mouse in the window. Neat! But how do we look for these 1\'s from Arduino? And what can we do with them?

## \...to Arduino

Ok! On this page we\'re going to look for those 1\'s coming in from Processing, and, if we see them, we\'re going to turn on an LED on pin 13 (on some Arduinos, like the Uno, pin 13 is the on-board LED, so you don\'t need an external LED to see this work).

At the top of our Arduino sketch, we need two global variables - one for holding the data coming from Processing, and another to tell Arduino which pin our LED is hooked up to.

    language:cpp
     char val; // Data received from the serial port
     int ledPin = 13; // Set the pin to digital I/O 13

Next, in our `setup()` method, we\'ll set the LED pin to an output, since we\'re powering an LED, and we\'ll start Serial communication at 9600 baud.

    language:cpp
     void setup() 

Finally, in the `loop()` method, we\'ll look at the incoming serial data. If we see a \'1\', we set the LED to HIGH (or on), and if we don\'t (e.g. we see a \'0\' instead), we turn the LED off. At the end of the loop, we put in a small delay to help the Arduino keep up with the serial stream.

    language:cpp
     void loop() 
       if (val == '1') 
        else 
       delay(10); // Wait 10 milliseconds for next reading
    }

This is what your code should look like when you\'re done:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/f/2/3/b/6/51a51dfcce395fe124000001.png)](https://cdn.sparkfun.com/assets/f/2/3/b/6/51a51dfcce395fe124000001.png)

Voila! If we load up this code onto our Arduino, and run the Processing sketch from the previous page, you should be able to turn on an LED attached to pin 13 of your Arduino, simply by clicking within the Processing canvas.

## Shaking Hands (Part 1)

So far we\'ve shown that Arduino and Processing can communicate via serial when one is talking and the other is listening. Can we make a link that allows data to flow both ways, so that Arduino and Processing are both sending *and* receiving data? You bet! In the biz we call this a serial \'handshake\', since both sides have to agree when to send and receive data.

On this page and the next, we\'re going to combine our two previous examples in such a way that Processing can both receive \'Hello, world!\' from Arduino AND send a 1 back to Arduino to toggle an LED. Of course, this also means that Arduino has to be able to send \'Hello, world!\' while listening for a 1 from Processing. Whew!

Let\'s start with the Arduino side of things. In order for this to run smoothly, both sides have to know what to listen for and what the other side is expecting to hear. We also want to minimize traffic over the serial port so we get more timely responses.

Just like in our Serial read example, we need a variable for our incoming data and a variable for the LED pin we want to light up:

    language:cpp
    char val; // Data received from the serial port
    int ledPin = 13; // Set the pin to digital I/O 13
    boolean ledState = LOW; //to toggle our LED

Since we\'re trying to be efficient, we\'re going to change our code so that we only listen for 1\'s, and each time we hear a \'1\' we toggle the LED on or off. To do this we added a boolean (true or false) variable for the HIGH or LOW state of our LED. This means we don\'t have to constantly send a 1 or 0 from Processing, which frees up our serial port quite a bit.

Our `setup()` method looks mostly the same, with the addition of an `establishContact()` function which we\'ll get to later - for now just type it in.

    language:cpp
    void setup() 
    

In our loop function, we\'ve just combined and slimmed down the code from our two earlier sketches. Most importantly, we\'ve changed our LED code to toggle based on our new boolean value. The \'!\' means every time we see a one, we set the boolean to the opposite of what it was before (so LOW becomes HIGH or vice-versa). We also put our \'Hello, world!\' in an else statement, so that we\'re only sending it when we haven\'t seen a \'1\' come in.

    language:cpp
    void loop()
    
        delay(100);
      } 
        else 
    }

Now we get to that `establishContact()` function we put in our `setup()` method. This function just sends out a string (the same one we\'ll need to look for in Processing) to see if it hears anything back - indicating that Processing is ready to receive data. It\'s like saying \'Marco\' over and over until you hear a \'Polo\' back from somewhere.

    language:cpp
    void establishContact() 
    }

Your Arduino code should look like this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/f/a/1/4/6/51ae469bce395f3536000000.png)](https://cdn.sparkfun.com/assets/f/a/1/4/6/51ae469bce395f3536000000.png)

That\'s it for the Arduino side, now on to Processing!

## Shaking Hands (Part 2)

For the Processing side of things, we\'ve got to make a few changes. We\'re going to make use of the `serialEvent()` method, which gets called every time we see a specific character in the serial buffer, which acts as our delimiter - basically it tells Processing that we\'re done with a specific \'chunk\' of data - in our case, one \'Hello, world!\'.

The beginning of our sketch is the same except for a new `firstContact` boolean, which let\'s us know when we\'ve made a connection to Arduino.

    language:java
    import processing.serial.*; //import the Serial library
     Serial myPort;  //the Serial port object
     String val;
    // since we're doing serial handshaking, 
    // we need to check if we've heard from the microcontroller
    boolean firstContact = false;

Our `setup()` function is the same as it was for our serial write program, *except* we added the `myPort.bufferUntil('\n');` line. This let\'s us store the incoming data into a buffer, until we see a specific character we\'re looking for. In this case, it\'s a carriage return (\\n) because we sent a Serial.print*ln* from Arduino. The \'ln\' at the end means the String is terminated with a carriage return, so we know that\'ll be the last thing we see.

    language:java
    void setup() 

Because we\'re continuously sending data, our `serialEvent()` method now acts as our new `draw()` loop, so we can leave it empty:

    language:java
    void draw() 

Now for the big one: `serialEvent()`. Each time we see a carriage return this method gets called. We need to do a few things each time to keep things running smoothly:

- read the incoming data
- see if there\'s actually anything in it (i.e. it\'s not empty or \'null\')
- trim whitespace and other unimportant stuff
- if it\'s our first time hearing the right thing, change our `firstContact` boolean and let Arduino know we\'re ready for more data
- if it\'s *not* our first run, print the data to the console and send back any valid mouse clicks (as 1\'s) we got in our window
- finally, tell Arduino we\'re ready for more data

That\'s a lot of steps, but luckily for us Processing has functions that make most of these tasks pretty easy. Let\'s take a look at how it all breaks down:

    language:java
    void serialEvent( Serial myPort) 
      }
      else 

        // when you've parsed the data you have, ask for more:
        myPort.write("A");
        }
      }
    }

Oof. That\'s a lot to chew on, but if you read carefully line by line (especially the comments), it\'ll start to make sense. If you\'ve got your Arduino code finished and loaded onto your board, try running this sketch. You should see \'Hello, world!\' coming in on the console, and when you click in the Processing window, you should see the LED on pin 13 turn on and off. Success! You are now a serial handshake expert.

## Tips and Tricks

In developing your own projects with Arduino and Processing, there are a few \'gotchas\' that are helpful to keep in mind in case you get stuck.

- make sure your baud rates match
- make sure you\'re reading off the right port in Processing - there\'s a `Serial.list()` command that will show you all the available ports you can connect to.
- if you\'re using the `serialEvent()` method, make sure to include the `port.bufferUntil()` function in your `setup()` method.
- also, make sure that whatever character you\'re buffering until (e.g., \'\\n\') is a character that you\'re actually sending from Arduino.
- If you want to send over a number of sensor values, it\'s a good idea to count how many bytes you\'re expecting so you know how to properly parse out the sensor data. (the example (shown below) that comes with Arduino gives a great example of this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/a/7/9/0/8/51ae5ff4ce395f4836000000.png)](https://cdn.sparkfun.com/assets/a/7/9/0/8/51ae5ff4ce395f4836000000.png)

*This is the example to select for some good sensor parsing code*