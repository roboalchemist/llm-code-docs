# Source: https://docs.edgeimpulse.com/projects/expert-network/bluetooth-fall-detection-arduino-nano-33.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bluetooth Fall Detection - Arduino Nano 33 BLE Sense

Created By: Roni Bandini

Public Project Link: [https://studio.edgeimpulse.com/public/130968/latest](https://studio.edgeimpulse.com/public/130968/latest)

## Project Demo

<iframe src="https://www.youtube.com/embed/bM0FFCcvyPQ" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/bt-fall-detection/intro.jpg?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=2bc49d82dc65c1b1b8b2c4c36207d1e4" width="750" height="1000" data-path=".assets/images/bt-fall-detection/intro.jpg" />
</Frame>

## Intro

A fall could be dangerous in any situation, but for certain working scenarios, consequences can be very harmful. Therefore, the idea of developing a Machine Learning fall detection and reporting system could be quite useful in some industries.

## How Does it Work?

Each worker has a small TinyML device in charge of detecting falls via the onboard accelerometer data, and reporting to a server through Bluetooth. The server is a Raspberry Pi running a Python script that scans specific BT announcements, parses the fall alert information, and stores it into a SQL Lite database for reports and alerts.

## Client Devices

The electronics part of the client build is easy: just a battery, a TP4056 and the Arduino Nano 33 BLE Sense. The board has an onboard accelerometer, onboard RGB led, and enough processing power to run an Edge Impulse library for inferencing locally.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/bt-fall-detection/diagram.jpg?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=7698ac2b0845f503b62e50b0ceb56a2f" width="1035" height="630" data-path=".assets/images/bt-fall-detection/diagram.jpg" />
</Frame>

To add install Edge Impulse Firmware on the Nano 33, simply download the firmware from this link [https://cdn.edgeimpulse.com/firmware/arduino-nano-33-ble-sense.zip](https://cdn.edgeimpulse.com/firmware/arduino-nano-33-ble-sense.zip). Unzip the contents, connect the Arduino to your computer with a microUSB cable, double-click the Reset button on the Arduino, and run `flash_window.bat` from inside the folder (or the Mac or Linux commands if you are on one of those platforms).

If you want to train your own fall model, go to the Edge Impulse Studio and log in, click on Data Acquisition, WebUSB, and choose the Inertial sensor. Obtain 5 minutes of data; Standing normally and Falling Down samples.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/bt-fall-detection/training.jpg?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=545f34990495d915857631a7ca7ef602" width="1014" height="543" data-path=".assets/images/bt-fall-detection/training.jpg" />
</Frame>

Design an Impulse with a 1500ms window size, 150ms window increase, and 100HZ frequency. Add Spectral Analysis with just 3 axis: accx, accy, accz. Choose Keras classification and 2 output features: Stand and Fall. For the Neural Network training, 50 training cycles with a 0.0005 learning rate, Autobalance the dataset, and 20% validation worked fine.

After model testing, go to the Deployment page and export an Arduino Library (which will contain your Machine Learning Model). Then import this library (Zip file) inside the Arduino IDE Sketch by selecting Include, Add Zip.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/bt-fall-detection/device.jpg?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=71615a5e20c73a6fc3e98281efc7f2d9" width="536" height="388" data-path=".assets/images/bt-fall-detection/device.jpg" />
</Frame>

Once running, every fall is advertised with this format:

`advertiseFall("Fall-"+worker+"-"+String(myCounter));`

For example: **Fall-Smith-1922**

The device will change it's RGB LED from green to red, whenever a fall is detected.

All of the code for this project, including both the Client script file and the Python server files can be downloaded from [this Github link](https://github.com/ronibandini/BTFall).

## Client 3D Printed Case

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/bt-fall-detection/3d-case.jpg?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=df3c74d60d49a12a422c09f11d8d41c2" width="800" height="556" data-path=".assets/images/bt-fall-detection/3d-case.jpg" />
</Frame>

The device will work without a case of course, but, to make it more convenient to wear and to hold all the pieces in place, two parts should be 3D printed and a strap should be attached. The Gcode files for this particular design can be [downloaded here](https://www.thingiverse.com/thing:5478745).

## Server Setup

The other component we need to build next is the Python and database server, listening for bluetooth data coming from the Arduino. A Raspberry Pi will run the code fine, so, simply install Raspberry Pi OS Lite on an SD Card, boot up, and upload the Python files linked above from the GitHub repo.

Next, create a database structure with:

`$ sudo python3 databaseSetup.py`

Start scanning for bluetooth packets from the Arduino with:

`$ sudo python3 scan.py`

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/bt-fall-detection/server-setup.jpg?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=e2a2d55ea297ba0ed4e268eedc76e298" width="800" height="403" data-path=".assets/images/bt-fall-detection/server-setup.jpg" />
</Frame>

Other scripts included are: `clearDatabase.py` (removes all database records), and `chart.py` (creates a chart rendered from all of the database records).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/bt-fall-detection/fall-report.jpg?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=3fca54b1bcff4ac5d4e29e8f67e9933d" width="674" height="504" data-path=".assets/images/bt-fall-detection/fall-report.jpg" />
</Frame>

## Conclusion

In this project, we have demonstrated a simple method for Fall Detection using a client / server system running on an Arduino Nano 33 BLE Sense turned into a wearable device, along with a listening server running on a Raspberry Pi.


Built with [Mintlify](https://mintlify.com).