# Source: https://learn.adafruit.com/adafruit-microphone-amplifier-breakout/measuring-sound-levels.md

# Adafruit Microphone Amplifier Breakout

## Measuring Sound Levels

The Audio signal from the output of the amplifier is a varying voltage. &nbsp;To measure the sound level, we need to take multiple measurements to find the minimum and maximum extents or "peak to peak amplitude"&nbsp;of the signal. &nbsp;  
  
In the example below, we choose a sample window of 50 milliseconds. &nbsp;That is sufficient to measure sound levels of frequencies as low as 20 Hz - the lower limit of human hearing.  
  
After finding the minimum and maximum samples, we compute the difference and convert it to volts and the&nbsp;output is printed to the serial monitor.

```
/****************************************
Example Sound Level Sketch for the 
Adafruit Microphone Amplifier
****************************************/

const int sampleWindow = 50; // Sample window width in mS (50 mS = 20Hz)
unsigned int sample;

void setup() 
{
   Serial.begin(9600);
}


void loop() 
{
   unsigned long startMillis= millis();  // Start of sample window
   unsigned int peakToPeak = 0;   // peak-to-peak level

   unsigned int signalMax = 0;
   unsigned int signalMin = 1024;

   // collect data for 50 mS
   while (millis() - startMillis &lt; sampleWindow)
   {
      sample = analogRead(0);
      if (sample &lt; 1024)  // toss out spurious readings
      {
         if (sample &gt; signalMax)
         {
            signalMax = sample;  // save just the max levels
         }
         else if (sample &lt; signalMin)
         {
            signalMin = sample;  // save just the min levels
         }
      }
   }
   peakToPeak = signalMax - signalMin;  // max - min = peak-peak amplitude
   double volts = (peakToPeak * 5.0) / 1024;  // convert to volts

   Serial.println(volts);
}
```

![](https://cdn-learn.adafruit.com/assets/assets/000/003/637/medium800/sensors_Capture.jpg?1396799275)

OK, so that's not very exciting. &nbsp;What else can you do with it?

# Scrolling Sound Level Meter

So now&nbsp;we will take the peak-to-peak measurement and use it to drive a [Bicolor&nbsp;LED Matrix](http://www.adafruit.com/products/902) to display the sound level. &nbsp;To make it more interesting, we will scroll the display so that the last 8 measurements are graphed in real-time.  
  
To do this you will&nbsp;need to download &nbsp;the [Adafruit GFX Library](https://github.com/adafruit/Adafruit-GFX-Library "Link: https://github.com/adafruit/Adafruit-GFX-Library"), [Adafruit BusIO](https://github.com/adafruit/Adafruit_BusIO) and [LED Backpack Library](https://github.com/adafruit/Adafruit-LED-Backpack-Library). &nbsp;The Wire Library is included in the Arduino IDE installation.

## Assemble the Matrix
Follow the tutorial [here](http://learn.adafruit.com/adafruit-led-backpack/):![sensors_matrix.jpeg](https://cdn-learn.adafruit.com/assets/assets/000/003/641/medium640/sensors_matrix.jpeg?1396799301)

## Connect the Matrix
The Matrix backpack has 4 pins, connected as follows:  
  

1. '+' -\> 5v  
2. '-' &nbsp;-\> GND  
3. D -\> SDA (Analog Pin 4)  
4. C -\> SCL (Analog Pin 5)  

![sensors_2013_01_12_IMG_1166-1024.jpg](https://cdn-learn.adafruit.com/assets/assets/000/003/638/medium640/sensors_2013_01_12_IMG_1166-1024.jpg?1396799282)

## Upload the Code
Paste the code below into the Arduino IDE and upload it. &nbsp;Speak in a normal voice about 6-8 inches from the microphone and the&nbsp;sound level meter matrix display&nbsp;should start scrolling.  
![sensors_2013_01_12_IMG_1168-1024.jpg](https://cdn-learn.adafruit.com/assets/assets/000/003/639/medium640/sensors_2013_01_12_IMG_1168-1024.jpg?1396799287)

## Adjust the Gain
Although the amplifier is capable of a rail-to-rail signal (3.3v in this case), the code maps a 1v peak-to-peak signal to the full scale of the display. &nbsp;  
  
This can be changed in the code. &nbsp;Or&nbsp;you can adjust the gain trimmer-pot&nbsp;of the amplifier with a small straight-bladed screwdriver. &nbsp;The amplifier gain is adjustable from&nbsp;25x to 125x.  
![sensors_2013_01_12_IMG_1177-1024.jpg](https://cdn-learn.adafruit.com/assets/assets/000/003/640/medium640/sensors_2013_01_12_IMG_1177-1024.jpg?1396799295)

Danger: 

```
/****************************************
Scrolling Sound Meter Sketch for the 
Adafruit Microphone Amplifier
****************************************/

#include &lt;Wire.h&gt;
#include "Adafruit_LEDBackpack.h"
#include "Adafruit_GFX.h"

// Include the Matrix code for display
Adafruit_BicolorMatrix matrix = Adafruit_BicolorMatrix();

const int maxScale = 8;
const int redZone = 5;

const int sampleWindow = 50; // Sample window width in mS (50 mS = 20Hz)
unsigned int sample;

void setup() 
{
   Serial.begin(9600);

   matrix.begin(0x70);  // pass in the address
}


void loop() 
{
   unsigned long startMillis= millis();  // Start of sample window
   unsigned int peakToPeak = 0;   // peak-to-peak level

   unsigned int signalMax = 0;
   unsigned int signalMin = 1024;

   while (millis() - startMillis &lt; sampleWindow)
   {
      sample = analogRead(0); 
      if (sample &lt; 1024)  // toss out spurious readings
      {
         if (sample &gt; signalMax)
         {
            signalMax = sample;  // save just the max levels
         }
         else if (sample &lt; signalMin)
         {
            signalMin = sample;  // save just the min levels
         }
      }
   }
   peakToPeak = signalMax - signalMin;

   // map 1v p-p level to the max scale of the display
   int displayPeak = map(peakToPeak, 0, 1023, 0, maxScale);

   // Update the display:
   for (int i = 0; i &lt; 7; i++)  // shift the display left
   {
      matrix.displaybuffer[i] = matrix.displaybuffer[i+1];
   }

   // draw the new sample
   for (int i = 0; i &lt;= maxScale; i++)
   {
      if (i &gt;= displayPeak)  // blank these pixels
      {
         matrix.drawPixel(i, 7, 0);
      }
      else if (i &lt; redZone) // draw in green
      {
         matrix.drawPixel(i, 7, LED_GREEN);
      }
      else // Red Alert!  Red Alert!
      {
         matrix.drawPixel(i, 7, LED_RED);
      }
   }
   matrix.writeDisplay();  // write the changes we just made to the display
}
```

- [Previous Page](https://learn.adafruit.com/adafruit-microphone-amplifier-breakout/assembly-and-wiring.md)
- [Next Page](https://learn.adafruit.com/adafruit-microphone-amplifier-breakout/more-cool-projects.md)

## Featured Products

### Electret Microphone Amplifier - MAX4466 with Adjustable Gain

[Electret Microphone Amplifier - MAX4466 with Adjustable Gain](https://www.adafruit.com/product/1063)
Add an ear to your project with this well-designed electret microphone amplifier. This fully assembled and tested board comes with a 20-20KHz electret microphone soldered on. For the amplification, we use the Maxim MAX4466, an op-amp specifically designed for this delicate task! The amplifier...

In Stock
[Buy Now](https://www.adafruit.com/product/1063)
[Related Guides to the Product](https://learn.adafruit.com/products/1063/guides)
### Adafruit Bicolor LED Square Pixel Matrix with I2C Backpack

[Adafruit Bicolor LED Square Pixel Matrix with I2C Backpack](https://www.adafruit.com/product/902)
What's better than a single LED? Lots of LEDs! A fun way to make a small colorful display is to use a [1.2" Bi-color 8x8 LED Matrix](http://www.adafruit.com/products/458). Matrices like these are 'multiplexed' - so to control all the 128 LEDs you need 24 pins....

In Stock
[Buy Now](https://www.adafruit.com/product/902)
[Related Guides to the Product](https://learn.adafruit.com/products/902/guides)
### Tiny Premium Breadboard

[Tiny Premium Breadboard](https://www.adafruit.com/product/65)
This is a tiny little breadboard... half the size of a half-size breadboard!&nbsp;

**As of Sep 8, 2022** - This Tiny breadboard has been updated to make plugging and un-plugging boards and headers a buttery-smooth&nbsp;operation. Updated design also includes a metal...

In Stock
[Buy Now](https://www.adafruit.com/product/65)
[Related Guides to the Product](https://learn.adafruit.com/products/65/guides)

## Related Guides

- [Adafruit LED Backpacks](https://learn.adafruit.com/adafruit-led-backpack.md)
- [3D Printed Animatronic Robot Head](https://learn.adafruit.com/3d-printed-animatronic-robot-head.md)
- [Animating Multiple LED Backpacks](https://learn.adafruit.com/animating-multiple-led-backpacks.md)
- [Tiny Arduino Music Visualizer](https://learn.adafruit.com/piccolo.md)
- [LED Ampli-Tie](https://learn.adafruit.com/led-ampli-tie.md)
- [Wave Shield Voice Changer](https://learn.adafruit.com/wave-shield-voice-changer.md)
- [Battery Powered Raspberry Pi Displays w/RaspiRobot Shield](https://learn.adafruit.com/raspirobot-battery-powered-raspberry-pi-displays.md)
- [Trinket Sound-Reactive LED Color Organ](https://learn.adafruit.com/trinket-sound-reactive-led-color-organ.md)
- [Electronic Demon Costume](https://learn.adafruit.com/electronic-demon-costume.md)
- [FFT: Fun with Fourier Transforms](https://learn.adafruit.com/fft-fun-with-fourier-transforms.md)
- [CircuitPython Hardware: LED Backpacks & FeatherWings](https://learn.adafruit.com/micropython-hardware-led-backpacks-and-featherwings.md)
- [3D Printed Wireless MIDI Controller Guitar](https://learn.adafruit.com/ez-key-wireless-midi-controller-guitar.md)
- [Matrix and 7-Segment LED Backpack with the Raspberry Pi](https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi.md)
- [Circle of Fifths Euclidean Synth with synthio and CircuitPython](https://learn.adafruit.com/circle-of-fifths-euclidean-synth-with-synthio-and-circuitpython.md)
- [Adafruit STSPIN220 Stepper Motor Driver Breakout Board](https://learn.adafruit.com/adafruit-stspin220-stepper-motor-driver-breakout-board.md)
