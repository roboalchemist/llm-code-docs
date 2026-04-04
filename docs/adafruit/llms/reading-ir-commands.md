# Source: https://learn.adafruit.com/ir-sensor/reading-ir-commands.md

# IR Sensor

## Reading IR Commands

For our final project, we will use a remote control to send messages to a microcontroller. For example, this might be useful for a robot that can be directed with an IR remote. It can also be good for projects that you want to control from far away, without wires.

For a remote in this example we'll be using an Apple clicker remote. You can use any kind of remote you wish, or you can steal one of these from an unsuspecting hipster.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/594/medium800/light_appleremote.jpeg?1396764356)

We'll use the code from our previous sketch for raw IR reading but this time we'll edit our printer-outer to have it give us the pulses in a C array, this will make it easier for us to use for pattern matching.```
void printpulses(void) {
  Serial.println("\n\r\n\rReceived: \n\rOFF \tON");
  for (uint8_t i = 0; i &lt; currentpulse; i++) {
    Serial.print(pulses[i][0] * RESOLUTION, DEC);
    Serial.print(" usec, ");
    Serial.print(pulses[i][1] * RESOLUTION, DEC);
    Serial.println(" usec");
  }
 
  // print it in a 'array' format
  Serial.println("int IRsignal[] = {");
  Serial.println("// ON, OFF (in 10's of microseconds)");
  for (uint8_t i = 0; i &lt; currentpulse-1; i++) {
    Serial.print("\t"); // tab
    Serial.print(pulses[i][1] * RESOLUTION / 10, DEC);
    Serial.print(", ");
    Serial.print(pulses[i+1][0] * RESOLUTION / 10, DEC);
    Serial.println(",");
  }
  Serial.print("\t"); // tab
  Serial.print(pulses[currentpulse-1][1] * RESOLUTION / 10, DEC);
  Serial.print(", 0};");
}
```

I uploaded the new sketch and pressed the&nbsp; **Play** &nbsp;button on the Apple remote and got the following:

```
int IRsignal[] = { // ON, OFF (in 10's of microseconds) 
912, 438, 
68, 48, 
68, 158, 
68, 158, 
68, 158, 
68, 48, 
68, 158,  
68, 158,  
68, 158,  
70, 156,  
70, 158,  
68, 158,  
68, 48, 
68, 46,  
70, 46,  
68, 46,  
68, 160,  
68, 158,  
70, 46,  
68, 158,  
68, 46,  
70, 46,
68, 48,  
68, 46,  
68, 48,  
66, 48,  
68, 48,  
66, 160,  
66, 50,  
66, 160,  
66, 52,  
64, 160, 
66, 48,  
66, 3950,  
908, 214, 
66, 3012, 
908, 212, 
68, 0};
```

We'll try to detect that code.

Let's start a new sketch called&nbsp;**IR Commander&nbsp;(you can download the final code from GitHub at the green button below or click Download Project Zip in the complete code listing).&nbsp;**

[Open the GitHub repo for the code on this page](https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/master/IR_Sensor/Arduino/IR_Commander/ircommander.ino)
https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/IR_Sensor/Arduino/IR_Commander/IR_Commander.ino

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/IR_Sensor/Arduino/IR_Commander/ircommander.h

This code uses parts of our previous sketch. The first part we'll do is to create a function that just listens for an IR code an puts the pulse timings into the&nbsp;**pulses[]**&nbsp;array. It will return the number of pulses it heard as a return-value.

```
int listenForIR(void) {
  currentpulse = 0;
 
  while (1) {
    uint16_t highpulse, lowpulse;  // temporary storage timing
    highpulse = lowpulse = 0; // start out with no pulse length
 
//  while (digitalRead(IRpin)) { // this is too slow!
    while (IRpin_PIN &amp; (1 &lt;&lt; IRpin)) {
       // pin is still HIGH
 
       // count off another few microseconds
       highpulse++;
       delayMicroseconds(RESOLUTION);
 
       // If the pulse is too long, we 'timed out' - either nothing
       // was received or the code is finished, so print what
       // we've grabbed so far, and then reset
       if ((highpulse &gt;= MAXPULSE) &amp;&amp; (currentpulse != 0)) {
         return currentpulse;
       }
    }
    // we didn't time out so lets stash the reading
    pulses[currentpulse][0] = highpulse;
 
    // same as above
    while (! (IRpin_PIN &amp; _BV(IRpin))) {
       // pin is still LOW
       lowpulse++;
       delayMicroseconds(RESOLUTION);
       if ((lowpulse &gt;= MAXPULSE)  &amp;&amp; (currentpulse != 0)) {
         return currentpulse;
       }
    }
    pulses[currentpulse][1] = lowpulse;
 
    // we read one high-low pulse successfully, continue!
    currentpulse++;
  }
}
```

Our new&nbsp;**loop()**&nbsp;will start out just listening for pulses

```
void loop(void) {
  int numberpulses;
 
  numberpulses = listenForIR();
 
  Serial.print("Heard ");
  Serial.print(numberpulses);
  Serial.println("-pulse long IR signal");
}
```

When we run this it will print out something like...![](https://cdn-learn.adafruit.com/assets/assets/000/000/595/medium800/light_pulsecounter.gif?1447976294)

OK time to make the sketch compare what we received to what we have in our stored array:![](https://cdn-learn.adafruit.com/assets/assets/000/000/596/medium800/light_ircompare.gif?1447976302)

As you can see, there is some variation. So when we do our comparison we can't look for preciesely the same values, we have to be a little 'fuzzy'. We'll say that the values can vary by 20% - that should be good enough.```
// What percent we will allow in variation to match the same code \\ #define FUZZINESS 20
 
void loop(void) {
  int numberpulses;
 
  numberpulses = listenForIR();
 
  Serial.print("Heard ");
  Serial.print(numberpulses);
  Serial.println("-pulse long IR signal");
 
  for (int i=0; i&lt; numberpulses-1; i++) {
    int oncode = pulses[i][1] * RESOLUTION / 10;
    int offcode = pulses[i+1][0] * RESOLUTION / 10;
 
    Serial.print(oncode); // the ON signal we heard
    Serial.print(" - ");
    Serial.print(ApplePlaySignal[i*2 + 0]); // the ON signal we want 
 
    // check to make sure the error is less than FUZZINESS percent
    if ( abs(oncode - ApplePlaySignal[i*2 + 0]) &lt;= (oncode * FUZZINESS / 100)) {
      Serial.print(" (ok)");
    } else {
      Serial.print(" (x)");
    }
    Serial.print("  \t"); // tab
 
    Serial.print(offcode); // the OFF signal we heard
    Serial.print(" - ");
    Serial.print(ApplePlaySignal[i*2 + 1]); // the OFF signal we want 
 
    if ( abs(offcode - ApplePlaySignal[i*2 + 1]) &lt;= (offcode * FUZZINESS / 100)) {
      Serial.print(" (ok)");
    } else {
      Serial.print(" (x)");
    }
 
    Serial.println();
  }
}
```

![](https://cdn-learn.adafruit.com/assets/assets/000/000/597/medium800/light_codecompareok.gif?1447976311)

This loop, as it goes through each pulse, does a little math. It compares the absolute (**abs()**) difference between the code we heard and the code we're trying to match abs(oncode - ApplePlaySignal[i\*2 + 0]) and then makes sure that the error is less than FUZZINESS percent of the code length (oncode \* FUZZINESS / 100)

We found we had to tweak the stored values a little to make them match up 100% each time. IR is not a precision-timed protocol so having to make the FUZZINESS 20% or more is not a bad thing

Finally, we can turn the&nbsp;**loop()**&nbsp;into its own function which will return&nbsp; **true** &nbsp;or&nbsp; **false** &nbsp;depending on whether it matched the code we ask it to. We also commented out the printing functions

```
boolean IRcompare(int numpulses, int Signal[]) {
 
  for (int i=0; i&lt; numpulses-1; i++) {
    int oncode = pulses[i][1] * RESOLUTION / 10;
    int offcode = pulses[i+1][0] * RESOLUTION / 10;
 
    /*
    Serial.print(oncode); // the ON signal we heard
    Serial.print(" - ");
    Serial.print(Signal[i*2 + 0]); // the ON signal we want 
    */
 
    // check to make sure the error is less than FUZZINESS percent
    if ( abs(oncode - Signal[i*2 + 0]) &lt;= (Signal[i*2 + 0] * FUZZINESS / 100)) {
      //Serial.print(" (ok)");
    } else {
      //Serial.print(" (x)");
      // we didn't match perfectly, return a false match
      return false;
    }
 
    /*
    Serial.print("  \t"); // tab
    Serial.print(offcode); // the OFF signal we heard
    Serial.print(" - ");
    Serial.print(Signal[i*2 + 1]); // the OFF signal we want 
    */
 
    if ( abs(offcode - Signal[i*2 + 1]) &lt;= (Signal[i*2 + 1] * FUZZINESS / 100)) {
      //Serial.print(" (ok)");
    } else {
      //Serial.print(" (x)");
      // we didn't match perfectly, return a false match
      return false;
    }
 
    //Serial.println();
  }
  // Everything matched!
  return true;
}
```

We then took more IR command data for the 'rewind' and 'fastforward' buttons and put all the code array data into&nbsp; **ircodes.h&nbsp;** to keep the main sketch from being too long and unreadable&nbsp;[(you can get all the code from github)](http://github.com/adafruit/IR-Commander)

Finally, the main loop looks like this:

```
void loop(void) {
  int numberpulses;
 
  numberpulses = listenForIR();
 
  Serial.print("Heard ");
  Serial.print(numberpulses);
  Serial.println("-pulse long IR signal");
  if (IRcompare(numberpulses, ApplePlaySignal)) {
    Serial.println("PLAY");
  }
    if (IRcompare(numberpulses, AppleRewindSignal)) {
    Serial.println("REWIND");
  }
    if (IRcompare(numberpulses, AppleForwardSignal)) {
    Serial.println("FORWARD");
  }
}
```

We check against all the codes we know about and print out whenever we get a match. You could now take this code and turn it into something else, like a robot that moves depending on what button is pressed.

After testing, success!

![](https://cdn-learn.adafruit.com/assets/assets/000/000/598/medium800/light_mulitirbutton.gif?1447976321)

- [Previous Page](https://learn.adafruit.com/ir-sensor/making-an-intervalometer.md)
- [Next Page](https://learn.adafruit.com/ir-sensor/circuitpython.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### IR (Infrared) Receiver Sensor

[IR (Infrared) Receiver Sensor](https://www.adafruit.com/product/157)
IR sensor tuned to 38KHz, perfect for receiving commands from a TV remote control. Runs at 3V to 5V so it's great for any microcontroller.  
  
To use, connect pin 3 (all the way to the right) to 5V power, pin 2 (middle) to ground and listen on pin 1. It doesn't do any decoding...

In Stock
[Buy Now](https://www.adafruit.com/product/157)
[Related Guides to the Product](https://learn.adafruit.com/products/157/guides)
### Super-bright 5mm IR LED

[Super-bright 5mm IR LED](https://www.adafruit.com/product/387)
Infrared LEDs are used for remote controls (they're the little LED in the part you point at your TV) and 'night-vision' cameras, and these little blue guys are high powered ones! They are 940nm wavelength, which is what nearly all devices listen to. They're 20 degree beamwidth,...

In Stock
[Buy Now](https://www.adafruit.com/product/387)
[Related Guides to the Product](https://learn.adafruit.com/products/387/guides)
### Mini Remote Control

[Mini Remote Control](https://www.adafruit.com/product/389)
This little remote control would be handy for controlling a robot or other project from across the room. It has 21 buttons and a layout we thought was handy: directional buttons and number entry buttons. The remote uses the NEC encoding type and sends data codes 0 thru 26 (it skips #3, #7,...

In Stock
[Buy Now](https://www.adafruit.com/product/389)
[Related Guides to the Product](https://learn.adafruit.com/products/389/guides)
### Super-bright 5mm IR LED (25 pack)

[Super-bright 5mm IR LED (25 pack)](https://www.adafruit.com/product/388)
Infrared LEDs are used for remote controls (they're the little LED in the part you point at your TV) and 'night-vision' cameras, and these little blue guys are high powered ones! They are 940nm wavelength, which is what nearly all devices listen to. They're 20 degree beamwidth,...

In Stock
[Buy Now](https://www.adafruit.com/product/388)
[Related Guides to the Product](https://learn.adafruit.com/products/388/guides)
### Adafruit METRO 328 - Arduino Compatible - with Headers

[Adafruit METRO 328 - Arduino Compatible - with Headers](https://www.adafruit.com/product/2488)
This is the&nbsp; **Adafruit METRO Arduino-Compatible - with&nbsp;headers.&nbsp;** It's a fully assembled and tested microcontroller and physical computing board with through-hole headers attached.&nbsp; If you don't want a&nbsp;Metro with the headers attached for...

In Stock
[Buy Now](https://www.adafruit.com/product/2488)
[Related Guides to the Product](https://learn.adafruit.com/products/2488/guides)

## Related Guides

- [RePaper eInk Development Board](https://learn.adafruit.com/repaper-eink-development-board.md)
- [Adafruit MSA301 Triple Axis Accelerometer](https://learn.adafruit.com/msa301-triple-axis-accelerometer.md)
- [Bluetooth Controlled Motorized Camera Slider](https://learn.adafruit.com/bluetooth-motorized-camera-slider.md)
- [Adafruit  PCA9685 16-Channel Servo Driver](https://learn.adafruit.com/16-channel-pwm-servo-driver.md)
- [Adalight Project Pack](https://learn.adafruit.com/adalight-diy-ambient-tv-lighting.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [Introducing Adafruit Trellis ](https://learn.adafruit.com/adafruit-trellis-diy-open-source-led-keypad.md)
- [Sending an SMS with Temboo](https://learn.adafruit.com/sending-an-sms-with-temboo.md)
- [20mm LED Pixels](https://learn.adafruit.com/20mm-led-pixels.md)
- [Remote controlled door lock using a fingerprint sensor & Adafruit IO](https://learn.adafruit.com/remote-controlled-door-lock-using-a-fingerprint-sensor-and-adafruit-io.md)
- [Character LCDs](https://learn.adafruit.com/character-lcds.md)
- [Smart Measuring Cup](https://learn.adafruit.com/smart-measuring-cup.md)
- [Memories of an Arduino](https://learn.adafruit.com/memories-of-an-arduino.md)
- [Arduino Lesson 2. LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds.md)
- [Smart Cocktail Shaker](https://learn.adafruit.com/smart-cocktail-shaker.md)
