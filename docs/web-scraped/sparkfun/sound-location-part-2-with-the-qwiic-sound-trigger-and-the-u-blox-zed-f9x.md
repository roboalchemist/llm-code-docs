# Source: https://learn.sparkfun.com/tutorials/sound-location-part-2-with-the-qwiic-sound-trigger-and-the-u-blox-zed-f9x

## Introduction

In the [previous tutorial](https://learn.sparkfun.com/tutorials/sound-location-with-the-qwiic-sound-trigger-and-the-u-blox-zed-f9x), we showed you how to calculate the location of a sound using the new [SparkX Qwiic Sound Trigger](https://www.sparkfun.com/products/17979) and the [u-blox ZED-F9P GNSS receiver](https://www.sparkfun.com/products/16481).

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

The Qwiic Sound Trigger can be used on its own, or as part of your Qwiic system. It is based on the VM1010 from Vesper Technologies and the TI PCA9536 GPIO expander. The VM1010 is a clever little device which can be placed into a very low power \"Wake On Sound\" mode. When it detects a sound, it wakes up and pulls its TRIG (D~OUT~) pin high. The VM1010 can then be placed into \"Normal\" mode by pulling the MODE pin low; it then functions as a regular microphone. The analog microphone signal is available on the AUDIO (V~OUT~) pin. All of this happens really quickly, within 50 microseconds (much faster than a capacitive MEMS microphone), so you don\'t miss the start of the audio signal. This makes it ideal for use as a sound trigger!

The u-blox ZED-F9P GNSS receiver is an old friend. It is a top-of-the-line module for high accuracy GNSS location solutions including RTK that is capable of 10mm, three-dimensional accuracy. With this board, you will be able to know where your (or any object\'s) X, Y, and Z location is within roughly the width of your fingernail! Something that doesn't get discussed as much as it should is that the ZED-F9P can also capture the timing of a signal on its INT pin with ***nanosecond*** resolution! It does that through a UBX message called TIM_TM2.

In this tutorial, we take this to the next dimension. Quite literally! Last time, we used two sound trigger systems to calculate where a sound came from along the line from one trigger to the other. That's a one-dimensional (1D) system. If we add a third sound trigger, we can *triangulate* the location of a sound in two dimensions (2D) allowing us to plot the position in X and Y or East and North!

Let\'s talk first about *triangulation*....

## Sound Source Triangulation

Last time, we learned that we can calculate the location of a sound by measuring the *difference* in the sound's time-of-arrival at two sound triggers. In our 1D example, we:

- Converted the time difference into distance (by multiplying by the speed of sound)
- Subtracted that distance from the distance between our two sound triggers
- And then divided by 2 to calculate the distance from the closest trigger (the one that detects the sound first)

In 2D, there is a little more math involved. Let's call our three sound trigger systems A, B and C. A is our reference or *origin*. If we position trigger B due East from A, we can call the line that joins A to B our X axis. Remember when you used to draw graphs in math class? You had the origin in the bottom left corner of your graph paper and you drew the X axis horizontally out to the right. We are doing the same thing here. Trigger A is our origin at X = 0 and Y = 0. We write that as (0,0). If Trigger B is 8 metres (8m) away from A, then its location is X = 8 and Y = 0. We write that as (8,0).

[![Pictured are the coordinates of two points A and B and the line formed between them](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_1.png)

So far, so good. Now, where should we position trigger C? In reality, it doesn't really matter. We could position C so that ABC forms a perfect equilateral triangle (a triangle where all three sides are the same length). That would give us the best coverage of the area. But the coordinates of C would be (4,6.93). Not pleasant.

[![Pictured is an equilateral triangle formed from points A, B and C](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_2.png)

To keep the math simpler for this example, let's position C 6m due North from A. The coordinates of C are X = 0 and Y = 6. We write that as (0,6).

[![Pictured is a right triangle formed from points A, B and C.](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_3.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_3.png)

We know the distance from A to B is 8m, and that the distance from A to C is 6m. But what about the distance from B to C? We need to know that too. If we get out a tape measure and measure it, we'll find it is exactly 10m. If you remember Pythagoras' Theorem from your math class, *the square on the hypotenuse is equal to the sum of the squares on the other two sides*, we can calculate the distance from B to C by:

- Squaring (multiplying by itself) the distance from A to B: 8 x 8 = 64
- Squaring (multiplying by itself) the distance from A to C: 6 x 6 = 36
- Summing (adding) them: 64 + 36 = 100
- Calculating the square root: √100 = 10

[![Pictured are squares formed on the three sides of the triangle](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_4.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_4.png)

Again, to keep the math easier, let's pretend that the speed of sound is 1 metre per second (1m/s), not 343.42m/s.

Now, let's suppose our sound trigger system is running and it detects a sound:

- The time recorded by trigger A is 10:00:03.605551
- The time recorded by trigger B is 10:00:05.385165
- The time recorded by trigger C is 10:00:05.000000

Let's calculate the differences in those times:

- A records the sound first, so we will use that as our reference
- B records the sound 10:00:05.385165 - 10:00:03.605551 = 1.779614 seconds later
- C records the sound 10:00:05.000000 - 10:00:03.605551 = 1.394449 seconds later

With the speed of sound being 1m/s, we now know that the sound travelled an extra 1.779614m when travelling to B compared to A. And we know that the sound travelled an extra 1.394449m when travelling to C compared to A.

What we do not know is how far the sound travelled to get to A. That's the first thing we need to calculate.

Let's call the location of the sound: S. Let's call the coordinates of S: ( x , y ). Let's call the distance from S to A: D.

If we sketch that - not to scale - it looks like this:

[![Pictured is right triangle A B C with point S located within the triangle](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_5.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_5.png)

We know that:

- The distance from S to A is D metres
- The distance from S to B is D + 1.779614 metres
- The distance from S to C is D + 1.394449 metres

In order to find the location of S, we need to use triangles. That's why this technique is called "triangulation". In trigonometry and geometry, triangulation is the process of determining the location of a point by forming triangles to it from known points.

If we divide our diagram up into more triangles:

[![Pictured is the triangle formed from points A B and S](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_6.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_6.png)

We can use Pythagoras' Theorem to calculate the distances we need:

- D^2^ = x^2^ + y^2^
- (D + 1.779614)^2^ = (8 - x)^2^ + y^2^
- (D + 1.394449)^2^ = x^2^ + (6 - y)^2^

We can write that as:

- D^2^ = x^2^ + y^2^
- y^2^ = (D + 1.779614)^2^ - (8 - x)^2^
- x^2^ = (D + 1.394449)^2^ - (6 - y)^2^

We need to solve for D. To begin, let's substitute the value for y^2^ from the second equation into the first equation:

- D^2^ = x^2^ + (D + 1.779614)^2^ - (8 - x)^2^

Multiplying out the brackets, that becomes:

- D^2^ = x^2^ + D^2^ + 1.779614.D + 1.779614.D + 1.779614^2^ - ( 8^2^ - 8x - 8x + x^2^ )

Simplifying, it becomes:

- D^2^ = x^2^ + D^2^ + 3.559228.D + 3.167026 - (64 - 16.x + x^2^)

If we remove the brackets:

- D^2^ = x^2^ + D^2^ + 3.559228.D + 3.167026 - 64 + 16.x - x^2^

The D^2^ cancel out and so do the x^2^ leaving:

- 0 = 3.559228.D + 3.167026 - 64 + 16.x

One final rearrange leaves:

- 16.x = -3.559228.D + 60.832974

If we divide through by 16 we are left with:

- x = -0.222452.D + 3.802061

Now let's go back to our three triangles:

- D^2^ = x^2^ + y^2^
- y^2^ = (D + 1.779614)^2^ - (8 - x)^2^
- x^2^ = (D + 1.394449)^2^ - (6 - y)^2^

This time, let's substitute the value for x^2^ from the third equation into the first equation:

- D^2^ = (D + 1.394449)^2^ - (6 - y)^2^ + y^2^

Multiplying out the brackets, that becomes:

- D^2^ = D^2^ + 1.394449D + 1.394449D + 1.944488 - (36 - 6y - 6y + y^2^) + y^2^

If we remove the brackets:

- D^2^ = D^2^ + 1.394449D + 1.394449D + 1.944488 - 36 + 6y + 6y - y^2^ + y^2^

Again, the D^2^ cancel out and so do the y^2^ leaving:

- 0 = 2.788898.D + 1.944488 - 36 + 12.y

One final rearrange leaves:

- 12.y = -2.788898.D + 34.055512

If we divide through by 12 we are left with:

- y = -0.232408.D + 2.837959

Now we can put our values for x and y back into our first equation:

- D^2^ = x^2^ + y^2^

- D^2^ = (-0.222452.D + 3.802061)^2^ + (-0.232408.D + 2.837959)^2^

Multiplying out the brackets, we get:

- D^2^ = 0.049485.D^2^ - 1.691552.D + 14.455668 + 0.054013.D^2^ - 1.319129.D + 8.054011

Simplifying:

- 0.896502.D^2^ + 3.010681.D - 22.509679 = 0

Now, I'm sure you will remember *quadratic equations* from your math class too? We can solve for D using the equation:

- ( -b +/- √(b^2^ - 4.a.c ) ) / 2.a

- a = 0.896502

- b = 3.010681

- c = -22.509679

Inserting our values, D is:

- ( -3.010681 +/- √(9.064200 + 80.719889) ) / 1.793004

Which equals:

- 3.605550 or -6.963804

We can ignore the negative value since it is not within our triangle. Now we know that D is 3.605550m !

Looking back at our equations for x and y:

- x = -0.222452.D + 3.802061
- y = -0.232408.D + 2.837959

If we insert the value for D, we can finally calculate the x and y coordinates of S:

- ( -0.802062 + 3.802061 , -0.837959 + 2.837959 )

Which is:

- ( 3.000 , 2.000 )

[![Pictured are the calculated coordinates of point S](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_7.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_7.png)

Fancy that!

This technique can be used on any configuration of trigger locations. They don't have to be positioned in a neat right angle triangle. If you would like proof of that and would like to see the math to solve it, have a look at the section called [Here There Be Dragons!](https://learn.sparkfun.com/tutorials/sound-location-part-2-with-the-qwiic-sound-trigger-and-the-u-blox-zed-f9x#here-there-be-dragons)

## Now, The Good News

Thanks for sticking with us. The good news is that we've written more Python code to do that math for you!

The [GitHub Hardware Repo](https://github.com/sparkfunX/Qwiic_Sound_Trigger) contains [two examples](https://github.com/sparkfunX/Qwiic_Sound_Trigger/tree/master/Examples) for the Sound Trigger. You can run these in the Arduino IDE. The second example is the crowd pleaser! It runs on the [MicroMod Data Logging Carrier Board](https://www.sparkfun.com/products/16829) together with the [Artemis Processor Board](https://www.sparkfun.com/products/16401) but it should work just fine with any of our processor boards. It communicates with our [ZED-F9P Breakout](https://www.sparkfun.com/products/16481) and the [Qwiic Sound Trigger](https://www.sparkfun.com/products/17979) to capture sound events and log them to SD card as u-blox UBX TIM_TM2 messages.

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

Once you have your three sound event UBX TIM_TM2 files, our [Sound_Trigger_Analyzer_2D.py](https://github.com/sparkfunX/Qwiic_Sound_Trigger/tree/master/Utils) will process the files for you and calculate the location of the sound events!

- Copy the TIM_TM2.ubx file from the SD card from the first system. Rename the file so you know which system it came from. You might want to call it TIM_TM2_A.ubx.
- Do the same for the TIM_TM2.ubx files from the second and third systems. Again, rename them so you know which system they came from.
- Place all three files in the same folder / directory as the Sound_Trigger_Analyzer_2D.py Python file

Run the Python code by calling:

    language:python
    python Sound_Trigger_Analyzer_2D.py TIM_TM2_A.ubx TIM_TM2_B.ubx TIM_TM2_C.ubx 8.0 6.0 10.0 20.0

- Replace TIM_TM2_A.ubx with the name of the file from the first system (A)
- Replace TIM_TM2_B.ubx with the name of the file from the second system (B)
- Replace TIM_TM2_C.ubx with the name of the file from the third system (C)
- Replace the 8.0, 6.0 and 10.0 with the distances between your sound triggers in metres
  - You must enter them in the correct order: **A-B** then **A-C** then **B-C**
- The 20.0 is optional. It is the temperature in Celcius (Centigrade). Change this to your actual temperature for added accuracy

The Python code will calculate and display the (x,y) coordinates of any valid sound events it finds. The coordinate system uses the location of A as the origin, and the line running from A to B as the X axis. The Y axis is (of course) 90 degrees counterclockwise from X.

The calculation code assumes that the X coordinate of C is *between* A and B. If C lies to the left of A, or the right of B, then you need to rename your points. If C is to the left of A, then B becomes A, C becomes B, and A becomes C:

[![Pictured are two triangles](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_8.png)](https://cdn.sparkfun.com/assets/learn_tutorials/2/3/2/0/SoundTutorial2_8.png)

Enjoy your coordinates!