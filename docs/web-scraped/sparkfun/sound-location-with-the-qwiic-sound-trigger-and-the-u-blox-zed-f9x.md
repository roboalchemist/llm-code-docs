# Source: https://learn.sparkfun.com/tutorials/sound-location-with-the-qwiic-sound-trigger-and-the-u-blox-zed-f9x

## Introduction

In this tutorial, we show you how to calculate the location of a sound using the [SparkX Qwiic Sound Trigger](https://www.sparkfun.com/products/17979) and the [u-blox ZED-F9P GNSS receiver](https://www.sparkfun.com/products/16481).

[![SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/3/5/2/16481-SparkFun_GPS-RTK-SMA_Breakout_-_ZED-F9P__Qwiic_-01a.jpg)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html)

### [SparkFun GPS-RTK-SMA Breakout - ZED-F9P (Qwiic)](https://www.sparkfun.com/sparkfun-gps-rtk-sma-breakout-zed-f9p-qwiic.html) 

[ GPS-16481 ]

The SparkFun GPS-RTK-SMA raises the bar for high-precision GPS and is the latest in a line of powerful RTK boards featuring t...

[ [\$259.95] ]

[![Qwiic Sound Trigger](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/1/4/9/17979-Qwiic_Sound_Trigger-01.jpg)](https://www.sparkfun.com/qwiic-sound-trigger.html)

### [Qwiic Sound Trigger](https://www.sparkfun.com/qwiic-sound-trigger.html) 

[ SPX-17979 ]

The Qwiic Sound Trigger is based on the VM1010 from Vesper Technologies and the TI PCA9536 GPIO expander. The VM1010 is a ...

**Retired**

The Qwiic Sound Trigger can be used on its own, or as part of your Qwiic system. It is based on the VM1010 from Vesper Technologies and the TI PCA9536 GPIO expander. The VM1010 is a clever little device which can be placed into a very low power \"Wake On Sound\" mode. When it detects a sound, it wakes up and pulls its TRIG (D~OUT~) pin high. The VM1010 can then be placed into \"Normal\" mode by pulling the MODE pin low; it then functions as a regular microphone. The analog microphone signal is available on the AUDIO (V~OUT~) pin. All of this happens really quickly, within 50 microseconds (much faster than a capacitive MEMS microphone), so you don\'t miss the start of the audio signal. This makes it ideal for use as a sound trigger! If you turn the Qwiic Sound Trigger over, you will see a small hole ringed in white. That's the opening for the microphone. You need to have the rear of the board pointing towards your sound source, not the front.

[![Pictured is the rear of the Qwiic Sound Trigger showing the microphone hole](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/1/9/17979-Qwiic_Sound_Trigger-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/1/9/17979-Qwiic_Sound_Trigger-03.jpg)

The u-blox ZED-F9P GNSS receiver is an old friend. It is a top-of-the-line module for high accuracy GNSS location solutions including RTK that is capable of 10mm, three-dimensional accuracy. With this board, you will be able to know where your (or any object\'s) X, Y, and Z location is within roughly the width of your fingernail! Something that doesn't get discussed as much as it should is that the ZED-F9P can also capture the timing of a signal on its INT pin with ***nanosecond*** resolution! It does that through a UBX message called TIM_TM2.

Together, these two boards form the heart of our noise source location system. Want to figure out where a sound came from? These boards let you do that!

We are also going to show you how to log the TIM_TM2 data from the ZED-F9P to SD card using the MicroMod Data Logging Carrier Board and Artemis Processor Board. But our example code can be adapted to any board if required. Then we'll go on to show how you can use our example Python code to process the data and calculate the location of the sound!

But first, let\'s talk about sound itself....

## The Speed Of Sound

We all know that sound travels slower than light. If you see a flash of lightning, it can be several seconds before you hear the clap of thunder. It's roughly 5 seconds for every mile. Count 15 seconds and the storm is 3 miles away from you. But let's go metric.

The speed of sound is about 343.42 metres per second (767 mph). But it changes with both temperature and humidity. It is 343.42 m/s at 20 °C (68 °F) at 0% humidity. On a hot, cold or wet day, it changes. It changes with pressure / altitude too because the temperature of air is linked to its pressure through the Ideal Gas Law. You might remember that from your chemistry lessons at school.

The equation we are going to use for the speed of sound is:

  Speed of Sound (m/s) = 331.3 + 0.606T
  ---------------------------------------

where T is the temperature in Celcius (Centigrade), not Kelvin.

So, the speed changes by approx. 0.6 metres per second or 0.2% for every degree change in temperature. We'll include that in our calculations.

## Calculating the Location of a Sound

Now that we know how fast sound travels, we can talk about how we go about calculating the location of the sound.

Let's say that we have two sound triggers, one at each end of a corridor, and we want to calculate where the sound of footsteps came from. If the sound triggers are 10 metres (10m) apart and the footstep came from 3m away from one, 7m away from the other, then:

- It takes 3 / 343.42 = 8.74x10^-3^ seconds (8.74 milliseconds) for the sound to reach the first sound trigger
- It takes 7 / 343.42 = 20.38x10^-3^ seconds (20.38 milliseconds) for the sound to reach the second sound trigger

But how do we calculate the location if all we have is the time each sound trigger hears the footstep? Like this:

- We have a ZED-F9P at each end and timestamp each trigger event very accurately
- The *difference* between the two timestamps will be 11.65ms (20.38ms - 8.74ms)
- We can use the time difference to calculate the location, because we know how far apart the sound triggers are
- In 11.65ms sound travels 343.42 \* 0.01165 = 4.0m
- We can calculate the distance from the first sound trigger by subtracting 4.0m from 10.0m and then dividing by 2
- Our sound came from 3.0m away from the first sound trigger

If we want to calculate the location of a sound in two dimensions, X and Y, or East and North, then we need *three* sound triggers so we can *triangulate* the location. We will show you how to do that in the next tutorial!

## Accuracy and Sources of Error

Looking at the datasheet for the ZED-F9P high precision GNSS module, we see that it quotes a 99% accuracy for its time pulse signal of 60 nanoseconds. If we look at the datasheet for the ZED-F9T high accuracy timing module, we see that it offers a big improvement: 5 nanosecond accuracy for the time pulse in absolute timing mode; and 8 nanosecond time-mark resolution. So, really, if we want the highest accuracy, we should be using the ZED-F9T.

[![SparkFun GNSS Timing Breakout - ZED-F9T (Qwiic)](https://cdn.sparkfun.com/r/600-600/assets/parts/1/8/3/3/2/18774-SparkFun_GNSS_Timing_Breakout_-_ZED-F9T__Qwiic_-01.jpg)](https://www.sparkfun.com/sparkfun-gnss-timing-breakout-zed-f9t-qwiic.html)

### [SparkFun GNSS Timing Breakout - ZED-F9T (Qwiic)](https://www.sparkfun.com/sparkfun-gnss-timing-breakout-zed-f9t-qwiic.html) 

[ GPS-18774 ]

The SparkFun GNSS Timing Breakout offers a unique entry into SparkFun\'s geospatial catalog featuring the ZED-F9T GNSS receive...

[ [\$309.95] ]

Now 60ns is really not very long. It is 0.00000006 of a second. But how far does sound travel in 60ns? If we multiply 343.42 by 0.00000006, we get 20.6 x 10^-6^ metres. Or 0.02 mm. OK. That's pretty good! So we don't need to worry too much about the timing accuracy of the ZED-F9P. And don't forget that the TIM_TM2 message, which captures our time-mark or interrupt, has nanosecond resolution.

But what about our VM1010 sound trigger? Well, the datasheet doesn't contain the numbers we really need, which is the minimum and maximum delay from the sound crossing the detection threshold to the TRIG (D~OUT~) signal going high. But, so long as there is not a big difference from chip to chip, the delay doesn't really matter. If the time delay is fixed, it will cancel out in our calculations. But if one chip has a different delay to another, that will affect the accuracy. So let's measure it!

Here is an oscilloscope trace of 100 sound events detected on two VM1010's. The oscilloscope is being triggered by one VM1010 on the yellow trace. The purple trace is the TRIG (D~OUT~) signal from the second VM1010. They were being triggered by a short 'click' sound from a dog training aid. And, yes, we were careful to make sure they were both the same distance from the click!

[![Pictured is the oscilloscope screen showing the sound events](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/2/3/1/9/SoundTutorial1_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/1/9/SoundTutorial1_1.png)

One of the interesting things I noticed is that when I **press** the button on the dog training aid, to produce the first of a pair of clicks, the output signal from the second VM1010 follows the rising edge group at \~140 microseconds **before** the first. When I **release** the button on the training aid, to make a second click, the output from the second VM1010 follows the group \~50 microseconds **after** the first. I don't yet have a theory about why it does that... But it must have something to do with slight differences in the intensity or frequency spectrum of each click.

Anyway, if we take 140 microseconds to be the worst case error between these two VM1010's, that corresponds to a distance of 343.42 \* 0.00014 = 0.048m or 4.8cm. That's still pretty respectable and not too far away from the accuracy we could expect if we were to survey-in the position of each sensing point.

In summary, we can make a hand-waving argument that we can expect the accuracy of our sound location system to be better than 10cm. Happy days!

## Example Code

The [GitHub Hardware Repo](https://github.com/sparkfunX/Qwiic_Sound_Trigger) contains [two examples](https://github.com/sparkfunX/Qwiic_Sound_Trigger/tree/master/Examples) for the Sound Trigger. You can run these in the Arduino IDE.

The first example, as the name suggests, is very simple. It uses the Qwiic (I^2^C / Wire) bus to communicate with the PCA9536 on the Sound Trigger. If a sound event is detected, you see a serial message showing how long it was since the last sound event. Then the event is cleared (reset) ready for the next one. The red LED on the sound trigger will light up briefly on each event. The LED on your board (LED_BUILTIN) will flash for a full second on each event.

The second example is the crowd pleaser! It runs on the [MicroMod Data Logging Carrier Board](https://www.sparkfun.com/products/16829) together with the [Artemis Processor Board](https://www.sparkfun.com/products/16401) but it should work just fine with any of our processor boards. It communicates with our [ZED-F9P Breakout](https://www.sparkfun.com/products/16481) and the [Qwiic Sound Trigger](https://www.sparkfun.com/products/17979) to capture sound events and log them to SD card as u-blox UBX TIM_TM2 messages.

[![SparkFun MicroMod Data Logging Carrier Board](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/7/5/0/16829-SparkFun_MicroMod_Data_Logging_Carrier_Board-01A.jpg)](https://www.sparkfun.com/sparkfun-micromod-data-logging-carrier-board.html)

### [SparkFun MicroMod Data Logging Carrier Board](https://www.sparkfun.com/sparkfun-micromod-data-logging-carrier-board.html) 

[ DEV-16829 ]

The MicroMod Data Logging Carrier offers a low-power data logging platform using the MicroMod system allowing you to choose y...

[ [\$22.95] ]

[![SparkFun MicroMod Artemis Processor](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/1/3/0/16401-SparkFun_MicroMod_Artemis_Processor-01.jpg)](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html)

### [SparkFun MicroMod Artemis Processor](https://www.sparkfun.com/sparkfun-micromod-artemis-processor.html) 

[ DEV-16401 ]

Featuring the Artemis Module, this processor is capable of machine learning, Bluetooth, I2C, GPIO, PWM, SPI & packaged to fit...

[ [\$17.50] ]

## Hardware Connections

- Solder a 6-way row of header pins to the Qwiic Sound Trigger so you can access the TRIG pin.
- Please see the [Data Logging Hookup Guide](https://learn.sparkfun.com/tutorials/micromod-data-logging-carrier-board-hookup-guide)
- Insert the Artemis Processor into the MicroMod Data Logging Carrier Board and secure with the screw.
- Connect your ZED-F9P GNSS breakout to the Carrier Board using a Qwiic cable.
- Connect an antenna to your GNSS board. The antenna must have a clear view of the sky. Extend and feed the cable through a window if you need to.
- Insert a formatted micro-SD card into the socket on the Carrier Board.
- Connect the Qwiic Sound Trigger to the ZED-F9P using a second Qwiic cable.
- Use a jumper cable to connect the TRIG pin on the Qwiic Sound Trigger to the INT pin on the ZED-F9P breakout.
- Connect the Carrier Board to your computer using a USB-C cable.

[![Pictured is the Qwiic Sound Trigger connected to the ZED-F9P and Micro Mod data logging carrier board](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/1/9/SoundTutorial1_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/1/9/SoundTutorial1_2.png)

To minimise I^2^C bus errors, it is a good idea to open the I^2^C pull-up split pad links on the MicroMod Data Logging Carrier Board and the u-blox module breakout and the Qwiic Sound Trigger.

## Software Setup

- Ensure you have the SparkFun Apollo3 boards installed
- This code has been tested using version 1.2.1 of the Apollo3 boards on Arduino IDE 1.8.13.
- Select \"SparkFun Artemis MicroMod\" as the board type.
- Press upload to upload the code onto the Artemis.
- Open the Serial Monitor at 115200 baud to see the output.

Each time the Qwiic Sound Trigger detects a sound, it pulls its TRIG pin high. The ZED-F9P will detect this on its INT pin and generate a TIM_TM2 message. The Artemis will log the TIM_TM2 messages to SD card. You can then study the timing of the sound pulse with nanosecond resolution and calculate the location of the sound!

The code will \"debounce\" the sound event and reset the VM1010 for the next event after 250ms.

Note: TIM_TM2 can only capture the timing of one rising edge and one falling edge per navigation solution. So with setNavigationFrequency set to 4Hz, we can only see the timing of one rising edge every 250ms. The code \"debounces\" each sound event to make sure there will only be one rising edge event per navigation solution.

TIM_TM2 messages are only produced when a rising or falling edge is detected on the ZED-F9P's INT pin. If you disconnect your TRIG to INT jumper wire, the messages will stop.

Data is logged in u-blox UBX format. Please see the u-blox protocol specification for more details. You can replay and analyze the data using [u-center](https://www.u-blox.com/en/product/u-center) should you want to.