# Source: https://learn.sparkfun.com/tutorials/photon-remote-water-level-sensor

## Introduction 

With the advent of cheap Microcontrollers (MCUs), and especially WiFi-MCUs of late, custom DIY automation of many monotonous tasks and [telemetry](https://en.wikipedia.org/wiki/Telemetry) (remote data collection) is now easily possible.

In this tutorial, we are going to automate a pump for a well based on a remote measurements of a water tank and send weather warnings based on atmospheric pressure readings, as well as collect a bunch of other data. This same type of system could easily be adapted for automated farm/garden watering or other things that need to be turned on and off when some condition is met (like lights in a warehouse/greenhouse at certain times), measured via remote telemetry.

### The Problem

My friend, Andre, owns a [CSA](https://en.wikipedia.org/wiki/Community-supported_agriculture) farm in Boulder, CO called [Jacob Springs Farm](https://www.facebook.com/JacobSpringsFarm). They make some tasty meat, milk, and eggs, so, if you\'re local, check them out.

[![jsf sign and water tank](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/1-jsf_sign_and_water_tank.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/1-jsf_sign_and_water_tank.jpg)

*The farm sign on 75th and Arapahoe in Boulder, CO and the water tank behind it. You can see the water level is nearly empty, as is typical without any automation/telemetry system in place.*

They aren\'t legally allowed to run a city water line to the property, so they use a well and their own storage tanks. The pump for the well is manually turned on or off using a twist timer (which is actually only rated for 50% of the pump\'s current load), and typically they have no idea how much water is in the tanks (unless they\'re empty). I\'ve heard hilariously tragic stories of people being in the shower and having the water run out during winter. They have to run out to the barn, all soaped up and in their towel, turn on the water, and wait for the water heater to fill up and heat so they can finish their shower. Other times the water runs out while preparing dinner or doing dishes, and the low water pressure makes for slow going.

[![jsf existing setup and barn](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/2-existing_setup_and_barn.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/2-existing_setup_and_barn.jpg)

*The barn with the pump control, and the existing pump control timer.*

The water tanks are on one corner of the property (the highest elevation), far from any power outlets, and the pump for the well is at the other end. In order to manage the water system for the farm, I\'ve developed this system that measures the water height with an ultrasonic sensor and controls the pump from that data. While I was at it, I added some extra environmental sensors.

### Required Materials

This project is two-fold: remote telemetry (measurements) coupled with automated weather warnings, and remote control/automation of a hefty (2 hp) pump. To follow along with this tutorial, you\'ll need the following products and tools:

#### Pump Remote Control Box

For the automation of the pump, you will need:

- 1 contactor to turn on/off the pump, rated for the pump load (3hp, 2200W in this case, but [choose the contactor](https://www.usbreaker.com/miva/merchant.mvc?Screen=SRCH&Store_Code=UBI&Search=%22Chint%20NC1(Contactor)%20Family%22) with an appropriate horsepower rating for your application), or a relay if the load is light enough
- 10A [relay](https://www.sparkfun.com/products/13815) to control the contactor
- [Particle Photon WiFi MCU](https://www.sparkfun.com/products/13774) to control the relay
- [Photon ProtoShield](https://www.sparkfun.com/products/13598?_ga=1.96621276.273388466.1418147030)
- female headers
- male-male jumper wires
- 5 V power supply for the photon
- box to hold the photon and relay
- [PIR sensor](https://www.sparkfun.com/products/13285?_ga=1.59381230.273388466.1418147030) to check if someone is near the control box/contactor
- 10 k resistor for the PIR
- a few mounting screws (5), I used [#8 1-1/4\" drywall screws](http://www.homedepot.com/p/Grip-Rite-8-x-1-1-4-in-Philips-Bugle-Head-Coarse-Thread-Sharp-Point-Drywall-Screws-5-lb-Pack-114CDWS5/100120906), a [DIN rail](https://en.wikipedia.org/wiki/DIN_rail) is more professional
- appropriate wiring for your loads (check [here](http://www.powerstream.com/Wire_Size.htm) for max amperage for different wire gauges) \-- I used about 2 ft of 18 AWG for control of the contactor, and about 5ft of 10 AWG for wiring leading to the pump

[![control box supplies](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/3-pump_control_supplies.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/3-pump_control_supplies.jpg)

*Some of the supplies used for the pump control box. Not shown here: 10 k resistor, jumper wires, headers, screws, relay, contactor.*

#### Remote Telemetry Box (water height, etc)

The other half of the project is remote data collection. For this, you will need:

- [Particle Photon WiFi MCU](https://www.sparkfun.com/products/13774)
- [SMA to u.FL cable](https://www.sparkfun.com/products/9145) (may not be necessary if you can get wifi reception without the antenna)
- [Duck Antenna](https://www.sparkfun.com/products/558?_ga=1.63593068.273388466.1418147030) (may not be necessary if you can get wifi reception without the antenna), you can also use a [cantenna](http://www.turnpoint.net/wireless/cantennahowto.html) or [yagi antenna](https://www.google.com/search?q=yagi+antenna&oq=yagi+antenna&aqs=chrome..69i57j0j69i65l2j0l2.1308j1j7&sourceid=chrome&ie=UTF-8#safe=off&tbm=shop&q=wifi+yagi+antenna) for longer-range reception
- [Photon Battery Shield](https://www.sparkfun.com/products/13626?_ga=1.63593068.273388466.1418147030)
- LiPo battery (I used [2000 mAh](https://www.sparkfun.com/products/8483), but you can go [higher or lower capacity](https://www.sparkfun.com/categories/54) depending on budget and how often you want to take measurements)
- solar cell (I used [3.5 W](https://www.sparkfun.com/products/13782) but that\'s overkill, just to be safe \-- if trying to save money, you could use the [2 W](https://www.sparkfun.com/products/13781))
- CdS photocell
- 1 k resistor for use with the photocell
- [BME280 pressure/humidity/temperature sensor](https://www.sparkfun.com/products/13676)
- [MaxSonar EZ3 ultrasonic range finder](https://www.sparkfun.com/products/8501) (measures water height), although I recommend the [waterproof HRXL for robustness](https://www.sparkfun.com/products/11724)
- box to hold it all
- hookup wire (22 AWG)
- a few mounting screws (2), I used [#8 1-1/4\" drywall screws](http://www.homedepot.com/p/Grip-Rite-8-x-1-1-4-in-Philips-Bugle-Head-Coarse-Thread-Sharp-Point-Drywall-Screws-5-lb-Pack-114CDWS5/100120906)
- some twine or wire to hold the solar panel down

[![telemetry supplies](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/4-telemetry_supplies.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/4-telemetry_supplies.jpg)

*Most all of the supplies used for the telemetry box.*

Here\'s a wish list containing all the SparkFun parts used in this project:

#### Tools

- Drill
- drill bits: 3/4\", 5/8\", 1/2\", 1/8\"
- soldering iron, solder, optional: third hand, copper sponge (for cleaning soldering iron tip)
- wire strippers
- hot glue gun and hot glue
- heat gun for shrink wrap (can use hair dryer in a pinch)
- screw driver
- two pairs needle-nosed pliers
- exacto knife
- tape measure
- sledge hammer for driving a grounding rod into the ground

[![tools](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/5-tools.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/5-tools.jpg)

*Here\'s most of the tools I used (not pictured: copper sponge).*

[![more tools](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/6-tools2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/6-tools2.jpg)

*Here\'s some other tools I used, and the tools used to cut the headers to size (right).*

#### Other Supplies

- Gore-Tex® repair patch kit (I sourced locally at REI, but also available [here](https://www.rei.com/product/676442/mcnett-gore-tex-fabric-repair-kit-ii-taslan))
- acetone or other solvent to remove adhesive from Gore-Tex® patch (may not need this for the [Simms patches](http://www.fishusa.com/product/Simms-Gore-Tex-Repair-Kit?utm_source=google_ps&utm_medium=cpc&utm_campaign=google_ps&gclid=Cj0KEQjwlLm3BRDjnML3h9ic_vkBEiQABa5oeZbs1iEln0T5E_PB8BetjfdzQJw6q6JOEMaM2PHGMjwaApaq8P8HAQ))
- 2 [PG-7 cable glands](http://www.amazon.com/Black-Plastic-Waterproof-Connectors-Glands/dp/B00841YHHY/ref=sr_1_1?s=industrial&ie=UTF8&qid=1458541426&sr=1-1&keywords=pg7+cable+glands&refinements=p_85%3A2470955011)
- [silicone](http://www.homedepot.com/p/GE-Silicone-II-2-8-oz-Clear-Kitchen-and-Bath-Caulk-GE284-3TG/100004845)
- small glass piece, I got mine from [Hobby Lobby](http://www.hobbylobby.com/Beads-Jewelry/Jewelry-Findings/Bezels/Nickel-Round-Pendant-Frames-with-Glass/p/13249)
- AC cord with bare leads for testing contactor
- aluminum foil (for shielding the ultrasonic sensor from static from the plastic water tank)
- grounding rod for grounding the aluminum foil housing (I used 1/2\" 10\' EMT conduit)

[![other supplies](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/7-other_supplies.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/7-other_supplies.jpg)

*Other supplies that were used.*

### Suggested Reading

Before embarking upon this tutorial, you may find the following links useful:

[](https://learn.sparkfun.com/tutorials/photon-development-guide)

### Photon Development Guide 

August 20, 2015

A guide to the online and offline Particle IDE\'s to help aid you in your Photon development.

[](https://learn.sparkfun.com/tutorials/photon-battery-shield-hookup-guide)

### Photon Battery Shield Hookup Guide 

July 2, 2015

The Photon Battery Shield has everything your Photon needs to run off, charge, and monitor a LiPo battery. Read through this hookup guide to get started using it.

## Prepping the Photons 

The first thing is to get your Photons prepped and ready to accept firmware over WiFi.

If you have never used the Particle Photon before, you will need to visit the Particle website to learn how to setup a Photon for first time use. You will need to connect it to your local network, pair the device with your free Particle cloud account, and possibly update firmware before you will be ready to upload your first program. All of that information can be found at the following link:

[Getting Started with the Photon](https://docs.particle.io/guide/getting-started/start/photon/)

Once your Photon setup, you will also need to install the Particle Command Line Interface (CLI) on your computer. This will allow us to watch the serial output from the Photon in our terminal/command console.

[Install the Particle CLI](https://docs.particle.io/guide/getting-started/connect/photon/)

## Build the Pump Controller

The contactor/relay idea is used here to control a pump for a well, but could also be used to control a solenoid for a sprinkler/watering system (you\'d probably only need a relay in that case), or to switch on lights, motors, or pumps in a structure (greenhouse, warehouse, etc), heavy-duty heaters, or other remote control needs you might have.

### Triacs, Contactors, and Relays \-- Oh My

To begin, let\'s discuss the various ways to control AC power.

To switch lighter, resistive AC loads (like a small electric heater), a [**relay**](https://www.sparkfun.com/products/13815) can be used. However, once you need to switch a pump on or off, or another inductive load, a different kind of switch is usually needed. Why? It\'s because when inductive loads start up, they exert a huge load\--but only temporarily. See this [stackexchange question](http://electronics.stackexchange.com/questions/196976/relay-ratings-at-120v-and-240v-can-i-use-a-20a-240v-relay-with-a-13a-120v-pump). Using an undersized relay with an inductive load like a pump can be a dangerous proposition; the heat from the start up of an [inductive load](http://www.wisegeek.org/what-is-an-inductive-load.htm) could eventually fuse the relay contacts together, leaving your pump constantly on and you not even knowing it.

[![inrush current from various sources](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/8-inrush_currents.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/8-inrush_currents.jpg)

*Inrush currents from various electrical things. [Source: here.](http://www.hongfa.com/pdf/EXPLANATION%20TO%20TERMINOLOGY%20AND%20GUIDELINES%5CExplanation%20to%20terminology%20and%20guidelines_General%20relay_en.pdf)*

*Here is a video of the contactor I installed in operation and the kWh meter. You can clearly see that when the pump turns on, there\'s a huge inrush of current. After that, the current subsides.*

A [**triac**](https://en.wikipedia.org/wiki/TRIAC) is another way to control AC with silent operation, though I won\'t go into any details as this project didn\'t use any.

For a beefy motor, like a well pump or other industrial sized applications (like turning on the lights in an entire warehouse, etc), you want to use a [**contactor**](https://en.wikipedia.org/wiki/Contactor). These are rated by \[UL\](https://en.wikipedia.org/wiki/UL\_(safety_organization)) for certain motor loads, like 1 hp (\~750 W), 2 hp (\~1500 W), etc. In our case, we have a motor that I measured at 1500 W \-- about 2 hp. Oversizing electrical components is usually the safest bet, so I picked a 3 hp contactor from [US Breaker Inc.](http://www.usbreaker.com/miva/merchant.mvc?), which had some of the best prices I could find. The [datasheet](http://www.usbreaker.com/Telemecanique_Contactor/LC1D4011_Telemecanique_LC1-D40-11_Contactor_Replacement.pdf) tells us it can handle 3 hp at 120 V. The coil, which controls the contactor, takes about 2 A at startup and about 0.2 A thereafter, so a 10 A relay is more than enough to handle this, plus we can then easily control this from a MCU. The coil runs off of straight-up 120 V, so we don\'t need another power supply to control the contactor, just a relay that can switch up to 2 A at 120 V.

[![the beefy 3 hp contactor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/9-beefcake.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/9-beefcake.jpg)

*The beefy 3 hp contactor I used. This thing is hefty, and should be reliable long-term.*

The breaker is rated for 800,000 cycles, which should last about 91 years if the breaker is switched every hour (and it will probably be switched much less often). US Breaker has \[other contactors that can handle up to 7.5 hp inductive loads (5600 W) at 120 V\](https://www.usbreaker.com/miva/merchant.mvc?Screen=SRCH&Store_Code=UBI&Search=%22Chint%20NC1(Contactor)%20Family%22) in case you need more beef.

### Electrical Setup

If you\'re new to soldering check out [this tutorial](https://learn.sparkfun.com/tutorials/how-to-solder---through-hole-soldering) and practice on some scrap parts before trying the real thing. Solder the relay together, if you\'re using the [SparkFun Kit](https://www.sparkfun.com/products/13815). You can find assembly instructions for the relay kit in this [hookup guide](https://learn.sparkfun.com/tutorials/beefcake-relay-control-hookup-guide).

Cut 2 sets of female headers to the correct size (20 units) by first scoring with an exacto knife (I do it on all sides of the headers), then use two pairs of needle-nosed pliers to make a clean break. Score each side a few times to get a deep cut. It will probably take you a few tries to get the hang of it, so don\'t get discouraged when the first few don\'t work out.

[![cutting headers](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/10-cutting_headers.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/10-cutting_headers.jpg)

*Break headers to the correct size by first scoring with an exacto knife around the perimeter, then using two needle-nosed pliers to make a clean break.*

Assemble 3 male-to-male jumpers into a connector for the PIR and relay. There should be a 10kΩ resistor between the 5V (Vin) and dataline for the PIR. The 5V line should be split, one to go to the relay and one to the PIR. Before soldering things together, put some heatshrink on the wires so it is easy to cover up bare wires. After soldering, heat the heatshrink with the heat gun until they tightly grip the wires (don\'t heat for more than 5-8 seconds).

[![jumper setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/11-jumper_setup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/11-jumper_setup.jpg)

*I used my third hand tool to help me hold everything in place while I soldered.*

Solder the headers to the ProtoShield. Solder the PIR data header to the D7 hole, the Vcc header to the Vin hole, and the GND header to one of the GND holes. Solder another jumper to the other GND hole and one more jumper to the D0 hole for the relay.

[![protoboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/12-protoboard.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/12-protoboard.jpg)

*Here\'s a top view of the completed protoboard. Make sure to plug the Photon in the right direction (use the white guidelines on the board).*

Next, test the relay and contactor to make sure everyone\'s riding on the gravy train. Connect the GND, Vin, and D0 jumpers to the GND, 5V, and CTRL of the relay board, respectively. Upload the code below (via [build.particle.io](http://build.particle.io)) to your Photon to test the relay (listen for the clicking every few seconds to make sure it works and watch the LED. You can also test the resistance between the \'load\' and \'normally open\' screw terminals on the relay to make sure it goes between 0 and infinity if you wish.

    language:c
    void setup() 

    void loop() 

Next is the contactor. Hook up some wire from an AC plug to the relay terminal, then from the other relay terminal to the contactor A1 connector, and last the other end of the AC wire to the contactor A2 terminal. Run the relay test again and make sure the contactor is switching. You will definitely notice when the contactor is working, as it clicks on and off with [authoritah](https://www.youtube.com/watch?v=k1vKDM7wfiA). You can again use a multimeter to watch the resistance between some of the \'T\' and \'L\' terminals if you wish; it should drop from 1 to 0 when the relay is on.

[![contactor relay hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/13-testing_contactor_relay_fritzing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/13-testing_contactor_relay_fritzing.jpg)

*Circuit diagram of the contactor and relay.*

[![contactor relay hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/14-contactor_relay.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/14-contactor_relay.jpg)

*My action shot of the contactor and relay.*

Not surprisingly, the beefy contactor is much louder than the relatively cutesy little relay.

Connect the PIR sensor to the Photon: connect the D7 jumper to the signal line (black wire), the Vin to the red wire, and the white wire to GND. There\'s a tutorial [here](http://bildr.org/2011/06/pir_arduino/) explaining more about this sensor, but it\'s pretty simple \-- when motion is detected, the output pin from the sensor pulls low. Power up the Photon, and upload this code:

    language:c
    void setup() 

    void loop() 
    }

Check to make sure the PIR sets off the alarm when you wave your hand in front of it. You can tell if it\'s working because the D7 LED will light up when the alarm is triggered. Additionally, you can type \'particle serial monitor\' in your terminal/command console (with the Photon plugged into your computer via USB) to watch the serial output from the device, which should print \'Motion Detected\' when you wave your hand in front of it.

[![contactor relay hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/15-control_box.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/15-control_box.jpg)

*The full circuit diagram of the pump controller. Caution: the colors on your PIR sensor wires may differ form the one in the diagram.*

### Physical Construction

First, drill a hole in the front of the case for the PIR sensor. The PIR sensor used here has a diameter of about 0.85\", or 21.5 mm, so I used a 3/4\" drill bit and widened the hole with the 1/2\" drill bit. I hot-glued the PIR in there. Add some hot glue on the corners of the board to hold it to the red box. For a more secure job, drill holes, and use 2mm screws and nuts to secure the board to the case.

[![PIR sensor hole](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/16-PIR_hole_size.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/16-PIR_hole_size.jpg)

*The hole for the PIR sensor should measure about 0.85\".*

Next, drill a 1/2\" hole in the side of the case. Drill some 1/8\" holes for mounting the ProtoShield and relay, if you want to secure the board with 6-32 screws or a similar size. For ease and quickness, I just hotglued the boards to the box.

String the 5V power supply cord through the 1/2\" hole we drilled in the side of the enclosure, and plug the micro-USB power cord into the Photon. If you want to be more professional, use a PG-7 cable gland to string the wires through. Attach some wires to the relay, leaving enough length to connect to the AC leads in your field installation (I used 18-gauge wire, since this will only be carrying about 0.2A at steady-state). If you drilled mounting holes for the relay and protoboard earlier, secure the boards using screws. Otherwise, use a hot glue gun to attach the boards to the case. Finally, hot glue the wires through the hole for strain relief and to prevent pull-out of the wires from the relay.

[![completed control box](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/17-complete_control_box.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/17-complete_control_box.jpg)

*Complete setup of the control box and strain relief of the pass-through wires.*

Finally, screw the box together with the six screws on top.

### Field Installation

Use some screws to attach the box to a wall near your pump and AC leads and some screws as mounting for the contactor, if you\'re not going with a [DIN rail](https://en.wikipedia.org/wiki/DIN_rail). I used some extra screws we had laying around, they seem like [#8 1-1/4\" drywall screws](http://www.homedepot.com/p/Grip-Rite-8-x-1-1-4-in-Philips-Bugle-Head-Coarse-Thread-Sharp-Point-Drywall-Screws-5-lb-Pack-114CDWS5/100120906), and I drilled shallow 1/8\" pilot holes before screwing them in.

[![pump control fully installed](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/18-fully_mounted.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/18-fully_mounted.jpg)

*The control box and contactor completely mounted.*

Once the contactor screws are in, hang the contactor on them, and tighten the screws so that the contactor won\'t be rattling around much. Take the contactor back off, attach your wires to the terminals L1, T1, A1, A2, and the GND terminal (you will ideally want a small bolt/nut for this GND connection, seems like 6-32 with ½\" length would work). If you\'re going to be in a dusty area (for example, we\'re in a wood shop) use protection and cover the contactor with plastic, etc. Finally, hook up the wires correctly to the pump and power cord, as shown in the full circuit diagram below.

[![contactor relay hookup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/15-control_box.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/15-control_box.jpg)

*The full circuit diagram of the pump controller.*

Run the relay test program from earlier to verify everything is working.

We\'ll come back to data collection and automation of the pump control after installing the remote sensor.

## Build the Remote Telemetry Box

### Energy Considerations \-- Battery and Solar Cell Sizing

The plan is to periodically wake up the Photon to take a measurement, then put it into deep sleep if the battery level is not very full. The Photon energy use specs are [here](https://docs.particle.io/datasheets/photon-datasheet/#recommended-operating-conditions). The maximum average WiFi operating current is 100mA, and the maximum deep sleep operating current is 0.1mA. Assuming an on time of 60 seconds and an off time of 5 minutes, we use about 400mAh per day. If we want to have the Photon last for three days without any sunlight (sometimes it can blizzard here for a day or two), we need at least 1200mAh of battery capacity. The nearest battery size available from SparkFun, rounding up, is [2000mAh](https://www.sparkfun.com/products/8483). However, you can [play with the sleep cycle time by copying this spreadsheet](https://docs.google.com/spreadsheets/d/1qNA7Z43Yw0bW2yuVs8VUf3akaNJOnrERbDrT77fp0a4/edit?usp=sharing) and get down to a pretty small battery size. Also, by sleeping the Photon longer at night when there\'s less water usage, we can extend the battery life dramatically.

  Pin Label   Pin Description
  ----------- ------------------
  1           Switch contact 1
  2           Switch contact 2
  \+          LED anode
  \-          LED cathode

A Watt = V \* A, so our [3.5W solar cell](https://www.sparkfun.com/products/13782) providing power at 5V is pushing 0.7A. We should be able to charge our 2000mAh battery pretty quickly (about 3h) under ideal conditions. However, the cell will get dusty, days will be cloudy, etc, so it\'s best to oversize when in doubt. If you want to save some bucks, the [2W solar cell](https://www.sparkfun.com/products/13781) should push about 0.4A under ideal conditions.

### Physical Construction

Drill ½\" holes for the cable gland and pressure/humidity hole on the side of the box you expect to get the least rainfall/water exposure, and a ¼\" hole for the antenna on the same side. Drill another ½\" hole in the lid of the box for the photocell window. I accidentally installed the antenna on the top of the box, where rain will hit it directly. If you want to mount the battery shield with 6-32 screws, drill some 1/8\" holes as well on the bottom of the box. Put silicone around the photocell hole on the cover and press the glass on the outside of the hole. Put silicone around the cable gland hole and the antenna hole, and install both of them.

[![holes in telemetry box](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/19-telemetry_box_holes.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/19-telemetry_box_holes.jpg)

*Drill four holes in the telemetry box: one for the antenna, one for the photocell, one for pressure/humidity equilibration, and one feedthrough for the wires. You will want to put the hole for the antenna on the same side as the cable gland and humidity equilibration hole.*

#### Waterproof Holes

We need a hole to let humidity, pressure, and temperature equilibrate with our BME280 sensor, but we don\'t want to let rain water in. The solution I came up with is to use a GoreTex repair patch pad and to use a solvent to get rid of the adhesive on the area that lets humidity through. Most solvents you\'ve got laying around should be fine (acetone, mineral spirits, goof-off, ethanol\--such as Everclear), but check with [this chart](http://peer.tamu.edu/curriculum_modules/Properties/module_3/activity4.htm) before trying any solvents not mentioned here. Take a rag, paper towel or napkin, douse it with some acetone, and rub off the adhesive on the back of the repair patch. This will dissolve the adhesive after a bit of work. When you can touch the spot you\'ve treated and don\'t feel the sticky adhesive, you\'re probably good. I\'m not sure if the adhesive lets moisture and pressure through very well or not, as I haven\'t tested, but, once the adhesive is removed, it works well.

[![acetone_treatment](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/20-acetone_treatment.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/20-acetone_treatment.jpg)

*Use a rag or napkin, etc to remove the adhesive from the center of the Gore-Tex® patch.*

Put a bit of silicone around the hole just to make sure it gets sealed well, and apply the patch.

### Electrical Hookup

#### Battery Shield

Solder the four legs of the SMD barrel jack plug to the board, as described [here](https://learn.sparkfun.com/tutorials/photon-battery-shield-hookup-guide#using-and-charging-a-lipo-battery).

[![the SMD barrel jack soldered onto the battery shield](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/21-SMD_barrel.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/21-SMD_barrel.jpg)

*Solder the four legs of the barrel jack onto the battery shield. [Source: here.](https://learn.sparkfun.com/tutorials/photon-battery-shield-hookup-guide#using-and-charging-a-lipo-battery)*

You can test it with the MAX17043 library. Details on using the battery shield are beyond the scope of this project tutorial, as that information can be found in the [Battery Shield Hookup Guide](https://learn.sparkfun.com/tutorials/photon-battery-shield-hookup-guide#using-the-max17043-lipo-fuel-gauge).

#### BME 280 Pressure, Humidity, Temperature

The BME280 can read pressure, humidity, and temperature, so it makes a nice mini weather station. Changes in air pressure are an easy way to [predict incoming storms](http://science.opposingviews.com/barometric-pressure-rise-fall-rains-23043.html) (unless you\'re in a more tropical climate, like the gulf coast). We can use [some guidelines](http://www.islandnet.com/~see/weather/eyes/barometer3.htm) to classify pressure changes on the hour timescale, and we\'ll post that information to a Twitter account. Basically, if pressure is dropping, the rate of the drop indicates how soon a storm is likely on the way. Dropping air pressure usually also means [rising wind speeds](http://www.bohlken.net/airpressure2.htm); rising pressure usually means good weather.

Here\'s a table of pressure drop over three hours that we\'re going to use to classify our data, [referenced from here](http://www.islandnet.com/~see/weather/eyes/barometer3.htm):

  Classification          min pressure rate (inHg/min \* 10\^6)   max pressure (inHg/min \*10\^6)   lower limit % change over 3 hours
  ----------------------- --------------------------------------- --------------------------------- -----------------------------------
  Steady                  0                                       16                                0
  Changing slowly         16                                      246                               0.01
  Changing moderately     246                                     574                               0.15
  Changing rapidly        574                                     984                               0.35
  Changing very rapidly   984                                                                       0.59

Essentially, if we have a 0.6% change in pressure in three hours, the pressure is changing very rapidly and bad weather may be on the way. We\'ll post to a Twitter account and set up text alerts for when pressure is dropping very rapidly. The spreadsheet for the calculations is [here](https://docs.google.com/spreadsheets/d/1EZp625r88_ZleHsTxqA1DUwct9kukQOlJ92fQBmHfDo/edit?usp=sharing), in case you want copy it and mess with it.

Solder some M-M jumpers to the BME280 board, and solder the other ends to GND, 3.3V, and D0/D1 (SDA/SCL) pins on the battery shield, respectively.

[![the BME280 fritzing diagram](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/22-bme280-fritzing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/22-bme280-fritzing.jpg)

*The circuit diagram for hooking up the BME280 to the Particle Photon. Note the SDA/SCL pins are D0/D1 on the Photon.*

[![the BME280 sensor board soldered to the photon battery shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/23-BME280.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/23-BME280.jpg)

*Male-male jumpers have been soldered betwixt the BME280 and the Photon battery shield (I had accidentally soldered to the A4/A5 pins at this point, which are SDA/SCL on Arduino UNO).*

Start a new Photon project on [www.build.particle.io](http://build.particle.io), [include the library \"SPARKFUNBME280\"](https://docs.particle.io/guide/getting-started/build/photon/#using-libraries) (click the \'Libraries\' icon on the left, search in the box for BME280, click the SPARKFUNBME280 library, click \'Include in App\', click the name of your app, click \'Add to App\') and upload this code to your photon to test the sensor:

    language:c
    /******************************************************************************
    I2C_and_SPI_Multisensor.ino
    BME280 Particle Photon example

    Sensor A is I2C and connected through D0/D1 (SDA/SCL)
    ******************************************************************************/

    #include "SparkFunBME280/SparkFunBME280.h"

    BME280 mySensorA;

    void setup()
    

    void loop()
    

Type \'particle serial monitor\' in your command prompt/terminal, and check to make sure the output is reasonable and working.

#### CdS Photocell

To measure light levels, we\'ll use a CdS photocell. We\'re going to use a 1 k resistor as a pull-down. Information on how to use a photocell can be found [here](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino---v32/experiment-6-reading-a-photoresistor). Solder the connections as so:

[![Photon to CdS circuit schematic, with BME280](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/24-bme280_cds_fritzing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/24-bme280_cds_fritzing.jpg)

*The circuit diagram for hooking up the BME280 and CdS photocell to the Particle Photon. Note the SDA/SCL pins are D0/D1 on the Photon.*

[![all connections soldered to the battery shield; the CdS before shrinkwrapping](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/25-CdS-hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/25-CdS-hookup.jpg)

*The CdS photocell hookup is pretty simple, just 3.3V, GND, and A1.*

It ended up being tough for me to place the CdS cell in the glass window because my wires were too short, so leave yourself some extra room with at least eight inches of wiring between the battery shield and the CdS cell.

Test the reading of the photocell with a flashlight, using this code:

    language:c
    void setup() 

    void loop() 

Check the serial output with \'particle serial monitor\', and make sure the number goes up when you shine a bright light on it. The number should read in the thousands; the range of the Photon analog signal is from 0 to 4095, so make sure the reading isn\'t near 4095 unless you\'re in broad daylight or close to a bright LED. There\'s a nice classification of voltage output levels for different lighting conditions [here](https://learn.adafruit.com/photocells/using-a-photocell).

#### Sensing Distance (Water Height) with an Ultrasonic Sensor

Because air and water have different densities, the water reflects some of the ultrasonic waves sent at it, for example, by something like the [MaxSonar-EZ3 sensor](https://www.sparkfun.com/products/8501) ([manufacturer\'s page here](http://www.maxbotix.com/Ultrasonic_Sensors/MB1030.htm)). Again, I recommend the [waterproof version](https://www.sparkfun.com/products/11724) for reliability.

To add this part to the telemetry box, first measure the distance from where you will put the telemetry box to where the ultrasonic sensor will go, and cut three sufficient lengths of wire. I used 22 AWG hookup wire and ended up with about 8 to 10 ft of wire. Solder the wires to the GND, +5, and PW holes on the device, by soldering the ends of the wires. Pass the wires through the cable gland, and solder the other ends of the wires to the battery shield: GND, 3.3V (or Vin), and A0.

[![Photon to CdS, BME280, and ultrasonic circuit schematic](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/26-bme280_cds_ultrasonic_fritzing.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/26-bme280_cds_ultrasonic_fritzing.jpg)

*The circuit diagram for hooking up the MaxSonic ultrasonic sensor, BME280 and CdS photocell to the Particle Photon battery shield. Note the SDA/SCL pins are D0/D1 on the Photon.*

[![soldered connections to the ultrasonic sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/27-ultrasonic-hookup.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/27-ultrasonic-hookup.jpg)

*The soldered connection between the ultrasonic PW, GND, and 5V (can take 2.5-5V), and the Photon Battery Shield.*

[![cables passed through the cable gland to the battery shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/28-ultrasonic_cables.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/28-ultrasonic_cables.jpg)

*Make sure to pass the wires through the cable gland before soldering to the Battery Shield.*

Test the device by uploading this code to your Photon:

    language:c
    float uSperInch = 147; // from datasheet
    float distance;
    unsigned long duration;

    void setup() 

    void loop() 

The [datasheet from the manufacturer\'s page](http://www.maxbotix.com/documents/MB1030_Datasheet.pdf) says the pulse width is 147uS/inch, and it seemed to be right around there for me. Double check the readings with a measuring tape though.

### Finishing the Telemetry Box

The few last things to do are pass through the solar cell barrel jack, stuff everything in the box (maybe with a little hot glue), and make sure all the external holes look well sealed up.

We have to cut the solar cell wire in two, and, using your wire strippers, strip each wire down. Then pass the wires through the cable gland and solder them back together. I used heat shrink to make the connections clean. The solar cell cable length is very short, so you might want to add some extensions. You could also add enough of an extension so that the box is in the shade (so it doesn\'t get too hot, especially if you\'re in the desert).

[![solar cell cables passed through the cable gland to the battery shield](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/29-solar-passthru.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/29-solar-passthru.jpg)

*Chop the solar cell cable, put it through the cable gland, and re-attach it.*

Finally, connect the battery and the solar cell to the Battery Shield, and put everything in the box as best you can. I hot-glued most things down, but in the sun, things get pretty hot (as we\'ll see from the measurements), so the glue tends to un-stick. I did hot-glue the CdS cell to the glass window, and even after it un-stuck (and I reopened the box), it was still pretty easy to put back in the window due to the shape of the glue. Lastly, tighten the six screws down on the top of the box, tighten the cable gland, and maybe put some silicone on the cable gland to make sure it\'s good and waterproof.

[![all the telemetry pieces in the box](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/30-everything_telemetry.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/30-everything_telemetry.jpg)

*Here\'s everything in the altered box. The extra loops of wire are from the ultrasonic sensor wires.*

### Field Installation

Put the box and solar cell in a place that\'s going to get some sun. String the wires from the box through to the water tank. This is where things get tricky. If you have giant plastic water tanks, like we do, you\'ll likely get static electricity buildup that will interfere with the measurements. As long as the sensor isn\'t touching the tank (I also covered the sensor in aluminum foil and grounded it with a ground rod), it should be ok. If the tank isn\'t plastic, you can drill a 5/8\" hole somewhere in the tank. I covered most of the ultrasonic sensor with black electrical tape as a bit of protection.

If your tank is outside, you will probably be getting condensation at times. The waterproof sensor may fix this problem, otherwise, mount the non-waterproof sensor *above* the tank (with a hole to let the ultrasound pass into the tank) so that condensation won\'t be happening on the sensor.

[![the ultrasonic sensor protected by tape and the hole it goes into](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/31-ultrasonic-and-hole.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/31-ultrasonic-and-hole.jpg)

*I put black electrical tape on the sensor for some protection and shoved it into the 5/8\" hole on top of the water tank.*

The water tanks on the property where this was installed are gigantic plastic (polyethylene, probably) tanks. The pump is about a half mile away, and the whole distance is bridged by PVC pipe. [Possibly due to this, there seems to some static buildup in the system.](http://www.shimadzu.com/an/hplc/support/lib/lctalk/14/14lab.html) As evidence, I\'ve felt a massive static field (6-12 inches above the tank) before while climbing on top of the tanks. This appeared to be effecting the ultrasonic sensor, as it would perform great in lab tests, but out in the field it would get wonky after a few measurements (reading values smaller than the minimum distance), and correct measurements would come and go during the day and night. Things seemed to go haywire after the water started flowing for an hour or two\--in either direction, in or out.

The other strange thing about this whole deal is when I would plug the photon into my computer, the readings would be OK again, and when I unplugged it, they would go back to being very small and incorrect.

[![the effects of static electricity on the ultrasonic measurements](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/32-static_effects.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/32-static_effects.jpg)

*About an hour after the pump was turned on, the ultrasonic measurement went a bit crazy. Then, a few hours later, it settled back down to the accurate reading. The same thing happened the next morning after the water had been flowing out of the tanks for a few hours.*

To combat this, I drove a 10ft 1/2\" EMT conduit rod about nine feet into the ground with a sledge hammer. I took a wire and connected one end to the EMT conduit. On the other end, I tied a stainless steel bolt to it and dropped it in the water tank. I also tied a wire around the ultrasonic sensor\'s plastic housing and connected it to the EMT rod. It seemed to help somewhat, but still didn\'t completely fix the problem.

[![DIY grounding rod](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/33-diy_grounding_rod.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/33-diy_grounding_rod.jpg)

*The DIY grounding rod: before pounding (left) and after (right).*

The only way I was able to get the sensor to reliably read water height was to suspend it above the tank, without the plastic housing touching the water tanks. I wrapped the sensor in aluminum foil (except the front face) and attached the ground wire to the foil. I then drilled some holes in a [1.5\" aluminum flat bar](http://www.homedepot.com/p/Everbilt-1-1-2-in-x-36-in-Aluminum-Flat-Bar-with-1-8-in-Thick-801967/204273995), attached the bar to the water tank, and attached a grounding wire to the bar. After that, the readings were stable.

However, after a few days, the readings started going haywire. I found there was condensation on the sensor that caused this. If your water tank is outside, mount the sensor *above* the tank (using something like the metal plate I used), and put a hole in the tank (larger than the sensor diameter), directly below the sensor.

[![the aluminum bar after drilling holes](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/33.1-bar_and_bolts.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/33.1-bar_and_bolts.jpg)

*I drilled two 5/8\" holes for the two ultrasonic sensors I\'m using, a few holes for bolts to hold it to the water tank, and a hole for a grounding wire.*

[![suspension of the sensor](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/33.2-suspended_bar.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/33.2-suspended_bar.jpg)

*The aluminum bar suspended from the water tank with the sensor in place.*

Some people claim [plastic can\'t be grounded](http://blog.polyprocessing.com/blog/polyethylene-storage-tanks-chemical-incompatibilities), and they may be right. However, adding a [grounding lug](https://www.grainger.com/content/qt-safety-bonding-grounding-255) at the inlet to the tank may work, although I haven\'t tried this.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/33.3_out_of_tank_sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/33.3_out_of_tank_sensor.jpg)

*My installation of the out-of-tank waterproof ultrasonic sensor. The sensor is mounted slightly above the tank, with a hole drilled in the tank. This prevents condensation from interfering with the sensor (only necessary if the tank is outdoors).*

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/33.4_installed_telemetry_box.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/33.4_installed_telemetry_box.jpg)

*Final installation of the telemetry box. I ended up using a yagi antenna (bought from Ebay) to be able to get wifi reception reliably.*

Using the [waterproof HRXL sensor](https://www.sparkfun.com/products/11724) may completely bypass the static electricity problem; I\'m not sure. In any case, it would be a better idea for long-term robustness to use the waterproof sensor.

Finally, you need to know the distance from the bottom of the tank to the front of the sensor, so get out your measuring tape and check that now, and make a note of it. To get the water height, we simply take the total water tank height and subtract the distance read from the ultrasonic sensor.

## The Code

The code for this project lives on GitHub. You can find all the latest by following the link below.

[Photon Remote Water Level Sensor Code](https://github.com/wordsforthewise/solar-powered-particle-photon-telemetry-and-automation)

### Minimum Viable Product

In the startup world, a [minimum viable product](https://en.wikipedia.org/wiki/Minimum_viable_product) (MVP) is something that gets the job done and nothing more. I\'ll give you an example of the MVP for the setup we\'ve built here.

#### Particle Publish and Subscribe

Using the function [Particle.Publish()](https://docs.particle.io/reference/firmware/photon/#particle-publish-), we can quickly toss up a variable online so other Photons or devices can use it. In this example it will be used to send the water height and let our pump control box know the water height sensor is still online, and it can also be used to send commands, like \'turn on the pump\', or \'don\'t deep sleep our telemetry Photon quite yet\'.

The format of a publish is [MQTT-like](https://en.wikipedia.org/wiki/MQTT). A subscription works like a prefix filter. If you subscribe to \"foo\", you will receive any event whose name begins with \"foo\", including \"foo\", \"fool\", \"foobar\", and \"food/indian/sweet-curry-beans\".

I set up my prefix organization and subscribes as so:

    language:c
    Particle.subscribe("jsf/waterSystem/", eventHandler, MY_DEVICES);

If I want the water height sensor to tell the control box that it\'s still online, I would do:

    language:c
    Particle.publish("jsf/waterSystem/waterTankSensor/online", "true");

You can also use the [\'private\' flag with your publishes](https://docs.particle.io/reference/firmware/photon/#particle-publish-), and use the [\'MY_DEVICES\' flag with your subscribes](https://docs.particle.io/reference/firmware/photon/#particle-subscribe-), if you want to improve security.

Depending on your situation, you may be sleeping the telemetry Photon for a long time and only have it on for a few minutes or seconds. In this case, it makes updating the software tough. For that, I created a Python script that senses when the Photon comes online and tells it to wait a bit for a software update. If you want to use it, install Python \-- I like using [Python(x,y) for Windows](http://python-xy.github.io/), and run this script (first install sseclient, requests, and json using \[pip\](https://en.wikipedia.org/wiki/Pip\_(package_manager)) or [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall); type \'easy_install sseclient\' or \'pip install sseclient\' in your command prompt or terminal for sseclient, requests, and json):

    language:python
    from sseclient import SSEClient 
    import requests, re, json

    access_token = "YOUR ACCESS TOKEN HERE"
    publish_prefix_head = "myFarm" # for subscribing to incoming messages, e.g. myFarm
    publish_prefix = "myFarm/waterSystem" # e.g. myFarm/waterSystem
    messages = SSEClient('https://api.spark.io/v1/events/' + publish_prefix_head + '?access_token=' + access_token)
    r = requests.post('https://api.particle.io/v1/devices/events', data = )
    if r.json()['ok']==True:
        print 'successfully sent update request'

    with open('recorded messages.txt', 'w') as record:
        for msg in messages:
            event = str(msg.event).encode('utf-8')
            data = str(msg.data).encode('utf-8')
            if re.search('jsf', event):
                dataJson = json.loads(data)
                if event == publish_prefix + '/waterTankSensor/online' and dataJson['data'] == "true":
                    r = requests.post('https://api.particle.io/v1/devices/events', data = )
                    if r.json()['ok']==True:
                        print 'successfully sent update request'
                if event == publish_prefix + '/waterTankSensor/updateConfirm':
                    if dataJson['data'] == 'waiting for update':
                        print 'device waiting for update...'
                    if dataJson['data'] == 'not waiting for update':
                        print 'device no longer waiting for update.'

Save the code in a file called \'updatefirmware.py\', and, once you type \'python updatefirmware.py\' (from the same directory the file is located in, of course), it will print some messages out. When the device is waiting for an update, it will print \'device waiting for update\...\'. Then you can head to [build.particle.io](http://build.particle.io), and flash your device.

#### Telemetry Box

Create a new Photon app on build.particle.io, and [include the ThingSpeak library](https://docs.particle.io/guide/getting-started/build/photon/#using-libraries) in it (make sure it\'s the \"ThingSpeak\" library, and not the \"thingspeak\" library\--note the capitalization). Right now it shows up as the first result from searching for \'things\'. Also include the SPARKFUNMAX17043 and SPARKFUNBME280 libraries. Here is the full code:

    language:c
    #include "SparkFunBME280/SparkFunBME280.h"
    BME280 mySensorA;
    float tempF;
    float pressure;
    float RH;

    #include "SparkFunMAX17043/SparkFunMAX17043.h"
    // MAX17043 battery manager IC settings
    float batteryVoltage;
    float batterySOC;
    bool batteryAlert;

    #include "ThingSpeak/ThingSpeak.h"
    //################### update these vars ###################
    unsigned long myChannelNumber = your channel number here;  //e.g. 101992
    const char * myWriteAPIKey = "your api key here"; // write key here, e.g. ZQV7CRQ8PLKO5QXF
    //################### update these vars ###################
    TCPClient client;
    unsigned long lastMeasureTime = 0;
    unsigned long measureInterval = 60000; // can send data to thingspeak every 15s, but give the matlab analysis a chance to add data too

    // ultrasonic distance sensor for water height measurement
    float uSperInch = 147; // from datasheet
    float distance;
    unsigned long duration;
    float waterHeight;
    //################### update these vars ###################
    float totalDistance = 64; // the distance from the sensor to the bottom of the water tank
    //################### update these vars ###################

    // photocell
    float lightIntensity;

    // connection settings
    STARTUP(WiFi.selectAntenna(ANT_EXTERNAL)); // use the u.FL antenna, get rid of this if not using an antenna
    float batterySOCmin = 40.0; // minimum battery state of charge needed for short wakeup time
    unsigned long wakeUpTimeoutShort = 300; // wake up every 5 mins when battery SOC > batterySOCmin
    unsigned long wakeUpTimeoutLong = 900; // wake up every 15 mins during long sleep, when battery is lower
    unsigned long connectedTime; // millis() at the time we actually get connected, used to see how long it takes to connect
    unsigned long connectionTime; // difference between connectedTime and startTime

    // for updating software
    bool waitForUpdate = false; // for updating software
    unsigned long updateTimeout = 600000; // 10 min timeout for waiting for software update
    unsigned long communicationTimeout = 300000; // wait 5 mins before sleeping
    unsigned long bootupStartTime;

    // for publish and subscribe events
    //################### update these vars ###################
    String eventPrefix = "your prefix"; // e.g. myFarm/waterSystem
    //################### update these vars ###################

    bool pumpOn;

    void setup() 

    void loop() 
                if ((millis() - bootupStartTime) > updateTimeout) 
        } else  else 
        }
    }

    void eventHandler(String event, String data)
     else 
      } else if (event == eventPrefix + "/waterTankPump/pumpOn") 
      Serial.print(event);
      Serial.print(", data: ");
      Serial.println(data);
    }

    void doTelemetry() 

Variables you should change when you do this:

- eventPrefix (e.g. myFarm/waterSystem; for publish/subscribe events)
- myWriteAPIKey (grab from your ThingSpeak telemetry channel)
- myChannelNumber (from ThingSpeak telemetry channel)
- totalDistance (the distance from the sensor to the bottom of the water tank

I\'ve bracketed these variables with:

    language:c
    //################### update these vars ###################

so you know what you have to change.

Additionally, you can adjust the batterySOCmin and wakeupTimeout variables if you use a different sized battery.

#### Control Box

Again, include the ThingSpeak library. Use this code, changing variables where applicable:

    language:c
    #include "ThingSpeak/ThingSpeak.h"
    // channel we're writing to
    //################### update these vars ###################
    unsigned long myWriteChannelNumber = your channel number; // e.g 101223
    const char * myWriteAPIKey = "your write API key for the pump controller channel";
    //################### update these vars ###################
    TCPClient client;
    unsigned long lastMeasureTime = 0;
    unsigned long measureInterval = 60000; // can send data to thingspeak every 15s, but once a minute is fine

    bool pumpOn = false;
    float waterHeight = 1000; // we want to make sure the relay isn't falsely triggered on from the get-go
    //################### update these vars ###################
    float lowerCutoff = 20; // lowest acceptable water height, in inches
    float higherCutoff = 42; // highest acceptable water height, in inches
    float totalDistance = 64; // the distance from the sensor to the bottom of the water tank
    //################### update these vars ###################
    int success;
    unsigned long relayStartTime;
    unsigned long lastSignal = millis();
    unsigned long pumpTimeout = 900000; // turn off the pump if haven't heard from sensor in 15 mins
    unsigned long pumpOffTime = 3600000; // make sure we don't turn on the pump more than once per hour
    long pumpOffTimeStart = -pumpOffTime; // so we can turn on pump when we startup if we need to

    // PIR motion sensor
    int relayPin = 0;
    int PIRpin = 7;
    int PIRval;

    // for publish and subscribe events
    //################### update these vars ###################
    String eventPrefix = "myFarm/waterSystem"; // e.g. myFarm/waterSystem
    //################### update these vars ###################

    void setup() 

    void loop() 

    int relayControl(String relayState)
    
        else if (relayState == "off") 
        else 
    }

    void autoPumpControl() 
        }
        if (waterHeight < lowerCutoff)  else if (waterHeight > higherCutoff)  else 
    }

    void checkPIR() 
    }

    void recordThingSpeakData() 
    }

    String boolToText(bool thing)
    

    int boolToNum(bool thing)
    

    void eventHandler(String event, String data)
     else if (event == eventPrefix + "/waterTankSensor/online")  else if (event == eventPrefix + "/waterTankSensor/waterHeight") 
    }

Variables you should change when you do this:

- eventPrefix (e.g. myFarm/waterSystem; for publish/subscribe events)
- myWriteAPIKey (grab from your ThingSpeak pump controller channel)
- myWriteChannelNumber (from ThingSpeak pump controller channel)
- lowerCutoff (lowest acceptable water height, in inches)
- higherCutoff (highest acceptable water height, in inches)
- totalDistance (distance from ultrasonic sensor face to bottom of water tank)

I\'ve bracketed these variables with:

    language:c
    //################### update these vars ###################

so you know what you have to change.

Some of the code may be confusing, especially something like

    language:c
    thing ? result = 1 : result = 0;

This is shorthand for an if-else statement. It\'s the equivalent of

    language:c
    if (thing)  else 

#### Default Firmware Feature/Bug

There are a few challenges when working with the Photon and its development environment. One of the biggest problems is that sometimes new firmware versions break old code. For example, from the time I developed this original system (Oct 2015) to the time this tutorial was written (Mar 2016), a new firmware version came out (0.4.9), which is incompatible with my old code. The worst part about it is, the Photon sits there blinking a red error message on the LED and is impossible to flash without physically accessing the device. Kind of a pain when it\'s on top of a roof and in a watertight enclosure held together by 6 screws (and there\'s a bunch of melting snow everywhere).

I think what ended up being broken with the new firmware was the WiFi.selectAntenna() function, which was silly and tiny. Regardless, we want to disable automatic firmware updates for our devices running important tasks like this, so it can keep running for years. To do this, click the \'Devices\' icon on the left of [build.particle.io](http://build.particle.io), click the star (left) and the arrow (right) next to the device we\'re going to flash, then choose the 0.4.9 firmware (without Default). Re-flash your device, and it\'s good to go. Do this for both the telemetry and control box Photons.

[![just say \'no\' to default firmware](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/34-no_default_firmware.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/34-no_default_firmware.jpg)

*Leaving the firmware on \'default\' will auto-upgrade and can break your system. Just say \'no\' to default firmware, and set it to 0.4.9 for this tutorial\'s code.*

## Setting Up the ThingSpeak Channels

### The Telemetry Channel

There are many sites out there for storing your IoT data. Here are two: [dweet.io](https://dweet.io/) and my personal favorite, [The Mathworks\' ThingSpeak](https://thingspeak.com/). ThingSpeak already has some nice built-in features, like Google visualization plugins, Twitter interfacing, React (which can do something like post a tweet when data meets a threshhold), MATLAB analysis, and more. It\'s also [open-source](https://github.com/iobridge/thingspeak).

First, sign up for a ThingSpeak account if you don\'t already have one. Next, create a channel by going to Channels-\>My Channels-\>New Channel. Click the checkboxes next to each field (1 through 8) and label them:

- Water Height (inches)
- P (inHg)
- pressure change rate (inHg/min)\*10\^6
- T (F)
- RH %
- light intensity
- battery V
- battery SOC

Check the box next to \'Make Public\' if you want other people to be able to view it without needing the read API key. To finish, click \'Save Channel\'.

Now, click \"API Keys\" in the menu bar that should be around the middle of your screen. Copy the \"Write API\" key, and put that in your Photon telemetry box code as the `myWriteAPIKey` variable. Also copy the \"Channel ID\" number from your ThingSpeak channel page, and set that as the `myChannelNumber` variable in your Photon telemetry code.

[![ThingSpeak API key location](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/35-thingspeak_api_keys.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/35-thingspeak_api_keys.jpg)

*Click on \'API Keys\' and your keys (that you need in your Photon code) should be right there.*

Once you power up your telemetry Photon, you should see the data start getting populated (your ThingSpeak page will auto-refresh every 15-ish seconds).

Now, we\'ll set up a Twitter feed to post info on our data, which can be used to send alerts on rapidly dropping pressure (which can signal bad weather). Create a Twitter account, sign in, and go back to your ThingSpeak page. Click on \"Apps\" on the top menu bar. Click \"ThingTweet\", and then \"Link Twitter Account\".

Once you\'ve linked your Twitter account, go back to the \'Apps\' page and click on MATLAB analysis. Use this code, changing the API keys and channel ID for your channel:

    language:MATLAB
    % Calcuclates the pressure difference over the last 3 hours
    % writes to channel as long as the time difference between 
    % the two points is at least 2 hours

    % Channel ID to read data from
    ChannelID = 101982;
    % Pressure Field IDs
    PressureFieldID = 2;
    PressureChangeID = 3;

    % TODO - Put your API keys here:
    writeAPIKey = 'your write API key';
    readAPIKey = 'your read API key'; % this is only necessary if the channel is private

    % Get humidity data for the last 60 minutes from the MathWorks Weather
    % Station Channel. Learn more about the THINGSPEAKREAD function by going to
    % the Documentation tab on the right side pane of this page.

    [pressure, timestamps, chInfo] = thingSpeakRead(ChannelID, 'ReadKey', readAPIKey,  'Fields', PressureFieldID, 'NumMinutes', 180);

    [m,n]=size(pressure)
    display(m)

    if m > 1 % we need at least 2 points to do the calculation
        % Calculate the pressure change
        pressureChange = pressure(end)-pressure([1]);
        % pressure(end) gets us the most recent pressure reading, which is last in the pressure variable (a Matlab matrix) 
        display(pressureChange, 'pressure change (inHg)'); % this shows up below when you hit run
        timeDiff = minutes(diff([timestamps([1]), timestamps(end)])); % difference in minutes between the first and last readings
        display(timeDiff);
        pressureChangeRate = pressureChange/timeDiff * 1000000;
        display(pressureChangeRate, 'pressure change rate (inHg/min)*10^6');

        % Write the average humidity to another channel specified by the
        % 'writeChannelID' variable

        % Learn more about the THINGSPEAKWRITE function by going to the Documentation tab on
        % the right side pane of this page.
        if timeDiff > 60.0 % make sure the time difference is at least 1 hour between the points
            for n=1:8 % quite a bit of a hack, but it works
                pause(2); % they don't allow more than 2s pauses (delays) here, and I didn't take the time
                % to figure out how to do a callback, etc
            end
            thingSpeakWrite(ChannelID, pressureChangeRate, 'Fields', PressureChangeID, 'writekey', writeAPIKey);
            display('writing to channel')
        end
    else
        display('not enough data in channel yet')
    end

Make sure to hit \'save and run\', and you can check the output below the code area to see it working. Scroll down a bit, click \"React\", then set up a react to run on new data insertion. The picture below shows the details for the react, which are:

  Option name             Value
  ----------------------- -----------------------------------------
  React name              calculate pressure rate of change
  Condition type          Numeric
  Test frequency          On Data Insertion
  Condition: If channel   (your telemetry channel name)
  Condition               field: 2 (P (inHg)); Is greater than; 0
  Action                  MATLAB analysis
  Code to execute         Calculate Pressure Change
  Options                 Run each time condition is met

[![ThingSpeak reacts for pressure drop](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/36-pressure_reacts.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/36-pressure_reacts.jpg)

*Screenshots of the Reacts for pressure drop (bad weather approaching) alerts. I actually ended up having the pressure rate of change test frequency being \'on data insertion\', and the tweets happen every 60 minutes.*

Finally, go back to \'Apps\' one more time to set up some Twitter alerts. Click on \'React\' and then \'New React\'. Set the values as shown in the picture above, and the table below:

Option name

Value

React name

pressure drop

Condition type

Numeric

Test frequency

On every 60 minutes

Condition: If channel

(your telemetry channel name)

Condition

field: 3 (pressure change rate (inHg/min\*10\^6); Is greater than; 984

Action

ThingTweet

then tweet

#rapid_pressure_drop Pressure dropping %%trigger%% inHg/min\*10\^6, storm could be on the way.

Using Twitter account

(your twitter account here)

Options

Run each time condition is met

The %%trigger%% is replaced by the value of the field. Hit \'Save React,\' and you\'re good to go.

### The Control Box Channel

Set up another ThingSpeak channel, with just two fields set as:

- pump on
- motion detected

The API keys from this will be used in the control box Photon code.

### ThingSpeak Google Gauges

Another nice feature of ThingSpeak is the ease with which nice looking graphics can be made (once you get the hang of it). For example, a Google Gauge can be embedded in your ThingSpeak channel (or anywhere else with JavaScript). Unfortunately, ThingSpeak recently disabled JavaScript apps from being on public pages, so this will only work on private views or other custom applications.

[![Google Gauge example](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/37-google_gauge.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/37-google_gauge.jpg)

*The Google Gauge provides a quick way to take in information.*

To get this gauge going for the water tank fullness, go to ThingSpeak.com, click Apps-\>Plugins-\>New-\>Google Gauge-\>Create, and use this code for the JavaScript:

    language:javascript
    <script type='text/javascript' src='https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js'></script>
    <script type='text/javascript' src='https://www.google.com/jsapi'></script>
    <script type='text/javascript'>

      // set your channel id here
      var channel_id = channel ID here; // eg 101992
      // set your channel's read api key here
      var api_key = 'your readAPI key here';
      // maximum value for the gauge
      var max_gauge_value = 42; // this is the maximum water height from your telemetry code
      // name of the gauge
      var gauge_name = 'Water tank level (%)';

      // global variables
      var chart, charts, data;

      // load the google gauge visualization
      google.load('visualization', '1', );
      google.setOnLoadCallback(initChart);

      // display the data
      function displayData(point) 

      // load the data
      function loadData() 

        });
      }

      // initialize the chart
      function initChart() ; // customize the red, yellow, and green levels if you want

        loadData();

        // load new data every 15 seconds
        setInterval('loadData()', 15000);
      }

    </script>

Don\'t forget to change the `\<title>` in the HTML section. Then simply click checkboxes on the channels for which you want the Gauge to be visible. You can drag and drop the Gauge (while viewing the channel) to be anywhere on the page.

## Setting Up Text Alerts

If you want to get an alert via text or email when the pressure drops rapidly (or for other data events), it can be done with [ifttt.com](http://ifttt.com). Head over there and setup an account, and [connect your phone to IFTTT](https://ifttt.com/sms). Click \'My Recipes\' on the top menu, click \'Create a Recipe\', then click \'this\'. Search for \'twitter,\' and click on the Twitter icon. Unfortunately, IFTTT\'s \"tweet from search\" feature seems to be broken, hopefully it\'s fixed soon. For now, the best we can do is send a text every time we post a new tweet. This unfortunately means we can\'t tweet more mundane things right now, since it would be annoying getting that many texts.

[![ThingSpeak reacts for pressure drop](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/38-IFTTT_main.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/38-IFTTT_main.jpg)

*Click on \'Create a Recipe\' to get started.*

Click \'New tweet by a specific user\', then enter your username after the \"@\" symbol, similar to \"@JSF_auto_farm\". Next, click \'that\', search for SMS, and click \'Send an SMS\'. I just left the message as the default. Click \'Create Action\' and \'Create Recipe\', and that\'s it! If you had to create and link accounts for everything to get to this point, it will be much faster next time you want a text alert for some remote measurement.

When IFTTT does eventually get their Twitter search feature fixed, we can use a hashtag to filter our results. After clicking \'this\', search for \'twitter\', then choose \'New tweet from search\'. Use this as the search:

\"@your_twitter_username\" \"#rapid_pressure_drop\"

replacing your_twitter_username with the one you picked previously.

### Alternate: Use Gmail to Send Texts

For the \'that\' portion, you can also choose Gmail (you will have to link a Gmail account for this step), and click \'Send an email\'. If you want to send a text, you can do it as so:

1234567890@vtext.com

Instructions for using email to send a text with any carrier can be found [here](http://www.makeuseof.com/tag/email-to-sms/). I was having trouble getting the texts to consistently go through via Gmail with IFTTT, so I switched to the straight IFTTT SMS feature.

There are many other ways to set up SMS alerts, such as [Twilio](http://www.instructables.com/id/Send-SMS-from-Arduino-over-the-Internet-using-ENC2/), \[SendGrid\](https://sendgrid.com/marketing/sendgrid-services?cvosrc=PPC.Google.sendgrid&cvo_cid=SendGrid%20-%20US%20-%20Brand%20-%20(English)&mc=Paid%20Search&mcd=AdWords&keyword=sendgrid&network=g&matchtype=e&mobile=&content=&search=1&gclid=Cj0KEQjw5ti3BRD89aDFnb3SxPcBEiQAssnp0vQjWtm5suVbWc1LH1ttqbI4AjmB6nc5-v0L3T5GgocaAp6A8P8HAQ), or [IOBridge](http://connect.iobridge.com/). None of these methods have been tested with this setup yet.

## Final Data Analysis 

Here\'s some data from field testing:

[![light values during the day](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/39-light_intensity.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/39-light_intensity.jpg)

*Full Colorado sunlight is bright.*

[![temperature during the day](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/40-box_temperatures.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/40-box_temperatures.jpg)

*The temp inside the box got up to about 95\...when it was 60 out. May have to move this into the shade after all. There were also some strange gyrations going on.*

[![battery SOC during the day](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/41-battery_SOC.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/41-battery_SOC.jpg)

*The battery never dropped below 40% over one night. I\'m also running two ultrasonic sensors, which draws a bit more power.*

[![pressure change during the day](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/3/8/42-pressure_change.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/3/8/42-pressure_change.jpg)

*The pressure was dropping in the \'moderate\' regime this day.*