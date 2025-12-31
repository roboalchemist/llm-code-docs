# Source: https://learn.sparkfun.com/tutorials/weather-meter-hookup-guide

## Introduction

Weather stations require specialized sensors to accurately measure and report on weather conditions. For all of your DIY weather project needs, we have the [Weather Meters](https://www.sparkfun.com/products/15901)!

[![Weather Meter Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/4/5/3/9/15901-Weather_Meter-02.jpg)](https://www.sparkfun.com/weather-meter-kit.html)

### [Weather Meter Kit](https://www.sparkfun.com/weather-meter-kit.html) 

[ SEN-15901 ]

Whether you are measuring wind speed, direction or rain, this is the Weather Meter for you.

[ [\$79.95] ]

These meters allow you to measure **wind speed**, **wind direction**, and **rainfall** easily over RJ11 connections.

### Required Materials

To follow along with this project tutorial, you will need the following materials:

- 1x Weather Meter kit
- 1x [Phillips Head screwdriver](https://www.sparkfun.com/products/14234)
- 1x [Flathead screwdriver (optional)](https://www.sparkfun.com/products/14234)

### Suggested Reading

If you aren\'t familiar with the following concepts, we recommend checking out these tutorials before continuing.

[](https://learn.sparkfun.com/tutorials/analog-vs-digital)

### Analog vs. Digital 

This tutorial covers the concept of analog and digital signals, as they relate to electronics.

[](https://learn.sparkfun.com/tutorials/digital-logic)

### Digital Logic 

A primer on digital logic concepts in hardware and software.

[](https://learn.sparkfun.com/tutorials/data-types-in-arduino)

### Data Types in Arduino 

Learn about the common data types and what they signify in the Arduino programming environment.

[](https://learn.sparkfun.com/tutorials/reed-switch-hookup-guide)

### Reed Switch Hookup Guide 

Magnetically-actuated reed switches are the perfect component for non-contact proximity sensors. This tutorial provides a quick overview and example hook up.

## Hardware Overview

When you receive your meters, unbox all of the components, and ensure you have all of the necessary pieces.

[![Included Parts](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/WeatherMeter_Parts_included.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/WeatherMeter_Parts_included.jpg)

You should have:

- Two (2) metal tubes
- Three (3) sensors:
  - rain gauge
  - anemometer
  - wind vane
- Two (2) gear clamps
- One (1) center mount armature
- One (1) side mount armature
- One (1) bag screws/nuts
- One (1) pack plastic zip ties

All of the sensors in the weather meter kit are [passive components](https://www.allaboutcircuits.com/textbook/semiconductors/chpt-1/active-versus-passive-devices/). This means you will need a voltage source in order to measure anything with them.

Each sensor is terminated with an RJ11 connector.

### Rain Gauge

The rain gauge, as you may have guessed, measures rainfall. You sould get a rain gauge that looks similar to the image below.

[![Rain Gauge](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/RainGauge.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/RainGauge.jpg)

[]**[Heads up!](https://learn.sparkfun.com/tutorials/weather-meter-hookup-guide#rain_gauge_level)** Depending on the version of the weather meter that you receive, the rain gauge\'s may look different. There may be a level bubbler and a deeper reservoir for collecting water. Don\'t worry, the overall functionality is the same!\
\

[][![](https://cdn.sparkfun.com/r/300-300//assets/parts/1/4/5/3/9/15901-Weather_Meter-03.jpg)](https://cdn.sparkfun.com//assets/parts/1/4/5/3/9/15901-Weather_Meter-03.jpg)

The sensor is a [self-emptying tipping bucket collector](https://www.weathershack.com/static/ed-tipping-bucket-rain-gauge.html). This means that for each **0.011\" (0.2794 mm) of rain** that falls in the sensor, the bucket will tilt, dumping the water out and closing a momentary contact.

The closure of the momentary switch can be measured using interrupt pins or a digital counter. The center conductors of the RJ11 connector are connected to the gauge\'s switch.

### Anemometer

An anemometer measures wind speed.

[![Anemometer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Anemometer_4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Anemometer_4.jpg)

The wind moves the cups on the anemometer, which in turn, rotate a enclosed magnet. The magnet closes a reed switch on each rotation, which is reflected on the output. You can measure this on the two inner conductors of the RJ11 connector (pins 2 and 3), using a digital counter or interrupt pins on your microcontroller. To convert this into a functional wind speed, use the conversion of **1.492 mph = 1 switch closure/second**. For those in metric land, this is **2.4 km/h**.

### Wind Vane

The wind vane indicates the direction that the wind is blowing.

[![Wind Vane](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/WindVane.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/WindVane.jpg)

While you\'d think think this would be a simple thing to represent with electronic components, this is actually the most complex gauges of the three. Internally on the vane are eight switches, each with their own unique resistor.

[![Wind Vane internal circuitry](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/WindVane_Switches.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/WindVane_Switches.JPG)

*The eight switches and their respective resistors internally on the wind vane.*

As the wind vane rotates, a magnet closes the reed switches, and may close two at a time due to their proximity to each other. With the use of an external resistor, a voltage divider can be created. Measuring the voltage output with an analog-to-digital converter on your microcontroller allows you to determine the direction the wind vane is pointing.

As the voltage output will depend on the value of the external resistor used, there is not one common conversion function. For an example of how to calculate this, please reference the datasheet linked in the [Resources and Going Further](https://learn.sparkfun.com/tutorials/weather-meter-hookup-guide#resources-and-going-further) for the meters.

Since the values outputted by the wind vane are are based on degrees, you can, in theory, have any value represent any direction. However, we recommend having the value at degree 0 represent North for ease of use. There are also very tiny, barely-visible direction indicators on all four sides of the wind vane. If you choose different values to indicate directions, be sure to mark then accordingly. When installing and positioning your weather meters, ensure that any direction markings are pointed in the correct orientation.

Please note that the wind vane \"points\" in the direction **from which the wind is blowing**.

## Hardware Assembly

The weather meter is an easy kit to assemble \-- there are only mechanical connections that need to be made.

### Armature

To begin, find the two metal tubes, and slide them together.

[![Assemble tubes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Assemble_tubes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Assemble_tubes.jpg)

Next, add the armature to the top of the tube set. Make sure to line up the nub on the armature with the notch in the tube.

[![Armature Attachment](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Armature_attachment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Armature_attachment.jpg)

Use one of the included screws and nuts to lock it in place.

[![Securing armature to tube with a screw](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Attach_Armature_Screw.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Attach_Armature_Screw.jpg)

### Anemometer

Next, we will mount the anemometer on one side of the armature.

The anemometer has a nub on it that matches notches in the armature. This will help secure the anemometer once attached and only allows the sensor to be mounted in one direction.

[![Anemometer Alignment](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Anemometer_alignment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Anemometer_alignment.jpg)

Slide the anemometer onto the armature until it locks in place.

[![Mouting anemometer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Anemometer_attachment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Anemometer_attachment.jpg)

Use an included screw and nut to lock the sensor in place (make sure these are tight).

[![Screw/nut attachment of anemometer](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Anemometer_screw_attachment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Anemometer_screw_attachment.jpg)

### Wind Vane

To attach the wind vane, you will follow the same procedure as installing the anemometer.

Line up the sensor and the armature, and push the wind vane into place.

[![Align the wind vane](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Wind_vane_alignment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Wind_vane_alignment.jpg)

Once again, use a screw and nut to secure the sensor in place.

[![Vane attached with screw](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/vane_screw_attachment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/vane_screw_attachment.jpg)

### Rain Gauge

To attach the rain gauge, we also need a secondary armature. This is used to keep the rain gauge away from the other sensors to ensure it can get an accurate measurement. If the rain gauge is mounted underneath the wind vane or the anemometer, they can block rainfall into the gauge or offset the readings due to runoff.

Attach the rain gauge armature to the metal tube using the attached screws and nuts. The two halves piece together with the metal tube in between. Once you have it located where the rain gauge will be clear of the anemometer and wind vane, tighten it into place.

[![Rain Gauge Armature Attachment](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Rain_gauge_Armature_Attachment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Rain_gauge_Armature_Attachment.jpg)

Once again, the rain gauge has notches to ensure it mounts snugly on the armature.

[![Rain Gauge Alignment](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Rain_Gauge_Alignment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Rain_Gauge_Alignment.jpg)

Line these up, and push the rain gauge into place.

[![Raing Gauge Attachment](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Rain_Gauge_Attachment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Rain_Gauge_Attachment.jpg)

Using one of the remaining small screws, secure the rain gauge in place.

[![Secure Raing Gauge with Screw](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/AttachingRainGauge.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/AttachingRainGauge.jpg)

The rain gauge has two tabs with holes on either side. These can be used to mount the sensor on different surfaces such as rooftops or fences as well.

### Wire Management

If you\'ve gotten this far, congratulations! Now it\'s on to the easy part \-- cable management. Luckily, this isn\'t nearly as difficult as [some wiring projects](https://www.reddit.com/r/cablefail/).

Unravel the wires from the anemometer and the wind vane. On the bottom side of the armature, you will see clips to hold these wires in place. Slide the wire from each sensor into those.

[![Armature Wire Clips](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Wire_Management.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Wire_Management.jpg)

Once you have both of those cables plugged in, you will notice that the anemometer cable is much shorter than the wind vane. As we mentioned in the Hardware Overview, the anemometer switch conductors are shared between the anemometer and the wind vane. You will need to plug the anemometer cable into the wind vane.

[![Plug Anemometer Cable into Wind Vane](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Anemometer_plugIn_to_Vane.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Anemometer_plugIn_to_Vane.jpg)

Run all of the remaining wires down the metal tubes, and use the included zip ties to secure them. This will prevent wind from yanking your wires out from your associated electronics.

[![Zip ties](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/ZipTies.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/ZipTies.jpg)

Success! You now have an assembled weather meter! Make sure your rain gauge is clear of the anemometer and wind vane, and didn\'t shift during assembly. Your weather meter will look similar to the image below.

[![Angled Assembled Meters](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Angled_Assembled_Meters.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Angled_Assembled_Meters.jpg)

You can now mount this, attach it to various electronics, or just use it as an impromptu lightsaber in battle.

### Mount the Meter (Optional)

Now that you\'ve got your meter assembled, you need to place it somewhere with weather! You can use the included gear clamps to help mount and secure your meter.

To show a demonstration of how to use the gear clamp, we slid a gear clamp around our meter and a piece of PVC pipe. Then tighten the gear clamp using a flat head screw driver.

[![Gear clamp](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/6/8/1/Mounting_Hardware.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/6/8/1/Mounting_Hardware.jpg)

Keep in mind that there are many different ways to approach this problem. You will need to find a mounting solution that works specifically for your application.