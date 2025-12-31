# Source: https://learn.sparkfun.com/tutorials/building-an-autonomous-vehicle-the-batmobile

## Answering the Why

Why build an autonomous vehicle for [A+PRS](https://avc.sparkfun.com/)?

[![Smiling big in Batmobile](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Smiles-3.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Smiles-3.JPG)

*Test driving the Batmobile*

The thrill of taking a corner, extremely low to the ground, with your gut telling you these g-forces are not normal\... that's why we spend countless hours building these silly Power Wheels vehicles. The giggles and grins are unavoidable! These cars are so much fun to drive \-- and even more fun to race!

[![Toni the race car driver](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Toni-Racecar-Driver.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Toni-Racecar-Driver.gif)

In 2016, SparkFun had its eighth annual [Autonomous Vehicle Competition](https://avc.sparkfun.com). This year saw the introduction of a new rule: you needed to carry a human (or a 20lb dead weight in the form of a watermelon if you were too chicken). To do this, my wife, Alicia, and I modified a Batmobile Power Wheels and combined it with a Razor chassis. The result was an extremely zippy electric go-kart that left a perma-grin on everyone who drove it.

Our goal was to create a vehicle that could quickly and easily switch between human driver and driverless modes so that we could compete in both PRS and A+PRS categories. In the end, Alicia placed a very respectable third place in the driver category, and I did not finish (DNF) in the autonomous category, running into numerous hay bales.

This tutorial attempts to document a six-month build process for an Autonomous + Power Racing Series (A+PRS) vehicle. Every autonomous vehicle is unique, and the requirements of each will vary from build to build.

[![Batmobile with top off](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Top_Off.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Top_Off.JPG)

### Materials

You can see our overall budget, including a list of components and vendors [here](https://docs.google.com/spreadsheets/d/1ArnGv4S5Yt92EbWMC0-9kvYVRUPvtWbAeWbnaERji5Y/edit?usp=sharing).

[A+PRS Batmobile Material Spreadsheet](https://docs.google.com/spreadsheets/d/1ArnGv4S5Yt92EbWMC0-9kvYVRUPvtWbAeWbnaERji5Y/edit?usp=sharing)

\
You can get all the code from our repo [here](https://github.com/nseidle/APRS).

[A+PRS Batmobile GitHub Repository](https://github.com/nseidle/APRS)

\

## Chassis

The AVC rules stipulate that you cannot spend more than \$500 on your total budget and that you have to stay within certain size restrictions. We started trolling craigslist to see what was out there and immediately found a plethora of free or cheap "broken" Power Wheels. When a Batmobile for \$25 popped up, we quickly snagged it.

[![Dusty Batmobile](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Batmobile.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Batmobile.jpg)

*Dusty with dog hair and dead spiders \-- it\'s perfect!*

The primary failure of all used Power Wheels is a dead battery. The Batmobile was no different; as soon as we put in a new 12V SLA (Sealed Lead Acid), it happily, albeit slowly, drove around. There is nothing magical about "Power Wheels" branded batteries; get the right voltage (usually 12V, sometimes 6V), and you can use almost any battery you'd like.

The original batmobile chassis blow molded plastic at its finest. The wheels are hollow, the motor is designed to move a child slowly (and reasonably safely), and the steering is littered with bits of metal but mostly loose and wobbly. While the stock chassis was capable of moving adults weighing in at around 200lbs, we knew it wouldn't handle racing, so we decided to find a metal chassis to sit underneath.

[![Razor Drifter in box](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Razor_Drifter.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Razor_Drifter.jpg)

*Note the size of the motor and battery. Those are about to get **much** larger.*

Razor is known for their kick scooters, but they're in the electric go-kart market as well. We found a [Razor Drifter](https://www.razor.com/products/ride-ons/ground-force-drifter/) Open Box for \$165. The Drifter had the steering, brakes, wheels and chassis sorted out for us! Additionally, the Drifter came with a stock 24V battery, 250W motor and 250W motor controller.

Many [PRS and AVC competitors](https://www.flickr.com/photos/sparkfun/sets/72157674124240695) are talented enough to weld their own chassis together. DIY welding is a great way to save money, but it may take weeks of fabrication. Because we planned to enter the autonomous field, we decided to find a ready-made chassis and spend our time building and debugging the autonomous bits.

## Putting on a Hat

Once we had the Power Wheels and the Razor chassis, we had to combine the two.

We slid the razor chassis underneath the plastic batmobile shell. The razor chassis has strength where we needed it most: steering, chassis, brakes, drive train, everything. The plastic batmobile is just there as a shell. The four solid plastic+rubber razor wheels make contact with the ground. The four hollow batmobile wheels hover above the ground and are there only for cosmetic looks (for the lulz).

[![A Power Wheels meets a Drifter](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/PowerWheels_and_Chassis.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/PowerWheels_and_Chassis.jpg)

*A Power Wheels meets a Drifter*

At some point you have to get out the reciprocating saw and severely modify your beautiful Power Wheels. We laid the Batmobile over the Razor and proceeded to chop off all the bits that got in the way.

[![Bare metal chassis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Chassis.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Chassis.jpg)

*Bare metal chassis before shell is laid on top*

[![Combined Batmobile](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Power_Wheel_on_Chassis.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Power_Wheel_on_Chassis.jpg)

*Seats? Where we\'re going, we don\'t need seats!*

Pleasingly, the Batmobile sits on top of the chassis under its own structural support. We didn't need to add all-thread or other standoffs. Even though they don't do anything, we reattached the original wheels just so it looked extra wacky.

## Motor and Motor Control

[![New larger motor on chassis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Motor_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Motor_1.jpg)

*Moar!*

In 2016, A+PRS allowed 48V systems, so the first thing we did was remove the 24V motor and install a 1,000W 48V/21A motor. The PRS rules limit any system to 1,400W, so we could have gone larger had budget constraints not been kicking in fast. New mounting holes were drilled into the chassis, and a different gear had to be mounted to the end of the motor. But it all went well. The stock chassis even included a chain tensioner that proved invaluable!

The MY1020 48V motor we used is common on the PRS circuit and performed great. However, our original 1,000W motor controller (you should already be able to tell what's coming) did not do so well. Our first tests of the 48V system in an open parking lot worked great until the motor controller overheated and failed. And when MOSFET-based motor controllers fail, they fail unsafe, meaning our vehicle decided to go to 100 percent throttle and stay there. This is [why we have safety switches](https://learn.sparkfun.com/tutorials/how-to-build-a-remote-kill-switch)! Alicia and I were able to kill the vehicle before anyone got hurt.

This failure should have been prevented: a motor controller should be rated for at least 2 times what you calculate your maximum load will be. In our case, if we wanted to control a 1kW motor, we should have been using a motor controller rated to a constant 2kW load. Luckily, the A+PRS rules don't require you to record how much money you spent (and burned up); you have to report only what is on the vehicle as it rolls on race day.

[![Larger 5kW motor controller](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Motor_Controller.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Motor_Controller.JPG)

*The new, larger 5kW motor controller*

We quickly located a larger, 5kW motor controller (this one even had reverse!) and got it on order. This larger motor controller has been working swimmingly ever since. Find a motor controller with reverse. You'll be tempted to drive your souped-up Power Wheels in weird places (like the SparkFun inventory aisles), and a reverse gear allows for hilarious 5-point turns.

## Brakes

[![Small Drum Brake](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Drum_Brake.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Drum_Brake.jpg)

*Go-kart drum brakes on eBay*

The Razor chassis had the classic drum brake, perhaps the weakest link of the Razor. While the stock brake was probably the appropriate size for a 75lb child with stock 24V batteries, our brakes got *really* squishy once we added an additional 125lbs of meat bag, batteries and plastic bits. We rarely, if ever, used the brakes during races, but the [PRS rules](http://www.powerracingseries.org/) stipulate that your qualifying lap must end with the driver crossing the finish line and braking to a stop:

> At the end of the hot lap, your car will have to come to a complete stop within 18ft of when its transponder crossed the start/finish line. Deliberately skidding, swerving or spinning out is not an acceptable method of braking for the brake test.

Alicia had to do an impressive combination of hard braking, swerving, skidding and sliding with such a dramatic flair that she wooed the judges into not noticing how dodgy our brakes were. We'll have disc brakes installed before we roll in the 2017 race.

## Batteries

[![Batteries installed on chassis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Battery_On_Chassis.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Battery_On_Chassis.jpg)

*Battery holder welded onto the front of the chassis*

As part of the motor upgrade, we needed to increase the battery voltage to 48V. To save money, we reused the super common batteries that came with the 24V Razor chassis. Razor was smart; they looked at the SLA (Sealed Lead Acid) battery industry and picked the most common size. This just happened to be the same battery that goes into nearly every [UPS](https://en.wikipedia.org/wiki/Uninterruptible_power_supply) on the planet. We purchased two additional UPS-size batteries (way cheaper than buying Razor-brand batteries) and wired them in series.

[![4 batteries combined into one unit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Battery_Unit.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Battery_Unit.jpg)

*Four batteries combined in series*

Taping the cells together and adding a bead of hot glue between the cells made the pack nicely rigid. A low-cost, polarized, high-current connector finished off the pack. We had an old strap lying around that made all the difference in the world; it's a lot more comfortable carrying the pack one-handed by its handle than with two hands underneath.

[![Polarized high current connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Battery_Connector.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Battery_Connector.jpg)

Avoid fires and other bad things. Use polarized connectors for your batteries.

## Wire

[![Soldering large gauge wire](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Soldering_Wire.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Soldering_Wire.jpg)

*Soldering large-gauge wire*

We originally spec'd out some really nice, super flexible silicone-sheathed 8AWG wire for power distribution. I don't think we would do this again; 10AWG would have been fine, and probably even 12AWG. As 8-gauge is far less common, the wire and connectors are more expensive, and the larger gauge wire takes a lot more soldering heat \-- it's just a pain to work with. If you need the current capacity, go for it, but for our extremely zippy, 48V 20A vehicle, 8-gauge wire was overkill.

If you decide to use super flexible, large gauge wire, spend some time on the internet reading about how to solder this type of wire.

The best technique I found:

- Make sure you've got heat shrink in place
- Turn your soldering iron up to 425C (way hotter than the 325C usually needed)
- Push the ends of wire together
- Wrap tightly with 30AWG wire wrap wire
- Liberally apply flux
- Heat and insert lots of solder until the joint turns silver

Here's a good video demonstrating this technique:

## Kill Switch

We documented [how to build a wireless kill switch](https://learn.sparkfun.com/tutorials/how-to-build-a-remote-kill-switch) while making margaritas. It was a ton of fun, so we\'ll skip the bits of the wireless kill switch system here.

[![Smiling girl in power wheels](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Smiles.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Smiles.JPG)

*Zroooommmm!*

In addition to the wireless disconnect, we had a large, red mushroom kill switch that disconnected the battery with a pleasing and authoritative \"thunk.\" Pulling up on the mushroom button reconnects the battery to the system.

[![Mushroom kill switch on vehicle](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Kill_Switch.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Kill_Switch.JPG)

*Batman logo or Bitman logo?*

As a pleasant bonus feature, the mushroom kill switch got rid of the nasty sparks. When connecting the battery to the motor controller, there was such an inrush of current into the capacitors and electronics that the connector would spark. Once we got the kill switch installed, we could connect/disconnect batteries without these sparks.

[![Large gauge power connector](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Power_Connector.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Power_Connector.JPG)

*Connector between kill switch and power bus*

The top of the Batmobile was easily removed, but because it had the kill switch installed we needed a way to disconnect it easily from the power bus. We found a great high-power connector in a dead server UPS. These are often called \"winch connectors\", because they are higher current. With this connector, we are able to quickly disconnect the kill switch and remove the top when we need to get at the inside of the vehicle.

## Control Electronics

[![Main controller board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Locomotion_Control-2.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Locomotion_Control-2.JPG)

*Power converters, motor kill relays, steering relays, locomotion controller and wireless communication*

The control electronics are complex. We had a total of seven microcontrollers on this beast, plus three used in the distance sensors for a total of 216 bits of processing power. The system operated on an I^2^C bus with the brain sending commands to the locomotion controller and LCD and receiving data from the sensors.

[![Wiring inside the Batmobile](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/AVC-Wiring.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/AVC-Wiring.JPG)

*The wiring underneath the Batmobile cover*

For a previous [2010 AVC entry](https://www.flickr.com/photos/sparkfun/4535755865/in/album-72157623889963470/), I did **everything** on a single microcontroller. This made coding and debugging a challenge. On our 2016 entry, we focused each sub-system to do *one thing* very well.

The subsystems are broken down as follows:

- Brain Controller: A [SAMD21 Mini](https://www.sparkfun.com/products/13664) was used to communicate with and process all the data from the distance sensors, GPS and compass, and to send out commands to control throttle and steering. It monitored a start switch and relayed debug information to an LCD.
- Locomotion Controller: An [Arduino Pro Mini](https://www.sparkfun.com/products/11113) read the throttle, steering position, brake switch and autonomous rocket switch. It controlled motor speed and the linear actuator for steering.
- Wireless Kill Switch: An Arduino Pro Mini lived in the wireless kill switch, a requirement for the autonomous part of our Batmobile. To learn more about the wireless controller, check out our tutorial on [how to build a wireless kill switch](https://learn.sparkfun.com/tutorials/how-to-build-a-remote-kill-switch).
- A dedicated Arduino Pro Mini controlled the relays for the wireless kill switch system.
- Debug LCD: We counted our [LCD screen](https://www.sparkfun.com/products/9568?_ga=1.105004803.1411252641.1461206980) as a microcontroller since it has an Arduino in it.
- Sensor Combinator: A SAMD21 Mini polled the serial GPS and I^2^C compass.
- Laser Controller: A SAMD21 Mini controlled the three serial-based laser distance sensors, combined the relevant information and responded to requests from the Brain.
- Three STM32s were the brains within the laser distance sensors.

## Interested in learning more about distance sensing? 

Learn all about the different technologies distance sensors use and which products would work best for you next project.

[Take me there!](https://www.sparkfun.com/distance_sensing)

![](https://cdn.sparkfun.com/assets/custom_pages/3/4/2/distance-sensing-image.jpg)

------------------------------------------------------------------------

## Control Electronics - Brain

[![Controller and reverse knob](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Reverse_and_Main_Controller.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Reverse_and_Main_Controller.JPG)

The Brain is a [SAMD21 Mini](https://www.sparkfun.com/products/13664). It sends commands over the I^2^C bus to the locomotion controller and debug LCD.

**4-pin JST connector at the top of the image:** We used a 4-wire bus (5V, GND, SDA, SCL) for communication and had various taps throughout the bus to allow devices to be attached. This worked *really* well and allowed for devices to be moved around when needed.

**4-pin JST connector to the left:** This was four wires to the button. To tell the vehicle to begin navigating under autonomous control, we used a [metal momentary push button](https://www.sparkfun.com/products/11970) that illuminates when everything is online and happy. The human presses the button twice, and the car commences racing.

**Big gray handle:** This was the original forward and reverse knob that we reused to control the direction switch on the motor controller (two pins when shorted together caused one direction, when open caused the other direction).

The massive and poorly written control code for the Brain can be found [here](https://github.com/nseidle/APRS/tree/master/TheBrain).

**EEPROM for Waypoints**

The SAMD21 does not have internal EEPROM. Because we needed to store GPS waypoints and other configuration data to non-volatile memory, we used an external [I^2^C EEPROM](https://www.sparkfun.com/products/525). Yes, you can use something called emulated EEPROM on the SAMD21, but, every time you reprogram the board, you will overwrite anything previously stored in emulated EEPROM. The external EEPROM made it much easier to store and recall waypoints and settings without having to mash together in the main control code.

## Control Electronics - Locomotion

[![Locomotion Controller PCB](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Locomotion_Control.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Locomotion_Control.jpg)

*Locomotion Controller hooked up*

Note the polarized connectors and prodigious labeling! You DO NOT want to be guessing what gets plugged into where at 11 p.m. before race day. The Locomotion Controller code is available [here](https://github.com/nseidle/APRS/tree/master/LocomotionControl), and the PCB layout [here](https://github.com/nseidle/APRS/tree/master/LocomotionPCB).

Because we eventually wanted this beast to be autonomous, we needed to put a controller in the middle between the throttle and the motor controller. We used an [Arduino Pro Mini](https://www.sparkfun.com/products/11113) that did a huge variety of sensing and control:

- Read the throttle
- Output analog voltage to the motor controller
- Read the brake switch
- Read the steering position
- Controlled the linear steering actuator
- Read the human/robot control switch
- Received and responded to control commands over I^2^C

[![Panic button and third switch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/The_Third_Switch.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/The_Third_Switch.jpg)

*Don\'t panic*

The controller would monitor the rocket switch and brake switch. If a human ever pressed the brakes or turned off the rocket switch, the controller would go into safety shutdown and ignore any commands from the brain.

[![12V linear actuator on desk](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Steering_Actuator-2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Steering_Actuator-2.jpg)

Steering was controlled using a 12V linear actuator over-voltaged to 24V for extra speed. Two relays controlled the forward/backward motion.

[![Trimpot on rack and pinion steering](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Steering_Position_Sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Steering_Position_Sensor.jpg)

Steering position was obtained by cutting a hex wrench to about 1" and inserting that wrench into the bolt that rotates with the wheel. The wrench was then connected to a 10k trimpot using adhesive-lined heat shrink \-- this trick is known as the \"poor man's coupler:\" a 3-wire ribbon connected the trimpot back to the locomotion controller. It worked well, but we had to keep the analog signal wire away from the power bus; otherwise, bad noise got into the ADC readings.

[![Actuator on chassis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Steering_Actuator.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Steering_Actuator.JPG)

*Chassis with the Batmobile raised to see the steering actuator*

For future vehicles, we\'re going to change this setup. It worked well enough, but once the bolt connected the actuator to the steering, you couldn't drive the car; only the computer could. So rather than driving the car to the start line, we had to carry this 75lb beast. So painful. In the future, we plan to find a back-drivable actuator or maybe drive-by-wire.

## Control Electronics - Displays

[![Throttle and displays](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Throttle.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Throttle.JPG)

*Throttle and displays*

We cut notches in a 1" tube of PVC and mounted two displays in the Batmobile. The center display is the power meter. Nearly every A+PRS and PRS competitor used these super [low-cost power meters](https://www.amazon.com/gp/product/B013PKYILS/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1) to show the battery voltage. We had some issues with it, but it worked well enough. In the end, we noticed the drop in vehicle speed (indicating battery drain) long before we noticed the display was indicating a lower pack voltage. But, it did help us make decisions about when to pit (never!) because the nominal 48V pack voltage was dropping down to 42V where we could begin to damage the SLA.

The display on the right is the 20x4 character debug LCD. It's basically a souped-up version of our [20x4 SerLCD](https://www.sparkfun.com/products/9568) display (it's a prototype product, coming soon to a theater near you!).

## Control Electronics - Sensors

[![GPS and compass connected to SAMD21](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Sensor_Combinator.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Sensor_Combinator.jpg)

*GPS+Compass connected to SAMD21*

The Sensor Combinator is a SAMD21 Mini that monitors a GPS receiver and an I^2^C compass. We decided to use a SAMD21 because it can be configured to have multiple hardware serial and I^2^C ports. This is needed if you want to isolate I^2^C devices from the main bus. We wanted the Brain to ask for the heading and get the heading; the Sensor Combinator took care of the low-level I^2^C function of the compass and heading calculations. Similarly, the Combinator listened to the serial stream from the u-blox based GPS module and parsed out all the needed Latitude/Longitude/SIV information.

The code for the Sensor Combinator can be found [here](https://github.com/nseidle/APRS/tree/master/SensorCollator).

## Control Electronics - Lasers

[![Batmobile with top off](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Top_Off.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Top_Off.JPG)

*Laser tape measures seen on the front of the car, wrapped in foil*

We hacked three laser tape measures in order to get distance to any objection front, left or right of the car. Laser tape measures are getting cheaper, and while the read rate (3Hz at the best of times) is not great for LIDAR, it\'s fast enough for basic, low-cost autonomy.

[![Lasers wired to controller](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Lasers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Lasers.jpg)

*Laser Controller at front of car*

Unfortunately, the laser tape measures threw off enough RF to interfere with our GPS module, so we wrapped the lasers in foil. These sensors deserve their own tutorial, which will be written soon.

[![PCB with connectors](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/8/9/Laser_Control.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/5/8/9/Laser_Control.JPG)

*Laser Controller with labels*

Again we chose the [SAMD21 Mini](https://www.sparkfun.com/products/13664) to help us control and combine the serial information coming from the three sensors. The Laser Controller would send the pertinent control strings to the tape measures and monitor the responses, combining them into distances for left/right/center. The Brain would request these values from the Laser Controller over I^2^C.

Note the prodigious amounts of labels and polarized connectors ([JSTs](https://www.sparkfun.com/products/9916) work great!). This system required lots of debugging but worked well because we were able to quickly disconnect and reconnect various aspects of the system.

The code for the Laser Controller can be found [here](https://github.com/nseidle/APRS/tree/master/LaserControl).

## Problems

As with any project, we had a large number of problems and hurdles to overcome along the way. Here are a few that really hurt.

\*\* EMI and GPS \*\*

The Laser tape measures caused significant interference with GPS reception. We eventually moved the GPS module to the rear of the car, which improved positional accuracy. However, the motor caused interference with the compass.

\*\* DC Motor EMF \*\*

DC motors produce a ton of electromagnetic noise. We originally had the 48V battery powering the entire car. However, when the motor would kick on, it would cause enough ripple to make the Brain glitch and reset. We tried powering the I^2^C bus separately, but, because the Locomotion Controller needed to be attached to the motor controller, a GND connection had to be shared. The noise eventually found its way over the I^2^C bus. In the future we will optically isolate the I^2^C bus.

\*\* Lack of EEPROM \*\*

Because the SAMD21 doesn't have internal EEPROM, we were unable to store GPS waypoints on the board. We fixed this by using an I^2^C-based EEPROM.

\*\* Switching Steering Between Driver/Driverless \*\*

It was difficult to attach and detach the linear actuator from the rack and pinion steering. Once the actuator was attached to the steering, a driver could not actively steer (for example, to the starting line). This could be fixed with a different actuator that could be back-driven, or we could go full monty and detach the steering column from the steering and have it control a trimpot that, in turn, controls the linear actuator (drive by wire).