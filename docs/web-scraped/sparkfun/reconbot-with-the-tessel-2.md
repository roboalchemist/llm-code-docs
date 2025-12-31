# Source: https://learn.sparkfun.com/tutorials/reconbot-with-the-tessel-2

## Let\'s Build a Robot!

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/bots-eye-view.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/bots-eye-view.png)

You are about to build a robot that you can control from a browser on your phone or laptop. You can guide the robot by looking through the robot\'s \"eyes\" (*first-person-view*, or FPV), because it\'s going to stream live video for you so you can see what\'s in front of it. You can pilot your robot around corners and into nooks and crannies, chase your cat, entertain guests or just bonk it into a chair leg over and over again---it\'s all up to you!

The browser-based controls emulate a thumb-pad joystick, hearkening back to the tactile controls of radio-controlled (RC) cars. The virtual joystick for our robot controls both direction and speed. It\'ll snap back to center (and the robot will stop moving) when it\'s not being actively dragged and held.

Your robot will be independent of wires and external connections: you\'ll control it over your local WiFi network, and we\'ll use a USB power bank to give it juice.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/018.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/018.jpg)

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

## Materials

To build our robot, you\'ll need the following parts:

#### Additional Supplies

- 1 Long, plastic wire tie
- [Monoprice Hook and Loop Fastening Cable Ties](https://www.amazon.com/Monoprice-106457-Hook-Fastening-Cable/dp/B004AFUJZC/) (Amazon)
- [Scotch Exterior Mounting Tape, 1-Inch by 60-Inch](https://www.amazon.com/Scotch-Exterior-Mounting-1-Inch-60-Inch/dp/B00004Z4BV) (Amazon)
- 1 [Creative Live! Cam Sync HD 720P Webcam](https://www.amazon.com/Creative-Live-Sync-720P-Webcam/dp/B0092QJRPC/) (Amazon)
- 1 [iXCC 8000mAh Compact Power Bank](https://www.amazon.com/iXCC-8000mAh-Compact-Power-Bank/dp/B017JL7DI4/) (Amazon)

### Meet the Supporting Hardware

#### Shadow Chassis and Wheels

The [SparkFun Shadow Chassis](https://www.sparkfun.com/products/13301) is an economic and straightforward platform for constructing a robot. It comes as a kit that has a bunch of parts---our robot will use many, but not all of the parts in the kit.

[![Parts Used from SparkFUn Shadow Chassis](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/shadow-chassis-parts.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/shadow-chassis-parts.jpg)

The chassis will be the \"body\" of our robot, a frame to which we can attach motors, [wheels](https://www.sparkfun.com/products/13259), a camera, and our robot\'s other components.

#### Camera

While creating the robot, we experimented with several different USB cameras and ultimately settled on the [Creative Live! Cam Sync HD 720P Webcam](https://www.amazon.com/Creative-Live-Sync-720P-Webcam/dp/B0092QJRPC/). While we\'ll admit the product name is quite a mouthful, we like this camera because:

1.  It\'s reliable: this camera is a work horse---you\'ll see.
2.  It\'s easy to mount and position: the clip for mounting this camera to a monitor or similar vertical surface is perfectly suited for easy attachment to the top panel of Shadow Chassis (as you\'ll see below).

#### Battery Pack

You\'ll be powering the bot with any adequate USB power bank; the [iXCC 8000mAh Compact Power Bank](https://www.amazon.com/iXCC-8000mAh-Compact-Power-Bank/dp/B017JL7DI4/) (Amazon) is inexpensive and handy.

## Build It

To construct the robot, we\'ll put the chassis partially together and wire up a motor circuit. Then we\'ll install the robot\'s software and test the motors before completing the chassis construction.

### Constructing the Chassis Base

#### Connect Motor Mounts

Each of the robot\'s two motors will have two supporting plastic mounts from the Shadow Chassis kit: one near the front of the motor and one at the back. When attached, the motor mounts will look like this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/motor-mounts.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/motor-mounts.jpg)

The back mounts are easy to attach---they just slide on. The front mounts require a quarter-turn to attach. Start by positioning the front mount as shown in the photo below, taking care not to pinch the motor\'s wires underneath the mount. Note the position of the motor\'s protruding white plastic axle to help you orient the motor.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/motor-support-01.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/motor-support-01.jpg)

Now, rotate the mount counter-clockwise 90 degrees until it clicks into place around the motor. After it\'s secured, it should be positioned as in the photo below:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/motor-support-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/motor-support-02.jpg)

Now you can construct the chassis base:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/chassis-structure.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/chassis-structure.jpg)

1.  Connect the mounted motors to the chassis by snapping the mounts into the chassis base. Pay attention to the orientation. The wires should be on the inside and the rear mounts of the motor should be toward the front of the robot (at the top in the preceding photo).
2.  Connect the struts at each of the four corners. Push hard to snap into place. Attach an extra support piece at the front of the robot for stability.
3.  Attach the wheels to the motor axles.
4.  Flip the base over and attach the little semicircular support nubbin from the Shadow Chassis kit near the back end of the robot (toward bottom left of the following photo)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/chassis-bottom-verso.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/chassis-bottom-verso.jpg)

Some more views of the chassis base (this version has black motors):

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/001.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/001.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/002.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/002.jpg)

### Attach the Camera

With the top panel in hand---that\'s the other big piece in the Shadow Chassis kit---loop one of the \~\~Hook and Loop Fastening Cable Ties\~\~ Velcro ties through the two oblong cut-outs positioned between the wheel mounts:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/003.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/003.jpg)

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/004.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/004.jpg)

Next, place the top panel (shiny side down) in front of you. Cut a piece of two-sided tape or mounting tape, approximately half the length of the bottom side of the camera clip (or full length, it\'s up to you) and attach to the camera clip, like so:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/005.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/005.jpg)

Then flip the camera over and fasten it to the rough side of the top panel. Use the Velcro tie to wrap the camera\'s USB cable:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/006.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/006.jpg)

Make sure the front \"lip\" of the camera clip is flush with the edge of the top panel, and that the camera lens itself is centered:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/007.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/007.jpg)

Cut another piece of double sided tape and attach to one side of the USB battery:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/battery-001.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/battery-001.jpg)

Remove the adhesive paper from the other side of the tape, and place the battery on the top panel:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/battery-002.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/battery-002.jpg)

### Attach the Breadboard

Now for a shocking twist: set the top assembly aside and grab the bottom assembly and then **carefully remove the adhesive strip paper from the breadboard** (we\'re going to reuse it) and place the breadboard over the hole in the front section of the bottom panel. (*As it turns out, most people never remove this adhesive cover strip!*).

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/008.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/008.jpg)

Turn the bottom assembly over and press the paper backing onto the adhesive surface that\'s exposed through the hole. Turns out they are the same size! Using a sharp utility knife, trim off the excess paper.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/009.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/009.jpg)

Once trimmed, the underside of the chassis base should like this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/010.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/010.jpg)

### Wire the Motor Driver Circuit

Turn the bottom assembly right-side-up and insert the Motor Driver breakout onto the breadboard, as shown here:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/012.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/012.jpg)

Wire in the Motor Driver, by following the diagram here:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/motor-diagram.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/motor-diagram.png)

Start by making the breadboard connections (we\'ll connect to the Tessel 2 in a few moments). As you assemble, your work should look similar to following image:

[![motor driver circuit on breadboard](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/013.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/013.jpg)

### Connecting the Tessel 2

Position the Tessel 2 near the rear of the robot on the bottom panel and complete the connections for the motor driver.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/014.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/014.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/015.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/015.jpg)

To help you verify your wiring, review the following tables:

  Motor   Wire    Driver Pin
  ------- ------- ------------
  Left    Black   AO1
  Left    Red     AO2
  Right   Black   BO2
  Right   Red     BO1

\

  Motor   Tessel Pin      Driver Pin   Color In Diagram
  ------- --------------- ------------ ------------------
  Left    Port A, Pin 5   PWMA         Blue
  Left    Port A, Pin 4   AIN2         Green
  Left    Port A, Pin 3   AIN1         Yellow
  Right   Port B, Pin 5   PWMB         Blue
  Right   Port B, Pin 4   BIN2         Green
  Right   Port B, Pin 3   BIN1         Yellow

![The SparkFun Motor Driver Breakout, view of reverse side](https://cdn.sparkfun.com//assets/parts/3/1/5/7/09457-04.jpg)

Above: the pins of the SparkFun Motor Driver Breakout board. Note that this view is of the *bottom* of the board. As attached to your breadboard, connections will be flipped left-to-right.

## Prepping and Testing the Robot

Before you secure all of your connections and put the top on your robot, put the chassis aside for a few minutes, and install the robot\'s software. You\'ll want to test to make sure your motors run in the expected directions before putting it all together. Trust us. We speak from experience.

### Installing the Robot\'s Software

#### Get the Software

If you have `git` installed and feel comfortable using that tool, open your terminal and run:

[git clone https://github.com/bocoup/j5ik-reconbot-tessel-edition.git;]\
[cd j5ik-reconbot-tessel-edition;]\
[npm install;]

If `git` is not your thing, you can also download the project as a zip file:

[Reconbot Project Folder](https://github.com/bocoup/j5ik-reconbot-tessel-edition/archive/master.zip)

You can always find the most up to date content at in the [GitHub repository](https://github.com/bocoup/j5ik-reconbot-tessel-edition) as well.

Extract the contents however you prefer, then open your terminal and navigate to the extracted project directory.

#### Install the Software

From your project directory, run:

[npm install;]

\...And that should do it! Go ahead and open the project directory in your preferred editor, and familiarize yourself with the location of each file. The structure should look something like this:

    language:console
     .
     ├── app
     │   ├── index.html
     │   ├── pep.js
     ├── lib
     │   └── rover.js
     ├── node_modules
     │   ├── express
     │   ├── johnny-five
     │   ├── socket.io
     │   ├── tessel-av
     │   └── tessel-io
     ├── .tesselinclude
     ├── index.js
     ├── install.js
     └── package.json

##### Installing `mjpg-streamer` on the Tessel

Next, install needed video software on your Tessel.

To support one of the most important components of this project---an efficient video stream over a Wireless LAN connection---you\'ll need to install `mjpg_streamer`. To do that, you *could* SSH to the board and manually install it by using `opkg` (Open PacKaGe Management, a package manager for embedded Linux)---but instead you\'ll use another JavaScript program! Yay!

In the project\'s directory, there\'s a script called `install.js`---this contains our installation operations. Feel free to open and read the contents of that file if you\'re curious how it works. You can type---or copy and paste---the following command into your terminal:

[t2 run install.js]

Hit enter and let the script run to completion. The result should look similar to the following:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/install.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/install.png)

### Testing the Motors

Now\'s the time to make any needed adjustments to the motor driver circuit. Double-check the \"Pre-Flight Check\" above to make sure your Tessel is prepped and powered. You may want to use the (USB micro) wall adapter to power the motors during this step.

**Warning: Be ready for motion!** Lift your robot off of the ground before executing \`motors.js\`---motors are going to spin! Remember, the breadboard end of the robot chassis is the front of the robot (helpful for determining which direction the motors should be rotating).

With your Tessel and robot chassis base ready and off the ground, type---or copy and paste---the following command in your terminal:

[t2 run motors.js]

This script will cause the robot\'s motors to run alternately forward and backward, accelerating from slow to top speed. A console log message will let you know which way the motors *should* be turning at any given time.

#### Troubleshooting Motor Connections

Don\'t freak out if one (or both) of your motors is spinning in the wrong direction. If your left motor is spinning the wrong way, swap the red and black connections on the motor driver\'s A01 and A02 pins. If the right motor is misbehaving, swap the red and black connections on B01 and B02.

If your script crashes suddenly or your Tessel becomes unresponsive, double-check to make sure that you are providing the motors with enough power---remember, the Tessel\'s USB connection to your computer cannot provide enough current. You\'ll need to use the DC adapter or a standalone USB power bank.

## Finishing the Robot\'s Construction

Onward! Secure the Tessel 2 to the lower chassis with wire ties, and use a piece of scotch tape across the pin headers on the Tessel 2 to hold the wires in place so they don\'t jiggle out of place when the robot is roving. Connect the USB camera to either of the USB host inputs:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/016.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/016.jpg)

Align the top assembly over the bottom assembly and snap it into place. The camera should be on the breadboard end of the chassis.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/017.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/017.jpg)

Give your assembled **Reconbot: Tessel 2 Edition** a turn and admire your handiwork:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/018.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/018.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/019.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/019.jpg)

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/020.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/020.jpg)

Nice looking robot, eh?

## Running the Robot

**Warning: Be ready for motion!** Pick your bot up off the ground when you run this so it doesn\'t roll away unexpectedly.

Now all you need to do is run:

[t2 run index.js]

Once the program is started, the console should print out an IP address that you can open in your web browser

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/t2-run.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/t2-run.png)

Visit that IP address in a web browser on the same WiFi network, and you should see streaming video from your robot and be able to control it using the thumb joystick!

If you\'re curious about how the robot actually works, read on!

## How the Robot Works

The software for this project is similar in structure to the software in the Johnny-Five Inventors Kit Guide [Experiment 10: Using the BME280](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-10-using-the-bme280)---if you haven\'t read that guide, we suggest doing so now and working through that experiment. That will help to familiarize you with how we will be using Web Sockets in the robot\'s application.

The robot\'s code is composed of two main \"chunks\":

1.  **Client code**. This code runs inside a web browser (on your laptop or phone, e.g.) and consists of an HTML page and some JavaScript. The client code is responsible for displaying the robot\'s streaming video, as well as the display and behavior of the steering controls. The HTML and JavaScript that make up the client code are delivered to your web browser by the server code when you connect to the Tessel. The client code is contained within the `app/` directory of the project.
2.  **Server code**. This Node.js application code runs on the Tessel when you execute `t2 run index.js`. The server code creates a web server to respond to requests from web browsers. It starts a process that streams video from the webcam and makes it available for browsers that connect. It also takes incoming steering data from the browser-based controls and translates it into speed and direction of the robot\'s motors (wheels).

### How the Web Interface Works (The Client Code)

The client code---which executes in your browser---is responsible for rendering the controls, showing the streaming video and sending steering and speed instructions to the server.

The client application\'s user interface is a single HTML file (`app/index.html`). The important parts of this file are:

- An `<img>` element to display the `mjpg-streamer` \"video stream\". This `img` is sized so that the video stream fills the browser\'s viewport.
- A `<canvas>` element to display the touch-driven virtual thumb-stick.
- JavaScript (inline in a `<script>` tag) to draw the shapes of the controls into the `canvas`, capture and process interaction events (e.g. touch) and send socket messages containing axis value payloads to the server application.

#### How Steering Works

The virtual thumbstick is designed in a way that hearkens back to traditional radio-controlled (RC) transmitters. Take a look at a \"real\" RC transmitter control:

And our version:

Interacting with the thumbstick causes a message to be sent over the connected socket to the server. This message contains an object representing a point `` for the coordinates (relative to the thumbstick) last touched. Values for both `x` (left-right) and `y` (up-down) axes are between -100 and 100.

            (X, Y)

    -100,   0,100    100,
    100              100
      \       |       /
       \      |      /
        \     |     /
         \    |    /
          \   |   /
           \  |  /
            \ | /
             \|/
    -100,-----+-------100,
      0      /|\       0
            / | \
           /  |  \
          /   |   \
         /    |    \
        /     |     \
       /      |      \
      /       |       \
    -100,   0,-100   100,
    -100            -100

On the server, this point object is used to compute an angle, which is then used to find a \"turn coefficient\", which is then used to calculate how much \"turn\" to apply to the motors. Yay, trigonometry!

### How the Server Code Works

The code that runs on your Tessel is a Node.js application. It:

- *hosts an HTTP server*. This is what will serve the HTML page and the streaming video you\'ll see in your browser when you connect to the Tessel. Using the built-in module `http`, as well as the popular third-party web framework module `express`, the server code serves static content (HTML and JavaScript) as well as routing requests for `/video` to support the streaming video.
- *hosts a web socket*. Remember, the virtual thumbstick in the browser will be sending data messages about its position to the server so that the robot\'s direction and speed can be controlled. The code combines uses the `socket.io` module to pull this off.
- *controls the robot hardware itself*. As the server receives axis data on the web socket, it passes these values along to an `update(...)` method on an object that is controlling the robot itself (an instance of a class called `Rover`.

Let\'s take a look at the supporting cast---a script that fires up a video-streaming process and a class (`Rover`) for controlling the robot\'s movements.

#### How the Video is Streamed

At the beginning of `index.js`, an instance of `av.Camera` is created, which itself controls an `mjpg_streamer` child process that streams video, which is available at port `8080` on the Tessel.

#### How the Robot Controls its Motors

`lib/rover.js` contains a class called `Rover`, which encapsulates the logic for actually moving the two-wheeled robot around. Most of `Rover`\'s functionality is within a method called `update(...)`. `update(...)` takes in axis information (direction and speed information from the controller) and converts that into the right kind of motor motion.

There\'s a bunch of trigonometry in `update(...)` and we don\'t want to make you glaze over completely (though, by all means, explore the source code if you\'re curious!). It does the heavy lifting of calculating and converting angles, computing \"move\" and \"turn\" values, scaling values to the correct speed and updating the motors.

#### How it all Fits Together

`index.js` is the script that pulls it all together, and this is the script you\'ll run on the Tessel using `t2 run` (or `t2 push`). Here is the script in its entirety (and then we\'ll break it down):

    language:javascript

    "use strict";

    // Built-in Dependencies
    const cp = require("child_process");
    const Server = require("http").Server;
    const os = require("os");
    const path = require("path");

    // Third Party Dependencies
    const five = require("johnny-five");
    const av = require("tessel-av");
    const express = require("express");
    const Socket = require("socket.io");
    const Tessel = require("tessel-io");

    // Internal/Application Dependencies
    const Rover = require("./lib/rover");

    // Application, Server and Socket
    const app = express();
    const server = new Server(app);
    const socket = new Socket(server);
    const video = new av.Camera();

    // Configure express application server:
    app.use(express.static(path.join(__dirname, "app")));
    app.get("/video", (request, response) => `);
    });

    // Start the HTTP Server
    const port = 80;
    const listen = new Promise(resolve => );

    // Initialize the Board
    const board = new five.Board();

    board.on("ready", () => ,
        // Right Motor
        ,
      ]);

      console.log("Reconbot(T2): Initialized");
      socket.on("connection", connection => );
      });

      listen.then(() => .local`);
        console.log(`http://$`);

        process.on("SIGINT", () => );
      });
    });

##### Breaking down index.js

The very first thing we encounter is a Use Strict Directive---this informs the JavaScript engine that this code conforms to a [safe subset of JavaScript](https://tc39.github.io/ecma262/#sec-strict-variant-of-ecmascript). It will also appear at the beginning of the `lib/rover.js`:

    language:javascript
    "use strict";

##### Getting our Dependencies in Order

This is the program\'s \"setup\" stage, and we need to organize and require all of the application\'s dependencies: built-in node modules, third-party packages and our own modules:

    language:javascript
    // Built-in Dependencies
    const cp = require("child_process");
    const Server = require("http").Server;
    const os = require("os");
    const path = require("path");

    // Third Party Dependencies
    const av = require("tessel-av");
    const express = require("express");
    const five = require("johnny-five");
    const Socket = require("socket.io");
    const Tessel = require("tessel-io");

    // Internal/Application Dependencies
    const Rover = require("./lib/rover");

##### Starting up the Streaming Video

To create our video stream, all we have to do is instantiate a new `av.Camera` object:

    language:javascript
    const video = new av.Camera();

##### Starting the Web Server and Web Socket

We\'ll be using a web application framework called [`Express`](http://expressjs.com/en/4x/api.html) to provide the logic necessary to support what our web server does:

    language:javascript
    const app = Express();

We\'ll need a web server (via Node\'s built-in `http` module) to handle delegating incoming requests to our application:

    language:javascript
    const server = new Server(app);

And a web socket hosted by that http server:

    language:javascript
    const socket = new Socket(server);

Most of what our web application needs to deliver is static content: an HTML document, specifically. For that, we can use Express\' [`static` \"middleware\"](https://expressjs.com/en/starter/static-files.html). Long story short, the following makes it so clients (i.e. browsers) can request and successfully receive files that live under the `app/` directory:

    language:javascript
    app.use(Express.static(path.join(__dirname, "app")));

But the `app` does need to do one fancy thing. When the browser requests `/video`, our app redirects it to the specific URL where the streaming video is available:

    language:javascript
    // Configure express application server:
    app.use(Express.static(path.join(__dirname, "app")));
    app.get("/video", (request, response) => `);
    });

Finally, we\'ll fire up the web server so it\'s listening on port 80 (default HTTP port):

    language:javascript
    // Start the HTTP Server
    const port = 80;
    const listen = new Promise(resolve => );

##### Initializing the Tessel Board

*Note*: If this is your first exposure to using the Johnny-Five [`Board`](http://johnny-five.io/api/board/) class to represent the state of the Tessel 2\'s board, we recommend you read (at the least) [Experiment 1: Blink an LED](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-1-blink-an-led) for a little background.

This `Board` instantiation looks a little different from other Johnny-Five Tessel examples. We\'re explicitly disabling the automatic `REPL` (interactive console). We also tell the board not to respond in its default way to `SIGINT` events. `SIGINT` is a signal sent by Unix-based systems when a process is interrupted, like when you type `ctrl-C` after using the `t2 run` command. We\'ll shortly define how we *do* want the robot to respond if the process is interrupted.

    language:javascript
    // Initialize the Board
    const board = new five.Board();

When the [`board`](http://johnny-five.io/api/board) emits the `ready` event, the Tessel 2\'s hardware is ready for interaction.

    language:javascript
    board.on("ready", () => );

##### Creating the Rover Object

Within the `"ready"` event handler, we can be confident that the Tessel hardware is ready to go. The next step is to instantiate an object of the `Rover`. When we instantiate a `Rover`, we need to give it some information about the motors attached to the board. Each motor has three relevant pin connections: `pwm` (pulse-width modulation), `dir` (direction) and `cdir` (counter-direction). You can read more about this in the documentation for Johnny-Five\'s [`Motor`](http://johnny-five.io/api/motor/) class. The pin numbers correspond to how the pins on the motor driver are connected to the Tessel.

    language:javascript
    const rover = new Rover([
      // Left Motor
      ,
      // Right Motor
      ,
    ]);

Phew! Now the robot is ready to rock. A message is logged that says \"Reconbot(T2): Initialized\":

    language:javascript
    console.log("Reconbot(T2): Initialized");

##### Handling socket connection events

When you open the robot\'s controlling web page in a browser, it will trigger a `"connection"` event on the web socket. The `"connection"` handler logs a message confirming the connection and sets up an event handler for `"remote-control"` events. Remote control events are fired when new axis data is sent from the thumbstick controls. This axis data gets passed on to the `rover`.

    language:javascript
    socket.on("connection", connection => );
    });

That\'s it for hardware interaction control! The next few lines helpfully show the URL for your robot\'s controlling web page. Remember how we turned off default `SIGINT` handling? Here\'s where we circle back and define how we *do* want `SIGINT` events to be handled---making sure to close the web server before exiting the process.

    language:javascript
    listen.then(() => .local`);
      console.log(`http://$`);
      process.on("SIGINT", () => );
    });

### Deployment And Operation of the Robot

It\'s time to deploy and run the software on our robot---which also means it\'s time to drive!

Whenever you\'re ready, go ahead and type---or copy and paste---the following command into your terminal:

[t2 run index.js]

Once the program is deployed and started, you will see the URL of the controller application displayed:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/deployed.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/deployed.png)

Go ahead and open that URL in a browser on your mobile device or laptop. If **your friend** is positioned directly in front of the bot, you might see something like this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/pilot-eye-view-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/pilot-eye-view-03.jpg)

**Note:** The left and right arrows located in the upper corners will swap the virtual thumb stick from one side of the screen to other.

While they will see this:

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/3/7/person-eye-view-03.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/3/7/person-eye-view-03.jpg)