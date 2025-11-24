# Source: https://learn.adafruit.com/force-sensitive-resistor-fsr/using-an-fsr.md

# Force Sensitive Resistor (FSR)

## Using an FSR

## Analog Voltage Reading Method
The easiest way to measure a resistive sensor is to connect one end to Power and the other to a&nbsp; **pull-down** &nbsp;resistor to ground. Then the point between the fixed pulldown resistor and the variable FSR resistor is connected to the analog input of a microcontroller such as an Arduino (shown).  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/434/medium800/force___flex_fsrpulldowndia.png?1396762989)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/435/medium800/force___flex_fsrpulldownsch.gif?1447975571)

For this example I'm showing it with a 5V supply but note that you can use this with a 3.3v supply just as easily. In this configuration the analog voltage reading ranges from 0V (ground) to about 5V (or about the same as the power supply voltage).

The way this works is that as the resistance of the FSR decreases, the total resistance of the FSR and the pulldown resistor decreases from about 100Kohm to 10Kohm. That means that the current flowing through both resistors&nbsp;_increases_&nbsp;which in turn causes the voltage across the fixed 10K resistor to increase. Its quite a trick!

| Force (lb) | Force (N) | FSR Resistance | (FSR + R) ohm  
 | Current thru FSR+R | Voltage across R |
| --- | --- | --- | --- | --- | --- |
| None | None | Infinite | Infinite! | 0 mA | 0V |
| 0.04 lb | 0.2 N | 30 Kohm | 40 Kohm | 0.13 mA | 1.3 V |
| 0.22 lb | 1 N | 6 Kohm | 16 Kohm | 0.31 mA | 3.1 V |
| 2.2 lb | 10 N | 1 Kohm | 11 Kohm | 0.45 mA | 4.5 V |
| 22 lb | 100 N | 250 ohm  
 | 10.25 Kohm | 0.49 mA | 4.9 V |

  
  
_This table indicates the approximate analog voltage based on the sensor force/resistance w/a 5V supply and 10K pulldown resistor._

Note that our method takes the somewhat linear resistivity but does not provide linear voltage! That's because the voltage equasion is:

**Vo = Vcc ( R / (R + FSR) )**

That is, the voltage is proportional to the&nbsp; **inverse** &nbsp;of the FSR resistance.

## Simple Demonstration of Use
Wire the FSR as same as the above example, but this time lets add an LED to pin 11.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/436/medium800/force___flex_FSRandLED.png?1396763015)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/437/medium800/force___flex_FSRledsch.gif?1447975580)

This sketch will take the analog voltage reading and use that to determine how bright the red LED is. The harder you press on the FSR, the brighter the LED will be! Remember that the LED has to be connected to a PWM pin for this to work, I use pin 11 in this example.

These examples assume you know some basic Arduino programming. If you don't,&nbsp;[maybe spend some time reviewing the basics at the Arduino tutorial?](http://www.ladyada.net/learn/arduino/index.html)

```
/* FSR testing sketch. 
 
Connect one end of FSR to 5V, the other end to Analog 0.
Then connect one end of a 10K resistor from Analog 0 to ground
Connect LED from pin 11 through a resistor to ground 
 
For more information see www.ladyada.net/learn/sensors/fsr.html */
 
int fsrAnalogPin = 0; // FSR is connected to analog 0
int LEDpin = 11;      // connect Red LED to pin 11 (PWM pin)
int fsrReading;      // the analog reading from the FSR resistor divider
int LEDbrightness;
 
void setup(void) {
  Serial.begin(9600);   // We'll send debugging information via the Serial monitor
  pinMode(LEDpin, OUTPUT);
}
 
void loop(void) {
  fsrReading = analogRead(fsrAnalogPin);
  Serial.print("Analog reading = ");
  Serial.println(fsrReading);
 
  // we'll need to change the range from the analog reading (0-1023) down to the range
  // used by analogWrite (0-255) with map!
  LEDbrightness = map(fsrReading, 0, 1023, 0, 255);
  // LED gets brighter the harder you press
  analogWrite(LEDpin, LEDbrightness);
 
  delay(100);
}
```

## Simple Code for Analog FSR Measurements
Here is a code example for measuring the FSR on an analog pin.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/438/medium800/force___flex_fsrpulldowndia.png?1396763038)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/439/medium800/force___flex_fsrpulldownsch.gif?1447975589)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/440/medium800/force___flex_simpletestout.gif?1447975598)

This code doesn't do any calculations, it just prints out what it interprets as the amount of pressure in a qualitative manner. For most projects, this is pretty much all thats needed!```
/* FSR simple testing sketch. 
 
Connect one end of FSR to power, the other end to Analog 0.
Then connect one end of a 10K resistor from Analog 0 to ground 
 
For more information see www.ladyada.net/learn/sensors/fsr.html */
 
int fsrPin = 0;     // the FSR and 10K pulldown are connected to a0
int fsrReading;     // the analog reading from the FSR resistor divider
 
void setup(void) {
  // We'll send debugging information via the Serial monitor
  Serial.begin(9600);   
}
 
void loop(void) {
  fsrReading = analogRead(fsrPin);  
 
  Serial.print("Analog reading = ");
  Serial.print(fsrReading);     // the raw analog reading
 
  // We'll have a few threshholds, qualitatively determined
  if (fsrReading &lt; 10) {
    Serial.println(" - No pressure");
  } else if (fsrReading &lt; 200) {
    Serial.println(" - Light touch");
  } else if (fsrReading &lt; 500) {
    Serial.println(" - Light squeeze");
  } else if (fsrReading &lt; 800) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  delay(1000);
} 
```

## In-Depth Code for Analog FSR Measurements
This Arduino sketch that assumes you have the FSR wired up as above, with a 10K? pull down resistor and the sensor is read on Analog 0 pin. It is pretty advanced and will measure the approximate Newton force measured by the FSR. This can be pretty useful for calibrating what forces you think the FSR will experience.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/441/medium800/force___flex_fsrpulldowndia.png?1396763071)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/442/medium800/force___flex_fsrpulldownsch.gif?1447975609)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/443/medium800/force___flex_fsrtester.gif?1447975620)

```
/* FSR testing sketch. 
 
Connect one end of FSR to power, the other end to Analog 0.
Then connect one end of a 10K resistor from Analog 0 to ground 
 
For more information see www.ladyada.net/learn/sensors/fsr.html */
 
int fsrPin = 0;     // the FSR and 10K pulldown are connected to a0
int fsrReading;     // the analog reading from the FSR resistor divider
int fsrVoltage;     // the analog reading converted to voltage
unsigned long fsrResistance;  // The voltage converted to resistance, can be very big so make "long"
unsigned long fsrConductance; 
long fsrForce;       // Finally, the resistance converted to force
 
void setup(void) {
  Serial.begin(9600);   // We'll send debugging information via the Serial monitor
}
 
void loop(void) {
  fsrReading = analogRead(fsrPin);  
  Serial.print("Analog reading = ");
  Serial.println(fsrReading);
 
  // analog voltage reading ranges from about 0 to 1023 which maps to 0V to 5V (= 5000mV)
  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  Serial.print("Voltage reading in mV = ");
  Serial.println(fsrVoltage);  
 
  if (fsrVoltage == 0) {
    Serial.println("No pressure");  
  } else {
    // The voltage = Vcc * R / (R + FSR) where R = 10K and Vcc = 5V
    // so FSR = ((Vcc - V) * R) / V        yay math!
    fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
    fsrResistance *= 10000;                // 10K resistor
    fsrResistance /= fsrVoltage;
    Serial.print("FSR resistance in ohms = ");
    Serial.println(fsrResistance);
 
    fsrConductance = 1000000;           // we measure in micromhos so 
    fsrConductance /= fsrResistance;
    Serial.print("Conductance in microMhos: ");
    Serial.println(fsrConductance);
 
    // Use the two FSR guide graphs to approximate the force
    if (fsrConductance &lt;= 1000) {
      fsrForce = fsrConductance / 80;
      Serial.print("Force in Newtons: ");
      Serial.println(fsrForce);      
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30;
      Serial.print("Force in Newtons: ");
      Serial.println(fsrForce);            
    }
  }
  Serial.println("--------------------");
  delay(1000);
}
```

## BONUS! &nbsp;Reading FSR Measurements Without Analog Pins.
Because FSR's are basically resistors, its possible to use them even if you don't have any analog pins on your microcontroller (or if say you want to connect more than you have analog input pins. The way we do this is by taking advantage of a basic electronic property of resistors and capacitors. It turns out that if you take a capacitor that is initially storing no voltage, and then connect it to power through a resistor, it will charge up to the power voltage slowly. The bigger the resistor, the slower it is.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/444/medium800/force___flex_RCtimecapture.jpg?1396763093)

_This capture from an oscilloscope shows whats happening on the digital pin (yellow). The blue line indicates when the sketch starts counting and when the couting is complete, about 1.2ms later._

This is because the capacitor acts like a bucket and the resistor is like a thin pipe. To fill a bucket up with a very thin pipe takes enough time that you can figure out how wide the pipe is by timing how long it takes to fill the bucket up halfway.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/445/medium800/force___flex_RCtimediag.png?1396763106)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/446/medium800/force___flex_RCtimesch.gif?1447975630)

In this case, our 'bucket' is a 0.1uF ceramic capacitor. You can change the capacitor nearly any way you want but the timing values will also change. 0.1uF seems to be an OK place to start for these FSRs.```
/* FSR simple testing sketch. 
 
Connect one end of FSR to power, the other end to pin 2.
Then connect one end of a 0.1uF capacitor from pin 2 to ground 
 
For more information see www.ladyada.net/learn/sensors/fsr.html */
 
int fsrPin = 2;     // the FSR and cap are connected to pin2
int fsrReading;     // the digital reading
int ledPin = 13;    // you can just use the 'built in' LED
 
void setup(void) {
  // We'll send debugging information via the Serial monitor
  Serial.begin(9600);   
  pinMode(ledPin, OUTPUT);  // have an LED for output 
}
 
void loop(void) {
  // read the resistor using the RCtime technique
  fsrReading = RCtime(fsrPin);
 
  if (fsrReading == 30000) {
    // if we got 30000 that means we 'timed out'
    Serial.println("Nothing connected!");
  } else {
    Serial.print("RCtime reading = ");
    Serial.println(fsrReading);     // the raw analog reading
 
    // Do a little processing to keep the LED blinking
    fsrReading /= 10;
    // The more you press, the faster it blinks!
    digitalWrite(ledPin, HIGH);
    delay(fsrReading);
    digitalWrite(ledPin, LOW);
    delay(fsrReading);
  }
  delay(100);
}
 
// Uses a digital pin to measure a resistor (like an FSR or photocell!)
// We do this by having the resistor feed current into a capacitor and
// counting how long it takes to get to Vcc/2 (for most arduinos, thats 2.5V)
int RCtime(int RCpin) {
 int reading = 0;  // start with 0
 
  // set the pin to an output and pull to LOW (ground)
  pinMode(RCpin, OUTPUT);
  digitalWrite(RCpin, LOW);
 
  // Now set the pin to an input and...
  pinMode(RCpin, INPUT);
  while (digitalRead(RCpin) == LOW) { // count how long it takes to rise up to HIGH
    reading++;      // increment to keep track of time 
 
    if (reading == 30000) {
      // if we got this far, the resistance is so high
      // its likely that nothing is connected! 
      break;           // leave the loop
    }
  }
  // OK either we maxed out at 30000 or hopefully got a reading, return the count
 
  return reading;
}
```

![](https://cdn-learn.adafruit.com/assets/assets/000/000/447/medium800/force___flex_RCtimeout.gif?1447975639)

It is possible to calculate the actual resistance from the reading but unfortunately, variations in the IDE and arduino board will make it inconsistant. Be aware of that if you change IDE versions of&nbsp;OS's, or use a 3.3V arduino instead of 5V, or change from a 16mhz Arduino to a 8Mhz one (like a lilypad) there may be differences due to how long it takes to read the value of a pin. Usually that isn't a big deal but it can make your project hard to debug if you aren't expecting it!- [Previous Page](https://learn.adafruit.com/force-sensitive-resistor-fsr/connecting-to-an-fsr.md)
- [Next Page](https://learn.adafruit.com/force-sensitive-resistor-fsr/example-projects.md)

## Featured Products

### Round Force-Sensitive Resistor (FSR) -  0.3 ~ 10 Newton Force

[Round Force-Sensitive Resistor (FSR) -  0.3 ~ 10 Newton Force](https://www.adafruit.com/product/166)
FSRs are sensors that allow you to detect physical pressure, squeezing and weight. They are simple to use and low cost. This sensor is an Alpha MF01A-N-221-A01&nbsp;with 1/2 diameter sensing region.

We used to stock the Interlink model 402 FSR - the Alpha version is almost half the price...

In Stock
[Buy Now](https://www.adafruit.com/product/166)
[Related Guides to the Product](https://learn.adafruit.com/products/166/guides)
### Square Force-Sensitive Resistor (FSR)

[Square Force-Sensitive Resistor (FSR)](https://www.adafruit.com/product/1075)
FSRs are sensors that allow you to detect physical pressure, squeezing and weight. They are simple to use and low cost. This sensor is an Alpha MF02A-N-221-A01 FSR with a 38mm square sensing region. Note that this sensor can't detect _where_ on the square you pressed (for that, <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/1075)
[Related Guides to the Product](https://learn.adafruit.com/products/1075/guides)
### Extra-long force-sensitive resistor (FSR)

[Extra-long force-sensitive resistor (FSR)](https://www.adafruit.com/product/1071)
FSRs are sensors that allow you to detect physical pressure, squeezing and weight. They are simple to use and low cost. This sensor is a Interlink model 408 FSR with a massive 1/4-inch x 24-inch sensing region. You can press anywhere along the strip and the pressure will be recognized. Note...

In Stock
[Buy Now](https://www.adafruit.com/product/1071)
[Related Guides to the Product](https://learn.adafruit.com/products/1071/guides)
### Terminal Block - 2-pin 3.5mm - pack of 5!

[Terminal Block - 2-pin 3.5mm - pack of 5!](https://www.adafruit.com/product/724)
Nothing makes a project harder to maintain than a lot of loose wiring. That's why we like to use terminal blocks whenever making PCB-to-Wire connections. These particular 3.5mm terminal blocks are our favorite: big enough for a range of wire gauges, easy to adjust with a screwdriver, and...

In Stock
[Buy Now](https://www.adafruit.com/product/724)
[Related Guides to the Product](https://learn.adafruit.com/products/724/guides)

## Related Guides

- [Adafruit VEML6070 UV Sensor Breakout](https://learn.adafruit.com/adafruit-veml6070-uv-light-sensor-breakout.md)
- [Adafruit NAU7802 24-Bit ADC - STEMMA QT / Qwiic](https://learn.adafruit.com/adafruit-nau7802-24-bit-adc-stemma-qt-qwiic.md)
- [Arcade Stick Conversion](https://learn.adafruit.com/arcade-stick-conversion.md)
- [Calibrating Sensors](https://learn.adafruit.com/calibrating-sensors.md)
- [Wireless ESP32-S2 Touch Screen Controller for Pure Data](https://learn.adafruit.com/wireless-esp32-s2-controller-for-pure-data.md)
- [NAU7802 Pet Food Scale](https://learn.adafruit.com/nau7802-pet-food-scale.md)
- [Clue Coffee Scale](https://learn.adafruit.com/clue-coffee-scale.md)
- [ReBoots Animated LED Boot Laces](https://learn.adafruit.com/re-boots-animated-dancing-boot-laces.md)
- [SensoGlove Teardown](https://learn.adafruit.com/sensoglove-teardown.md)
- [ICEdot Teardown](https://learn.adafruit.com/icedot-teardown.md)
- [Tilt Sensor](https://learn.adafruit.com/tilt-sensor.md)
- [Wireless LED Juggling Balls with ESP-NOW](https://learn.adafruit.com/wireless-juggling-balls-esp-now.md)
- [CuteCircuit Twirkle Shirt Teardown](https://learn.adafruit.com/cutecircuit-twirkle-shirt-teardown.md)
- [Power Glove Wireless MIDI Controller](https://learn.adafruit.com/power-glove-bluetooth-midi-controller.md)
- [Flora MIDI Drum Glove](https://learn.adafruit.com/midi-drum-glove.md)
