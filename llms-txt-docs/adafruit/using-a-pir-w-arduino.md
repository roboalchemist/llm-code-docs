# Source: https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/using-a-pir-w-arduino.md

# PIR Motion Sensor

## Using a PIR w/Arduino

## Reading PIR Sensors

Connecting PIR sensors to a microcontroller is really simple. The PIR acts as a digital output, it can be high voltage or low voltage, so all you need to do is listen for the pin to flip high (detected) or low (not detected) by listening on a digital input on your Arduino

Its likely that you'll want retriggering, so be sure to put the jumper in the **H** &nbsp;position!

Power the PIR with 5V and connect ground to ground. Then connect the output to a digital pin. In this example we'll use pin 2.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/543/medium800/proximity_pirardbb.gif?1447976079)

The code is very simple, and is basically just keeps track of whether the input to pin 2 is high or low. It also tracks the&nbsp;_state_&nbsp;of the pin, so that it prints out a message when motion has started and stopped.```
/*
 * PIR sensor tester
 */
 
int ledPin = 13;                // choose the pin for the LED
int inputPin = 2;               // choose the input pin (for PIR sensor)
int pirState = LOW;             // we start, assuming no motion detected
int val = 0;                    // variable for reading the pin status
 
void setup() {
  pinMode(ledPin, OUTPUT);      // declare LED as output
  pinMode(inputPin, INPUT);     // declare sensor as input
 
  Serial.begin(9600);
}
 
void loop(){
  val = digitalRead(inputPin);  // read input value
  if (val == HIGH) {            // check if the input is HIGH
    digitalWrite(ledPin, HIGH);  // turn LED ON
    if (pirState == LOW) {
      // we have just turned on
      Serial.println("Motion detected!");
      // We only want to print on the output change, not state
      pirState = HIGH;
    }
  } else {
    digitalWrite(ledPin, LOW); // turn LED OFF
    if (pirState == HIGH){
      // we have just turned of
      Serial.println("Motion ended!");
      // We only want to print on the output change, not state
      pirState = LOW;
    }
  }
}
```

Don't forget that there are some times when you don't need a microcontroller. A PIR sensor can be connected to a relay (perhaps with a transistor buffer) without a micro!- [Previous Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/testing-a-pir.md)
- [Next Page](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/circuitpython-code.md)

## Primary Products

### PIR (motion) sensor

[PIR (motion) sensor](https://www.adafruit.com/product/189)
PIR sensors are used to detect motion from pets/humanoids from about 20 feet away (possibly works on zombies, not guaranteed). This one has an adjustable delay before firing (approx 2-4 seconds), adjustable sensitivity **and** we include a 1 foot (30 cm) cable with a socket so you...

In Stock
[Buy Now](https://www.adafruit.com/product/189)
[Related Guides to the Product](https://learn.adafruit.com/products/189/guides)

## Related Guides

- [PropMaker Jack O'Lantern](https://learn.adafruit.com/propmaker-jack-o-lantern.md)
- [No-Code WipperSnapper Summoning Horn](https://learn.adafruit.com/adafruit-io-wippersnapper-summoning-horn.md)
- [Capacitive Touch Holiday Light Control](https://learn.adafruit.com/capacitive-touch-holiday-light-control.md)
- [Raspberry Pi Video Synth with Blinka and Processing](https://learn.adafruit.com/raspberry-pi-video-synth-with-blinka-and-processing.md)
- [Magical Mistletoe](https://learn.adafruit.com/magical-mistletoe.md)
- [Proximity Based Lighting](https://learn.adafruit.com/proximity-based-lighting.md)
- [Calibrating Sensors](https://learn.adafruit.com/calibrating-sensors.md)
- [Fog Machine with Motion Sensor and Adafruit IO](https://learn.adafruit.com/fog-machine-remote-trigger.md)
- [Feather Freezer Door Alarm](https://learn.adafruit.com/feather-door-alarm.md)
- [Tombstone Prop-Maker RP2040](https://learn.adafruit.com/tombstone-prop-maker-rp2040.md)
- [Track a Turtle with WipperSnapper](https://learn.adafruit.com/track-a-turtle-with-wippersnapper.md)
- [Sitcom SFX Door Trigger](https://learn.adafruit.com/sitcom-sfx-door-trigger.md)
- [Tree with Animated Eyes and Motion Sensor](https://learn.adafruit.com/tree-ent-sculpture-with-animated-eyes.md)
- [MIDI Laser Harp with Time of Flight Distance Sensors](https://learn.adafruit.com/midi-laser-harp-time-of-flight-sensors.md)
- [LPC824 NeoPixel IR Distance Sensor](https://learn.adafruit.com/lpc824-neopixel-ir-distance-sensor.md)
