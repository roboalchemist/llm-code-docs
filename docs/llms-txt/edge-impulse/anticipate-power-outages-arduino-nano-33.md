# Source: https://docs.edgeimpulse.com/projects/expert-network/anticipate-power-outages-arduino-nano-33.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Anticipate Power Outages with Machine Learning - Arduino Nano 33 BLE Sense

Created By: Roni Bandini

Public Project Link: [https://studio.edgeimpulse.com/public/90995/latest](https://studio.edgeimpulse.com/public/90995/latest)

<Frame caption="EdenOff: Anticipate power outages with Machine Learning">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edenoff/edenoff-header.jpg?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=e3baec9befc908153ae12777ebdf502f" width="936" height="702" data-path=".assets/images/edenoff/edenoff-header.jpg" />
</Frame>

## Our Story

<Frame caption="Edenoff TinyML device">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edenoff/edenoff-device.jpg?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=3bd779523cd8dc35c386f818a81b8b5c" width="628" height="836" data-path=".assets/images/edenoff/edenoff-device.jpg" />
</Frame>

With power outages normally occurring in Argentina and other regions of Latin America, we ask the question, “Can a tiny Arduino device placed inside a power outlet anticipate outages using Machine Learning?” On one hand, the Argentinian government says power outages occur due to a lack of private infrastructure investment. On the other, electricity distributors in the area argue that non-discriminated subsidized rates and inadequate regulations are the cause of the power outages. In one case or the other, private companies' production and equipment, which are not easy to replace or import in Argentina, suffer.

Can we apply Machine Learning to power outages?

This question was the starting point for this project named EdenOff, named after Edenor; one of two power distributors in Buenos Aires.

What variables could be forwarded to a Machine Learning model to anticipate a power cut? Our answer: temperature. From December through February, there are challenging months in Argentina with peaks of temperature reaching 104 degrees Fahrenheit / 40 degrees celsius resulting in intensive use of air conditioning (AC). Below, Figure 3 depicts the average temperatures in Argentina in these months.

<Frame caption="Med Temp Per Month in Celsius">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edenoff/med-temp.jpg?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=36f39ec79eb01a7d76d7f65772587b40" width="936" height="538" data-path=".assets/images/edenoff/med-temp.jpg" />
</Frame>

Another relevant variable is AC reading. AC outlets should be stable at 220 Volts and significant variations usually means trouble.

One of many interesting things about Machine Learning is that we don’t have to determine rules in advance like in standard algorithm based code:

```
if (temperature>X & ACvariation>Y) {alarm=on;}
```

We can just use historical data to train a model and make inferences. That model could be placed into a cheap single-board microcontroller without even an internet connection.

## Model Training

<Frame caption="Edge Impulse Neural Network Display">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edenoff/impulse.jpg?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=831bd7949e334dbc8bceb8f535450acc" width="936" height="540" data-path=".assets/images/edenoff/impulse.jpg" />
</Frame>

For machine learning (ML) we will use Edge Impulse; a free platform for developers which provides powerful and interesting features that speed up any machine learning project.

Since this prototype does not use Edge Impulse supported sensors, data acquisition will be made separately.

How can such data be obtained? Data is obtained by power distributors, from auditors, or even from private custom records such as tracking AC variation and temperature to a database.

The model will be trained with a failure and a regular database with the following labeled columns: timestamp, temperature, voltage, as well as a column with the latest five average AC readings. The purpose of the AC reading column is to detect any recent variations in the service. Figure 5 displays what our failure dataset case looks like.

<Frame caption="Failure Dataset Case">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edenoff/dataset.jpg?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=dbbbde9bf470621548004917e91a7601" width="936" height="676" data-path=".assets/images/edenoff/dataset.jpg" />
</Frame>

After a trial and error procedure, Keras (a deep learning API) with 75 training cycles and Neural Network with a 0.0005 learning rate, turned out to be effective. Edge Impulse visual and testing tools were an excellent way to determine whether datasets and training are correct, before starting to code.

Now that we are sure predictions work, we can to export an Arduino-ready library and create the electronics.

## Hardware

<Frame caption="The device fits into a power outlet">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edenoff/device-hardware.jpg?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=fb1d1f75a943a0a49e96f13f9d73542c" width="628" height="836" data-path=".assets/images/edenoff/device-hardware.jpg" />
</Frame>

* Arduino Nano BLE 33: powerful board compatible with Edge Impulse TinyML
* Zmpt101b voltage sensor: to read AC from the outlet
* 7 Segment 4 digit display
* Digital Buzzer
* Female to female jumper wires
* 3.7v battery
* Lipo Charger

*Note 1: to simplify the project onboard a HTS221 temperature sensor is used, but for a real case scenario an external temperature sensor should be used.*

*Note 2: In previous projects, I was asked about using standard Arduino Nano with external sensors. The most important thing about Arduino Nano BLE 33 Sense is not it’s sensors but the processor. You will not be able to replace it with a regular Arduino Nano. If you cannot get BLE 33 Sense, check out the Arduino Portenta H7.*

<Frame caption="Display of wall mount">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edenoff/wall-mount.jpg?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=ca2a081adfbdcf4d3e9ce0c86a34da58" width="628" height="836" data-path=".assets/images/edenoff/wall-mount.jpg" />
</Frame>

*Note 3: Zmpt101b voltage sensor requires a setup calibration. You can find a small screw in the board to do that. You may also need to adjust the following function inside the .ino code to obtain reliable voltage readings.*

```
Veff = (((VeffD - 420.76) / -90.24) * -210.2) + 210.2;
```

## Connections

* Zmpt101b GND and 5V to Arduino GND and 5V. Then signal pin to Arduino A0. AC to screw pins.
* Display to GND and 5V, D12 and D11
* Buzzer to GND and D10.
* Battery to VIN and GND

## Software

* Install HTS221 library. Even when this is an on board module, the HTS221 library is required. Go to Sketch > Include Library > Manage Libraries > Search HTS221
* Download this ZIP file > Add via Sketch > Add Zip.
* Download the .ino file > load it into Arduino BLE 33 > connect the Arduino using micro USB cable, and upload

Regarding code settings:

**Threshold** is used to compare against **result.classification\[ix].value** for failure dataset. See below:

```
float threesold=0.85;
```

**testFail** is used to force a fail message and buzzer for testing purposes on iterations #1, #3, and #5. See below:

```
int testFail=1;
```

If you want to make an average of more than 5 readings, you will have to change the formula. See below:

```
iterationsForAvg=5;
```

## 3D Printed Power Outlet Faceplate

<Frame caption="3D Printed Power Outlet Face">
  <img src="https://mintcdn.com/edgeimpulse/LSbqkaU8tx8Cie9-/.assets/images/edenoff/faceplate.jpg?fit=max&auto=format&n=LSbqkaU8tx8Cie9-&q=85&s=a699a1b037bda91aa27b583d610bd8ac" width="936" height="674" data-path=".assets/images/edenoff/faceplate.jpg" />
</Frame>

This model was made considering Argentina's power outlet specifications but you can make your own and place the entire prototype inside a power outlet if needed.

Final notes:

Instead of Arduino BLE 33 Sense, Raspberry Pi 4 could be used, temperature could be obtained from the internet along with power distributor's demand data. Several actions could be triggered when a power cut is coming like starting a gas-based generator, alerting employees by Telegram, turning off expensive machines with Linux commands or relays, etc.

This machine learning project covers some points that could be used for other enterprise-related products like third-party sensors, importing CSV datasets, and custom axis for inferences.


Built with [Mintlify](https://mintlify.com).