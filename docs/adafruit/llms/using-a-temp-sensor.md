# Source: https://learn.adafruit.com/tmp36-temperature-sensor/using-a-temp-sensor.md

# TMP36 Temperature Sensor

## Using a Temp Sensor

## Connecting to a Temperature Sensor

These sensors have little chips in them and while they're not that delicate, they do need to be handled properly. Be careful of static electricity when handling them and make sure the power supply is connected up correctly and is between 2.7 and 5.5V DC - so don't try to use a 9V battery!

They come in a "TO-92" package which means the chip is housed in a plastic hemi-cylinder with three legs. The legs can be bent easily to allow the sensor to be plugged into a breadboard. You can also solder to the pins to connect long wires. [If you need to waterproof the sensor, you can see below for an Instructable for how to make an excellent case.](https://www.instructables.com/Waterproof-a-LM35-Temperature-Sensor/)

## Reading the Analog Temperature Data
Unlike the FSR or photocell sensors we have looked at, the TMP36 and friends doesn't act like a resistor. Because of that, there is really only one way to read the temperature value from the sensor, and that is plugging the output pin directly into an Analog (ADC) input.  
![](https://cdn-learn.adafruit.com/assets/assets/000/000/476/medium800/temperature_tmp36fritz.gif?1447975816)

Remember that you can use anywhere between 2.7V and 5.5V as the power supply. For this example I'm showing it with a 5V supply but note that you can use this with a 3.3v supply just as easily. No matter what supply you use, the analog voltage reading will range from about 0V (ground) to about 1.75V.

If you're using a 5V Arduino, and connecting the sensor directly into an Analog pin, you can use these formulas to turn the 10-bit analog reading into a temperature:

**Voltage at pin in milliVolts = (_reading from ADC_) \* (5000/1024)**&nbsp;  
This formula converts the number 0-1023 from the ADC into 0-5000mV (= 5V)

If you're using a 3.3V Arduino, you'll want to use this:

**Voltage at pin in milliVolts = (_reading from ADC_) \* (3300/1024)**&nbsp;  
This formula converts the number 0-1023 from the ADC into 0-3300mV (= 3.3V)

Then, to convert millivolts into temperature, use this formula:

**Centigrade temperature = [(analog voltage in mV) - 500] / 10**

# Arduino Sketch - Simple Thermometer

This example code for Arduino shows a quick way to create a temperature sensor, it simply prints to the serial port what the current temperature is in both Celsius and Fahrenheit.

```
//TMP36 Pin Variables
int sensorPin = 0; //the analog pin the TMP36's Vout (sense) pin is connected to
                        //the resolution is 10 mV / degree centigrade with a
                        //500 mV offset to allow for negative temperatures
 
/*
 * setup() - this function runs once when you turn your Arduino on
 * We initialize the serial connection with the computer
 */
void setup()
{
  Serial.begin(9600);  //Start the serial connection with the computer
                       //to view the result open the serial monitor 
}
 
void loop()                     // run over and over again
{
 //getting the voltage reading from the temperature sensor
 int reading = analogRead(sensorPin);  
 
 // converting that reading to voltage, for 3.3v arduino use 3.3
 float voltage = reading * 5.0;
 voltage /= 1024.0; 
 
 // print out the voltage
 Serial.print(voltage); Serial.println(" volts");
 
 // now print out the temperature
 float temperatureC = (voltage - 0.5) * 100 ;  //converting from 10 mv per degree wit 500 mV offset
                                               //to degrees ((voltage - 500mV) times 100)
 Serial.print(temperatureC); Serial.println(" degrees C");
 
 // now convert to Fahrenheit
 float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
 Serial.print(temperatureF); Serial.println(" degrees F");
 
 delay(1000);                                     //waiting a second
}
```

## Getting Better Precision
For better results, using the 3.3v reference voltage as ARef instead of the 5V will be more precise and less noisy  

This example from the light&temp datalogging tutorial has a photocell but you can ignore it

**Note we've changed the TMP36 to A1**

![](https://cdn-learn.adafruit.com/assets/assets/000/000/477/medium800/temperature_sensorwiring.gif?1447975829)

Danger: 

```python
/* Sensor test sketch
  for more information see http://www.ladyada.net/make/logshield/lighttemp.html
  */
 
#define aref_voltage 3.3         // we tie 3.3V to ARef and measure it with a multimeter!
 
 
 
 
//TMP36 Pin Variables
int tempPin = A1;        //the analog pin the TMP36's Vout (sense) pin is connected to
                        //the resolution is 10 mV / degree centigrade with a
                        //500 mV offset to allow for negative temperatures
int tempReading;        // the analog reading from the sensor
 
void setup(void) {
  // We'll send debugging information via the Serial monitor
  Serial.begin(9600);   
 
  // If you want to set the aref to something other than 5v
  analogReference(EXTERNAL);
}
 
 
void loop(void) {
 
  tempReading = analogRead(tempPin);  
 
  Serial.print("Temp reading = ");
  Serial.print(tempReading);     // the raw analog reading
 
  // converting that reading to voltage, which is based off the reference voltage
  float voltage = tempReading * aref_voltage;
  voltage /= 1024.0; 
 
  // print out the voltage
  Serial.print(" - ");
  Serial.print(voltage); Serial.println(" volts");
 
  // now print out the temperature
  float temperatureC = (voltage - 0.5) * 100 ;  //converting from 10 mv per degree wit 500 mV offset
                                               //to degrees ((volatge - 500mV) times 100)
  Serial.print(temperatureC); Serial.println(" degrees C");
 
  // now convert to Fahrenheight
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
  Serial.print(temperatureF); Serial.println(" degrees F");
 
  delay(1000);
}
```

- [Previous Page](https://learn.adafruit.com/tmp36-temperature-sensor/testing-a-temp-sensor.md)
- [Next Page](https://learn.adafruit.com/tmp36-temperature-sensor/tmp36-with-circuitpython.md)

## Featured Products

### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### Half Sized Premium Breadboard - 400 Tie Points

[Half Sized Premium Breadboard - 400 Tie Points](https://www.adafruit.com/product/64)
This is a cute, half-size breadboard with&nbsp;400 tie points, good for small projects. It's 3.25" x 2.2" / 8.3cm&nbsp;x 5.5cm&nbsp;with a standard double-strip in the middle and two power rails on both sides.&nbsp;You can pull the power rails off easily to make the breadboard as...

In Stock
[Buy Now](https://www.adafruit.com/product/64)
[Related Guides to the Product](https://learn.adafruit.com/products/64/guides)
### TMP36 - Analog Temperature sensor

[TMP36 - Analog Temperature sensor](https://www.adafruit.com/product/165)
Wide range, low power temperature sensor outputs an analog voltage that is proportional to the ambient temperature. To use, connect pin 1 (left) to power (between 2.7 and 5.5V), pin 3 (right) to ground, and pin 2 to analog in on your microcontroller. The voltage out is 0V at -50°C and...

In Stock
[Buy Now](https://www.adafruit.com/product/165)
[Related Guides to the Product](https://learn.adafruit.com/products/165/guides)

## Related Guides

- [Circuit Playground Sound-Controlled Robot](https://learn.adafruit.com/circuit-playground-sound-controlled-robot.md)
- [Multi-tasking the Arduino - Part 1](https://learn.adafruit.com/multi-tasking-the-arduino-part-1.md)
- [NeoPixel Painter](https://learn.adafruit.com/neopixel-painter.md)
- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [Adafruit 2.8" TFT Touch Shield v2 - Capacitive or Resistive](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2.md)
- [SMS Texting Pet Food Dish](https://learn.adafruit.com/sms-texting-pet-food-dish.md)
- [Ladyada's Learn Arduino - Lesson #1](https://learn.adafruit.com/ladyadas-learn-arduino-lesson-number-1.md)
- [Arduino Lesson 17. Email Sending Movement Detector](https://learn.adafruit.com/arduino-lesson-17-email-sending-movement-detector.md)
- [Nokia 5110/3310 Monochrome LCD](https://learn.adafruit.com/nokia-5110-3310-monochrome-lcd.md)
- [Arduino Lesson 8. Analog Inputs](https://learn.adafruit.com/adafruit-arduino-lesson-8-analog-inputs.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [Arduino Lesson 13. DC Motors](https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
- [DS1307 Real Time Clock Breakout Board Kit](https://learn.adafruit.com/ds1307-real-time-clock-breakout-board-kit.md)
