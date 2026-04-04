# Source: https://learn.adafruit.com/pi-thermal-printer/pi-setup-part-3.md

# Internet of Things Printer for Raspberry Pi

## Raspberry Pi Setup: 3 of 3

# Install Adafruit Code
Connect the power cable to boot the system. Negotiating a wireless connection will take a moment, so wait about a minute before trying to access the system using SSH.

Once logged in, install the Adafruit thermal printer library and example code:

```
git clone https://github.com/adafruit/Python-Thermal-Printer
```

Make sure a roll of paper is installed in the printer and the top is securely latched. Then we’ll test all the basic functionality:

```
cd Python-Thermal-Printer
python printertest.py
```

This should progress through different text sizes, styles and formats, as well as barcodes and images.

If this does <u>not</u> work, the most likely culprits are:

- One of the prerequisite Python libraries is not installed (serial, imaging, unidecode) — explained in Raspberry Pi Setup Part 2 of 3.
- The serial port has not been properly disengaged for application use — also explained in Raspberry Pi Setup Part 2 of 3.
- Wrong connection between printer and Raspberry Pi — explained in Assembly.  

The first two will likely give an informative error response. The latter will just produce no results. # Configure the Weather Scripts
Before running the weather scripts, you must create another developer account in order to use the DarkSky weather API.

Go to [https://darksky.net/dev/](https://darksky.net/dev/)&nbsp;and sign up for an account.

Get your API secret key, and go ahead and modify the following line in **forecast.py** and **timetemp.py**

```
API_KEY = "YOUR_API_KEY"
```

Save the changes, then run the script again:

```
python forecast.py
```

This should now print the current weather and the forecast for NYC, the default location. Change the latitude and longitude variables too to reflect the location you'd like to get the weather for. I use[NASA's site](https://mynasadata.larc.nasa.gov/latitudelongitude-finder/)

If this works, also edit the file **timetemp.py** and make the same change there. This is a different script that prints the current time and local weather conditions.

# Configure the Twitter Script
As written, the sketch will search for Tweets originating from Adafruit, but you can change this to any search string supported by the Twitter SearchAPI. FIrst step though is to set up authentication…

```
      nano twitter.py
    
```

Look for this section of code:

```
# Twitter application credentials -- see notes above -- DO NOT SHARE.
consumer_key    = 'PUT_YOUR_CONSUMER_KEY_HERE'
consumer_secret = 'PUT_YOUR_CONSUMER_SECRET_HERE'
```

Copy the Consumer key and Consumer secret strings from the Twitter application page into the corresponding spots, keeping the quotes around them.  
  
Just below this is the search term. You can change Adafruit to any other valid Twitter account.

```
queryString = 'from:Adafruit'
```

Different search types are possible, such as by tag. Refer to the SEARCH OPERATORS section of the [Twitter Developers Documentation](https://dev.twitter.com/docs/using-search "Link: https://dev.twitter.com/docs/using-search") for guidance.  
  
Any search string used by the “Gutenbird” sketch for the original Internet of Things Printer can also be used here.

# Test the Main Script
The “main” script starts by printing a greeting image, performs once-daily actions (weather forecast and Sudoku puzzle), then goes into Twitter-monitoring mode.

```
sudo python main.py
```

The “main” script <u>must</u> be run as root (i.e. using “ **sudo** ”) because it directly accesses hardware — the GPIO pins for the button and LED.  
  
**It may take a few minutes to run!**

Each morning at 6:30 am, the once-daily actions are performed again. You can change this time (or the actions) by editing the main.py script.  
Press control+C to stop the program. We’ll set it up to run automatically when the printer is turned on…

![](https://cdn-learn.adafruit.com/assets/assets/000/004/403/medium800/raspberry_pi_sudoku.jpg?1396811978)

# Configure Auto-Start
With the software now tested “manually,” let’s make it start automatically upon booting:

```
sudo nano /etc/rc.local
```

Before the final “exit 0” line, add these two lines:

```
cd /home/pi/Python-Thermal-Printer
python main.py &amp;
```

If you downloaded or otherwise placed the printer software in a different location, the first line should be changed accordingly. “sudo” isn’t necessary here because the rc.local script is already run as root.  
  
Reboot the system to test the startup function:

```
sudo reboot
```

After 30 seconds to a minute, you should see the status light come on. After another 30 seconds, the greeting image should be printed, then the “once daily” functions. After that, the printer will go into Twitter-monitoring mode.

# Regular Operation
When the printer is idle, tap the button for the current time and local weather conditions.  
  
Hold the button down to initiate an orderly shutdown. This is always a good idea — you don’t want to just pull the plug on most Linux systems. There may be many files open at any given time, and this gives the system a chance to put things in order.

- [Previous Page](https://learn.adafruit.com/pi-thermal-printer/twitter-setup.md)
- [Next Page](https://learn.adafruit.com/pi-thermal-printer/troubleshooting.md)

## Primary Products

### Adafruit IoT Pi Printer Project Pack

[Adafruit IoT Pi Printer Project Pack](https://www.adafruit.com/product/1289)
Build an "Internet of Things" connected mini printer that will do your bidding! This is a fun weekend project that comes with a beautiful laser cut case. Once assembled, the little printer connects wirelessly to get Internet data for printing onto 2 1/4" wide receipt paper....

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1289)
[Related Guides to the Product](https://learn.adafruit.com/products/1289/guides)

## Featured Products

### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### Raspberry Pi - Skill badge, iron-on patch

[Raspberry Pi - Skill badge, iron-on patch](https://www.adafruit.com/product/906)
You are learning to use the small Linux based board, the Raspberry Pi! Adafruit offers a fun and exciting "badges" of achievement for electronics, science and engineering. We believe everyone should be able to be rewarded for learning a useful skill, a badge is just one of the many...

In Stock
[Buy Now](https://www.adafruit.com/product/906)
[Related Guides to the Product](https://learn.adafruit.com/products/906/guides)
### Adafruit Pi Unassembled T-Cobbler Breakout Kit for Raspberry Pi

[Adafruit Pi Unassembled T-Cobbler Breakout Kit for Raspberry Pi](https://www.adafruit.com/product/1105)
Now that you've finally got your hands on a [Raspberry Pi®](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi T-Cobbler from Adafruit, which can break out all those tasty...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1105)
[Related Guides to the Product](https://learn.adafruit.com/products/1105/guides)
### Mini Thermal Receipt Printer Starter Pack

[Mini Thermal Receipt Printer Starter Pack](https://www.adafruit.com/product/600)
Hit the ground running (and printing!) with this starter pack that includes a thermal printer and all the extras and save a few dollars while you're at it.  
  
Includes:

- [A mini thermal receipt printer](http://www.adafruit.com/products/597) - with cables and...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/600)
[Related Guides to the Product](https://learn.adafruit.com/products/600/guides)
### Thermal paper roll - 50' long, 2.25" wide

[Thermal paper roll - 50' long, 2.25" wide](https://www.adafruit.com/product/599)
A mini roll of thermal paper, this fits very nicely into our mini thermal printer. 2.25" wide (about 57mm) and 50 feet long (15 meters). BPA-free.  
  
[Perfect for use with our mini thermal printer!](http://www.adafruit.com/products/597)

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/599)
[Related Guides to the Product](https://learn.adafruit.com/products/599/guides)
### Mini Thermal Receipt Printer

[Mini Thermal Receipt Printer](https://www.adafruit.com/product/597)
Add a mini printer to any microcontroller project with this very cute thermal printer. Thermal printers are also known as receipt printers, they're what you get when you go to the ATM or grocery store. Now you can embed a little printer of your own into an enclosure. This printer is ideal...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/597)
[Related Guides to the Product](https://learn.adafruit.com/products/597/guides)
### Rugged Metal Pushbutton with White LED Ring

[Rugged Metal Pushbutton with White LED Ring](https://www.adafruit.com/product/558)
These chrome-plated metal buttons are rugged&nbsp;and look real good while doing it! Simply drill a 16mm hole into any material up to 1/2" thick and you can fit these in place, there's even a rubber gasket to keep water out of the enclosure. On the front of the button is a flat metal...

In Stock
[Buy Now](https://www.adafruit.com/product/558)
[Related Guides to the Product](https://learn.adafruit.com/products/558/guides)
### 5V 10A switching power supply

[5V 10A switching power supply](https://www.adafruit.com/product/658)
This is a beefy switching supply, for when you need a lot of power! It can supply 5V DC up to 10 Amps, running from 110V or 220V power (the plug it comes with is for US/Canada/Japan but you can use any plug adapter for your country, or just replace the cable with a standard computer/appliance...

In Stock
[Buy Now](https://www.adafruit.com/product/658)
[Related Guides to the Product](https://learn.adafruit.com/products/658/guides)

## Related Guides

- [Skill Badge Requirements: Raspberry Pi](https://learn.adafruit.com/skill-badge-requirements-raspberry-pi.md)
- [Adafruit Prototyping Pi Plate](https://learn.adafruit.com/adafruit-prototyping-pi-plate.md)
- [Adafruit Raspberry Pi Educational Linux Distro](https://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro.md)
- [Open Source Protective Face Shield Designs](https://learn.adafruit.com/open-source-face-shield-designs.md)
- [PyPortal IoT Plant Monitor with Google Cloud IoT Core and CircuitPython](https://learn.adafruit.com/pyportal-iot-plant-monitor-with-google-cloud-iot-core-and-circuitpython.md)
- [Adafruit QT Py ESP32-C3 WiFi Dev Board](https://learn.adafruit.com/adafruit-qt-py-esp32-c3-wifi-dev-board.md)
- [AstroPrint 3D Printing](https://learn.adafruit.com/astroprint-3d-printing.md)
- [No-Code Rain Sensing Smart Desktop Umbrella Stand](https://learn.adafruit.com/no-code-rain-sensing-smart-desktop-umbrella-stand.md)
- [MacroPad Remote Procedure Calls over USB to Control Home Assistant](https://learn.adafruit.com/macropad-remote-procedure-calls-over-usb-to-control-home-assistant.md)
- [PiPhone - A Raspberry Pi based Cellphone](https://learn.adafruit.com/piphone-a-raspberry-pi-based-cellphone.md)
- [Adafruit 128x64 OLED Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi.md)
- [Set up and Blink - MATLAB and Simulink with Raspberry Pi](https://learn.adafruit.com/how-to-use-matlab-and-simulink-with-raspberry-pi.md)
- [Mini Raspberry Pi Handheld Notebook](https://learn.adafruit.com/mini-raspberry-pi-handheld-notebook-palmtop.md)
- [Adafruit's Raspberry Pi Lesson 2. First Time Configuration](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration.md)
- [Huzzah Weather Display](https://learn.adafruit.com/huzzah-weather-display.md)
