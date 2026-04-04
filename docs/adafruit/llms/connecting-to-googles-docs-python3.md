# Source: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/connecting-to-googles-docs-python3.md

# DHT Humidity Sensing on Raspberry Pi or Beaglebone Black with GDocs Logging

## Connecting to Google Docs

Danger: 

Danger: 

[RE: DHT 22 Temperature and Humidity sensor with adafruit code](https://forums.adafruit.com/viewtopic.php?f=19&t=53299&p=271580#p271310)

# Create and prepare spreadsheet

First up you will need to [sign up for Google Docs](http://sheets.google.com) and create a spreadsheet. We're going to call ours DHT Humidity Logs.  
  
Once you've created it, delete all but one line (since we don't want 1000 empty rows):

![](https://cdn-learn.adafruit.com/assets/assets/000/017/252/medium800/raspberry_pi_deleteros.gif?1448046998)

Then make the one remaining line a header with row names:

![](https://cdn-learn.adafruit.com/assets/assets/000/017/253/medium800/raspberry_pi_title.gif?1448046993)

# Get OAuth2 credentials

As of April 2015 Google has deprecated the older simple authentication interface for accessing Google spreadsheet data. &nbsp;You must carefully follow the steps below to enable OAuth2 access to your Google spreadsheet. &nbsp;Unfortunately these steps are somewhat complex, so go through them very carefully to make sure you don't miss a step. &nbsp;If you run into problems try consulting the [gspread python library](https://github.com/burnash/gspread)&nbsp;that this script uses.

To get your OAuth2 credentials follow the steps on this page:

- [gspread - Using OAuth2 for Authorization](http://gspread.readthedocs.org/en/latest/oauth2.html)

After you follow the steps in the document above you should have downloaded a .json file, like `SpreadsheetData-(gibberish).json`. &nbsp; **Place this .json file in the same directory as the `google_spreadsheet.py` example.** &nbsp;If you don't place this file in the same directory then authentication will fail and you will not be able to update your spreadsheet!

One last step that **must be completed** is to share your Google spreadsheet to the email address associated with the OAuth2 credentials. &nbsp;Open the .json file and search for the **"client\_email":** line that looks like this (but with a different email address):

```
"client_email": "149345334675-md0qff5f0kib41meu20f7d1habos3qcu@developer.gserviceaccount.com",
```

Take note of that email address value and go to your Google spreadsheet in a web browser. &nbsp;Using the **File -\> Share...** menu item share the spreadsheet with **read and write access** to the email address found above. &nbsp; **Make sure to share your spreadsheet or you will not be able to update it with the script!**

# Run Python Code
First up we will have to install the **gspread** python library, which will do the heavy lifting of connecting to google docs and updating the spreadsheet! With your board connected and online, run the following:  
```
sudo pip3 install gspread oauth2client pyasn1 pyasn1-modules
```

Create a new file called&nbsp; **google\_spreadsheet.py** &nbsp;with&nbsp; **nano** &nbsp;or your favorite text editor and put the following in:

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/DHT_Google_Spreadsheet/google_spreadsheet.py

Next, in the **examples** directory again, edit **google\_spreadsheet.py** and adjust the configuration values towards the top of the file:

```
# Type of sensor, can be adafruit_dht.DHT11 or adafruit_dht.DHT22.
# For the AM2302, use the adafruit_dht.DHT22 class.
DHT_TYPE = adafruit_dht.DHT22

# Example of sensor connected to Raspberry Pi Pin 23
DHT_PIN  = board.D4
# Example of sensor connected to Beaglebone Black Pin P8_11
# DHT_PIN  = 'P8_11'

# Google Docs OAuth credential JSON file.  Note that the process for authenticating
# ...
GDOCS_OAUTH_JSON       = 'your SpreadsheetData-*.json file name'

# Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 'your google docs spreadsheet name'
```

Make sure `DHT_TYPE` is set to the type of sensor you are using (either `adafruit_dht.DHT11`or`adafruit_dht.DHT22`), and `DHT_PIN` is set to the GPIO pin number which is connected to your DHT sensor. If you're using an&nbsp; **AM2302,&nbsp;** use the `adafruit_dht.DHT22` class.  
  
In the example above a Raspberry Pi GPIO pin #23 is shown, however commented below it is an example of a Beaglebone Black using GPIO pin P8\_11.  
  
Next make sure to set the **`GDOCS_OAUTH_JSON`&nbsp;** to the name of the `SpreadsheetData-*.json` file in the same directory as the `google_spreadsheet.py` file. &nbsp;If you don't have a `SpreadsheetData-*.json` file then you accidentally missed the steps above. &nbsp;**Go back and carefully follow the [OAuth2 credential steps](../../../../dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/connecting-to-googles-docs-updated#get-oauth2-credentials)&nbsp;to get an OAuth2 credential .json file before continuing!**  
  
Finally **set**  **`GDOCS_SPREADSHEET_NAME` to the name of your spreadsheet** , like '_DHT Humidity Logs_'.  
  
**Save the file** and **execute the Python script by running** :

> **python3 google\_spreadsheet.py**

You should see the program run and after about 30 seconds a humidity and temperature measurement is displayed and written to the spreadsheet. The program will continue to run and log a measurement every 30 seconds until you force it to quit by pressing `Ctrl-C`.   
  
The measurement frequency can be adjusted by changing the `FREQUENCY_SECONDS` configuration in the python code.  
  
Open the spreadsheet on Google's site and you should see measurements added in real time!

https://www.youtube.com/watch?v=Skr2uPZzviM

[You can also see our spreadsheet here, it wont be running live after Aug 24, 2012 but it gives you an idea of the data format](https://docs.google.com/spreadsheet/ccc?key=0AlwXpwqqd84DdFVobHFCWXZLU2l2V212WnFrS3QwdkE#gid=0)- [Previous Page](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup.md)

## Featured Products

### Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi

[Adafruit Assembled Pi Cobbler Breakout + Cable for Raspberry Pi](https://www.adafruit.com/product/914)
Now that you've finally got your hands on a [Raspberry Pi® Model B](http://www.raspberrypi.org/), you're probably itching to make some fun embedded computer projects with it. What you need is an add on prototyping Pi Cobbler from Adafruit, which can break out all those...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/914)
[Related Guides to the Product](https://learn.adafruit.com/products/914/guides)
### BeagleBone Black Rev C - 4GB Flash - Pre-installed Debian

[BeagleBone Black Rev C - 4GB Flash - Pre-installed Debian](https://www.adafruit.com/product/1876)
Note: As of May 12, 2014 Adafruit is shipping Rev C. We have discontinued selling Rev B. There are no exchanges or "upgrades" for Rev B to Rev C.  
  
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C still has a blistering 1GHz processor and 512MB onboard DDR3...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1876)
[Related Guides to the Product](https://learn.adafruit.com/products/1876/guides)
### BeagleBone Black - Rev B

[BeagleBone Black - Rev B](https://www.adafruit.com/product/1278)
**[Adafruit is no longer shipping the BeagleBone Black Rev B, it has been replaced with the Rev C as of 5/12/14](https://www.adafruit.com/products/1876) - the Rev C now has 4G flash and also comes with Debian, it also costs slightly more. There are no exchanges or...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/1278)
[Related Guides to the Product](https://learn.adafruit.com/products/1278/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### AM2302 (wired DHT22)  temperature-humidity sensor

[AM2302 (wired DHT22)  temperature-humidity sensor](https://www.adafruit.com/product/393)
Discontinued - [**you can grab** AM2301B - Wired Enclosed AHT20 - Temperature and Humidity Sensor&nbsp; **instead!**](https://www.adafruit.com/product/5181)

The AM2302 is a wired version of the [DHT22](http://www.adafruit.com/products/385), in a large plastic...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/393)
[Related Guides to the Product](https://learn.adafruit.com/products/393/guides)
### DHT11 basic temperature-humidity sensor + extras

[DHT11 basic temperature-humidity sensor + extras](https://www.adafruit.com/product/386)
 **Discontinued -**  **you can grab the&nbsp;** [DHT20 - AHT20 Pin Module - I2C Temperature and Humidity Sensor](https://www.adafruit.com/product/5183)&nbsp; **instead!&nbsp;**

The DHT11 is a basic, ultra low-cost digital temperature and humidity sensor. It uses...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/386)
[Related Guides to the Product](https://learn.adafruit.com/products/386/guides)
### DHT22  temperature-humidity sensor + extras

[DHT22  temperature-humidity sensor + extras](https://www.adafruit.com/product/385)
The DHT22 is a basic, low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air and spits out a digital signal on the data pin (no analog input pins needed). It's fairly simple to use but requires careful timing...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/385)
[Related Guides to the Product](https://learn.adafruit.com/products/385/guides)
### BeagleBone Black Rev C - 4GB - Pre-installed Debian

[BeagleBone Black Rev C - 4GB - Pre-installed Debian](https://www.adafruit.com/product/1996)
If you liked the BeagleBone Black Rev B, you will love the Rev C! The Rev C has a blistering 1GHz AM3358 processor and 512MB onboard DDR3 RAM, two 46-pin headers, micro HDMI for audio/video output, USB ports, 10/100 Ethernet and other I/O features. The Rev C is an ultra-powered embedded...

In Stock
[Buy Now](https://www.adafruit.com/product/1996)
[Related Guides to the Product](https://learn.adafruit.com/products/1996/guides)

## Related Guides

- [Freq Show: Raspberry Pi RTL-SDR Scanner](https://learn.adafruit.com/freq-show-raspberry-pi-rtl-sdr-scanner.md)
- [Adding a Real Time Clock to Raspberry Pi](https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi.md)
- [LED Backpack Displays on Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/led-backpack-displays-on-raspberry-pi-and-beaglebone-black.md)
- [Raspberry Pi SelfieBlock](https://learn.adafruit.com/selfieblock.md)
- [How Cold Is It?](https://learn.adafruit.com/how-cold-is-it.md)
- [Bluetooth Temperature & Humidity Sensor](https://learn.adafruit.com/bluetooth-temperature-and-humidity-sensor.md)
- [Introducing the Raspberry Pi 2 - Model B](https://learn.adafruit.com/introducing-the-raspberry-pi-2-model-b.md)
- [Send Raspberry Pi Data to COSM](https://learn.adafruit.com/send-raspberry-pi-data-to-cosm.md)
- [Adafruit HTS221 - Temperature & Humidity Sensor](https://learn.adafruit.com/adafruit-hts221-temperature-humidity-sensor.md)
- [Using Piezo Buzzers with WipperSnapper](https://learn.adafruit.com/using-piezo-buzzers-with-wippersnapper.md)
- [Using Melexis MLX90614 Non-Contact Sensors](https://learn.adafruit.com/using-melexis-mlx90614-non-contact-sensors.md)
- [reef-pi Guide 2: Power Controller](https://learn.adafruit.com/reef-pi-power-controller.md)
- [Adafruit Pi Box Plus](https://learn.adafruit.com/adafruit-pi-box-plus.md)
- [Capacitive Touch Sensors on the Raspberry Pi](https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi.md)
- [Adafruit Si7021 Temperature + Humidity Sensor](https://learn.adafruit.com/adafruit-si7021-temperature-plus-humidity-sensor.md)
