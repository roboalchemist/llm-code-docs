# Source: https://learn.sparkfun.com/tutorials/hackers-in-residence---sound-and-motion-reactivity-for-wearables

## A Dance of Sound, Light and Motion

At SparkFun, I wanted a smarter jacket: a color changing jacket that would react to my surroundings. The concept seemed simple enough. Using sound and motion sensing as an interface I\'m able to change colors to merge with the environment. This elevates the need for buttons or switches that might otherwise take our user out of the present moment.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/reactive-jacket-01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/reactive-jacket-01.png)

*The finished product.*

There are a number of challenges, mainly comfort and control. I find one of the keys to comfort in wearing a lit up garment is having symbiosis with the surrounding environment. However, I needed to distinguish between the high energy atmosphere of a frenetic art opening and otherwise subdued activities like sharing a meal or waiting in line. We often don\'t take into account how bright our garments may be to in the eyes of others, and the aim of this project was to tackle this problem. One way to accomplish this synergy with one\'s environment is to listen before emoting, or, this this case, sense before lighting too brightly or deploying patterns too quickly.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/01.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/01.JPG)

*A long exposure photo displaying how sounds can be viewed across various frequencies.*

I used an accelerometer and microphone to sense the environment and wearers energy level. Rapid changes in acceleration and specifically rotations of the wearer are interpreted as being in an environment where lighting may be a bit brighter and patterns cycle faster.

I used a microphone to sense the ranges and volume of various frequencies. Fairly normal frequencies of human voices and minimal volumes would be interpreted to give a fairly consistent color without much movement. If there were low frequencies and louder volumes, the design assumes music is being played and introduces more colors.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/02.jpg)

*With little motion or sound, the colored spine appears to reflect the given color rather than emit.*

A specific color pallet was chosen to also merge the wearer into their surrounding. A pinkish mid range is in harmony with the rest of the design to blend in during times of inactivity while blues and turquoises become present during repeated audio with more low end. These blues are in direct contrast to the rest of the design and thereby become quite apparent.

## Planning it Out 

SparkFun\'s amazing facilities and warehouse made for the problem of choice. Generally, I choose components based on what is readily available or least costly. Given my unique circumstance, I wanted to choose the very best components to ease the development and optimize for the overall quality of the affect.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/03.2014_spark_warehouse1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/03.2014_spark_warehouse1.jpg)

## Assembling the Hardware

Here is the hardware I ended up using in the project.

\

Let\'s go over each component in detail.

#### Battery Power

I love these cell phone boost charger external batteries. Having the charger, boost regulator, battery, and protection circuitry all in one packages saves a ton of time and money. You can always charge your phone from it in a pinch and carrying an extra is easy with this thin design.

Of course I have to include a [Wake-on-Shake](https://www.sparkfun.com/products/11447). I\'m starting to put them in all my mobile projects and have all but stop using power switches to turn things off. I\'d been having entirely [too much fun](https://www.youtube.com/watch?v=IqHdbgaTaaI) with these.

#### Motion

I choose to put a [combined accelerometer and gyro](https://www.sparkfun.com/products/11028) on board to detect certain types of motion. Specifically, I wanted to isolate when one is spinning or turning around. I find this could in the future be a compelling control signal. The up and down motion of the body could be an indicator of walking, stillness, running, or dancing.

#### LEDs

I developed a variety of techniques for mounting LEDs for wearable use. [WS2812](https://grabcad.com/library/ws2812-rgb-led-strip-60-meter-1) LEDs are by far my favorite. By only needing 3 conductors, I can now use the best [conductive ribbon](https://www.sparkfun.com/products/10172) to attach them to my jacket. Using this very flexible e-textile spine makes it much more resilient to any movements and folding that a normal garment might undergo.

I cut a small portion out of the data trace of the conductive ribbon under where I\'ll solder each LED. This allows the data lines to not be shared by multiple LEDs, so the signal can pass cleanly. I\'ve started doing this a lot at [Crashspace](http://blog.crashspace.org/) and even helped with a [tutorial](http://www.instructables.com/id/LED-Matrix-Bike-Safety-Backpack/) if you want to try sewing and wearing these NeoPixel/WS2812 style addressable strip LEDs yourself.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/04.led-ribbon-cut.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/04.led-ribbon-cut.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/05.led-strand-soldered.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/05.led-strand-soldered.jpg)

I ended up affixing these within a [3d printed led housing](http://www.thingiverse.com/thing:259291) It adds some much needed diffusion and allows the LEDs to be unbuttoned should i want to wash the jacket.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/06small.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/06small.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/07small.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/07small.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/08small.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/08small.jpg)

I encourage you to go more [extreme](http://hackaday.io/project/41-LED-Stegosaurus-Spikes) with your 3d printed led diffusors, if you dare.

#### Sound

Microphones are fun! Yet, sound reactivity is hard. It is a ton of data to parse through. It takes some serious sophistication to even determine the frequency of incoming sound.

Luckily, there is help. An Arduino can determine what frequencies are present, but I found you don\'t get much indication of the volume within each frequency range.

I ended up testing a bunch of microphones (and their pre-amps) to determine which would give me the most fidelity at louder volumes. Using a set of [pure data patches](https://github.com/mpinner/SoundMotions/tree/master/puredata) I was able to generate tones, read the Arduino\'s frequency analysis, and compare.

I found the [sound detector](https://www.sparkfun.com/products/12642) performed better overall. I love the added benefits of having the preamp broken out so it is easily tuned and the sound detection portion works very well as an additional sensor.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/09.sound-tests.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/09.sound-tests.JPG)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/10.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/10.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/11.micTestSetup.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/11.micTestSetup.JPG)

[![Mic Test - Pure Data ](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/12.micTest.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/12.micTest.png)

*Performing some Mic tests with [Pure Data](http://puredata.info/).*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/13.micGraph.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/13.micGraph.png)

*Graph of all the results using different mic boards.*

#### MSGEQ7 - Graphic Equalizer Display Filter

After digging into the microphone performance and testing the software FFT. I decided a hardware solution would make more sense. The [MSGEQ7](https://www.sparkfun.com/products/10468) did a much better job of analyzing the sound for various frequencies. Also, delegating this responsibility to an external piece of hardware simplifies the code and frees up my Arduino to control the lighting and analyze the motion data.

The circuit for the MSGEQ7 required some components I didn\'t readily have on on hand. The [Spectrum Shield](https://www.sparkfun.com/products/10306) works very well, but it way too big to wear in any comfortable way. After consulting the [eagle files](http://cdn.sparkfun.com/datasheets/Dev/Arduino/Shields/SpectrumShield-v14.zip), I decided the best approach it was to cut it down to a more wearable size.

At half the size it still isn\'t small, but it matches the size of all my other components and will now layout quite consistently within the collar.

[![Cutting the Spectrum Shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/14.spectrum-cut.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/14.spectrum-cut.png)

#### Teensy 3.1

The Teensy is nice because you can power and program it directly from USB. This works well to get thing tested and running quickly.

The 5v tolerant inputs of the new Teensy 3.1 are great for the audio part of this project as running my microphone at 5v gets me more range.

Ultimately, I\'m happy to run a 3.3v micro to avoid all the voltage level conversion required to interface with most accelerometers.

The 3.3v logic also happens to work well enough for the ws2812/Neopixel LEDs, [barely](https://cdn.sparkfun.com/datasheets/Components/LED/WS2812.pdf).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/ws2811-at-3_3v.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/ws2811-at-3_3v.png)

Using any Teensy is a bit more complex to get up and running. You need to add a bunch of configuration, code, and libraries to your Arduino IDE. Luckily there is [a great installer](https://www.pjrc.com/teensy/teensyduino.html) available that make this very straight forward for any operating system.

The Teensy has very recently added some [audio offerings](http://www.pjrc.com/teensy/td_libs_Audio.html), which I may utilize to replace the msgeq7 portion of this project.

## Software, Integration, and Smoothing 

After selecting these components it comes time for some serious code, integration, and smoothing.

### EWMA: Exponentially Weighted Moving Average

I hope we\'ve all learned what it means to take the average of a given dataset. The average volume wouldn\'t be very interesting and certainly not very reactive. By calculating simple average over time of results will converge on a single value. This doesn\'t work because even large changes in sound or motion would not even be detected. It can also be a somewhat expensive operation to always be adding to bigger numbers and dividing.

A **moving** average is a great optimization and it allows you to recalculate each time a new datapoint arrives. This is a great optimization but continues to lack reactivity. I want instant feedback when loud sounds occur.

**Exponential weighting** really helps maintain this reactivity by weighting new data much more than the past values. This allows for instant feedback upon drastic changes while still avoiding the flicking and flashing experienced from noisy data.

In doing my research I found an EWMA is very often used to analyze financial markets as they need to quickly detect sudden rises and falls without paying too much mind to the minimal changes. This [blog post](http://connor-johnson.com/2014/02/01/smoothing-with-exponentially-weighted-moving-averages/) does an excellent job of describing EWMA in detail for our purposes of smoothing.

[![EWMA Correction](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/2/15.ewma_correction.png)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/15.ewma_correction.png)

I found a great [Arduino library for EWMA](https://github.com/CBMalloch/Arduino/tree/master/libraries/EWMA) and was quickly able to apply this smoothing with different coefficients to my motion axes and sound frequency ranges.