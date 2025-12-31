# Source: https://learn.sparkfun.com/tutorials/sunrise-machine-with-the-tessel-2

## Introduction

Some time ago, I began to have a hankering to be able to automatically photograph or film the sunrise wherever I may happen to be. I liked the idea of a little machine that could determine when the sun would rise in my location and take some time lapse images of it. Thus was born the idea of a Sunrise Machine.

The Sunrise Machine can, based on your latitude and longitude, automatically record the sunrise at your location using a basic USB webcam. It captures still images over time and creates time-lapse movies from them in MPEG-4 and animated-GIF formats. If you choose, it can also tweet those resulting GIFs on your behalf. You can configure it to record different day-sun events---sunset, solar noon, the start of the golden hour, even nautical twilight. You don\'t have to tweet the results, if that\'s not your thing, and you can always create a manual time-lapse video at any time by pressing a button. All still images and videos are stored for you on a USB thumb drive.

[![The Sunrise Machine](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/0/sunrise-machine.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/0/sunrise-machine.jpg)

I built an enclosure for my Sunrise Machine out of an old book. However, you can put yours in whatever you like, or not bother with an enclosure at all.

[![The Sunrise Machine open](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/0/sunrise-machine-inside.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/0/sunrise-machine-inside.jpg)

## Preflight Check

If this is your first time experimenting with the [Tessel 2](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/about-the-tessel-2), there are a few things you should be familiar with first! We recommend reading through our [Getting Started with the Tessel 2](https://learn.sparkfun.com/tutorials/getting-started-with-the-tessel-2) guide before diving into this project.

[](https://learn.sparkfun.com/tutorials/getting-started-with-the-tessel-2)

### Getting Started with the Tessel 2 

October 12, 2016

Get your Tessel 2 up and running by blinking and LED, the Hello World of embedded electronics.

### Dive Deeper into the Tessel 2

The entire [Johnny-Five Inventor\'s Kit Experiment Guide](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit) is full of great information if you\'re starting out with the Tessel 2. Pertinent experiments for this tutorial include [Experiment 4: Reading a Push Button](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-4-reading-a-push-button) and [Experiment 8: Driving an RGB LED](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit/experiment-8-driving-an-rgb-led).

[](https://learn.sparkfun.com/tutorials/experiment-guide-for-the-johnny-five-inventors-kit)

### Experiment Guide for the Johnny-Five Inventor\'s Kit 

June 28, 2016

Use the Tessel 2 and the Johnny Five Inventors kit to explore the world of JavaScript enabled hardware through 14 awesome experiments!

## Materials

The Johnny-Five Inventor\'s Kit includes most of the electronic components you need to build the Sunrise Machine.

[![Johnny-Five Inventor\'s Kit](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/4/5/3/13847-01.jpg)](https://www.sparkfun.com/products/13847)

### [Johnny-Five Inventor\'s Kit](https://www.sparkfun.com/products/13847) 

[ KIT-13847 ]

The Johnny-Five Inventor\'s Kit (J5IK) is your go-to source for developing projects using the Tessel 2 and the Johnny-Five pro...

**Retired**

In addition to the items in the kit, you\'ll need a USB camera, such as the [Creative Live! Cam Chat HD (Amazon)](https://www.amazon.com/dp/B004431UBM/ref=pd_lpo_sbs_dp_ss_2?pf_rd_p=1944687662&pf_rd_s=lpo-top-stripe-1&pf_rd_t=201&pf_rd_i=B0092QJRPC&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=6PXCKBP9WH670G3JXZ26), and a USB thumb drive.

If you do not have a Johnny-Five Inventor\'s Kit or would rather purchase the parts you\'ll need for this project separately, you can do so using the lists below:

#### Addition Supplies

- 1 USB thumb drive or [SD Card with USB Adaptor](https://www.sparkfun.com/products/11609)
- 1 [USB camera](https://www.sparkfun.com/products/13873)

## Setup

[![Twitter Logo](http://espp16.wp.st-andrews.ac.uk/files/2016/07/Twitter-Logo.png)](http://espp16.wp.st-andrews.ac.uk/files/2016/07/Twitter-Logo.png)

If you\'d like your Sunrise Machine to be able to tweet, you\'ll need to [obtain Twitter API credentials](https://apps.twitter.com/). You\'ll have to fill out a little form, but the use of the API is free. Once you\'re signed up, you\'ll have access to an API/developer dashboard. You\'ll need to find the following four things to make your Sunrise Machine talk to Twitter:

- Consumer Key
- Consumer Secret
- Access Token (Key)
- Access Token (Secret)

Access Token (Key) and Access Token (Secret) may need to be generated (you just to have to click a button to do it). Each of the four credentials are long strings. Copy and paste them somewhere safe.

For my Sunrise Machine, I created an entirely new Twitter user, but you can use your main Twitter account if you prefer. Or, if Twitter isn\'t your thing, you can disable it completely with a configuration value (more on that soon).

### Webcams and Calibration

In the course of building the Sunrise Machine, I discovered that some webcams require a period of \"warmup\" before capturing stills so that they can calibrate the correct exposure. This usually takes 2-3 seconds. Without calibration \"warmup\", images taken of bright scenes---like outside---would result in all-white images. Yikes! The Sunrise Machine\'s software can automatically calibrate your webcam before capturing images to help you get the best images possible. You can disable this feature if you like (see the configuration section below).

### USB and the Tessel

Working with a USB thumb drive and USB camera on a Tessel is eerily easy.

For the thumb drive: make sure it is formatted as Fat32 or something similar (MS-DOS FAT, ExFat---*not* Mac OS Extended). The Sunrise Machine will write files (images, movies and GIFs) directly to your thumb drive. If you\'re curious, a mounted USB thumb drive can be accessed at `/mnt/sda1` on the Tessel\'s file system. Use the `t2 root` command if you want to `ssh` in to your Tessel and have a look around the filesystem---the Tessel 2 runs OpenWRT Linux.

Similarly, plugging in a USB webcam to a Tessel makes the device available at `/dev/video0`.

### The Tessel and Time

The Tessel 2 isn\'t an independent timekeeper. Once the Tessel has power and its OpenWRT Linux boots, it will attempt to connect to an NTP (Network Time Protocol) server to obtain the current time. There are a couple of things to note about this. One, dates and times on the Tessel are UTC times---it doesn\'t know about your local timezone. Second, the Tessel can\'t tell what time it is at all if it does not have a network connection (i.e. if it\'s only tethered to your computer over USB but is not connected to your LAN).

The command `t2 list` will show you all nearby Tessels and how they are connected, e.g. for my Tessel, which I\'ve named *ichabod* after a local early settler of my town named, improbably, Ichabod Onion:

    $ t2 list
    INFO Searching for nearby Tessels...
        USB ichabod
        LAN ichabod

*ichabod* is, in this case, connected both to my USB port and my local WiFi network. Good. It\'ll know what time it is. In UTC, at least.

## Build It

Now you\'re ready to put your Sunrise Machine\'s components together.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/5/6/0/sunriseMachine.png)](https://cdn.sparkfun.com/assets/learn_tutorials/5/6/0/sunriseMachine.png)

1.  Plug in a USB thumb drive to one of the Tessel 2\'s USB ports.
2.  Plug in a USB webcam to the other USB port on the Tessel 2.
3.  Wire up the circuit containing a pushbutton and an RGB LED as shown in the wiring diagram.

## Program It

### Get the Software

If you have git installed and feel comfortable using that tool, open your terminal and run:

[git clone https://github.com/bocoup/j5ik-sunrise-machine; ]\
[cd j5ik-sunrise machine;]\
[npm install;]

If `git` is not your thing, you can also download the project as a zip file:

[Sunrise Machine Project Folder](https://github.com/bocoup/j5ik-sunrise-machine/archive/master.zip)

You can always find the most up to date content at in the [GitHub repository](https://github.com/bocoup/j5ik-sunrise-machine) as well.

Extract the contents however you prefer. Open your terminal, and navigate to the extracted project directory.

### Install the Software

First, install some dependencies. In your project directory, run the command:

[npm install]

#### Configuration: `config.js`

The only code changes you\'ll *need* to make from the supplied code with the Sunrise Machine are in its configuration. Copy the included `config.js.example` file to a new file named `config.js`:

    language:javascript
    module.exports = ;

This configuration object is organized such that the properties you\'re most likely to change are near the top.

- You\'ll want to change, at the very least, the **`lat` and `long` values** to the coordinates of [where you are located](http://www.latlong.net/).
- To account for the Tessel 2\'s proclivity for UTC, you can provide a `utcOffset` value. `-04:00` is the offset for daylight savings time on the east coast of the U.S. (EDT)---four hours \"behind\" UTC. This setting isn\'t critical---the dates used by the Tessel to figure out to record will still be accurate, but if you want logging and folder names for your images and movies to use your local time zone (i.e. not UTC), change this value.
- `autoSchedule` can be set to any of [suncalc\'s sun event names](https://github.com/mourner/suncalc#sunlight-times), or can be set to `false` to disable scheduled recording (you can always trigger manual movies by pressing the Sunrise Machine\'s pushbutton).
- If you enable `postToTwitter`, you\'ll need to fill in the Twitter API credentials that follow.
- I encourage you to experiment with the value of `calibrateCamera`. If you find that your camera is taking great stills without calibration, you can save power and time by disabling calibration (set this property to `0` or `false` to turn it off).
- You can disable the `statusLED` if you like. This can save power and your nerves if you find the light or blinking annoying (or it is reflecting off a window during capture or something).

At this point, your Sunrise Machine is configured and ready. If you\'re in a hurry, you can skip to the [Run It!](#run-it) section.

### Exploring the Code

When the Sunrise Machine\'s code is complete, your project directory will look like this:

    language:console
    ├── av.js
    ├── config.js
    ├── node_modules
    ├── recording.js
    ├── index.js
    └── tweet.js

`config.js` is the configuration file you just created. `node_modules` is where the project\'s dependencies---installed above---live.

The other components of the Sunrise Machine are:

- `tweet.js`, which integrates with the Twitter API and can upload animated GIFs
- `recording.js`, which provides a class that encapsulates the tasks of a time-lapse recording session (scheduling still capture, kicking off the processing of stills into movies, etc.)
- `av.js`, which contains lower-level code to execute the capture and processing of images and video
- `index.js`, which is the code that controls the Tessel\'s inputs and outputs and pulls it all together. This is the script you\'ll run on your Tessel.

We encourage you to dig into the module files and see how the pieces all fit together, if you\'re curious!

### Capturing and Processing Video with the Tessel 2: av.js

The image capture, video building and animated-GIF creating powers of the Sunrise Machine are significantly influenced by the existing [`tessel-av`](https://github.com/tessel/tessel-av) module, which is a great starting place for grabbing still images or streaming video. Like `tessel-av`, the Sunrise Machine\'s image-capture code takes advantage of the cross-platform [`ffmpeg` software](https://ffmpeg.org/), which is available for you already on your Tessel. No installation or configuration needed!

`ffmpeg` is a hugely-powerful command-line tool that can encode and decode (and transcode and mux and demux and stream and filter and play and and and) a dizzying array of different kinds of audio and video. Just learning how to put together commands to do simple video capture and storage can take a while (trust me).

Keep in mind that the Tessel 2 is able to do all this despite its mere *64MB of RAM*. It\'s quite a trooper.

`av.js` spawns `ffmpeg` processes using Node.js\' built-in `child_process` module. The `av` module contains an appropriately-titled `ffmpeg` function. The `ffmpeg` function spawns an `ffmpeg` child process with the arguments provided and returns a `Promise`:

    language:javascript
    function ffmpeg (opts)  else 
        });
        ffmpegProcess.stderr.on('data', data => );
      });
    }

Each of the four exported functions (`calibrate`, `captureStill`, `videoFromStills` and `animatedGIFFromVideo`) are intended to fulfill one AV task by invoking the `ffmpeg` function with the needed arguments. These functions also return a Promise. Here\'s a condensed view of the rest of the `av.js` module:

    language:javascript
    // "Calibrate" a camera for `duration` seconds by letting it output to /dev/null
    module.exports.calibrate = function (duration) ;

    // Capture a single still image at 320x240 from the attached USB camera
    module.exports.captureStill = function (filepath) ;

    // Build an MP4 video from a collection of JPGs indicated by `glob`
    module.exports.videoFromStills = function (glob, outfile) ;

    // Create an animated GIF from an MP4 video. First, generate a palette.
    module.exports.animatedGIFFromVideo = function (videofile, outfile) );
    };

Arguments are cobbled together in each function. Here\'s the entirety of the `captureStill` function, for instance:

    language:javascript
    // Capture a single still image at 320x240 from the attached USB camera
    module.exports.captureStill = function (filepath) ;

Note that the `animatedGIFFromVideo` function is a two-step process that first creates a palette from a movie and subsequently creates an animated GIF from the movie based on that palette. GIFs are restricted to 256 colors, so using an intelligently-generated palette can result in a higher-quality GIF.

### Tweeting Animated GIFS: tweet.js

`tweet.js` uses the `twitter` `npm` package to communicate with the Twitter API, making the several API calls necessary to upload an animated GIF. Once the GIF is uploaded, it posts a tweet containing the GIF. It exports a function, `tweetGIF`--- `index.js` can call this function to tweet a GIF.

### Taking Care of Details: recording.js

The JavaScript `class` exported by `recording.js`, `Recording`, encapsulates some of the tasks of managing a time-lapse recording session, like naming of files and managing timeouts between captures. A `Recording` instance can be started with its `start` method and canceled with its `cancel` method. The `Recording` handles the rest, invoking specific functions in the `av` module to accomplish tasks like calibration, capturing stills and building movies and GIFs.

### Where it all Happens: index.js

We\'ve met the supporting cast. Now let\'s walk through, in entirety, `index.js`, which is the script you\'ll run directly on your Tessel to make the Sunrise Machine go! Here it is, with lots of comments.

    language:javascript
    /* require external dependencies */
    const five      = require('johnny-five'); // Johnny-Five!
    const Tessel    = require('tessel-io'); // J5 I/O plugin for Tessel boards
    const suncalc   = require('suncalc'); // For calculating sunrise/set, etc., times
    const Moment    = require('moment'); // For wrangling Dates because otherwise ugh
    // Require other modules from sunriseMachine's code:
    const config    = require('./config');
    const Recording = require('./recording');
    const tweetGIF  = require('./tweet');

    // Instantiate a new `Board` object for the Tessel
    const board = new five.Board();

    // Instantiate some variables for later
    var currentRecording, scheduled;

    board.on('ready', () => 

      // button `press` callback. Start a manual recording, or cancel an in-progress recording
      function toggle ()  else 
      }

      function schedule () 
        const eventName    = config.autoSchedule;
        const now          = Moment();
        // Using noon explicitly when querying about sun events adds a level
        // of safety; using times near the start or end of the day can kick up
        // some unexpected results sometimes.
        const noonToday    = Moment().hour(12).minute(0);
        const noonTomorrow = Moment().add(1, 'days').hour(12).minute(0);

        // Ask `suncalc` for the times of various sun events today, at the
        // lat/long defined in the config
        var sunEvents = suncalc.getTimes(noonToday.valueOf(),
          config.lat, config.long);
        var eventDate, delta;

        if (!sunEvents.hasOwnProperty(eventName))  is not a known suncalc event`;
        }

        if (sunEvents[eventName].getTime() < now.valueOf()) 

        // Using the config.utcOffset value to bring the date into local timezone
        // Note that the actual date underneath is not changing, just its representation
        eventDate = Moment(sunEvents[eventName]).utcOffset(config.utcOffset);
        // How long is the event from now, in milliseconds?
        delta = eventDate - now;
        if (!scheduled)  recording`); // Kick off a recording
            scheduled = null; // Unset scheduled because we're done here
          }, delta);
        }
        return `Scheduled for $: $`;
      }

      // Kick off a time-lapse recording!
      function record (name) 
        // Create a new Recording object to do some heavy lifting for us
        const recording = new Recording(name, config);
        // Bind to a bunch of events on the Recording. Several of these update
        // the SM's status and/or log a message:
        recording.once('start', () =>  starting`);
        });
        recording.on('calibrate', () => setStatus('calibrating'));
        recording.on('capture:start', () => setStatus('capturing'));
        recording.once('cancel', () => log(`$ canceled`));

        // When one of the stills in a session is successfully captured, take note!
        recording.on('capture:done',  (filepath, images, totalnum) =>  of $`);
        });
        // When the stills are captured and the movies made, Tweet the result
        // if config indicates it should be done
        recording.once('done', videoFile => 
          log(`$ complete`);
        });
        // Once the Recording exits, put the SM back in standby (this will
        // cause the next recording to get scheduled, if needed)
        recording.once('exit', standBy);

        // Start the recording!
        recording.start();

        // Reference this Recording as the SM's currentRecording
        currentRecording = recording;
        return recording;
      }

      // Indicate the sunrise machine's "status" by changing the state of the
      // RGB LED and optionally logging a message
      function setStatus (status, msg) 
        if (msg) 
      }

      // This log function could be altered to log to a file, e.g.
      function log (msg) :
          $`);
      }
    });

## Run it

Run the sunrise machine by using the following command:

[ t2 run index.js]

That will deploy the `index.js` code and all of its needed dependencies to your Tessel.