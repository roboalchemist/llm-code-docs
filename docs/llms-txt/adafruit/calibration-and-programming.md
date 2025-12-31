# Source: https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts/calibration-and-programming.md

# Adafruit Analog Accelerometer Breakouts

## Calibration and Programming

# Static Calibration:
As with all sensors, there is some variation in output between samples of these accelerometers. For non-critical applications such as game controllers, or simple motion or tilt sensors, these variations are not important. But for applications requiring precise measurements, calibration to a reliable reference is a good idea.  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/498/medium800/sensors_Jiminy_Gravity.jpg?1396783816)

## Gravity as a&nbsp;Calibration Reference
Acceleration is measured in units of gravitational force or "G", where 1G represents the gravitational pull at the surface of the earth. &nbsp;[Despite what you may have heard](http://www.youtube.com/watch?v=2ORJ7B1bqEY), gravity is a pretty stable force and makes a convenient and reliable&nbsp;calibration reference if you happen to be a&nbsp;surface-dwelling earthling. Danger: 

## Calibration Method:
To calibrate the sensor to the gravitational reference, you need to determine the sensor output for each axis when it is precisely aligned with the axis of gravitational pull. &nbsp;Laboratory quality calibration uses precision positioning jigs. &nbsp;The method described here&nbsp;is simple and gives surprisingly&nbsp;good results.&nbsp; ![](https://cdn-learn.adafruit.com/assets/assets/000/002/514/medium800/sensors_Coordinates.png?1396783976)

 **Mount the Sensor:**  
First mount the sensor to a [small breadboard](http://www.adafruit.com/products/65)&nbsp;like the one on the left. &nbsp;The back and squared edges of the breadboard make a reasonably accurate set of reference planes to orient&nbsp;the sensor for calibration.  
  
**Wire the Sensor:**  
Wire the sensor&nbsp;as shown below. &nbsp;This is equivalent to the&nbsp;circuit shown on the previous page, with the addition of a switch.  
![sensors_tinybreadboard_LRG.jpg](https://cdn-learn.adafruit.com/assets/assets/000/002/515/medium640/sensors_tinybreadboard_LRG.jpg?1396783982)

![](https://cdn-learn.adafruit.com/assets/assets/000/002/513/medium800/sensors_Accelerometer_Calibration_bb-1024.jpg?1396783962)

## Run the&nbsp;Calibration Sketch

- Load the sketch below onto the Arduino and run it.  
- Open the Serial Monitor.  
- Lay the breadboard with the sensor on a flat surface

  - Press and hold the button until you see "Calibrate" in the serial monitor.
  - This will calibrate the minimum value for the z axis.

- Stand the breadboard on the front edge and press the button again. to calibrate +y  
- Repeat this for the three other edges to calibrate +x, -y and -x.  
- Turn the breadboard upside down and press the button again to calibrate +z. &nbsp;(Hint, the underside of a table works well to steady it.)

## Calibration Sketch Output:
  
Once calibrated, the output will show the calibrated raw range for each axis, followed by the&nbsp;measured "G" forces. &nbsp;The raw ranges can be used as constants in sketches.  
  
Raw Ranges: X: 408-616, Y: 398-610, Z: 422-625  
511, 511, 625 :: -0.01G, 0.07G, 1.00G  
Raw Ranges: X: 408-616, Y: 398-610, Z: 422-625  
511, 511, 625 :: -0.01G, 0.07G, 1.00G  
Raw Ranges: X: 408-616, Y: 398-610, Z: 422-625  
511, 511, 625 :: -0.01G, 0.07G, 1.00G  
Raw Ranges: X: 408-616, Y: 398-610, Z: 422-625  
511, 511, 625 :: -0.01G, 0.07G, 1.00G  
Raw Ranges: X: 408-616, Y: 398-610, Z: 422-625  
# Calibration Sketch
```
const int xInput = A0;
const int yInput = A1;
const int zInput = A2;
const int buttonPin = 2;

// Raw Ranges:
// initialize to mid-range and allow calibration to
// find the minimum and maximum for each axis
int xRawMin = 512;
int xRawMax = 512;

int yRawMin = 512;
int yRawMax = 512;

int zRawMin = 512;
int zRawMax = 512;

// Take multiple samples to reduce noise
const int sampleSize = 10;

void setup() 
{
  analogReference(EXTERNAL);
  Serial.begin(9600);
}

void loop() 
{
  int xRaw = ReadAxis(xInput);
  int yRaw = ReadAxis(yInput);
  int zRaw = ReadAxis(zInput);
  
  if (digitalRead(buttonPin) == LOW)
  {
    AutoCalibrate(xRaw, yRaw, zRaw);
  }
  else
  {
    Serial.print("Raw Ranges: X: ");
    Serial.print(xRawMin);
    Serial.print("-");
    Serial.print(xRawMax);
    
    Serial.print(", Y: ");
    Serial.print(yRawMin);
    Serial.print("-");
    Serial.print(yRawMax);
    
    Serial.print(", Z: ");
    Serial.print(zRawMin);
    Serial.print("-");
    Serial.print(zRawMax);
    Serial.println();
    Serial.print(xRaw);
    Serial.print(", ");
    Serial.print(yRaw);
    Serial.print(", ");
    Serial.print(zRaw);
    
    // Convert raw values to 'milli-Gs"
    long xScaled = map(xRaw, xRawMin, xRawMax, -1000, 1000);
    long yScaled = map(yRaw, yRawMin, yRawMax, -1000, 1000);
    long zScaled = map(zRaw, zRawMin, zRawMax, -1000, 1000);
  
    // re-scale to fractional Gs
    float xAccel = xScaled / 1000.0;
    float yAccel = yScaled / 1000.0;
    float zAccel = zScaled / 1000.0;
  
    Serial.print(" :: ");
    Serial.print(xAccel);
    Serial.print("G, ");
    Serial.print(yAccel);
    Serial.print("G, ");
    Serial.print(zAccel);
    Serial.println("G");
  
  delay(500);
  }
}

//
// Read "sampleSize" samples and report the average
//
int ReadAxis(int axisPin)
{
  long reading = 0;
  analogRead(axisPin);
  delay(1);
  for (int i = 0; i &lt; sampleSize; i++)
  {
    reading += analogRead(axisPin);
  }
  return reading/sampleSize;
}

//
// Find the extreme raw readings from each axis
//
void AutoCalibrate(int xRaw, int yRaw, int zRaw)
{
  Serial.println("Calibrate");
  if (xRaw &lt; xRawMin)
  {
    xRawMin = xRaw;
  }
  if (xRaw &gt; xRawMax)
  {
    xRawMax = xRaw;
  }
  
  if (yRaw &lt; yRawMin)
  {
    yRawMin = yRaw;
  }
  if (yRaw &gt; yRawMax)
  {
    yRawMax = yRaw;
  }

  if (zRaw &lt; zRawMin)
  {
    zRawMin = zRaw;
  }
  if (zRaw &gt; zRawMax)
  {
    zRawMax = zRaw;
  }
}
```

- [Previous Page](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts/arduino-wiring.md)
- [Next Page](https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts/circuitpython-code.md)

## Featured Products

### ADXL335 - 5V ready triple-axis accelerometer (+-3g analog out)

[ADXL335 - 5V ready triple-axis accelerometer (+-3g analog out)](https://www.adafruit.com/product/163)
We've updated our favorite triple-axis accelerometer to now have an on-board 3.3V regulator - making it a perfect choice for interfacing with a 5V microcontroller such as the Arduino. This breakout comes with 3 analog outputs for X, Y and Z axis measurements on a 0.75"x0.75"...

In Stock
[Buy Now](https://www.adafruit.com/product/163)
[Related Guides to the Product](https://learn.adafruit.com/products/163/guides)
### ADXL326 - 5V ready triple-axis accelerometer (+-16g analog out)

[ADXL326 - 5V ready triple-axis accelerometer (+-16g analog out)](https://www.adafruit.com/product/1018)
We've now got a wider range version of favorite triple-axis accelerometer - it even has an on-board 3.3V regulator - making it a perfect choice for interfacing with a 5V microcontroller such as the Arduino. This breakout comes with 3 analog outputs for X, Y and Z axis measurements on a...

In Stock
[Buy Now](https://www.adafruit.com/product/1018)
[Related Guides to the Product](https://learn.adafruit.com/products/1018/guides)
### Adafruit METRO 328 Fully Assembled - Arduino IDE compatible

[Adafruit METRO 328 Fully Assembled - Arduino IDE compatible](https://www.adafruit.com/product/50)
We sure love the ATmega328 here at Adafruit, and we use them&nbsp;_a lot_&nbsp;for our own projects. The processor has plenty of GPIO, Analog inputs, hardware UART SPI and I2C, timers and PWM galore - just enough for most simple projects. When we need to go small, we use a <a...></a...>

Out of Stock
[Buy Now](https://www.adafruit.com/product/50)
[Related Guides to the Product](https://learn.adafruit.com/products/50/guides)
### ADXL377 - High-G Triple-Axis Accelerometer (+-200g Analog Out)

[ADXL377 - High-G Triple-Axis Accelerometer (+-200g Analog Out)](https://www.adafruit.com/product/1413)
 **Discontinued -**  **you can grab the&nbsp;** [ADXL375 - High G Accelerometer (+-200g) with I2C and SPI - STEMMA QT / Qwiic](https://www.adafruit.com/product/5374) **instead!&nbsp;**

**Please note: The ADXL377 is "End of Life", <a...></a...>**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1413)
[Related Guides to the Product](https://learn.adafruit.com/products/1413/guides)

## Related Guides

- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Trinket Audio Player](https://learn.adafruit.com/trinket-audio-player.md)
- [Arduino Prototyping Mounting Plate](https://learn.adafruit.com/arduino-prototyping-mounting-plate.md)
- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [Wireless Power Switch with Arduino & the CC3000 WiFi Chip](https://learn.adafruit.com/wireless-power-switch-with-arduino-and-the-cc3000-wifi-chip.md)
- [WiFi Controlled LED Christmahanukwanzaa Tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree.md)
- [FTDI Friend](https://learn.adafruit.com/ftdi-friend.md)
- [Adafruit 1.14" 240x135 Color TFT Breakout LCD Display](https://learn.adafruit.com/adafruit-1-14-240x135-color-tft-breakout.md)
- [Adafruit AirLift Shield - ESP32 WiFi Co-Processor](https://learn.adafruit.com/adafruit-airlift-shield-esp32-wifi-co-processor.md)
- [How to Build a Testing Jig](https://learn.adafruit.com/how-to-build-a-testing-fixture.md)
- [TMP36 Temperature Sensor](https://learn.adafruit.com/tmp36-temperature-sensor.md)
- [Nokia 5110/3310 Monochrome LCD](https://learn.adafruit.com/nokia-5110-3310-monochrome-lcd.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [Ladyada's Bento Box](https://learn.adafruit.com/lady-adas-bento-box.md)
- [Low Power WiFi Datalogger](https://learn.adafruit.com/low-power-wifi-datalogging.md)
