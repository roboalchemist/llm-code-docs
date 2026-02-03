# Source: https://learn.adafruit.com/tilt-sensor/using-a-tilt-sensor.md

# Tilt Sensor

## Using a Tilt Sensor

Danger: 

## Simple Tilt-Activated LED
This is the most basic way of connecting to a tilt switch, but can be handy while one is learning about them. Simply connect it in series with an LED, resistor and battery. Tilt to turn on and off.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/498/medium800/force___flex_tiltLEDschem.gif?1447975892)

![](https://cdn-learn.adafruit.com/assets/assets/000/000/499/medium800/force___flex_tiltLEDlayout.gif?1447975903)

## Reading Switch State with a Microcontroller
Note that the layout above shows a 10K pullup resistor but for the code I use the 'built-in' pullup resistor that you can turn on by setting an input pin to HIGH output (its quite neat!) If you use the internal pull-up you can skip the external one.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/500/medium800/force___flex_tiltarduinolay.gif?1447975913)

```
/* Better Debouncer
 * 
 * This debouncing circuit is more rugged, and will work with tilt switches!
 *
 * http://www.ladyada.net/learn/sensor/tilt.html
 */
 
int inPin = 2;         // the number of the input pin
int outPin = 13;       // the number of the output pin
 
int LEDstate = HIGH;      // the current state of the output pin
int reading;           // the current reading from the input pin
int previous = LOW;    // the previous reading from the input pin
 
// the following variables are long because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long time = 0;         // the last time the output pin was toggled
long debounce = 50;   // the debounce time, increase if the output flickers
 
void setup()
{
  pinMode(inPin, INPUT);
  digitalWrite(inPin, HIGH);   // turn on the built in pull-up resistor
  pinMode(outPin, OUTPUT);
}
 
void loop()
{
  int switchstate;
 
  reading = digitalRead(inPin);
 
  // If the switch changed, due to bounce or pressing...
  if (reading != previous) {
    // reset the debouncing timer
    time = millis();
  } 
 
  if ((millis() - time) &gt; debounce) {
     // whatever the switch is at, its been there for a long time
     // so lets settle on it!
     switchstate = reading;
 
     // Now invert the output on the pin13 LED
    if (switchstate == HIGH)
      LEDstate = LOW;
    else
      LEDstate = HIGH;
  }
  digitalWrite(outPin, LEDstate);
 
  // Save the last reading so we keep a running tally
  previous = reading;
}
```

- [Previous Page](https://learn.adafruit.com/tilt-sensor/connecting-to-a-tilt-sensor.md)
- [Next Page](https://learn.adafruit.com/tilt-sensor/example-projects.md)

## Featured Products

### Tilt ball switch

[Tilt ball switch](https://www.adafruit.com/product/173)
The "poor man's" accelerometer! Tilt sensors are switches that can detect basic motion/orientation. The metal tube has a little metal ball that rolls around in it, when its tilted upright, the ball rolls onto the contacts sticking out of end and shorts them together.

<a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/173)
[Related Guides to the Product](https://learn.adafruit.com/products/173/guides)

## Related Guides

- [Force Sensitive Resistor (FSR)](https://learn.adafruit.com/force-sensitive-resistor-fsr.md)
- [Basic Resistor Sensor Reading on Raspberry Pi](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi.md)
- [Calibrating Sensors](https://learn.adafruit.com/calibrating-sensors.md)
- [Wireless ESP32-S2 Touch Screen Controller for Pure Data](https://learn.adafruit.com/wireless-esp32-s2-controller-for-pure-data.md)
- [Hang out your washing reminder - Adafruit IO + Vibration switch](https://learn.adafruit.com/hang-out-your-washing-reminder-adafruit-io-vibration-switch.md)
- [Circuit Playground Bike Glove](https://learn.adafruit.com/circuit-playground-bike-glove.md)
- [ICEdot Teardown](https://learn.adafruit.com/icedot-teardown.md)
- [Adafruit VEML6070 UV Sensor Breakout](https://learn.adafruit.com/adafruit-veml6070-uv-light-sensor-breakout.md)
- [NAU7802 Pet Food Scale](https://learn.adafruit.com/nau7802-pet-food-scale.md)
- [Adafruit HX711 24-bit ADC](https://learn.adafruit.com/adafruit-hx711-24-bit-adc.md)
- [Power Glove Wireless MIDI Controller](https://learn.adafruit.com/power-glove-bluetooth-midi-controller.md)
- [Clue Coffee Scale](https://learn.adafruit.com/clue-coffee-scale.md)
- [Adafruit NAU7802 24-Bit ADC - STEMMA QT / Qwiic](https://learn.adafruit.com/adafruit-nau7802-24-bit-adc-stemma-qt-qwiic.md)
- [Flora MIDI Drum Glove](https://learn.adafruit.com/midi-drum-glove.md)
- [Arcade Stick Conversion](https://learn.adafruit.com/arcade-stick-conversion.md)
