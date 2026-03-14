# Source: https://docs.edgeimpulse.com/projects/expert-network/dairy-manufacturing-with-ai-seeed-xiao-esp32c3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI-Assisted Monitoring of Dairy Manufacturing Conditions - Seeed XIAO ESP32C3

Created By: Kutluhan Aktar

Public Project Link: [https://studio.edgeimpulse.com/public/159184/latest](https://studio.edgeimpulse.com/public/159184/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_8.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=b7141897571b42b9343a9bad4cded06a" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_8.jpg" />
</Frame>

## Description

As many of us know, yogurt is produced by bacterial fermentation of milk, which can be of cow, goat, ewe, sheep, etc. The fermentation process thickens the milk and provides a characteristic tangy flavor to yogurt. Considering organisms contained in yogurt stimulate the gut's friendly bacteria and suppress harmful bacteria looming in the digestive system, it is not surprising that yogurt is consumed worldwide as a healthy and nutritious food\[^1].

The bacteria utilized to produce yogurt are known as yogurt cultures (or starters). Fermentation of sugars in the milk by yogurt cultures yields lactic acid, which decomposes and coagulates proteins in the milk to give yogurt its texture and characteristic tangy flavor. Also, this process improves the digestibility of proteins in the milk and enhances the nutritional value of proteins. After the fermentation of the milk, yogurt culture could help the human intestinal tract to absorb the amino acids more efficiently\[^2].

Even though yogurt production and manufacturing look like a simple task, achieving precise yogurt texture (consistency) can be arduous and strenuous since various factors affect the fermentation process while processing yogurt, such as:

* Temperature
* Humidity
* Pressure
* Milk Temperature
* Yogurt Culture (Starter) Amount (Weight)

In this regard, most companies employ food (chemical) additives while mass-producing yogurt to maintain its freshness, taste, texture, and appearance. Depending on the production method, yogurt additives can include dilutents, water, artificial flavorings, rehashed starch, sugar, and gelatine.

In recent years, due to the surge in food awareness and apposite health regulations, companies were coerced into changing their yogurt production methods or labeling them conspicuously on the packaging. Since people started to have a penchant for consuming more healthy and organic (natural) yogurt, it became a necessity to prepare prerequisites precisely for yogurt production without any additives. However, unfortunately, organic (natural) yogurt production besets some local dairies since following strict requirements can be expensive and demanding for small businesses trying to gain a foothold in the dairy industry.

After perusing recent research papers on yogurt production, I decided to utilize temperature, humidity, pressure, milk temperature, and culture weight measurements denoting yogurt consistency before fermentation so as to create an easy-to-use and budget-friendly device in the hope of assisting dairies in reducing total cost and improving product quality.

Even though the mentioned factors can provide insight into detecting yogurt consistency before fermentation, it is not possible to extrapolate and construe yogurt texture levels precisely by merely employing limited data without applying complex algorithms. Hence, I decided to build and train an artificial neural network model by utilizing the empirically assigned yogurt consistency classes to predict yogurt texture levels before fermentation based on temperature, humidity, pressure, milk temperature, and culture weight measurements.

Since XIAO ESP32C3 is an ultra-small size IoT development board that can easily collect data and run my neural network model after being trained to predict yogurt consistency levels, I decided to employ XIAO ESP32C3 in this project. To collect the required measurements to train my model, I used a temperature & humidity sensor (Grove), an integrated pressure sensor kit (Grove), an I2C weight sensor kit (Gravity), and a DS18B20 waterproof temperature sensor. Since the XIAO expansion board provides various prototyping options and built-in peripherals, such as an SSD1306 OLED display and a MicroSD card module, I used the expansion board to make rigid connections between XIAO ESP32C3 and the sensors.

Since the expansion board supports reading and writing information from/to files on an SD card, I stored the collected data in a CSV file on the SD card to create a data set. In this regard, I was able to save data records via XIAO ESP32C3 without requiring any additional procedures.

After completing my data set, I built my artificial neural network model (ANN) with Edge Impulse to make predictions on yogurt consistency levels (classes). Since Edge Impulse is nearly compatible with all microcontrollers and development boards, I had not encountered any issues while uploading and running my model on XIAO ESP32C3. As labels, I utilized the empirically assigned yogurt texture classes for each data record while collecting yogurt processing data:

* Thinner
* Optimum
* Curdling (Lumpy)

After training and testing my neural network model, I deployed and uploaded the model on XIAO ESP32C3. Therefore, the device is capable of detecting precise yogurt consistency levels (classes) by running the model independently.

Since I wanted to allow the user to get updates and control the device remotely, I decided to build a complementing Blynk application for this project: The Blynk dashboard displays the recent sensor readings transferred from XIAO ESP32C3, makes XIAO ESP32C3 run the neural network model, and shows the prediction result.

Lastly, to make the device as sturdy and robust as possible while operating in a dairy, I designed a dairy-themed case with a sliding (removable) front cover (3D printable).

So, this is my project in a nutshell 😃

In the following steps, you can find more detailed information on coding, logging data on the SD card, communicating with a Blynk application, building a neural network model with Edge Impulse, and running it on XIAO ESP32C3.

🎁🎨 Huge thanks to [Seeed Studio](https://www.seeedstudio.com/) for sponsoring these products:

⭐ XIAO ESP32C3 | [Inspect](https://www.seeedstudio.com/Seeed-XIAO-ESP32C3-p-5431.html)

⭐ XIAO Expansion Board | [Inspect](https://www.seeedstudio.com/Seeeduino-XIAO-Expansion-board-p-4746.html)

⭐ Grove - Temperature & Humidity Sensor | [Inspect](https://www.seeedstudio.com/Grove-Temp-Humi-Sensor-SHT40-p-5384.html)

⭐ Grove - Integrated Pressure Sensor Kit | [Inspect](https://www.seeedstudio.com/Grove-Integrated-Pressure-Sensor-Kit-MPX5700AP-p-4295.html)

🎁🎨 Huge thanks to [DFRobot](https://www.dfrobot.com/?tracking=60f546f8002be) for sponsoring a [Gravity: I2C 1Kg Weight Sensor Kit (HX711)](https://www.dfrobot.com/product-2289.html?tracking=60f546f8002be).

🎁🎨 Also, huge thanks to [Creality](https://store.creality.com/) for sending me a [Creality Sonic Pad](https://www.creality.com/products/creality-sonic-pad), a [Creality Sermoon V1 3D Printer](https://www.creality.com/products/creality-sermoon-v1-v1-pro-3d-printer), and a [Creality CR-200B 3D Printer](https://www.creality.com/products/cr-200b-3d-printer).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/home_3.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=1c989ef32ca429773793455f16fbc980" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/home_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_8.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=b7141897571b42b9343a9bad4cded06a" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_3.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=5c78b5773695ef7cd1cc275a44d164f8" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_5.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=ab64f3b361cde10c35f9f47c8a00d6dd" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/dairy-manufacturing-with-ai/gif_collect.gif" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_3.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=83ea229b0e500dd0014a77b5bb1c481f" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/dairy-manufacturing-with-ai/gif_run.gif" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_run_6.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=3b051f4b8c7fd471ea57a40031cf7822" width="1600" height="850" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_run_6.png" />
</Frame>

## Step 1: Designing and printing a dairy-themed case

Since I focused on building a budget-friendly and easy-to-use device that collects yogurt processing data and informs the user of the predicted yogurt consistency level before fermentation, I decided to design a robust and sturdy case allowing the user to access the SD card after logging data and weigh yogurt culture (starter) easily. To avoid overexposure to dust and prevent loose wire connections, I added a sliding front cover with a handle to the case. Also, I decided to emboss yogurt and milk icons on the sliding front cover so as to complement the dairy theme gloriously.

Since I needed to adjust the rubber tube length of the integrated pressure sensor, I added a hollow cylinder part to the main case to place the rubber tube. Then, I decided to fasten a small cow figure to the cylinder part because I thought it would make the case design align with the dairy theme.

I designed the main case and its sliding front cover in Autodesk Fusion 360. You can download their STL files below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_1.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=becdf1a2b6abb15d499d672de4884b9e" width="1600" height="846" data-path=".assets/images/dairy-manufacturing-with-ai/model_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_2.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=61908b6d964ff2cadf8301a4e3fd5c9f" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/model_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_3.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=55bb51355f5170361b377b5c32a66137" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/model_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_4.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=9e1b6d93e6f03852c62ebd74f4cd4b6b" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/model_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_5.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=dda4845fa3645a7380778d71c56b168f" width="1600" height="851" data-path=".assets/images/dairy-manufacturing-with-ai/model_5.png" />
</Frame>

For the cow figure (replica) affixed to the top of the cylinder part of the main case, I utilized this model from Thingiverse:

* [Cow](https://www.thingiverse.com/thing:2619138)

Then, I sliced all 3D models (STL files) in Ultimaker Cura.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_6.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=14eb0d154be8659e701089f91fb3a6bb" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/model_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_7.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=26258b6a3d8741d7567648d421add10f" width="1600" height="850" data-path=".assets/images/dairy-manufacturing-with-ai/model_7.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_8.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=e2c6a3e5326caca97eec3ca9f844886a" width="1600" height="847" data-path=".assets/images/dairy-manufacturing-with-ai/model_8.png" />
</Frame>

Since I wanted to create a solid structure for the main case with the sliding front cover representing dairy products, I utilized these PLA filaments:

* Beige
* ePLA-Matte Milky White

Finally, I printed all parts (models) with my Creality Sermoon V1 3D Printer and Creality CR-200B 3D Printer in combination with the Creality Sonic Pad. You can find more detailed information regarding the Sonic Pad in Step 1.1.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_finished_1.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=ce6de490750b9bdccdfd1a6b2687333f" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/model_finished_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/model_finished_2.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=e8f4e253630360cbf1e8b01257d1e144" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/model_finished_2.jpg" />
</Frame>

If you are a maker or hobbyist planning to print your 3D models to create more complex and detailed projects, I highly recommend the Sermoon V1. Since the Sermoon V1 is fully-enclosed, you can print high-resolution 3D models with PLA and ABS filaments. Also, it has a smart filament runout sensor and the resume printing option for power failures.

Furthermore, the Sermoon V1 provides a flexible metal magnetic suction platform on the heated bed. So, you can remove your prints without any struggle. Also, you can feed and remove filaments automatically (one-touch) due to its unique sprite extruder (hot end) design supporting dual-gear feeding. Most importantly, you can level the bed automatically due to its user-friendly and assisted bed leveling function.

:hash: Before the first use, remove unnecessary cable ties and apply grease to the rails.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sermoon_1%20(2).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=f7e0414724182bfe83f20920c9d714c7" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sermoon_1 (2).jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sermoon_2%20(1).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=5edc39bf7053ea864ed871977b922355" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sermoon_2 (1).jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sermoon_3%20(2).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=d8ab559a6327f8c490f9a6298cd91c05" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sermoon_3 (2).jpg" />
</Frame>

:hash: Test the nozzle and hot bed temperatures.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sermoon_4%20(1).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=80edfc36452dd2bbb05224b6f8f029ab" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sermoon_4 (1).jpg" />
</Frame>

:hash: Go to *Print Setup ➡ Auto leveling* and adjust five predefined points automatically with the assisted leveling function.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sermoon_5%20(1).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=bf06dbbf72fe9bd879e16fb7c50eb163" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sermoon_5 (1).jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sermoon_6.jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=3a45481b0aefb133f86acac52d51e2a8" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sermoon_6.jpg" />
</Frame>

:hash: Finally, place the filament into the integrated spool holder and feed the extruder with the filament.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sermoon_7%20(2).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=c3cf554c8d846c6323cd5476e8dabac5" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sermoon_7 (2).jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sermoon_8%20(1).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=9d01bd3d9ac7a0055902ec844deef7e1" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sermoon_8 (1).jpg" />
</Frame>

:hash: Since the Sermoon V1 is not officially supported by Cura, download the latest [Creality Slicer](https://www.creality.com/pages/download-sermoon-v1v1-pro) version and copy the official printer settings provided by Creality, including *Start G-code* and *End G-code*, to a custom printer profile on Cura.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/sermoon_slicer_1.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=4950e5260a2ea16a47da5f32e90f2a59" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/sermoon_slicer_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/sermoon_slicer_2%20(2).png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=4220d8451d57dd88afb53f36609c5334" width="1600" height="853" data-path=".assets/images/dairy-manufacturing-with-ai/sermoon_slicer_2 (2).png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/sermoon_slicer_3%20(2).png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=2366671f9bb70d60152663428c1994ad" width="1600" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/sermoon_slicer_3 (2).png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/sermoon_cura_1%20(1).png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=494e052fc41dbf5ef80a4f4a8710d19c" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/sermoon_cura_1 (1).png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/sermoon_cura_2.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=009c43bb0e064b233220026285846676" width="1600" height="850" data-path=".assets/images/dairy-manufacturing-with-ai/sermoon_cura_2.png" />
</Frame>

## Step 1.1: Improving print quality and speed with the Creality Sonic Pad

Since I wanted to improve my print quality and speed with Klipper, I decided to upgrade my Creality CR-200B 3D Printer with the [Creality Sonic Pad](https://www.creality.com/products/creality-sonic-pad).

Creality Sonic Pad is a beginner-friendly device to control almost any FDM 3D printer on the market with the Klipper firmware. Since the Sonic Pad uses precision-oriented algorithms, it provides remarkable results with higher printing speeds. The built-in input shaper function mitigates oscillation during high-speed printing and smooths ringing to maintain high model quality. Also, it supports G-code model preview.

Although the Sonic Pad is pre-configured for some Creality printers, it does not support the CR-200B officially yet. Therefore, I needed to add the CR-200B as a user-defined printer to the Sonic Pad. Since the Sonic Pad needs unsupported printers to be flashed with the self-compiled Klipper firmware before connection, I flashed my CR-200B with the required Klipper firmware settings via *FluiddPI* by following [this YouTube tutorial](https://www.youtube.com/watch?v=gfZ9Lbyh8qU).

If you do not know how to write a printer configuration file for Klipper, you can download the stock CR-200B configuration file from [here](https://github.com/ChewyJetpack/CR-200B-Klipper-Config/).

:hash: After flashing the CR-200B with the Klipper firmware, copy the configuration file *(printer.cfg)* to a USB drive and connect the drive to the Sonic Pad.

:hash: After setting up the Sonic Pad, select *Other models*. Then, load the *printer.cfg* file.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sonic_pad_2%20(2).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=9443f6f79cfe290c0893d5df52372cb9" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sonic_pad_2 (2).jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sonic_pad_4%20(2).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=3f843529448d488e83266c82b9bd0996" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sonic_pad_4 (2).jpg" />
</Frame>

:hash: After connecting the Sonic Pad to the CR-200B successfully via a USB cable, the Sonic Pad starts the self-testing procedure, which allows the user to test printer functions and level the bed.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sonic_pad_5.jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=355c4a99220b6e0513ee40bc5faf19f4" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sonic_pad_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sonic_pad_6%20(2).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=3792f881dd9fa020939416a52ab669dc" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sonic_pad_6 (2).jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sonic_pad_7%20(2).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=97f02e2696f8b8b6b35f711d8be153ab" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sonic_pad_7 (2).jpg" />
</Frame>

:hash: After completing setting up the printer, the Sonic Pad lets the user control all functions provided by the Klipper firmware.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sonic_pad_8.jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=92b00d6688cf0570f0f4f3553c33fbac" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sonic_pad_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_sonic_pad_9%20(1).jpg?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=1638cf5b16b54d0c5625fef41a95cf04" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/set_sonic_pad_9 (1).jpg" />
</Frame>

:hash: In Cura, export the sliced model in the *ufp* format. After uploading *.ufp* files to the Sonic Pad via the USB drive, it converts them to sliced G-code files automatically.

:hash: Also, the Sonic Pad can display model preview pictures generated by Cura with the *Create Thumbnail* script.

## Step 1.2: Assembling the case and making connections & adjustments

```
// Connections
// XIAO ESP32C3 :
//                                Grove - Temperature & Humidity Sensor
// A4   --------------------------- SDA
// A5   --------------------------- SCL
//                                Grove - Integrated Pressure Sensor
// A0   --------------------------- S
//                                Gravity: I2C 1Kg Weight Sensor Kit - HX711
// A4   --------------------------- SDA
// A5   --------------------------- SCL
//                                DS18B20 Waterproof Temperature Sensor
// D6   --------------------------- Data
//                                SSD1306 OLED Display (128x64)
// A4   --------------------------- SDA
// A5   --------------------------- SCL
//                                MicroSD Card Module (Built-in on the XIAO Expansion board)
// D10  --------------------------- MOSI
// D9   --------------------------- MISO
// D8   --------------------------- CLK (SCK)
// D2   --------------------------- CS (SS)
//                                Button (Built-in on the XIAO Expansion board)
// D1   --------------------------- +
```

First of all, I attached XIAO ESP32C3 to [the XIAO expansion board](https://wiki.seeedstudio.com/Seeeduino-XIAO-Expansion-Board/). Then, I connected [the temperature & humidity sensor (Grove)](https://wiki.seeedstudio.com/Grove-SHT4x/) and [the integrated pressure sensor kit (Grove)](https://wiki.seeedstudio.com/Grove-Integrated-Pressure-Sensor-Kit/) to the expansion board via Grove connection cables.

Since [the I2C weight sensor kit (Gravity)](https://wiki.dfrobot.com/HX711_Weight_Sensor_Kit_SKU_KIT0176) does not include a compatible connection cable for a Grove port, I connected the weight sensor to the expansion board via a 4-pin male jumper to Grove 4-pin conversion cable.

As shown in the schematic below, before connecting the DS18B20 waterproof temperature sensor to the expansion board, I attached a 4.7K resistor as a pull-up from the DATA line to the VCC line of the sensor to generate accurate temperature measurements.

To display the collected data, I utilized the built-in SSD1306 OLED screen on the expansion board. To assign yogurt consistency levels empirically while saving data records to a CSV file on the SD card, I used the built-in MicroSD card module and button on the expansion board.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/breadboard_1.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=0a8e55229dce6a2d69fad2dad0080048" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/breadboard_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/breadboard_2.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=ae8125f17ec5aa5ec5363ba80fe284e8" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/breadboard_2.jpg" />
</Frame>

After printing all parts (models), I fastened all components except the expansion board to their corresponding slots on the main case via a hot glue gun.

I attached the expansion board to the main case by utilizing M3 screws with hex nuts and placed the rubber tube of the integrated pressure sensor in the hollow cylinder part of the main case.

Then, I placed the sliding front cover via the dents on the main case.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/dairy-manufacturing-with-ai/assembly_1.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=0b78174af3dac989d4d44753ef5d21de" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/dairy-manufacturing-with-ai/assembly_2.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=3311a2658ec45178572b6f1dff8f710a" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/dairy-manufacturing-with-ai/assembly_3.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=736ed1c28e3163b4ab7d37d090f6c1f2" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/dairy-manufacturing-with-ai/assembly_4.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=7e3ba670267e7c484b1e23d6116b105e" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/dairy-manufacturing-with-ai/assembly_5.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=b05ae3f19a187677e91bcd7b2642bed5" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/assembly_6.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=dc3ee7b48236c2f81c37f0d21f6e3da8" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/assembly_7.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=b8ac0da748685388e44300004ee33e21" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/assembly_8.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=112d23cf78038766fd0b957ae8f95209" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/assembly_9.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=6db91c45e09f5513ad5d1809656af4ef" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_9.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/dairy-manufacturing-with-ai/assembly_10.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=af36ef40fe6e25634ea5960cc117c0e4" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_10.jpg" />
</Frame>

Finally, I affixed the small cow figure to the top of the cylinder part of the main case via the hot glue gun.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/dairy-manufacturing-with-ai/assembly_11.jpg?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=a50daccee14e60712dd61e0b422ef0a5" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/assembly_11.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/finished.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=9062a220eaa2d1eacd8e4f1237a9d573" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/finished.jpg" />
</Frame>

## Step 2: Creating a Blynk application and user interface for XIAO ESP32C3

Since I focused on building an accessible device, I decided to create a complementing Blynk application for allowing the user to display recent sensor readings, run the Edge Impulse neural network model, and get informed of the prediction result remotely.

[The Blynk IoT Platform](https://docs.blynk.io/en/) provides a free cloud service to communicate with supported microcontrollers and development boards, such as ESP32C3. Also, Blynk lets the user design unique web and mobile applications with drag-and-drop editors.

:hash: First of all, create an account on [Blynk](https://blynk.cloud/dashboard/login) and open Blynk.Console.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_1.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=9e072e1e2ea57aad7bf5b60adf3fbefb" width="1600" height="777" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_1.png" />
</Frame>

:hash: Before designing the web application on Blynk.Console, install [the Blynk library](https://github.com/blynkkk/blynk-library/releases/tag/v1.1.0) on the Arduino IDE to send and receive data packets via the Blynk cloud: Go to *Sketch ➡ Include Library ➡ Manage Libraries…* and search for *Blynk*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_1.1.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=95c1178ef690d0381544aa22dc7ebd18" width="1600" height="733" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_1.1.png" />
</Frame>

:hash: Then, create a new device with the *Quickstart Template*, named XIAO ESP32C3. And, select the board type as *ESP32*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_2.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=94757268a99a48a9a6e9bb0e9469138e" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_3.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=ca69fbc0b8f13db682612ba738ed5494" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_3.png" />
</Frame>

:hash: After creating the device successfully, copy the *Template ID*, *Device Name*, and *Auth Token* variables required by the Blynk library.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_4.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=33de13013ed15aba3d3714a82ce0c46b" width="1600" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_4.png" />
</Frame>

:hash: Open the *Web Dashboard* and click the *Edit* button to change the web application design.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_5.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=000371a08d1cc16f091edb64f86cb42d" width="1600" height="771" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_5.png" />
</Frame>

:hash: From the *Widget Box*, add the required widgets and assign each widget to a virtual pin as the datastream option.

Since Blynk allows the user to adjust the unit, data range, and color scheme for each widget, I was able to create a unique web user interface for the device.

* Temperature Gauge ➡ V4
* Humidity Gauge ➡ V12
* Pressure Gauge ➡ V6
* Milk Temperature Gauge ➡ V7
* Weight Gauge ➡ V8
* Switch Button ➡ V9
* Label ➡ V10

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_6.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=ce18921fb3d4929c3d77c09306f32aa2" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_7.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=d3923d51ce1be106e9bb41e876ce9a93" width="1600" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_7.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_8.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=64a50949c72ccdf49fdef25b07843bdb" width="1600" height="777" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_8.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_9.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=ea6d26216f8022461b837d7e5a8655db" width="1600" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_9.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_10.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=9eccbb35c106dbd9748585cc5af953d6" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_10.png" />
</Frame>

After completing designing the web user interface, I tested the virtual pin connection of each widget with XIAO ESP32C3.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_11.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=54b597148c57c3c4928661a8bc419e1a" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_11.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_set_12.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=2d68bc3d7789b3c94d05146917f08f1c" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_set_12.png" />
</Frame>

## Step 3: Setting up XIAO ESP32C3 on the Arduino IDE

Since the XIAO expansion board supports reading and writing information from/to files on an SD card, I decided to log the collected yogurt processing data in a CSV file on the SD card without applying any additional procedures. Also, I employed XIAO ESP32C3 to communicate with the Blynk application to run the neural network model remotely and transmit the collected data.

However, before proceeding with the following steps, I needed to set up [XIAO ESP32C3](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/) on the Arduino IDE and install the required libraries for this project.

:hash: To add the XIAO ESP32C3 board package to the Arduino IDE, navigate to *File ➡ Preferences* and paste the URL below under *Additional Boards Manager URLs*.

*[https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package\\\_esp32\\\_dev\\\_index.json](https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package\\_esp32\\_dev\\_index.json)*

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_xiao_wifi_1%20(2).png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=880d841d2c984d0925dce6813451f491" width="799" height="530" data-path=".assets/images/dairy-manufacturing-with-ai/set_xiao_wifi_1 (2).png" />
</Frame>

:hash: Then, to install the required core, navigate to *Tools ➡ Board ➡ Boards Manager* and search for *esp32*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_xiao_wifi_2.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=d7865e07de6a902acf0db233f0d1216b" width="975" height="549" data-path=".assets/images/dairy-manufacturing-with-ai/set_xiao_wifi_2.png" />
</Frame>

:hash: After installing the core, navigate to *Tools ➡ Board ➡ ESP32 Arduino* and select *XIAO\_ESP32C3*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/dairy-manufacturing-with-ai/set_xiao_wifi_3.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=c33aa7cb30f457462876c8f6b0329100" width="1600" height="833" data-path=".assets/images/dairy-manufacturing-with-ai/set_xiao_wifi_3.png" />
</Frame>

Since the provided XIAO ESP32C3 core's assigned pin numbers are not compatible with the expansion board's MicroSD card module, it throws an error on the Arduino IDE while attempting to access the SD card.

Therefore, I needed to change the assigned SS pin to 4 (GPIO4) in the *pins\_arduino.h* file.

:hash: The *pins\_arduino.h* file location: *\esp32\hardware\esp32\2.0.5\variants\XIAO\_ESP32C3*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/dairy-manufacturing-with-ai/update_SS_pin.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=2b3e86571aa0f7c053ad4b7ae5392666" width="1600" height="847" data-path=".assets/images/dairy-manufacturing-with-ai/update_SS_pin.png" />
</Frame>

:hash: Finally, download the required libraries for the temperature & humidity sensor, the I2C weight sensor, the DS18B20 temperature sensor, and the SSD1306 OLED display:

Sensirion arduino-core | [Download](https://github.com/Sensirion/arduino-core)

arduino-i2c-sht4x | [Download](https://github.com/Sensirion/arduino-i2c-sht4x)

DFRobot\_HX711\_I2C | [Download](https://github.com/DFRobot/DFRobot_HX711_I2C)

OneWire | [Download](https://github.com/PaulStoffregen/OneWire)

DallasTemperature | [Download](https://github.com/milesburton/Arduino-Temperature-Control-Library)

Adafruit\_SSD1306 | [Download](https://github.com/adafruit/Adafruit_SSD1306)

Adafruit-GFX-Library | [Download](https://github.com/adafruit/Adafruit-GFX-Library)

## Step 3.1: Displaying images on the SSD1306 OLED screen

To display images (black and white) on the SSD1306 OLED screen successfully, I needed to create monochromatic bitmaps from PNG or JPG files and convert those bitmaps to data arrays.

:hash: First of all, download the [LCD Assistant](http://en.radzio.dxp.pl/bitmap_converter/).

:hash: Then, upload a monochromatic bitmap and select *Vertical* or *Horizontal* depending on the screen type.

:hash: Convert the image (bitmap) and save the output (data array).

:hash: Finally, add the data array to the code and print it on the screen.

```
static const unsigned char PROGMEM sd [] = {
0x0F, 0xFF, 0xFF, 0xFE, 0x1F, 0xFF, 0xFF, 0xFF, 0x1F, 0xFE, 0x7C, 0xFF, 0x1B, 0x36, 0x6C, 0x9B,
0x19, 0x26, 0x4C, 0x93, 0x19, 0x26, 0x4C, 0x93, 0x19, 0x26, 0x4C, 0x93, 0x19, 0x26, 0x4C, 0x93,
0x19, 0x26, 0x4C, 0x93, 0x19, 0x26, 0x4C, 0x93, 0x19, 0x26, 0x4C, 0x93, 0x1F, 0xFF, 0xFF, 0xFF,
0x1F, 0xFF, 0xFF, 0xFF, 0x1F, 0xFF, 0xFF, 0xFF, 0x1F, 0xFF, 0xFF, 0xFF, 0x1F, 0xFF, 0xFF, 0xFF,
0x3F, 0xFF, 0xFF, 0xFF, 0x7F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFC, 0xC7, 0xFF, 0xFF, 0xF9, 0x41, 0xFF, 0x1F, 0xF9, 0xDD, 0xFF,
0x1F, 0xFC, 0xDD, 0xFF, 0x1F, 0xFE, 0x5D, 0xFF, 0x1F, 0xF8, 0x43, 0xFF, 0x1F, 0xFD, 0xFF, 0xFF,
0x3F, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFE
};

...

display.clearDisplay();
display.drawBitmap(48, 0, sd, 32, 44, SSD1306_WHITE);
display.display();
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/img_cv_1.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=c468aca998dcafd5428dd72d491aa9cd" width="524" height="426" data-path=".assets/images/dairy-manufacturing-with-ai/img_cv_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/img_cv_2.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=ec615ad47963f5307b048cda39c8ae58" width="1512" height="778" data-path=".assets/images/dairy-manufacturing-with-ai/img_cv_2.png" />
</Frame>

## Step 4: Logging yogurt processing information in a CSV file on the SD card w/ XIAO ESP32C3

After setting up XIAO ESP32C3 and installing the required libraries, I programmed XIAO ESP32C3 to collect environmental factor measurements and the culture (starter) amount in order to save them to the given CSV file on the SD card.

* Temperature (°C)
* Humidity (%)
* Pressure (kPa)
* Milk Temperature (°C)
* Starter Weight (g)

Since I needed to assign yogurt consistency levels (classes) empirically as labels for each data record while collecting yogurt processing data to create a valid data set for the neural network model, I utilized the built-in button on the XIAO expansion board in two different modes (long press and short press) so as to choose among classes and save data records. After selecting a yogurt consistency level (class) by short-pressing the button, XIAO ESP32C3 appends the selected class and the recently collected data to the given CSV file on the SD card as a new row if the button is long-pressed.

* Button (short-pressed) ➡ Select a class (Thinner, Optimum, Curdling)
* Button (long-pressed) ➡ Save data to the SD card

You can download the *AI\_yogurt\_processing\_data\_collect.ino* file to try and inspect the code for collecting yogurt processing data and for saving data records to the given CSV file on the SD card.

⭐ Include the required libraries.

```
#include &lt;FS.h>
#include &lt;SPI.h>
#include &lt;SD.h>
#include &lt;Adafruit_GFX.h>
#include &lt;Adafruit_SSD1306.h>
#include &lt;SensirionI2CSht4x.h>
#include &lt;DFRobot_HX711_I2C.h>
#include &lt;OneWire.h>
#include &lt;DallasTemperature.h>
```

⭐ Initialize the *File* class and define the CSV file name on the SD card.

```
File myFile;
// Define the CSV file name:
const char* data_file = "/yogurt_data.csv";
```

⭐ Define the 0.96 Inch SSD1306 OLED display on the XIAO expansion board.

```
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define OLED_RESET    -1 // Reset pin # (or -1 if sharing Arduino reset pin)

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
```

⭐ Define the temperature & humidity sensor object (Grove), the I2C weight sensor object (Gravity), and the DS18B20 waterproof temperature sensor settings.

```
SensirionI2CSht4x sht4x;

// Define the HX711 weight sensor.
DFRobot_HX711_I2C MyScale;

// Define the DS18B20 waterproof temperature sensor settings:
#define ONE_WIRE_BUS D6
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature DS18B20(&oneWire);
```

⭐ Define monochrome graphics.

⭐ Define the built-in button pin on the expansion board.

⭐ Then, define the button state and the duration variables to utilize the button in two different modes: long press and short press.

```
#define button D1
// Define the button state and the duration to utilize the integrated button in two different modes: long press and short press.
int button_state = 0;
#define DURATION 5000
```

⭐ Initialize the SSD1306 screen.

```
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.display();
  delay(1000);
```

⭐ Initialize the DS18B20 temperature sensor.

```
  DS18B20.begin();
```

⭐ Define the required settings to initialize the temperature & humidity sensor (Grove).

```
  sht4x.begin(Wire);
  uint32_t serialNumber;
  error = sht4x.serialNumber(serialNumber);
```

⭐ In the *err\_msg* function, display the error message on the SSD1306 OLED screen.

```
void err_msg(){
  // Show the error message on the SSD1306 screen.
  display.clearDisplay();
  display.drawBitmap(48, 0, _error, 32, 32, SSD1306_WHITE);
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,40);
  display.println("Check the serial monitor to see the error!");
  display.display();
}
```

⭐ Check the temperature & humidity sensor connection status and print the error message on the serial monitor, if any.

```
  if(error){
    Serial.print("Error: Grove - Temperature & Humidity Sensor not initialized!\n");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);
    err_msg();
  }else{
    Serial.print("Grove - Temperature & Humidity Sensor successfully initialized: "); Serial.println(serialNumber);
  }
```

⭐ Check the connection status between the I2C weight sensor and XIAO ESP32C3.

```
  while (!MyScale.begin()) {
    Serial.println("Error: HX711 initialization is failed!");
    err_msg();
    delay(1000);
  }
  Serial.println("HX711 initialization is successful!");
```

⭐ Set the calibration weight (g) and threshold (g) to calibrate the weight sensor automatically.

⭐ Display the current calibration value on the serial monitor.

```
  MyScale.setCalWeight(100);
  // Set the calibration threshold (g).
  MyScale.setThreshold(30);
  // Display the current calibration value.
  Serial.print("\nCalibration Value: "); Serial.println(MyScale.getCalibration());
  MyScale.setCalibration(MyScale.getCalibration());
  delay(1000);
```

⭐ Check the connection status between XIAO ESP32C3 and the SD card.

```
  if(!SD.begin()){
    Serial.println("Error: SD card initialization failed!\n");
    err_msg();
    while (1);
  }
  Serial.println("SD card is detected successfully!\n");
```

⭐ In the *get\_temperature\_and\_humidity* function, obtain the measurements generated by the temperature & humidity sensor.

```
void get_temperature_and_humidity(){
  // Obtain the measurements generated by the Grove - Temperature & Humidity Sensor.
  error = sht4x.measureHighPrecision(temperature, humidity);
  if(error){
    Serial.print("Error trying to execute measureHighPrecision(): ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);
  }else{
    Serial.print("\nTemperature : "); Serial.print(temperature); Serial.println("°C");
    Serial.print("Humidity : "); Serial.print(humidity); Serial.println("%");
  }
  delay(500);
}
```

⭐ In the *get\_pressure* function, get the measurements generated by the integrated pressure sensor (Grove).

⭐ Then, convert the accumulation of raw data to accurate pressure estimation.

```
void get_pressure(){
  // Obtain the measurements generated by the Grove - Integrated Pressure Sensor.
  rawValue = 0;
  // Convert the accumulation of raw data to the pressure estimation.
  for (int x = 0; x &lt; 10; x++) rawValue = rawValue + analogRead(pressure_s_pin);
  pressure = (rawValue - offset) * 700.0 / (fullScale - offset);
  Serial.print("\nPressure : "); Serial.print(pressure); Serial.println(" kPa");
}
```

⭐ In the *get\_weight* function, obtain the weight measurement generated by the I2C weight sensor.

⭐ Then, subtract the container weight from the total weight to get the net weight.

```
void get_weight(int calibration){
  weight = MyScale.readWeight();
  weight = weight - calibration;
  if(weight &lt; 0.5) weight = 0;
  Serial.print("\nWeight: "); Serial.print(weight); Serial.println(" g");
  delay(500);
}
```

⭐ In the *get\_milk\_temperature* function, obtain the temperature measurement generated by the DS18B20 temperature sensor.

```
void get_milk_temperature(){
  // Obtain the temperature measurement generated by the DS18B20 Waterproof Temperature Sensor.
  DS18B20.requestTemperatures();
  m_temperature = DS18B20.getTempCByIndex(0);
  Serial.print("\nMilk Temperature: "); Serial.print(m_temperature); Serial.println("°C");
}
```

⭐ In the *home\_screen* function, display the collected data and the selected class on the SSD1306 OLED screen.

```
void home_screen(){
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,0);
  display.println("Temp => " + String(temperature) + " *C");
  display.println("Humidity => " + String(humidity) + " %");
  display.println("Pres. => " + String(pressure) + " kPa");
  display.println();
  display.println("M_Temp => " + String(m_temperature) + " *C");
  display.println("Weight => " + String(weight) + " g");
  display.println();
  display.println("Selected Class => " + String(class_number));
  display.display();
}
```

⭐ In the *save\_data\_to\_SD\_Card* function:

⭐ Open the given CSV file on the SD card in the *APPEND* file mode.

⭐ If the given CSV file is opened successfully, create a data record from the recently collected data, including the selected yogurt consistency level (class), to be inserted as a new row.

⭐ Then, append the recently created data record and close the CSV file.

⭐ After appending the given data record successfully, notify the user by displaying this message on the SSD1306 OLED screen: *Data saved to the SD card!*

```
void save_data_to_SD_Card(fs::FS &fs, int consistency_level){
  // Open the given CSV file on the SD card in the APPEND file mode.
  // FILE MODES: WRITE, READ, APPEND
  myFile = fs.open(data_file, FILE_APPEND);
  delay(1000);
  // If the given file is opened successfully:
  if(myFile){
    Serial.print("\n\nWriting to "); Serial.print(data_file); Serial.println("...");
    // Create the data record to be inserted as a new row:
    String data_record = String(temperature) + "," + String(humidity) + "," + String(pressure) + "," + String(m_temperature) + "," + String(weight) + ',' + String(consistency_level);
    // Append the data record:
    myFile.println(data_record);
    // Close the CSV file:
    myFile.close();
    Serial.println("Data saved successfully!\n");
    // Notify the user after appending the given data record successfully.
    display.clearDisplay();
    display.drawBitmap(48, 0, sd, 32, 44, SSD1306_WHITE);
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(0,48);
    display.println("Data saved to the SD card!");
    display.display();
  }else{
    // If XIAO ESP32C3 cannot open the given CSV file successfully:
    Serial.println("\nXIAO ESP32C3 cannot open the given CSV file successfully!\n");
    err_msg();
  }
  // Exit and clear:
  delay(4000);
}
```

⭐ Detect whether the built-in button is short-pressed or long-pressed.

```
  button_state = 0;
  if(!digitalRead(button)){
    timer = millis();
    button_state = 1;
    while((millis()-timer) &lt;= DURATION){
      if(digitalRead(button)){
        button_state = 2;
        break;
      }
    }
  }
```

⭐ If the button is short-pressed, change the class number \[0 - 2] to choose among yogurt consistency levels (classes).

⭐ If the button is long-pressed, append the recently created data record to the given CSV file on the SD card.

```
  if(button_state == 1){
    // Save the given data record to the given CSV file on the SD card when long-pressed.
    save_data_to_SD_Card(SD, class_number);
  }else if(button_state == 2){
    // Change the class number when short-pressed.
    class_number++;
    if(class_number > 2) class_number = 0;
    Serial.println("\n\nSelected Class: " + String(class_number) + "\n");
  }
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_collect_1.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=08d64b529b65ccb6ef6d8ef00aafb176" width="1280" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/code_collect_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_collect_2.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=0fe943f159a6abaf1dd871f1bf6cd023" width="1497" height="772" data-path=".assets/images/dairy-manufacturing-with-ai/code_collect_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_collect_3.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=1c39ecb3cd2c0748baeaa00327881c69" width="1375" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/code_collect_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_collect_4.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=ff232d33296745ec91f7162f54abe19e" width="1456" height="772" data-path=".assets/images/dairy-manufacturing-with-ai/code_collect_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_collect_5.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=f0b8c2a02fd5fe1527ab1cf71b4baadb" width="1600" height="663" data-path=".assets/images/dairy-manufacturing-with-ai/code_collect_5.png" />
</Frame>

## Step 4.1: Collecting samples while producing yogurt to create a data set

After uploading and running the code for collecting yogurt processing data and for saving information to the given CSV file on the SD card on XIAO ESP32C3:

🐄🥛📲 The device shows the opening screen if the sensor and MicroSD card module connections with XIAO ESP32C3 are successful.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_1.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=381e809f85fce9859fb023b223cac881" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_1.jpg" />
</Frame>

🐄🥛📲 Then, the device displays the collected yogurt processing data and the selected class number on the SSD1306 OLED screen:

* Temperature (°C)
* Humidity (%)
* Pressure (kPa)
* Milk Temperature (°C)
* Starter Weight (g)
* Selected Class

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_2.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=25f4669c0d41b37902fa64e519dbf294" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_2.jpg" />
</Frame>

🐄🥛📲 If the button (built-in) is short-pressed, the device increments the selected class number in the range of 0-2:

* Thinner \[0]
* Optimum \[1]
* Curdling \[2]

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_3.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=5c78b5773695ef7cd1cc275a44d164f8" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_4.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=2f8fe46025103f283997ce4b34e90f95" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_4.jpg" />
</Frame>

🐄🥛📲 If the button (built-in) is long-pressed, the device appends the recently created data record from the collected data to the *yogurt\_data.csv* file on the SD card, including the selected yogurt consistency class number under the *consistency\_level* data field.

🐄🥛📲 After successfully appending the data record, the device notifies the user via the SSD1306 OLED screen.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_5.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=ab64f3b361cde10c35f9f47c8a00d6dd" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_5.jpg" />
</Frame>

🐄🥛📲 If XIAO ESP32C3 throws an error while operating, the device shows the error message on the SSD1306 OLED screen and prints the error details on the serial monitor.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_error.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=dbc0bee4ad5a780653fd8cc752d2906b" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_error.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/serial_error.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=aeb86f1fa2082a6e0b5d7f12fda971e3" width="1600" height="851" data-path=".assets/images/dairy-manufacturing-with-ai/serial_error.png" />
</Frame>

🐄🥛📲 Also, the device prints notifications and sensor measurements on the serial monitor for debugging.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/serial_collect_1.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=7caf0d2b268ef71f511d46b4c1080bf9" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/serial_collect_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/serial_collect_2.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=4549539cac9e9d5545be6fc996451b18" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/serial_collect_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/serial_collect_3.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=bf092096e8c994f082ad60ae977aacc9" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/serial_collect_3.png" />
</Frame>

To create a data set with eminent validity and veracity, I collected yogurt processing data from nearly 30 different batches. Since I focused on predicting yogurt texture precisely, I always used cow milk in my experiments but changed milk temperature, yogurt culture (starter) amount, and environmental factors while conducting my experiments.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_6.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=1c2bab6e732fe65d672b9da982a2c7e6" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_7.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=a14484e9102101c54784a3cc15c4198e" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_8.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=b7141897571b42b9343a9bad4cded06a" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/collect_9.jpg?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=b4d627a41cb05ec9588570c31853a71f" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/collect_9.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/dairy-manufacturing-with-ai/gif_collect.gif" />
</Frame>

🐄🥛📲 After completing logging the collected data in the *yogurt\_data.csv* file on the SD card, I elicited my data set.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/data_collection_3.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=7b43a2954fdd5e648dfa8111f4c3de41" width="1432" height="903" data-path=".assets/images/dairy-manufacturing-with-ai/data_collection_3.png" />
</Frame>

## Step 5: Building a neural network model with Edge Impulse

When I completed logging the collected data and assigning labels, I started to work on my artificial neural network model (ANN) to detect yogurt consistency (texture) levels before fermentation so as to improve product quality and reduce the total cost for small dairies.

Since Edge Impulse supports almost every microcontroller and development board due to its model deployment options, I decided to utilize Edge Impulse to build my artificial neural network model. Also, Edge Impulse makes scaling embedded ML applications easier and faster for edge devices such as XIAO ESP32C3.

Even though Edge Impulse supports CSV files to upload samples, the data type should be time series to upload all data records in a single file. Therefore, I needed to follow the steps below to format my data set so as to train my model accurately:

* Data Scaling (Normalizing)
* Data Preprocessing

As explained in the previous steps, I assigned yogurt consistency classes empirically while logging yogurt processing data from various batches. Then, I developed a Python application to scale (normalize) and preprocess data records to create appropriately formatted samples (single CSV files) for Edge Impulse.

Since the assigned classes are stored under the *consistency\_level* data field in the *yogurt\_data.csv* file, I preprocessed my data set effortlessly to create samples from data records under these labels:

* 0 — Thinner
* 1 — Optimum
* 2 — Curdling

Plausibly, Edge Impulse allows building predictive models optimized in size and accuracy automatically and deploying the trained model as an Arduino library. Therefore, after scaling (normalizing) and preprocessing my data set to create samples, I was able to build an accurate neural network model to predict yogurt consistency levels and run it on XIAO ESP32C3 effortlessly.

You can inspect [my neural network model on Edge Impulse](https://studio.edgeimpulse.com/public/159184/latest) as a public project.

## Step 5.1: Preprocessing and scaling the data set to create formatted samples for Edge Impulse

If the data type is not time series, Edge Impulse cannot distinguish data records as individual samples from one CSV file while adding existing data to an Edge Impulse project. Therefore, the user needs to create a separate CSV file for each sample, including a header defining data fields.

To scale (normalize) and preprocess my data set so as to create individual CSV files as samples automatically, I developed a Python application consisting of one file:

* process\_dataset.csv

Since Edge Impulse can infer the uploaded sample's label from its file name, the application reads the given CSV file (data set) and generates a separate CSV file for each data record, named according to its assigned yogurt consistency class number under the *consistency\_level* data field. Also, the application adds a sample number incremented by 1 for generated CSV files sharing the same label:

* Thinner.sample\_1.csv
* Thinner.sample\_2.csv
* Optimum.sample\_1.csv
* Optimum.sample\_2.csv
* Curdling.sample\_1.csv
* Curdling.sample\_2.csv

First of all, I created a class named *process\_dataset* in the *process\_dataset.py* file to bundle the following functions under a specific structure.

⭐ Include the required modules.

```
import numpy as np
import pandas as pd
from csv import writer
```

⭐ In the ***init*** function, read the data set from the given CSV file and define the yogurt consistency class names.

```
    def __init__(self, csv_path):
        # Read the data set from the given CSV file.
        self.df = pd.read_csv(csv_path)
        # Define the class (label) names.
        self.class_names = ["Thinner", "Optimum", "Curdling"]
```

⭐ In the *scale\_data\_elements* function, scale (normalize) data elements to define appropriately formatted data items in the range of 0-1.

```
    def scale_data_elements(self):
        self.df["scaled_temperature"] = self.df["temperature"] / 100
        self.df["scaled_humidity"] = self.df["humidity"] / 100
        self.df["scaled_pressure"] = self.df["pressure"] / 1000
        self.df["scaled_milk_temperature"] = self.df["milk_temperature"] / 100
        self.df["scaled_starter_weight"] = self.df["starter_weight"] / 10
        print("Data Elements Scaled Successfully!")
```

⭐ In the *split\_dataset\_by\_labels* function:

⭐ Split data records by the assigned yogurt consistency level (class).

⭐ Add the header defining data fields as the first row.

⭐ Create scaled data records with the scaled data elements and increase the sample number for each scaled data record sharing the same label.

⭐ Then, generate CSV files (samples) from scaled data records, named with the assigned yogurt consistency level and the given sample number.

⭐ Each sample includes five data items \[shape=(5,)]:

\*\[0.2304, 0.7387, 0.34587, 0.4251, 0.421] \*

* temperature
* humidity
* pressure
* milk\_temperature
* starter\_weight

```
    def split_dataset_by_labels(self, class_number):
        l = len(self.df)
        sample_number = 0
        # Split the data set according to the yogurt consistency levels (classes):
        for i in range(l):
            # Add the header as the first row:
            processed_data = [["temperature", "humidity", "pressure", "milk_temperature", "starter_weight"]]
            if(self.df["consistency_level"][i] == class_number):
                row = [self.df["scaled_temperature"][i], self.df["scaled_humidity"][i], self.df["scaled_pressure"][i], self.df["scaled_milk_temperature"][i], self.df["scaled_starter_weight"][i]]
                processed_data.append(row)
                # Increment the sample number:
                sample_number+=1
                # Create a CSV file for each data record, identified with the sample number.
                filename = "data/{}.sample_{}.csv".format(self.class_names[class_number], sample_number)
                with open(filename, "a", newline="") as f:
                    for r in range(len(processed_data)):
                        writer(f).writerow(processed_data[r])
                    f.close()
                print("CSV File Successfully Created: " + filename)
```

⭐ Finally, create appropriately formatted samples as individual CSV files and save them in the *data* folder.

```
dataset.scale_data_elements()
for c in range(len(dataset.class_names)):
    dataset.split_dataset_by_labels(c)
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_data_1.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=9fdfebff0ad693e473d047fb13bd587c" width="1600" height="853" data-path=".assets/images/dairy-manufacturing-with-ai/code_data_1.png" />
</Frame>

🐄🥛📲 After running the application, it creates samples, saves them under the *data* folder, and prints generated CSV file names on the shell for debugging.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/data_collection_2.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=e900b2feffac35be0b9876794e4dc15f" width="1393" height="837" data-path=".assets/images/dairy-manufacturing-with-ai/data_collection_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/data_collection_4.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=43c0d9ad814512768eba2dfad94dc72b" width="1520" height="905" data-path=".assets/images/dairy-manufacturing-with-ai/data_collection_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/data_collection_5.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=97c674930cd667b27b99baf39b844cee" width="1600" height="899" data-path=".assets/images/dairy-manufacturing-with-ai/data_collection_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/data_collection_6.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=e37e3fda9004c8652f9652f720af7deb" width="1556" height="903" data-path=".assets/images/dairy-manufacturing-with-ai/data_collection_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_data_2.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=37ed9591ee2870c88c8fe0b1dd66a907" width="1600" height="852" data-path=".assets/images/dairy-manufacturing-with-ai/code_data_2.png" />
</Frame>

## Step 5.2: Uploading formatted samples to Edge Impulse

After generating training and testing samples successfully, I uploaded them to my project on Edge Impulse.

:hash: First of all, sign up for [Edge Impulse](https://www.edgeimpulse.com/) and create a new project.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_set_1.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=858d4ffee7d70b35f9b2d506fbe8a9e6" width="1600" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/edge_set_1.png" />
</Frame>

:hash: Navigate to the *Data acquisition* page and click the *Upload existing data* button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_set_2.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=c1e4a10eda5e8fcb04803ded64a38d13" width="1600" height="747" data-path=".assets/images/dairy-manufacturing-with-ai/edge_set_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_set_3.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=6a6d33ae02c2e2d14255d8d0cf920aa6" width="1600" height="751" data-path=".assets/images/dairy-manufacturing-with-ai/edge_set_3.png" />
</Frame>

:hash: Then, choose the data category (training or testing) and select *Infer from filename* under *Label* to deduce labels from CSV file names automatically.

:hash: Finally, select CSV files and click the *Begin upload* button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_set_4.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=1df607d9546657ff286579339d58365a" width="1600" height="768" data-path=".assets/images/dairy-manufacturing-with-ai/edge_set_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_set_5.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=5de5fb8b2bf87773686fc5d410e60ba6" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/edge_set_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_set_6.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=22b7c03a23f50fe94389f96426b57f1e" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/edge_set_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_set_7.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=76982873ac595b8ea6e7364b44431d62" width="1600" height="776" data-path=".assets/images/dairy-manufacturing-with-ai/edge_set_7.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_set_8.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=6739221972c583e033037326dfc0ff75" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/edge_set_8.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_set_9.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=6dc511308c146fa83ebd348076d31653" width="1600" height="772" data-path=".assets/images/dairy-manufacturing-with-ai/edge_set_9.png" />
</Frame>

## Step 5.3: Training the model on yogurt consistency levels

After uploading my training and testing samples successfully, I designed an impulse and trained it on yogurt consistency levels (classes).

An impulse is a custom neural network model in Edge Impulse. I created my impulse by employing the *Raw Data* processing block and the *Classification* learning block.

The *Raw Data* processing block generate windows from data samples without any specific signal processing.

The *Classification* learning block represents a Keras neural network model. Also, it lets the user change the model settings, architecture, and layers.

:hash: Go to the *Create impulse* page. Then, select the *Raw Data* processing block and the *Classification* learning block. Finally, click *Save Impulse*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_train_1.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=be3634f8f42297751eb724822fcbcdbb" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/edge_train_1.png" />
</Frame>

:hash: Before generating features for the neural network model, go to the *Raw data* page and click *Save parameters*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_train_2.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=968a9d2b77d8abc106fdffa12c5f0892" width="1600" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/edge_train_2.png" />
</Frame>

:hash: After saving parameters, click *Generate features* to apply the *Raw data* processing block to training samples.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_train_3.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=25f24fa3299633cca7a40fa33c9889be" width="1600" height="776" data-path=".assets/images/dairy-manufacturing-with-ai/edge_train_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_train_4.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=a3ceb0c6ec868f52179031c45ab0dbda" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/edge_train_4.png" />
</Frame>

:hash: Finally, navigate to the *NN Classifier* page and click *Start training*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_train_5.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=5b763c95338df58da4631cbd4387729b" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/edge_train_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_train_6.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=68bf34486a1178a30daf44f3141ec623" width="1600" height="772" data-path=".assets/images/dairy-manufacturing-with-ai/edge_train_6.png" />
</Frame>

According to my experiments with my neural network model, I modified the neural network settings and layers to build a neural network model with high accuracy and validity:

📌 Neural network settings:

* Number of training cycles ➡ 50
* Learning level ➡ 0.005
* Validation set size ➡ 20

📌 Extra layers:

* Dense layer (20 neurons)
* Dense layer (10 neurons)

After generating features and training my model with training samples, Edge Impulse evaluated the precision score (accuracy) as *100%*.

The precision score (accuracy) is approximately *100%* due to the modest volume and variety of training samples from different batches. In technical terms, the model trains on limited validation samples. Therefore, I am still collecting data to improve my training data set.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_train_7.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=4afdef401cc84d3ed77c4181b9ec1dfd" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/edge_train_7.png" />
</Frame>

## Step 5.4: Evaluating the model accuracy and deploying the model

After building and training my neural network model, I tested its accuracy and validity by utilizing testing samples.

The evaluated accuracy of the model is *100%*.

:hash: To validate the trained model, go to the *Model testing* page and click *Classify all*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_test_1.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=a6815195b889995b91e80a0683304f5a" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/edge_test_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_test_2.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=a3496c1fc10df24aa3a3a942473dff9a" width="1600" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/edge_test_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_test_3.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=3a6e2aed9b0d2276289ae6351e6cd2b8" width="1600" height="776" data-path=".assets/images/dairy-manufacturing-with-ai/edge_test_3.png" />
</Frame>

After validating my neural network model, I deployed it as a fully optimized and customizable Arduino library.

:hash: To deploy the validated model as an Arduino library, navigate to the *Deployment* page and select *Arduino library*.

:hash: Then, choose the *Quantized (int8)* optimization option to get the best performance possible while running the deployed model.

:hash: Finally, click *Build* to download the model as an Arduino library.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_deploy_1.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=8b71ddae889e08d6937e87a1ccf2c0e2" width="1600" height="773" data-path=".assets/images/dairy-manufacturing-with-ai/edge_deploy_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_deploy_2.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=0e0bceafd3c4966e566e782fea4ff122" width="1600" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/edge_deploy_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/edge_deploy_3.png?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=ad6dad795e3b906cdbcc6bfa1832a893" width="1600" height="718" data-path=".assets/images/dairy-manufacturing-with-ai/edge_deploy_3.png" />
</Frame>

## Step 6: Setting up the Edge Impulse model on XIAO ESP32C3

After building, training, and deploying my model as an Arduino library on Edge Impulse, I needed to upload the generated Arduino library on XIAO ESP32C3 to run the model directly so as to create an easy-to-use and capable device operating with minimal latency, memory usage, and power consumption.

Since Edge Impulse optimizes and formats signal processing, configuration, and learning blocks into a single package while deploying models as Arduino libraries, I was able to import my model effortlessly to run inferences.

:hash: After downloading the model as an Arduino library in the ZIP file format, go to *Sketch ➡ Include Library ➡ Add .ZIP Library...*

:hash: Then, include the *IoT\_AI-driven\_Yogurt\_Processing\_inferencing.h* file to import the Edge Impulse neural network model.

```
#include &lt;IoT_AI-driven_Yogurt_Processing_inferencing.h>
```

After importing my model successfully to the Arduino IDE, I programmed XIAO ESP32C3 to run inferences when the switch button on the Blynk web application is activated so as to detect yogurt consistency (texture) levels before fermentation.

* Blynk Switch Button ➡ Run Inference

Also, I employed XIAO ESP32C3 to transmit the collected yogurt processing data to the Blynk application every 30 seconds and send the prediction (detection) result after running inferences successfully.

You can download the *AI\_yogurt\_processing\_run\_model.ino* file to try and inspect the code for running Edge Impulse neural network models and communicating with a Blynk application on XIAO ESP32C3.

You can inspect the corresponding functions and settings in Step 4.

⭐ Define the *Template ID*, *Device Name*, and *Auth Token* parameters provided by Blynk.Cloud.

```
#define BLYNK_TEMPLATE_ID "&lt;_TEMPLATE_ID_>"
#define BLYNK_DEVICE_NAME "&lt;_DEVICE_NAME_>"
#define BLYNK_AUTH_TOKEN "&lt;_AUTH_TOKEN_>"
```

⭐ Include the required libraries.

```
#include &lt;WiFi.h>
#include &lt;WiFiClient.h>
#include &lt;BlynkSimpleEsp32.h>
#include &lt;SPI.h>
#include &lt;Adafruit_GFX.h>
#include &lt;Adafruit_SSD1306.h>
#include &lt;SensirionI2CSht4x.h>
#include &lt;DFRobot_HX711_I2C.h>
#include &lt;OneWire.h>
#include &lt;DallasTemperature.h>
```

⭐ Define the required variables for communicating with the Blynk web application and the virtual pins connected to the dashboard widgets.

```
char auth[] = BLYNK_AUTH_TOKEN;
#define TEMP_WIDGET     V4
#define HUMD_WIDGET     V12
#define PRES_WIDGET     V6
#define M_TEMP_WIDGET   V7
#define WEIGHT_WIDGET   V8
#define BUTTON_WIDGET   V9
#define LABEL_WIDGET    V10
```

⭐ Define the required parameters to run an inference with the Edge Impulse model.

⭐ Define the features array (buffer) to classify one frame of data.

```
#define FREQUENCY_HZ        EI_CLASSIFIER_FREQUENCY
#define INTERVAL_MS         (1000 / (FREQUENCY_HZ + 1))

// Define the features array to classify one frame of data.
float features[EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE];
size_t feature_ix = 0;
```

⭐ Define the threshold value (0.60) for the model outputs (predictions).

⭐ Define the yogurt consistency level (class) names:

* Thinner
* Optimum
* Curdling

```
float threshold = 0.60;

// Define the yogurt consistency level (class) names:
String classes[] = {"Thinner", "Optimum", "Curdling"};
```

⭐ Define monochrome graphics.

⭐ Create an array including icons for each yogurt consistency level (class).

```
static const unsigned char PROGMEM *class_icons[] = {thinner, optimum, curdling};
```

⭐ Create the Blynk object with the Wi-Fi network settings and the *Auth Token* parameter.

```
Blynk.begin(auth, ssid, pass);
```

⭐ Initiate the communication between the Blynk web application (dashboard) and XIAO ESP32C3.

```
  Blynk.run();
```

⭐ In the *update\_Blynk\_parameters* function, transfer the collected yogurt processing data to the Blynk web application (dashboard).

```
void update_Blynk_parameters(){
  // Transfer the collected yogurt processing information to the Blynk dashboard.
  Blynk.virtualWrite(TEMP_WIDGET, temperature);
  Blynk.virtualWrite(HUMD_WIDGET, humidity);
  Blynk.virtualWrite(PRES_WIDGET, pressure);
  Blynk.virtualWrite(M_TEMP_WIDGET, m_temperature);
  Blynk.virtualWrite(WEIGHT_WIDGET, weight);
}
```

⭐ Obtain the incoming value from the switch (button) widget on the Blynk dashboard.

⭐ Then, change the model running status depending on the received value (True or False).

```
BLYNK_WRITE(BUTTON_WIDGET){
  int buttonValue = param.asInt();
  if(buttonValue){ model_running = true; }
  else{ Blynk.virtualWrite(LABEL_WIDGET, "Waiting..."); }
}
```

⭐ In the *run\_inference\_to\_make\_predictions* function:

⭐ Scale (normalize) the collected data depending on the given model and copy the scaled data items to the features array (buffer).

⭐ If required, multiply the scaled data items while copying them to the features array (buffer).

⭐ Display the progress of copying data to the features buffer on the serial monitor.

⭐ If the features buffer is full, create a signal object from the features buffer (frame).

⭐ Then, run the classifier.

⭐ Print the inference timings on the serial monitor.

⭐ Obtain the prediction (detection) result for each given label and print them on the serial monitor.

⭐ The detection result greater than the given threshold (0.60) represents the most accurate label (yogurt consistency level) predicted by the model.

⭐ Print the detected anomalies on the serial monitor, if any.

⭐ Finally, clear the features buffer (frame).

```
void run_inference_to_make_predictions(int multiply){
  // Scale (normalize) data items depending on the given model:
  float scaled_temperature = temperature / 100;
  float scaled_humidity = humidity / 100;
  float scaled_pressure = pressure / 1000;
  float scaled_milk_temperature = m_temperature / 100;
  float scaled_starter_weight = weight / 10;

  // Copy the scaled data items to the features buffer.
  // If required, multiply the scaled data items while copying them to the features buffer.
  for(int i=0; i&lt;multiply; i++){
    features[feature_ix++] = scaled_temperature;
    features[feature_ix++] = scaled_humidity;
    features[feature_ix++] = scaled_pressure;
    features[feature_ix++] = scaled_milk_temperature;
    features[feature_ix++] = scaled_starter_weight;
  }

  // Display the progress of copying data to the features buffer.
  Serial.print("Features Buffer Progress: "); Serial.print(feature_ix); Serial.print(" / "); Serial.println(EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE);

  // Run inference:
  if(feature_ix == EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE){
    ei_impulse_result_t result;
    // Create a signal object from the features buffer (frame).
    signal_t signal;
    numpy::signal_from_buffer(features, EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE, &signal);
    // Run the classifier:
    EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);
    ei_printf("\nrun_classifier returned: %d\n", res);
    if(res != 0) return;

    // Print the inference timings on the serial monitor.
    ei_printf("Predictions (DSP: %d ms., Classification: %d ms., Anomaly: %d ms.): \n",
        result.timing.dsp, result.timing.classification, result.timing.anomaly);

    // Obtain the prediction results for each label (class).
    for(size_t ix = 0; ix &lt; EI_CLASSIFIER_LABEL_COUNT; ix++){
      // Print the prediction results on the serial monitor.
      ei_printf("%s:\t%.5f\n", result.classification[ix].label, result.classification[ix].value);
      // Get the predicted label (class).
      if(result.classification[ix].value >= threshold) predicted_class = ix;
    }
    Serial.print("\nPredicted Class: "); Serial.println(predicted_class);

    // Detect anomalies, if any:
    #if EI_CLASSIFIER_HAS_ANOMALY == 1
      ei_printf("Anomaly : \t%.3f\n", result.anomaly);
    #endif

    // Clear the features buffer (frame):
    feature_ix = 0;
  }
}
```

⭐ If the switch (button) widget on the Blynk dashboard is activated, start running an inference with the Edge Impulse model to predict the yogurt consistency level.

⭐ Then, change the model running status to False.

```
if(model_running){ run_inference_to_make_predictions(1); model_running = false; }
```

⭐ If the Edge Impulse model predicts a yogurt consistency level (class) successfully:

⭐ Display the prediction (detection) result (class) on the SSD1306 OLED screen with its assigned monochrome icon.

⭐ Transfer the predicted label (class) to the Blynk web application (dashboard) to inform the user.

⭐ Clear the predicted label.

```
  if(predicted_class != -1){
      // Transfer the predicted label (class) to the Blynk application (dashboard).
      Blynk.virtualWrite(LABEL_WIDGET, classes[predicted_class]);
      // Print the predicted label (class) on the built-in screen.
      display.clearDisplay();
      display.drawBitmap(48, 0, class_icons[predicted_class], 32, 32, SSD1306_WHITE);
      display.setTextSize(1);
      display.setTextColor(SSD1306_WHITE);
      display.setCursor(0,40);
      display.println("Transferred to Blynk");
      String c = "Class: " + classes[predicted_class];
      int str_x = c.length() * 6;
      display.setCursor((SCREEN_WIDTH - str_x) / 2, 56);
      display.println(c);
      display.display();
      // Clear the predicted label (class).
      predicted_class = -1;
      delay(1000);
  }
```

⭐ Every 30 seconds, transmit the collected environmental factors and culture amount to the Blynk web application so as to update the assigned widgets for each data element on the Blynk dashboard.

```
  if(millis() - timer >= 30*1000){ update_Blynk_parameters(); Serial.println("\n\nBlynk Dashboard: Data Transferred Successfully!\n"); timer = millis(); }
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_run_1.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=a47d2bf7fc43e33c1911d0c92f9ef163" width="1561" height="771" data-path=".assets/images/dairy-manufacturing-with-ai/code_run_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_run_2.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=a136be4b7051a07545abda42230e62d3" width="1520" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/code_run_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_run_3.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=def0029a8200b979a5b8f2e448582c59" width="1600" height="749" data-path=".assets/images/dairy-manufacturing-with-ai/code_run_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_run_4.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=15ff21f16e4e720051f71a1a0924f064" width="1600" height="708" data-path=".assets/images/dairy-manufacturing-with-ai/code_run_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_run_5.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=d49ae7e62b508f8f87092e8a553808d0" width="1565" height="775" data-path=".assets/images/dairy-manufacturing-with-ai/code_run_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/code_run_6.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=0032839d81ffa7bc067866d48fdc61d1" width="1600" height="769" data-path=".assets/images/dairy-manufacturing-with-ai/code_run_6.png" />
</Frame>

## Step 7: Running the model on XIAO ESP32C3 to predict yogurt texture levels

My Edge Impulse neural network model predicts possibilities of labels (yogurt consistency classes) for the given features buffer as an array of 3 numbers. They represent the model's *"confidence"* that the given features buffer corresponds to each of the three different yogurt consistency levels (classes) \[0 - 2], as shown in Step 5:

* 0 — Thinner
* 1 — Optimum
* 2 — Curdling

After executing the *AI\_yogurt\_processing\_run\_model.ino* file on XIAO ESP32C3:

🐄🥛📲 The device shows the opening screen if the sensor and MicroSD card module connections with XIAO ESP32C3 are successful.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_1.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=83aca23dae7004eb437e59f4d8328f30" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_1.jpg" />
</Frame>

🐄🥛📲 Then, the device displays the collected environmental factor measurements and the culture (starter) amount on the SSD1306 OLED screen:

* Temperature (°C)
* Humidity (%)
* Pressure (kPa)
* Milk Temperature (°C)
* Starter Weight (g)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_2.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=508288dd764f9a8fae848963a1c9005b" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_2.1.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=41583f8d919f118c2b92b01556fa60f2" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_2.1.jpg" />
</Frame>

🐄🥛📲 Also, every 30 seconds, the device transmits the collected yogurt processing data to the Blynk web application so as to update the assigned widgets for each data element on the Blynk dashboard.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_run_1.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=6c3bf49a67fe92d936031694f40aec46" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_run_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_run_2.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=b7f8cbed095d8ba79d247368d5ffba9d" width="1600" height="850" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_run_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_run_3.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=b2b0a9c5930aa8c9373621219a5fcacd" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_run_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_run_4.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=4f3a3ef7eeed8699bcb37ab91e2b17e4" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_run_4.png" />
</Frame>

🐄🥛📲 If the switch (button) widget is activated on the Blynk dashboard, the device runs an inference with the Edge Impulse model and displays the detection result, which represents the most accurate label (yogurt consistency class) predicted by the model.

🐄🥛📲 Each yogurt consistency level (class) has a unique monochrome icon to be shown on the SSD1306 OLED screen when being predicted (detected) by the model:

* Thinner
* Optimum
* Curdling (Lumpy)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_run_5.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=d4470eb95bcf8cad2eea6f538227181a" width="1600" height="851" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_run_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_3.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=83ea229b0e500dd0014a77b5bb1c481f" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_4.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=389a6dbc4609b4bc1d134f044c43c5de" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_5.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=279d170ad5e2434b5b06f3a7a178f317" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_5.jpg" />
</Frame>

🐄🥛📲 After running the inference successfully, the device also transfers the predicted label (class) to the Blynk web application (dashboard) to inform the user.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/Y7jMOb3qtS7qHRYs/.assets/images/dairy-manufacturing-with-ai/blynk_run_6.png?fit=max&auto=format&n=Y7jMOb3qtS7qHRYs&q=85&s=3b051f4b8c7fd471ea57a40031cf7822" width="1600" height="850" data-path=".assets/images/dairy-manufacturing-with-ai/blynk_run_6.png" />
</Frame>

🐄🥛📲 Also, the device prints notifications and sensor measurements on the serial monitor for debugging.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/serial_run_0.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=45b177c4ee79144ba4c8a19ad14bf20f" width="1600" height="848" data-path=".assets/images/dairy-manufacturing-with-ai/serial_run_0.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/serial_run_1.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=5459ba48976a5ec298a4d62a28a29f61" width="1600" height="851" data-path=".assets/images/dairy-manufacturing-with-ai/serial_run_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/serial_run_2.png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=f4df4e51bc34d811163cf5d1452b4062" width="1600" height="851" data-path=".assets/images/dairy-manufacturing-with-ai/serial_run_2.png" />
</Frame>

As far as my experiments go, the device detects yogurt consistency (texture) levels precisely before fermentation :)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_6.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=9fb00b2c1459c9b25e16f3d4126bc091" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_7.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=05ccfef4c87b3c2e2ecfd5b832ef6047" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_8.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=97c69c65399f88589d82dcbeb4c11647" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/dairy-manufacturing-with-ai/gif_run.gif" />
</Frame>

After the fermentation process, I had yogurt batches with the exact consistency (texture) levels predicted by the Edge Impulse neural network model.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/run_model_9.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=8c2d582a7565dc154d20162ad1f45f29" width="750" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/run_model_9.jpg" />
</Frame>

## Videos and Conclusion

[Data collection | IoT AI-driven Yogurt Processing & Texture Prediction w/ Blynk](https://youtu.be/cpmZZqDV1yA)

[Experimenting with the model | IoT AI-driven Yogurt Processing & Texture Prediction w/ Blynk](https://youtu.be/aNV-MDR6RSI)

## Further Discussions

By applying neural network models trained on temperature, humidity, pressure, milk temperature, and culture weight measurements in detecting yogurt consistency (texture) levels, we can achieve to:

🐄🥛📲 improve product quality without food additives,

🐄🥛📲 reduce the total cost for local dairies,

🐄🥛📲 incentivize small businesses to produce organic (natural) yogurt.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/s-SUHRvkknXz1z1R/.assets/images/dairy-manufacturing-with-ai/home_3.jpg?fit=max&auto=format&n=s-SUHRvkknXz1z1R&q=85&s=1c989ef32ca429773793455f16fbc980" width="1333" height="1000" data-path=".assets/images/dairy-manufacturing-with-ai/home_3.jpg" />
</Frame>

## References

\[^1] Good Food team, *Yogurt*, BBC Good Food, *[https://www.bbcgoodfood.com/glossary/yogurt-glossary](https://www.bbcgoodfood.com/glossary/yogurt-glossary)*

\[^2] *Metabolism Characteristics of Lactic Acid Bacteria and the Expanding Applications in Food Industry*, Front. Bioeng. Biotechnol., 12 May 2021, Sec. Synthetic Biology, *[https://doi.org/10.3389/fbioe.2021.612285](https://doi.org/10.3389/fbioe.2021.612285)*


Built with [Mintlify](https://mintlify.com).