# Source: https://learn.sparkfun.com/tutorials/environmental-monitoring-with-the-tessel-2

## Introduction

Unfortunately Phant, our data-streaming service, is no longer in service. The system has reached capacity and, like a less-adventurous Cassini, has plunged conclusively into a fiery and permanent retirement. There are several other maker-friendly, data-streaming services and/or IoT platforms available as alternatives. The three we recommend are Blynk, ThingSpeak, and Cayenne. You can read our [blog post on the topic](https://www.sparkfun.com/news/2413) for an overview and helpful links for each platform. The code in this tutorial will need to be adjusted to work with the other data streams.

In the world of tomorrow, everything in our homes will be connected. The Internet of Things (IoT) is the real-world manifestation of that vision. The world of IoT includes network-connected appliances that have not, until now, had any such sophisticated capabilities.

The [Nest](https://nest.com/) product line, which started with intuitive smart thermostats and is expanding into other products, is one set of offerings in a growing market of so-called \"smart home\" offerings. Amazon\'s [Echo](https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-WiFi-Alexa/dp/B00X4WHP5E), which combines several home integration aspects into a single platform, is another.

## Our Own Smart Monitoring Device

There are many types of smart-home systems. Some remotely control a home device, like automatically turning lights on or off at certain times. Others optimize the behaviors of home systems, perhaps switching a home\'s electrical supply between solar and grid power at different times of the day or season.

In this tutorial, we\'ll hone in on the *monitoring* aspect of smart systems. We\'re going to build an air-conditioning monitoring device to collect information and store it in the cloud.

Our monitoring device will be able to detect the following over time:

- Whether the air conditioner is ON or OFF
- Temperature
- Relative humidity
- Air pressure

Data points from the sensors in the device will be uploaded to and stored in [Sparkfun\'s Phant-powered data.sparkfun.com service](https://learn.sparkfun.com/tutorials/pushing-data-to-datasparkfuncom/what-is-phant).

## Preflight Check

If this is your first time experimenting with the [Tessel 2](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/about-the-tessel-2), there are a few things you gotta do first! We recommend reading through our Getting Started with the Tessel 2 before diving into this project. We promise, it wont take that long.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-tessel-2)

### Getting Started with the Tessel 2 

October 12, 2016

Get your Tessel 2 up and running by blinking and LED, the Hello World of embedded electronics.

### Dive Deeper into the Tessel 2

The entire [Johnny-Five Inventor\'s Kit Experiment Guide](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit) is great stuff if you\'re starting out with the Tessel 2.

[](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit)

### Experiment Guide for the Johnny-Five Inventor\'s Kit 

June 28, 2016

Use the Tessel 2 and the Johnny Five Inventors kit to explore the world of JavaScript enabled hardware through 14 awesome experiments!

### Getting Started with Phant(data.sparkfun.com)

If you\'ve never worked with the data.sparkfun.com service before, the guide below will help you get started making your own stream for collecting data.

## Materials

To build the monitoring device, you\'ll need the following parts:

#### Parts to Source Elsewhere

- 47uF capacitor
- [Air Conditioner Extension Cord, 3\'](https://www.amazon.com/Prime-EC680503L-Conditioner-Appliance-Extension/dp/B0022NH41Q/) (Amazon)

### Meet the Supporting Hardware

#### Non-Invasive Current Sensor

The non-invasive current sensor has a \"jaw\" that clamps around a wire. It can read the amount of current flowing through the wire without the wire itself having to be modified (ergo, *non-invasive*). By plugging the air conditioner into the extension cord and then using the current sensor to detect how much current is going through the extension cord, we\'ll be able to tell when the AC is running.

The current sensor\'s output is a current much lower, but linearly related to, the current it\'s sensing.

[![Non-Invasive Current Sensor](https://cdn.sparkfun.com//assets/parts/6/2/6/2/11005-05a.jpg)](https://cdn.sparkfun.com//assets/parts/6/2/6/2/11005-05a.jpg)

#### TRRS Breakout

The non-invasive current sensor has a connector that looks like an audio jack on one end. It is a TRS (Tip-Ring-Sleeve) connector, shown on the left side of the diagram below. You may also have seen TRRS connectors (Tip-Ring-Ring-Sleeve, right side of diagram), which are commonly used for handsfree headsets. The [TRRS breakout](https://www.sparkfun.com/products/11570) makes each of the pieces of a TRRS connector (the tip, each of the two rings and the sleeve) accessible. The TRRS breakout will allow us to easily connect to the tip and the sleeve of the current sensor\'s connector so we can read its values.

[![TRRS](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/trs-trrs.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/trs-trrs.png)

## Build It

Let\'s begin by assembling the environment monitoring device!

Start by plugging the BME280 into the breadboard so that it straddles the [DIP support ravine](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard#anatomy-of-a-breadboard) (notch) that runs vertically down the middle of the breadboard. Next, connect the BME280 to the Tessel 2 with jumper wires as shown in the wiring diagram:

  BME280   Tessel 2
  -------- ---------------
  GND      GND
  3.3V     3.3V
  SCL      Port A, Pin 0
  SDA      Port A, Pin 1

[![voltage divider](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/assembly-01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/assembly-01.png)

Add the current sensor\'s voltage divider circuit.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/assembly-02-a.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/assembly-02-a.png)

Here\'s a closer look at the voltage divider circuit:

This voltage divider circuit \"conditions\" the output of the current sensor so that it is constrained to a range of input voltages that can be read by the Tessel 2 (0 - 3.3V). If you\'d like to learn more about the technical details, you can read about the circuit it is based on, described in the article [*CT \[Current Transformer\] Sensors --- Interfacing with an Arduino*, OpenEnergyMonitor.org](https://openenergymonitor.org/emon/buildingblocks/ct-sensors-interface).

[![CT Circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/CTCircuit.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/CTCircuit.png)

The final circuit should look like this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/tessel-environment-monitor-device.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/tessel-environment-monitor-device.png)

Next, you\'ll need a sharp utility knife and a safe, clean cutting surface. On your surface, lay the Air Conditioner Extension Cord flat, and use the utility knife to separate one of the three joined sections of wire. Make the cut approximately 3 to 4 inches long---just long enough to put the current sensor\'s top \"jaw\" through and safely clip it together.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/current-sensor.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/current-sensor.jpg)

**WARNING:** If you expose ***ANY*** wire during this process, immediately discard the entire extension cord and start over with an uncut cord. We recommend purchasing two of these just in case. **Exposed wire will put you at risk of fire or electrocution.**

## Program It

### Create A Cloud Data Stream

The application that we\'re going to create will post data reported by the BME280 and Non-Invasive Current Sensor circuit from the Tessel to [data.sparkfun.com](https://data.sparkfun.com/) (that\'s why this application **does** require a connection to the internet).

Before we get started with our own program, you\'ll need to create a new *data stream* on [data.sparkfun.com](https://data.sparkfun.com) so that you can send data to it from the monitoring device. You\'ll need to obtain the public and private keys for this data stream for use in the configuration of the air-conditioning monitor\'s code later.

[Create a new \"data stream\"](https://data.sparkfun.com/streams/make). You\'ll want to fill the form in with something similar to this:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/create-stream-01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/create-stream-01.png)

When you\'ve completed the form, click \"Save\" and you\'ll be brought to a screen that looks like this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/create-stream-02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/create-stream-02.png)

Below that section and at the bottom of that page, you will see an option to send the keys to an email address---I recommend doing this before you proceed.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/create-stream-03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/create-stream-03.png)

### Create A New Project And Install Dependencies

You should already have a `j5ik` directory---creating it is part of the [Tessel software setup process](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/software-installation-and-setup). Use a terminal application to go to that directory, and then:

[cd ../;]\
[mkdir environment-monitor;]\
[cd environment-monitor;]\
[npm init -y;]\
[npm install johnny-five tessel-io got;]

This is going to change (`cd`) to the parent directory of `j5ik/` and create an all new directory called `environment-monitor`. Once created, it will then change into `environment-monitor/` and initialize a new project workspace with `npm init -y`. The last line will install the modules `johnny-five`, `tessel-io` and `got` into this project. The `got` module provides \"Simplified HTTP requests\" and describes itself as:

> A nicer interface to the built-in http module.
>
> It supports following redirects, promises, streams, retries, automagically handling gzip/deflate and some convenience options

which is perfect for our project\'s needs!

### Application Overview

There are four main files for our application, and they will be created in the root of the project (i.e. the `environment-monitor/` directory):

- `current.js`: a module that exports a class called `Current`. `Current` represents a Non-Invasive Current Sensor and inherits from Johnny-Five\'s `Sensor` class.
- `ac.js`: a module that exports a class called `AC` which represents an Air Conditioner. `AC` inherits from `Current`.
- `config.js`: your application-specific configuration
- `index.js`: the application itself

### Class Heirarchy Overview

The next portion of this tutorial is dedicated to writing the software that will run our environment monitor. The bulk of this work will be spent creating cleanly separable classes that will be layered together in our application:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/inheritance-overview.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/inheritance-overview.png)

### Writing the Current Sensor Class

`Current` is a class that will extend Johnny-Five\'s `Sensor` class. Open your favorite code editor, create a file called `current.js` and save it in the `environment-monitor/` directory. Type---or copy and paste---the following JavaScript code into your `current.js` file:

    language:javascript
    "use strict";
    const five = require("johnny-five");

    class Current extends five.Sensor  else  else 
            }
          } else 
        });
      }
    }
    module.exports = Current;

### Exploring the Current Class

To provide a measurement of current in Amps, `Current`\'s `data` handler function needs to consider a number of individual data samples taken during a 1-second sampling cycle. Computations need to be performed on individual samples, and, at the end of each sampling cycle, a *root mean squared current* (rmsI) is calculated. `Current` objects then emit a `measurement` event and pass the `rmsI` along to anything that might be listening. `rmsI` is what we\'re after here---it represents the current going through the wire.

The first line of the `Current` module contains a Use Strict Directive to inform the JavaScript engine that this code conforms to a [safe subset of JavaScript](https://tc39.github.io/ecma262/#sec-strict-variant-of-ecmascript). `"use strict";` appears at the top of every code file for the air conditioning monitor, so I won\'t dive into it again:

    language:javascript
    "use strict";

Next, the module requires its only dependency: the `johnny-five` module:

    language:javascript
    const five = require("johnny-five");

Immediately following that, a new class, `Current`, is declared. `Current` extends the `Sensor` class provided by Johnny-Five. `Sensor` provides all of the base mechanics needed to implement a specific analog input sensor. `Current` will extend `Sensor` and provide some things to support our current sensor.

`Current`\'s constructor (the method that is invoked when a new `Current` object is created) defines a single formal parameter, `pin`. `pin` gets passed as an argument to the parent class\' constructor (that is, the constructor on `Sensor`) when `super(...)` is invoked. `Sensor` takes care of setting up an analog input on the `pin` indicated:

    language:javascript
    class Current extends five.Sensor 
    }

After the call to `super(...)`, a long list of let variable declarations follows. Don\'t worry if these don\'t make a lot of sense yet:

    language:javascript
    let aref = this.io.aref || 4.4;
    let cCount = 0;
    let sCount = 0;
    let lastSampleI = 0;
    let sampleI = 0;
    let lastFilteredI = 0;
    let filteredI = 0;
    let offsetI = 0;
    let sumSqI = 0;
    let rmsI = 0;
    // Turn Ratio: 100A:0.05mA
    //             2000:1
    // Burden: 100Ω
    // Calibration: 2000 / 100 = 20
    let calibration = 20;
    let ratioI = calibration * (aref / 1023);
    let last = Date.now();
    let isCalibrated = false;

All right, let\'s look at what some of these mean:

- `aref`: the value of the particular board\'s *analog reference*, which is the top end of the voltage that the board expects in the analog input range. [For the Tessel, we know this is +3.3V](https://www.github.com/rwaldron/tessel-io/blob/238076a49f316e6c343a178fe7afa8dfda39a7ad/lib/index.js#L507-L509), but other boards have different `aref` values (e.g. Arduino Uno is +5V). `this.io.aref` should contain the analog reference for whatever board Johnny-Five is running on currently.
- `cCount`: track the number of \"calibration\" cycles that have passed. Calibration is set to occur over 5 1000-ms cycles---that is, the first 5 seconds of the instance\'s lifetime will be used for calibration.
- `sCount`: track the number of samples collected in each 1000ms sampling cycle.
- `lastSampleI/sampleI`: the value of the previous and present Amps (current, or *I*) value.
- `lastFilteredI`, `filteredI`, `offsetI`, `sumSqI`: Used within individual sampling computations.
- `rmsI`: the calculated root mean squared (RMS) Amps value for the sampling cycle.
- `calibration/ratioI`: calculated calibration and Amps ratio based on turn ratio---a characteristic of the current sensor\'s hardware---and burden resistor---100Ω in our circuit. [More technical details](https://openenergymonitor.org/emon/buildingblocks/ct-sensors-interface)).
- `last`: tracks the *last* time a sampling cycle completed.
- `isCalibrated`: initially `false`; will become `true` once the calibration cycles are complete.

Next, we define a handler function for `"data"` events. These `"data"` events are defined within the super class `five.Sensor`. The only operation that occurs at the \"top level\" of this function execution context is to take note of the exact date and time (`let now = Date.now()`). `data` events fire frequently, about once every 25 milliseconds (this is the default sampling frequency of Johnny-Five\'s `Sensor` class).

    language:javascript
    this.on("data", () => );

From there, the operations choose a fork in the road. There are two primary conditional paths:

    language:javascript
    if (now > last + 1000)  else 

The first path handles execution when a full sampling cycle---1000ms or 1 second---is complete.

First the `rmsI` is calculated for this sampling cycle, then resets some variables (`sumSqI` and `sCount`). The value of *last* is assigned to the value of *now*; this will result in starting a new sampling cycle when the `data` handler is next invoked.

    language:javascript
    // Calculate (Amps = I)
    rmsI = ratioI * Math.sqrt(sumSqI / sCount);
    sumSqI = 0;
    sCount = 0;
    last = now;

If the instance is done calibrating (`isCalibrated`), then it can emit a `"measurement"` event with the value of the `rmsI` for the sampling cycle. Otherwise it continues calibration.

    language:javascript
    if (isCalibrated)  else  else 
    }

That\'s the end of the fork that handles the end of a sampling cycle. The other fork---the second primary condition---occurs *almost* every time the `data` handler is invoked, every time it\'s invoked and it\'s not the end of a sampling cycle.

This fork performs several computations on the most recent current value read from the sensor. The calculations here are ported from [OpenEnergyMonitor.org\'s \"EmonLib\"](https://github.com/openenergymonitor/EmonLib/blob/master/EmonLib.cpp#L187-L198).

This second fork evaluates a single sensor reading. It increments the `sCount` (sample count) by `1` in order to track the total number of samples collected within a single sampling cycle. It then performs some calcuations on the current value, with an eye toward ultimately being able to produce a `rmsI` value for the entire sampling cycle.

    language:javascript
    lastSampleI = sampleI;
    sampleI = this.value;
    offsetI = offsetI + ((sampleI - offsetI) / 1023);
    filteredI = sampleI - offsetI;
    sumSqI += filteredI * filteredI;
    sCount++;

Back out in the top-level scope, the very last line exports the `Current` class object so that it can be used by other code modules. I\'ll skip mentioning this when looking at the code in other modules for the air conditioning monitor.

    language:javascript
    module.exports = Current;

### Writing the `AC` Class

Open your favorite code editor, create a file called `ac.js` and save it in the `environment-monitor/` directory. Type---or copy and paste---the following JavaScript code into your `ac.js` file:

    language:javascript
    "use strict";
    const Current = require("./current");

    class AC extends Current 

          isActive = true;
        });

        Object.defineProperty(this, "isActive", ,
        });
      }
    }
    module.exports = AC;

### Exploring the `AC` Class

The `AC` class has only one dependency---the `Current` class we just created.

    language:javascript
    "use strict";
    const Current = require("./current");

Just like with the `Current` class, the next step is to declare a new class called `AC`, which extends the `Current` class. Instances of the `AC` class will forward the value of `setup.pin` along to `super(...)` during instantiation.

    language:javascript
    class AC extends Current 
    }

After the call to `super(...)`, a `let` variable named `isActive` is declared and assigned an initial value of `false`. This will be used to track whether or not the air conditioner is *active* or not. (The air conditioner might be switched *on* all the time, but we only want to know when it\'s actually actively cooling).

    language:javascript
    let isActive = false;

Next, we register a `"measurement"` event handler, which receives the `rmsI` value as an argument. To determine if the air conditioner is active or not\...

the handler first checks if the rounded `rmsI` is less than the value of `setup.minimumI`, which the application specifies as the \"minimum amps flowing when the air conditioner is active\". If it that condition evaluates to `true`, then that means that the air conditioner is *inactive*, so set `isActive` to `false` and *return immediately*. If that condition does not evaluate to `true`, that is: the value of the rounded `rmsI` is greater than or equal to the \"minimum amps flowing when the air conditioner is active\", then set `isActive` to `true`. Note that `isActive` is still the let variable declared *outside* of the event handler.

The `"measurement"` event handler\'s job is to determine whether the air conditioner is active. It determines this by looking at the value of `rmsI` (the root mean squared Amps of the sample), which it receives as an argument. The `setup` object passed to the `AC` constructor includes a `minimumI` property. `setup.minimumI` defines the minimum Amps flowing when the air conditioner is active. If `rmsI` is less than that value, then the air conditioner is not presently active (`isActive = false`). Otherwise, we can deduce that it *is* (`isActive = true`).

    language:javascript
    this.on("measurement", rmsI => 

      isActive = true;
    });

A bit about scope. `isActive` is declared within the function execution context of the `AC` class\' `constructor`. So is the `"measurement"` handler function, so code within it can access `isActive`. However, `isActive` isn\'t accessible directly on `AC` instances yet---for example, if you had an `AC` instance called `ac`, there is no `ac.isActive` property---yet.

What we can do is define an *accessor property*, also called a \"getter\", to expose the value of `isActive` on `AC` instance objects.

    language:javascript
    Object.defineProperty(this, "isActive", ,
    });

Note that we\'re only defining a \"getter\", not a \"setter\". You can check the value of `ac.isActive`, but if you tried to *set* the value (`ac.isActive = true`), you wouldn\'t be able to (it\'d throw `TypeError: Cannot set property isActive of #<AC> which has only a getter`). While this kind of protection isn\'t strictly necessary, it\'s important to me that I impart my preference for tamper-proof hardware state representations in my software.

### Creating the Configuration Module

Before move onto discussing the actual application code, we have one last supporting module file to create: `config.js`.

This module contains a single export, an object containing properties whose values are relevant configuration for our application.

The `interval` property defines how frequently, in milliseconds, new data is sent to data.sparkfun.com. I\'ve specified 10 seconds, but you may change this to whatever best suits your version of the application. Take care to replace `[Phant Public Key]` and `[Phant Private Key]` with the values generated when you created your data stream. If you followed my advice earlier, you will already have an email containing those values.

    language:javascript
    module.exports = ,
    };

### Writing the Environment Monitor Application

Open your favorite code editor, create a file called `index.js` and save it in the `environment-monitor/` directory. Type---or copy and paste---the following JavaScript code into your `index.js` file:

    language:javascript
    "use strict";
    const AC = require("./ac");
    const config = require("./config");
    const five = require("johnny-five");
    const got = require("got");
    const Tessel = require("tessel-io");

    const board = new five.Board();

    board.on("ready", () => .json`;
      const payload = 
      };
      const ac = new AC();
      // Once the AC instance is calibrated,
      // setup the BME280 and report status to phant
      // according to the specified interval.
      ac.on("calibrated", () => );
        board.loop(config.interval, () => ;
            got.post(url, payload);
          }
        });
      });
    });

### Exploring the Application Code

As you\'ve seen twice already in this tutorial, the first thing we do is require the modules that our application depends on. This time, we\'re requiring `got`, `johnny-five`, `tessel-io`, as well as our own `ac.js` and `config.js` module files.

    language:javascript
    "use strict";
    const AC = require("./ac");
    const config = require("./config");
    const five = require("johnny-five");
    const got = require("got");
    const Tessel = require("tessel-io");

If you\'ve previously read any or all of the [Experiment Guide for the Johnny-Five Inventor\'s Kit](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit), then the next part will look familiar. To quote from the guide itself:

> Johnny-Five supports many kinds of development boards. The support for some boards is built right in to Johnny-Five, but others --- including Tessels --- rely on external plugins encapsulated in modules. That's why the code requires the `tessel-io` `npm` module. Here, we tell Johnny-Five to use a `Tessel` object for IO when communicating with the board.

    language:javascript
    const board = new five.Board();

Next, a `"ready"` event handler is registered for the `board` instance (which represents the Tessel 2 itself). The `"ready"` event will be emitted when Johnny-Five and Tessel-IO have completed their respective initialization phases and the board is ready to interact with.

Before we start interacting with the hardware, there are two const declarations that get created. The value of `url` will be passed directly to `got.post(...)` and represents the API endpoint for posting data to your data stream, while the value of the `payload.body` property will be updated with the present environment values to send to data.sparkfun.com.

    language:javascript
    const url = `http://data.sparkfun.com/input/$.json`;
    const payload = 
    };

Now we get to see our `AC` class in action! The program instantiates a new `AC` instance object and assigns it to `ac`. If you look back at the `AC` class constructor definition, you\'ll see that it accepts a `setup` argument, an object. The `pin` property of the `setup` object will get forwarded on to `Current` and then on to `Sensor` to tell Johnny-Five which pin the component is connected to. The `minimumI` value represents the minimum amount of current, in Amps, that the air conditioner uses when active.

    language:javascript
    const ac = new AC();    

Immediately following the instantiation, the program registers a `"calibrated"` event with `ac`. Remember that `AC` inherits from `Current`? That means that the `ac` instance object will emit all of the events that come from its super class object as well. Very useful!

    language:javascript
    ac.on("calibrated", () => );

The `"calibrated"` event will fire once near the beginning of the `ac` instance\'s lifetime, and when it does, the program will treat that as an indication that all systems are \"go\".

The next step is instantiate a new `five.Multi` object, specifying `"BME280"` as `controller`. The `Multi` class is used to represent components that provide data from multiple sensors, each of which is represented by a Johnny-Five component class. In this case, an instance of `Multi` for a `BME280` will itself contain instances of:

- `Altimeter`
- `Barometer`
- `Hygrometer`
- `Thermometer`

\...all four of these sensors are packaged on the BME280. By making use of the `Multi` class, you can wrangle all four sensors with one component object.

    language:javascript
    const env = new five.Multi();

In the [Johnny-Five Inventors Kit Guide Experiment 10: Using the BME280](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-10-using-the-bme280), you learned how to respond to `"data"` events from the `BME280` `Multi` instance by creating a handler that forwarded values on to the browser via a [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) provided by [socket.io](http://socket.io/).

In this example, I\'d like to show you how to interact with sensors by simply waiting for them to be \"ready\" and then accessing data directly from the instance object\'s properties. The program will use the `board.loop(...)` method, check if the `Multi` instance (`env`, which is short for \"environment\") is \"ready\"; if it is, then it will post data to our data stream:

    language:javascript
    const env = new five.Multi();
    board.loop(config.interval, () => ;
        got.post(url, payload);
      }
    });

And that\'s it!

## Run It

Once all of this is saved in the right files and in the right directories, type---or copy and paste---the following into your terminal:

[t2 run index.js]

Once it\'s running, open your browser to https://data.sparkfun.com/streams/\[Phant Public Key\] and refresh it the browser as often as you\'d like to see the data appear in your public stream. The stream that I created for this project is available here: https://data.sparkfun.com/streams/wp063JWw94CmL10wYw1W , which I exported to Analog.io and captured a portion that shows my own air conditioner going inactive, followed by a the temperature in the apartment rising until the air conditioner becomes active again.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/analog.io-chart-01.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/analog.io-chart-01.png)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/analog.io-chart-02.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/analog.io-chart-02.png)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/8/analog.io-chart-03.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/8/analog.io-chart-03.png)

When you\'re ready to deploy it full time, push the project into the Tessel 2\'s flash memory by using the command:

[t2 push index.js]