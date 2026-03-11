# Source: https://docs.edgeimpulse.com/projects/expert-network/ai-pipeline-inspection-mmwave-radar.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI-Assisted Pipeline Diagnostics and Inspection with mmWave Radar

Created By: Kutluhan Aktar

Public Project Link: [https://studio.edgeimpulse.com/public/214371/latest](https://studio.edgeimpulse.com/public/214371/latest)

## Description

Since the beginning of the industrial revolution, accurate pipeline system maintenance has been crucial to keeping machine operations sustainable, profitable, and stable. Even though all machine parts and control units evolved from occupying rooms to fitting in our packets, pipeline system maintenance is still one of the most important aspects of keeping machines healthy while running automated manufacturing operations. From cooling processors with water on motherboards to supplying liquefied metal alloy or plastic for injection molding processes, a faulty pipeline system can engender various manufacturing problems while running machine operations, especially for small businesses with limited budgets not enough to cover expensive overhauling costs.

Therefore, establishing an efficient and accurate pipeline diagnostics mechanism conforming to general maintenance regulations can assist technicians in keeping machines durable far more than anticipated and prevent companies from squandering their resources on replacing or repairing high-value machine components due to the omission of proper pipeline diagnostics.

Pipe cracks are one of the most common defects while transferring liquids, especially with differing thermal conditions. During machine operations, mechanical and thermal stress cause minute defects in pipelines due to fatigue. When these small defects accumulate, the outcome mostly results in a varying inside turbulent pressure, which leads to slight form (shape) disfigurations, resulting in gradual deficiency over time due to tension. Furthermore, depending on operation processes and environment, there are lots of possible pipeline defects in addition to cracks, such as corrosion, abrasion, clogged joints due to chemical residue, leaking connection points due to high gas emissions, etc.

Although there are different external pipeline inspection devices utilizing computer vision (camera), magnetic field measurements, and acoustic detection (microphone)\[^1], these methods cannot be applied interchangeably to different pipeline systems. For instance, a device utilizing object detection with a thermal camera may not be able to detect internal crystals due to high gas permeability in a pipeline system transporting antifreeze to cool components.

Nonetheless, some groundbreaking new methods aim to detect potential pipeline system failures by examining changes in the vibration characteristics. Since accumulating stress due to pipeline defects affects material integrity and structure gradually, these failures can be detected by inspecting fluctuating vibrations as a non-destructive testing and evaluation (NDT\&E) mechanism. For example, in recent examinations, researchers applied ground penetrating radar (GPR) to detect cracks in a buried pipe\[^2] and microwave-based synthetic aperture radar (SAR) to inspect pipeline defects\[^3].

After perusing recent research papers on pipeline diagnostics based on vibrations, I noticed there are nearly no appliances focusing on collecting data from a mmWave radar module to extract data parameters, detecting potential pipeline defects, and providing real-time detection results with captured images of the deformed pipes for further examination. Therefore, I decided to build a budget-friendly and compact mechanism to diagnose pipeline defects with machine learning and inform the user of the model detection results with captured images of the deformed pipes simultaneously, in the hope of assisting businesses in keeping machines durable and stable by eliminating basic pipeline defects.

To diagnose different pipeline defects, I needed to collect accurate vibration measurements from a pipeline system so as to train my neural network model with notable validity. Therefore, I decided to build a simple pipeline system by utilizing pipes and fittings (adapters) with mediocre thermal conductivity, demonstrating three different pipeline defects in each primary section — color-coded. Since Seeed Studio provides mmWave radar modules with built-in algorithms to detect minute vibration changes to evaluate respiratory rate, heart rate, and sleep status, I decided to utilize a 60GHz mmWave module to extract my data parameters via the mentioned algorithms. Since Arduino Nicla Vision is a ready-to-use and compact edge device with a 2MP color camera and integrated WiFi/BLE connectivity, I decided to use Nicla Vision so as to run my neural network model, capture images of the deformed pipes, and inform the user of the model detection results with the captured pipe images. Due to architecture and library incompatibilities, I connected the mmWave module to Arduino Nano in order to extract and transmit radar data parameters to Nicla Vision via serial communication. Then, I connected four control buttons to Arduino Nano to send commands with the collected mmWave data parameters to Nicla Vision. Also, I added an ILI9341 TFT LCD screen to display the interface menu, including a custom radar indicator.

Since I focused on building a full-fledged AIoT device diagnosing pipeline system defects, I decided to develop a web application from scratch providing various features to the user. Firstly, I employed the web application to obtain the collected mmWave data parameters with the selected label from Nicla Vision via an HTTP GET request, save the received information to a MySQL database table, and display the stored data records on its interface in descending order. Via a single HTML button on the interface, the web application can also generate a pre-formatted CSV file from the stored data records in the database without requiring any additional procedures.

After completing my data set by collecting data from the custom pipeline system I assembled, I built my artificial neural network model (ANN) with Edge Impulse to make predictions on pipeline system defects (classes). Since Edge Impulse is nearly compatible with all microcontrollers and development boards, I had not encountered any issues while uploading and running my model on Nicla Vision. As labels, I utilized the three basic pipeline defects manifested by each main line (color-coded on the system):

* Clogged
* Cracked
* Leakage

After training and testing my neural network model, I deployed and uploaded the model on Nicla Vision as an Arduino library. Therefore, the device is capable of diagnosing pipeline system defects by running the model independently without any additional procedures or latency.

Then, I utilized the web application to obtain the model detection results with captured images of the deformed pipes from Nicla Vision via HTTP POST requests, save the received information to a particular MySQL database table, and display the stored model results with the assigned detection images on the application interface in descending order simultaneously.

Due to the fact that Nicla Vision can only generate raw image buffer (RGB565), this complementing web application executes a Python script to convert the received raw image buffer to a JPG file automatically before saving it to the server. After saving the converted image successfully, the web application adds it to the HTML table on the interface consecutively, allowing the user to inspect all previous model detection results and the assigned deformed pipe images in descending order.

Considering harsh operating conditions, I decided to design a unique PCB after completing the wiring on a breadboard for the prototype and testing my code and neural network model. Since I wanted my PCB design to emanate a unique and powerful water-damage sensation, I decided to design a Dragonite-inspired PCB since it was the first scary water-related Pokémon for me from the anime, despite being a Dragon/Flying type Pokémon. Thanks to the unique orange solder mask and blue silkscreen combination, only provided by PCBWay, this PCB turned out to be my coolest design yet :)

Since I decided to host my web application on LattePanda 3 Delta, I wanted to build a mobile and compact apparatus to display the web application in the field without requiring an additional procedure. To improve the user experience, I utilized a high-quality 8.8" IPS monitor from Elecrow. As explained in the following steps, I designed a two-part case (3D printable) in which I placed the Elecrow IPS monitor.

Lastly, to make the device as sturdy and compact as possible, I designed an emphasizing liquid-themed case with a sliding front cover and a modular camera holder providing a circular snap-fit joint (3D printable) for Nicla Vision and the 60GHz mmWave radar module.

So, this is my project in a nutshell 😃

In the following steps, you can find more detailed information on coding, capturing deformed pipe images, building a neural network model with Edge Impulse, running the model on Nicla Vision, and developing a full-fledged web application to obtain data parameters with captured images from Nicla Vision via HTTP POST requests.

🎁🎨 Huge thanks to [PCBWay](https://www.pcbway.com/) for sponsoring this project.

🎁🎨 Huge thanks to [Elecrow](https://www.elecrow.com/?idd=3) for sending me an [Elecrow 8.8" IPS Monitor (1920\*480)](https://www.elecrow.com/elecrow-8-8-inch-display-1920-480-ips-screen-lcd-panel-raspberry-pi-compatible-monitor.html?idd=3).

🎁🎨 Huge thanks to [DFRobot](https://www.dfrobot.com/?tracking=60f546f8002be) for sending me a [LattePanda 3 Delta 864](https://www.dfrobot.com/product-2594.html?tracking=60f546f8002be)

🎁🎨 Also, huge thanks to [Anycubic](https://www.anycubic.com/) for sponsoring a brand-new [Anycubic Kobra 2](https://www.anycubic.com/products/kobra-2).

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/finished_3.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=63e11b7b042259ed926eed3caa1cd703" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/finished_3.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/home_0.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=19d2576d93c5906424c8e1ee7bed3554" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/home_0.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_12.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=c74f8e187f68bad6bd99ab7d8743c51d" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_12.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_1.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=d8c9ccff45b95bf2d2abbba54f988c89" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_4.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=73260fa64728efb77b7c258cf1879a3c" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_4.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_6.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=368a74b6a6ba7c2ec8421fa438e80666" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_6.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_8.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=47086d844a871accbf99e44b294baa0b" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_8.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/ai-pipeline-inspection-mmwave/gif_collect_2.gif" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/run_1.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=b70fb21699db6b3102b7a3e9311746a3" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/run_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/run_2.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=756d146f8856540e54c19100525ba593" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/run_2.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/finished_5.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=f4b581b802037d5fa3f2421d6dd3b47f" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/finished_5.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/ai-pipeline-inspection-mmwave/gif_run_2.gif" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_2.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=eece9406a083ab028be55c958f43d74e" width="1600" height="852" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_4.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=e4beee12d26b1d203e1e0cb63b82e3d1" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_7.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=8f0bb7f5fbda6cf2c179c2043001467a" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_7.png" />
</Frame>

## Step 1: Designing and soldering the Dragonite-inspired PCB

Before prototyping my Dragonite-inspired PCB design, I tested all connections and wiring with Nicla Vision and Arduino Nano. Then, I checked the data transfer processes between Nicla Vision and the web application hosted on LattePanda 3 Delta.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/breadboard_1.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=edf59a7c4d417d2fc620b62229d76cc5" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/breadboard_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/breadboard_2.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=8edbb5bc6ed8f1c0d55d3baf33cb1131" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/breadboard_2.jpg" />
</Frame>

Then, I designed my Dragonite-inspired PCB by utilizing KiCad. As mentioned earlier, I wanted to design my PCB based on Dragonite since it was the first Pokémon that made me afraid of a water attack out of nowhere, despite being a Dragon/Flying type Pokémon :) Thanks to the unique orange solder mask and blue silkscreen combination, only provided by PCBWay, this PCB conveys a unique and effective water-damage sensation. I attached the Gerber file of the PCB below: You can order my design from PCBWay to build this device diagnosing pipeline system defects.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_1.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=0a4b1b9a2364a1c905b880855d792629" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_2.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=2eda846b9ab09c5499ae99b23d200a88" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_2.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_3.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=7cb3911079c1d58924a1753904345fbc" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_3.jpg" />
</Frame>

First of all, by utilizing a TS100 soldering iron, I attached headers (female), pushbuttons (6x6), resistors (220Ω), a 5mm common anode RGB LED, and a power jack to the PCB.

📌 Component list on the PCB:

*A1 (Headers for Arduino Nano)*

*Nicla1 (Headers for Nicla Vision)*

*mmWave1 (Headers for 60GHz mmWave Module)*

*S1 (Headers for ILI9341 TFT LCD Screen)*

*L1, L2, L3 (Headers for Bi-Directional Logic Level Converter)*

*K1, K2, K3, K4 (6x6 Pushbutton)*

*D1 (5mm Common Anode RGB LED)*

*R1, R2, R3 (220Ω Resistor)*

*J1 (Power Jack)*

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_4.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=f4e7178ebd0827128d4b5d4c24fbb6b6" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_4.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_5.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=b397381fbd08f60b07812525eef0028b" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_5.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_6.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=c7eedcb667a0fd6a4ad1f5c1e1b4de62" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_6.jpg" />
</Frame>

## Step 1.1: Making connections and adjustments

```
// Connections
// Arduino Nicla Vision :
//                                Arduino Nano
// UART_TX (PA_9)   --------------- A0
// UART_RX (PA_10)  --------------- A1
&
&
&
// Arduino Nano :
//                                Arduino Nicla Vision
// A0   --------------------------- UART_TX (PA_9)
// A1   --------------------------- UART_RX (PA_10)
//                                Seeed Studio 60GHz mmWave Sensor
// A2   --------------------------- TX
// A3   --------------------------- RX
//                                2.8'' 240x320 TFT LCD Touch Screen (ILI9341)
// D10  --------------------------- CS
// D9   --------------------------- RESET
// D8   --------------------------- D/C
// D11  --------------------------- SDI (MOSI)
// D13  --------------------------- SCK
// 3.3V --------------------------- LED
// D12  --------------------------- SDO(MISO)
//                                Control Button (A)
// D2   --------------------------- +
//                                Control Button (B)
// D4   --------------------------- +
//                                Control Button (C)
// D7   --------------------------- +
//                                Control Button (D)
// A4   --------------------------- +
//                                5mm Common Anode RGB LED
// D3   --------------------------- R
// D5   --------------------------- G
// D6   --------------------------- B
```

After completing soldering, I attached all remaining components to the Dragonite PCB via headers — Nicla Vision, Arduino Nano, 60GHz mmWave radar module, bi-directional logic level converters, and ILI9341 TFT LCD screen.

Due to architecture and library incompatibilities, I decided to connect the mmWave module and the ILI9341 TFT LCD screen to Arduino Nano so as to extract and display data parameters. Then, I utilized Arduino Nano to transmit the collected mmWave data parameters and user commands to Nicla Vision via serial communication.

Since Arduino Nano operates at 5V and Nicla Vision requires 3.3V logic level voltage, they cannot be connected with each other directly. Therefore, I utilized a bi-directional logic level converter to shift the voltage for the connections between Nicla Vision and Arduino Nano.

Even though the ILI9341 TFT screen can be supplied with 5V, it generates 3.3V interface voltage. Therefore, connecting its SPI pins to a 5V board like Arduino Nano leads to black screen and freezing issues. To make the ILI9341 screen stable, I utilized two bi-directional logic level converters shifting the voltage for the connections between the ILI9341 screen and Arduino Nano.

To be able to transfer commands to Nicla Vision via serial communication, I connected the software serial port of Arduino Nano (Nicla) to the hardware serial port of Nicla Vision (Serial1). To communicate with the [MR60BHA1 60GHz radar module](https://wiki.seeedstudio.com/Radar_MR60BHA1/), I connected the software serial port of Arduino Nano (mmWave) to the module's built-in UART interface.

I utilized the ILI9341 TFT screen to display ongoing operations and visualize the extracted mmWave data parameters by creating a simple radar indicator. Then, I added four control buttons to transfer the collected data parameters and user commands to Nicla Vision via serial communication. Also, I added an RGB LED to inform the user of the device status, denoting serial communication and data collection success.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_7.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=d734ae476417c7f89e67756e4fea65b9" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_7.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_8.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=a56059b1c4c545f654ab01ed4336e714" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_8.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_9.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=1370f04186ed48ae1d4ce92bc690010b" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_9.jpg" />
</Frame>

## Step 2: Designing and printing a liquid-themed case w/ Anycubic Kobra 2

Since I focused on building a user-friendly and accessible mechanism that collects mmWave data parameters and runs a neural network model to inform the user of the diagnosed pipeline defects via a PHP web application, I decided to design a rigid and compact case allowing the user to place the 60GHz mmWave module and position the built-in GC2145 camera on Nicla Vision effortlessly. To avoid overexposure to dust and prevent loose wire connections, I added a sliding front cover aligned proportionally to the diagonal top surface. Then, I designed a modular camera holder mountable to the back of the case via a circular snap-fit joint. Also, I decided to emboss pipe icons and the Arduino symbol on the sliding front cover to emphasize the edge pipeline diagnostic processes.

Since I needed to attach the Dragonite PCB to the main case, I decided to design an oblique structure for the case. In that regard, I was able to fit the PCB in the case without enlarging the case dimensions.

I designed the main case, its sliding front cover, and the modular camera holder in Autodesk Fusion 360. You can download their STL files below.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/model_1.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=522ea54e48909fa9fba5153dc27b730b" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_2.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=1cef9ae2556f5ba5de44daeac1d51ef5" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_3.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=72127fd28cf52870510170f20f854975" width="1600" height="850" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_4.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=2adb72cde44816fc796090ae1c97a616" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_5.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=4323e0e20030fc3b037cde3670808016" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_5.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_6.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=a50fe56d3b93dd31f0557024db2a7337" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_6.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_7.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=44a2dfabefda57fb19499b0de3d043c1" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_7.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_8.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=9ba224305c12f03c06d2eba07122e46c" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_8.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_9.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=e41b8fcba4a6a9835368ca134a8ae8ec" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_9.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/model_10.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=961ecfd7d071c57d21d958d5d7d090d6" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_10.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/model_11.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=d8c1eca559e34403e807d11ba1949bf0" width="1600" height="850" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_11.png" />
</Frame>

Then, I sliced all 3D models (STL files) in Ultimaker Cura.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/model_12.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=fb03f3df46ddb4cbb401938e6365fd25" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_12.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/model_13.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=962e2637b4f490ae484502e118928996" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_13.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_14.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=5f021aa1fb68c800a6d99ac6c37c82f9" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_14.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_15.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=0c8a31716651fccc162078fe9b7e83c8" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_15.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_16.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=1a2421aaf57c034e1a2158f7122d5ce0" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_16.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_17.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=ca94b42d21e67312ca087db9d8658d03" width="1600" height="850" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_17.png" />
</Frame>

Since I wanted to create a shiny structure for the main case and apply a unique liquid theme indicating water damage, I utilized these PLA filaments:

* eSilk Cyan
* ePLA-Matte Light Blue

Finally, I printed all parts (models) with my brand-new Anycubic Kobra 2 3D Printer.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/printed_1.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=6deaa9106377afb5726fa4f1ffcf8c0a" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/printed_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/printed_2.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=72c93021c05c8df4c7bbcca5eec2330e" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/printed_2.jpg" />
</Frame>

Since Anycubic Kobra 2 is budget-friendly and specifically designed for high-speed printing, I highly recommend Anycubic Kobra 2 if you are a maker or hobbyist needing to print multiple prototypes before finalizing a complex project.

Thanks to its upgraded direct extruder, Anycubic Kobra 2 provides 150mm/s recommended print speed (up to 250mm/s) and dual-gear filament feeding. Also, it provides a cooling fan with an optimized dissipation design to support rapid cooling complementing the fast printing experience. Since the Z-axis has a double-threaded rod structure, it flattens the building platform and reduces the printing layers, even at a higher speed.

Furthermore, Anycubic Kobra 2 provides a magnetic suction platform on the heated bed for the scratch-resistant spring steel build plate allowing the user to remove prints without any struggle. Most importantly, you can level the bed automatically via its user-friendly LeviQ 2.0 automatic bed leveling system. Also, it has a smart filament runout sensor and the resume printing function for power failures.

:hash: First of all, install the gantry and the spring steel build plate.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_1.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=474c63c00492a11b3b37ead76946dc77" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_2.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=e90b639c9fa269135048f101b1be86e9" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_2.jpg" />
</Frame>

:hash: Install the print head, the touch screen, and the filament runout sensor.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_3.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=573b987414d3e76836bdae05baf31103" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_3.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_4.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=04a7c96346bb3ac40d3d8072921f7c64" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_4.jpg" />
</Frame>

:hash: Connect the stepper, switch, screen, and print head cables. Then, attach the filament tube.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_5.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=72cac420970e1decdf258d3e00e1425d" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_5.jpg" />
</Frame>

:hash: If the print head is shaking, adjust the hexagonal isolation column under the print head.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_6.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=a484d80085d5236dde7ef6f4a9e7aff8" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_6.jpg" />
</Frame>

:hash: Go to *Prepare➡ Leveling ➡ Auto-leveling* to initiate the LeviQ 2.0 automatic bed leveling system.

:hash: After preheating and wiping the nozzle, Anycubic Kobra 2 probes the predefined points to level the bed.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_7.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=ccd3d5f3a70005c0d8668073acba7051" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_7.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_8.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=24590fe4ab5d9a1122065092db7a97fc" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_8.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_9.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=bb75bd76f8b266cc6511d942b488c35d" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_9.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_10.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=bdda6e55112e4935a259bb3d1b1d42f6" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_10.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_11.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=d2470ef7558fbb6141424d09f8dfd9cd" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_11.jpg" />
</Frame>

:hash: Finally, fix the filament tube with the cable clips, install the filament holder, and insert the filament into the extruder.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_12.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=f2037308408a88365ae0e192c82dff81" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_assembly_12.jpg" />
</Frame>

:hash: Since Anycubic Kobra 2 is not officially supported by Cura yet, download the latest [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/) version and import the printer profile (configuration) file provided by Anycubic.

:hash: Then, create a custom printer profile on Cura for Anycubic Kobra 2 and change *Start G-code* and *End G-code*.

:hash: Based on the provided *Start G-code* and *End G-code* in the configuration file, I modified new *Start G-code* and *End G-code* compatible with Cura.

```
Start G-code:

G90 ; use absolute coordinates
M83 ; extruder relative mode
G28 ; move X/Y/Z to min endstops
G1 Z2.0 F3000 ; lift nozzle a bit
G92 E0 ; Reset Extruder
G1 X10.1 Y20 Z0.28 F5000.0 ; Move to start position
G1 X10.1 Y200.0 Z0.28 F1500.0 E15 ; Draw the first line
G1 X10.4 Y200.0 Z0.28 F5000.0 ; Move to side a little
G1 X10.4 Y20 Z0.28 F1500.0 E30 ; Draw the second line
G92 E0 ; zero the extruded length again
G1 E-2 F500 ; Retract a little
M117
G21 ; set units to millimeters
G90 ; use absolute coordinates
M82 ; use absolute distances for extrusion
G92 E0
M107

End G-code:

M104 S0 ; Extruder off
M140 S0 ; Heatbed off
M107    ; Fan off
G91     ; relative positioning
G1 E-5 F3000
G1 Z+0.3 F3000 ; lift print head
G28 X0  F3000
M84            ; disable stepper motors
```

:hash: Finally, adjust the official printer settings depending on the filament type while copying them from PrusaSlicer to Cura.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_1.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=498a98cd680e34c3957e6d8d3590dd97" width="1600" height="851" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_2.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=f5d6b45a5ac21937ae2e558e98d730b7" width="1600" height="850" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_3.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=670136e4efdb790cf74c50f60cbce543" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_4.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=ce49b427d141567c2ec0c034ccedc7be" width="1600" height="850" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_5.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=a2c83f929e916f34ebb316a318f9c27b" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_5.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_6.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=377980d3589e8fed8858d094bfc3c418" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_6.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_7.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=2d0b2d3fc3db85bfe2a2340cea4761ba" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/kobra_2_set_7.png" />
</Frame>

## Step 2.1: Assembling the liquid-themed case

After printing all parts (models), I fastened Dragonite PCB to the diagonal top surface of the main case via a hot glue gun.

I placed Nicla Vision and the 60GHz mmWave module in the modular camera holder. Then, I attached the camera holder to the main case via its circular snap-fit joint.

Finally, I inserted the sliding front cover via the dents on the diagonal top surface of the main case.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_1.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=ff9326b6d166eb8358725bd8d838453e" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_2.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=b9bfce3090a1547692afea13c8b06f09" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_2.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_3.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=89f16cc540165446b778a6d1a7d39846" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_3.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_4.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=4f6f4777d9277ecaf5327f871957d673" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_4.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_5.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=09485627a7c35d5c011cf81b4280258d" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_5.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_6.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=e49f21900036a86d366bd4db9c5496c8" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_6.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_7.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=dafb3187c30e11289444013114942164" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_7.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_8.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=57f9656092ecaeba1de7f76257841457" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_8.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_9.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=751e67afa030ae90771614a86969df3c" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_9.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_10.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=e7b2c1c6fe16d2d3d3bef1a035846a82" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_10.jpg" />
</Frame>

As mentioned earlier, the modular camera holder can be utilized to place the 60GHz mmWave module and position the built-in GC2145 camera on Nicla Vision.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_11.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=b9634834423aa402197e221de6af692f" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_11.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_12.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=c74f8e187f68bad6bd99ab7d8743c51d" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_12.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/assembly_13.jpg?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=1afa0766e4f8907992cb2f7d0fc5c42c" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/assembly_13.jpg" />
</Frame>

## Step 2.2: Creating a LattePanda Deck to display the web application

Since I decided to utilize the web application to display the collected data parameters, generate the pre-formatted CSV file from the stored data records in the database, and show the model detection results with the captured images of the deformed pipes, I wanted to create a unique apparatus to inspect the web application.

Since I host this web application on my LattePanda 3 Delta, I decided to design a unique and compact LattePanda Deck compatible with not only LattePanda but also any single-board computer supporting HDMI.

I decided to employ [Elecrow's 8.8" (1920\*480) high-resolution IPS monitor](https://www.elecrow.com/elecrow-8-8-inch-display-1920-480-ips-screen-lcd-panel-raspberry-pi-compatible-monitor.html?idd=3) as the screen of my LattePanda Deck. Thanks to its converter board, this monitor can be powered via a USB port and works without installing any drivers. Therefore, it is a compact plug-and-play monitor for LattePanda 3 Delta, providing high resolution and up to 60Hz refresh rate.

Due to the fact that I wanted to build a sturdy and easy-to-use deck, I designed a two-part case covering the screen frame and providing a slot for the converter board. To avoid overexposure to dust and provide room for cable management, I added a mountable back cover adorned with the brand logo.

I designed the two-part case and its mountable back cover in Autodesk Fusion 360. You can download their STL files below.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_1.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=4fddfa308125fc7c05919862113f69a8" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_2.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=ccda7b5ba3987ab14f5cfb094b8ad86c" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_3.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=dfd939e2a3720963ab93123500a0ccbb" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_4.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=0674739ac44e2d86d03bd3009e97062c" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_5.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=36a002dcfd2eb50e9248a888fbfd158d" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_5.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_6.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=044e98c9655a6f9cb24bb8221027f919" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_6.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_7.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=91156365c0a740d72a9f5408376d7e5f" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_7.png" />
</Frame>

Then, I sliced all 3D models (STL files) in Ultimaker Cura.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_8.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=0e7e328cc28d9ca576b6fee002f0559d" width="1600" height="851" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_8.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_9.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=994f278d1d5972eacd8d0f7ebaf51cf5" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_9.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/model_elecrow_10.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=1da053f9810757a116db27c003f47020" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/model_elecrow_10.png" />
</Frame>

After printing all deck parts (models) with my Anycubic Kobra 2 3D Printer, I affixed the two-part case together via the hot glue gun.

Then, I fastened the Elecrow's IPS monitor to the case covering the screen frame and inserted the converter board into its slot.

After attaching the required cables to the converter board, I fixed the mountable back cover via M3 screws.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/elecrow_0.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=e552d190de66b269e1ebc3daccf0e8b7" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/elecrow_0.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/elecrow_1.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=c9e47b262a5c4111bae899d5237119fd" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/elecrow_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/elecrow_2.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=d62ca191ddd1295e4b5683bccd27da77" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/elecrow_2.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/elecrow_3.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=3224a07a7490c38f18c5699caeb85f05" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/elecrow_3.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/elecrow_4.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=52c79078116a741f33edd02bbd1c6624" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/elecrow_4.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/elecrow_5.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=99dc214a279b89f2c50af40d80c1ea6a" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/elecrow_5.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/elecrow_6.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=0812ca91c9dbce4b548a2aad23bbb637" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/elecrow_6.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/elecrow_7.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=4ea0470f77b8fab9631a78a8db4ec368" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/elecrow_7.jpg" />
</Frame>

After connecting the converter board to LattePanda 3 Delta via its USB and HDMI ports, LattePanda recognizes the IPS monitor automatically.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/elecrow_8.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=c995f9f018664cf1ed21ade29a5eaf43" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/elecrow_8.jpg" />
</Frame>

## Step 3: Developing a web application displaying real-time database updates in PHP, JavaScript, CSS, and MySQL

To provide an outstanding user interface for generating data samples and displaying model detection results, I developed a full-fledged web application from scratch in PHP, HTML, JavaScript, CSS, and MySQL.

First of all, the web application obtains the extracted mmWave data parameters and the selected pipeline diagnostic class from Nicla Vision via an HTTP GET request. After storing the received information in a particular MySQL database table, the web application lets the user generate a CSV file, including all stored data records as samples.

Also, the web application gets the inference data parameters, the diagnosed pipeline defect (class) by the neural network model, and the captured image of the deformed pipe from Nicla Vision via an HTTP POST request. After saving the received information to a particular MySQL database table for further inspection, the web application converts the received raw image buffer (RGB565) to a JPG file by executing a Python script. Then, the web application updates its interface automatically to show the latest stored information in database tables. On the interface, the application shows model detection results, the assigned detection images, and the collected data parameters in descending order so as to allow the user to check previous records easily.

As shown below, the web application consists of three folders and seven code files:

* /assets
* \-- background.jpg
* \-- class.php
* \-- data\_records.csv
* \-- icon.png
* \-- index.css
* \-- index.js
* /detections
* \-- /images
* \-- rgb565\_converter.py
* index.php
* show\_records.php
* update\_server.php

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/web_app_1.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=dfdc6d399d32bb5a44054b6fc93f0f32" width="1292" height="791" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/web_app_2.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=ceb13717d67bd91ec970bc58f1f18885" width="1301" height="776" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/web_app_3.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=f513c4fae71e65108d58e6dea0ca1761" width="1298" height="822" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_3.png" />
</Frame>

📁 *class.php*

In the *class.php* file, I created a class named *\_main* to bundle the following functions under a specific structure.

⭐ Define the *\_main* class and its functions.

```
class _main {
	public $conn;

	public function __init__($conn){
		$this->conn = $conn;
	}
```

⭐ In the *insert\_new\_data* function, insert the given data parameters extracted from a 60GHz mmWave sensor and the selected class to the *entries* MySQL database table.

```
	public function insert_new_data($date, $mmWave, $class){
		$sql_insert = "INSERT INTO `entries`(`date`, `mmwave`, `class`)
		               VALUES ('$date', '$mmWave', '$class');"
			          ;
		if(mysqli_query($this->conn, $sql_insert)){ return true; } else{ return false; }
	}
```

⭐ In the *insert\_new\_results* function, insert the given model detection results and assigned detection image name to the *detections* MySQL database table.

```
	public function insert_new_results($date, $mmWave, $img, $class){
		$sql_insert = "INSERT INTO `detections`(`date`, `mmwave`, `img`, `class`)
		               VALUES ('$date', '$mmWave', '$img', '$class');"
			          ;
		if(mysqli_query($this->conn, $sql_insert)){ return true; } else{ return false; }
	}
```

⭐ In the *get\_data\_records* function, retrieve all data records from the *entries* database table in descending order and return each column as separate lists.

```
	public function get_data_records(){
		$date=[]; $mmWave=[]; $class=[];
		$sql_data = "SELECT * FROM `entries` ORDER BY `id` DESC";
		$result = mysqli_query($this->conn, $sql_data);
		$check = mysqli_num_rows($result);
		if($check > 0){
			while($row = mysqli_fetch_assoc($result)){
				array_push($date, $row["date"]);
				array_push($mmWave, $row["mmwave"]);
				array_push($class, $row["class"]);
			}
			return array($date, $mmWave, $class);
		}else{
			return array(["Not Found!"], ["Not Found!"], ["Not Found!"]);
		}
	}
```

⭐ In the *get\_model\_results* function, retrieve all model detection results and the assigned detection image names from the *detections* database table in descending order. Then, return each column as separate lists.

```
	public function get_model_results(){
		$date=[]; $mmWave=[]; $class=[]; $img=[];
		$sql_data = "SELECT * FROM `detections` ORDER BY `id` DESC";
		$result = mysqli_query($this->conn, $sql_data);
		$check = mysqli_num_rows($result);
		if($check > 0){
			while($row = mysqli_fetch_assoc($result)){
				array_push($date, $row["date"]);
				array_push($mmWave, $row["mmwave"]);
				array_push($class, $row["class"]);
				array_push($img, $row["img"]);
			}
			return array($date, $mmWave, $class, $img);
		}else{
			return array(["Not Found!"], ["Not Found!"], ["Not Found!"], ["icon.png"]);
		}
	}
```

⭐ In the *create\_CSV* function:

⭐ Get the stored data records in the *entries* database table.

⭐ Create a CSV file — *data\_records.csv*.

⭐ Add the header to the created CSV file.

⭐ Generate rows from the retrieved data records.

⭐ Append each generated row to the CSV file as a sample.

⭐ Close the CSV file and return its name.

```
	public function create_CSV(){
		// Get the stored data records in the entries database table.
		$date=[]; $mmWave=[]; $label=[];
		list($date, $mmWave, $label) = $this->get_data_records();
		// Create the data_records.csv file.
		$filename = "assets/data_records.csv";
		$fp = fopen($filename, 'w');
		// Add the header to the CSV file.
		fputcsv($fp, ["p_1","p_2","p_3","p_4","p_5","p_6","p_7","pipe_label"]);
		// Generate rows from the retrieved data records.
		for($i=0; $i&lt;count($date); $i++){
			$line = explode(",", $mmWave[$i]);
			array_push($line, $label[$i]);
			// Append each generated row to the CSV file as a sample.
			fputcsv($fp, $line);
		}
		// Close the CSV file.
		fclose($fp);
		// Return the CSV file name — data_records.csv.
		return $filename;
	}
```

⭐ Define the required MariaDB database connection settings for LattePanda 3 Delta 864.

```
$server = array(
	"name" => "localhost",
	"username" => "root",
	"password" => "",
	"database" => "pipeline_diagnostics"
);

$conn = mysqli_connect($server["name"], $server["username"], $server["password"], $server["database"]);
```

📁 *update\_server.php*

⭐ Include the *class.php* file.

⭐ Define the *wave* object of the *\_main* class with its required parameters.

```
include_once "assets/class.php";

// Define the new 'wave' object:
$wave = new _main();
$wave->__init__($conn);
```

⭐ Get the current date & time and create the detection image file name.

```
$date = date("Y_m_d_H_i_s");

# Create the image file name.
$img_file = "PIPE_".$date;
```

⭐ If Nicla Vision sends the collected 60GHz mmWave sensor data parameters with the selected pipeline diagnostic class, save the received information to the *entries* MySQL database table.

```
if(isset($_GET["data"]) && isset($_GET["mmWave"]) && isset($_GET["class"])){
	if($wave->insert_new_data($date, $_GET["mmWave"], $_GET["class"])){
		echo "New Data Record Saved Successfully!";
	}else{
		echo "Database Error!";
	}
}
```

⭐ If Nicla Vision transmits the model detection results, save the received information to the *detections* MySQL database table.

```
if(isset($_GET["results"]) && isset($_GET["mmWave"]) && isset($_GET["class"])){
	if($wave->insert_new_results($date, $_GET["mmWave"], $img_file.".jpg", $_GET["class"])){
		echo "Detection Results Saved Successfully!";
	}else{
		echo "Database Error!";
	}
}
```

⭐ If Nicla Vision transfers an image of a deformed pipe via an HTTP POST request to update the server after running the neural network model, save the received raw image buffer (RGB565) as a TXT file to the *detections* folder.

⭐ Then, convert the recently saved RGB565 buffer (TXT file) to a JPG image file by executing a Python script via the terminal through the web application — *rgb565\_converter.py*.

⭐ After generating the JPG file from the raw image buffer, remove the converted TXT file from the server.

```
if(!empty($_FILES["captured_image"]['name'])){
	// Image File:
	$captured_image_properties = array(
	    "name" => $_FILES["captured_image"]["name"],
	    "tmp_name" => $_FILES["captured_image"]["tmp_name"],
		"size" => $_FILES["captured_image"]["size"],
		"extension" => pathinfo($_FILES["captured_image"]["name"], PATHINFO_EXTENSION)
	);

    // Check whether the uploaded file extension is in the allowed file formats.
	$allowed_formats = array('jpg', 'png', 'bmp', 'txt');
	if(!in_array($captured_image_properties["extension"], $allowed_formats)){
		echo 'FILE => File Format Not Allowed!';
	}else{
		// Check whether the uploaded file size exceeds the 5 MB data limit.
		if($captured_image_properties["size"] > 5000000){
			echo "FILE => File size cannot exceed 5MB!";
		}else{
			// Save the uploaded file (image).
			move_uploaded_file($captured_image_properties["tmp_name"], "./detections/".$img_file.".".$captured_image_properties["extension"]);
			echo "FILE => Saved Successfully!";
		}
	}

	// Convert the recently saved RGB565 buffer (TXT file) to a JPG image file by executing the rgb565_converter.py file.
	$raw_convert = shell_exec('python "C:\Users\kutlu\New E\xampp\htdocs\pipeline_diagnostics_interface\detections\rgb565_converter.py"');
	print($raw_convert);

	// After generating the JPG file, remove the recently saved TXT file from the server.
	unlink("./detections/".$img_file.".txt");
}
```

⭐ If requested, create a CSV file from the data records saved in the *entries* database table — *data\_records.csv*. Then, download the generated CSV file automatically.

```
if(isset($_GET["create_CSV"])){
	// Create the data_records.csv file.
	$filename = $wave->create_CSV();
	// Download the generated CSV file automatically.
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header("Cache-Control: no-cache, must-revalidate");
    header('Content-Disposition: attachment; filename="'.basename($filename).'"');
    header('Content-Length: '.filesize($filename));
	header('Pragma: public');
    readfile($filename);
}
```

📁 *show\_records.php*

⭐ Include the *class.php* file.

⭐ Define the *wave* object of the *\_main* class with its required parameters.

```
include_once "assets/class.php";

// Define the new 'wave' object:
$wave = new _main();
$wave->__init__($conn);
```

⭐ Obtain all data records from the *entries* database table as separate lists for each data parameter (column) and create HTML table rows by utilizing these arrays.

```
$date=[]; $mmWave=[]; $label=[];
list($date, $mmWave, $label) = $wave->get_data_records();
$records = "&lt;tr>&lt;th>Date&lt;/th>&lt;th>mmWave&lt;/th>&lt;th>Label&lt;/th>&lt;/tr>";
for($i=0; $i&lt;count($date); $i++){
	$records .= '&lt;tr class="'.$label[$i].'">
				  &lt;td>'.$date[$i].'&lt;/td>
				  &lt;td style="word-break:break-all;">'.$mmWave[$i].'&lt;/td>
				  &lt;td>'.$label[$i].'&lt;/td>
			    &lt;/tr>
			    ';
}
```

⭐ Fetch all model detection results with the assigned detection image names from the *detections* database table as separate lists for each column and generate HTML table rows by utilizing these arrays.

```
$date_R=[]; $mmWave_R=[]; $class=[]; $img=[];
list($date_R, $mmWave_R, $class, $img) = $wave->get_model_results();
$results = "&lt;tr>&lt;th>Date&lt;/th>&lt;th>mmWave&lt;/th>&lt;th>Model Prediction&lt;/th>&lt;th>IMG&lt;/th>&lt;/tr>";
for($i=0; $i&lt;count($date_R); $i++){
	$results .= '&lt;tr class="'.$class[$i].'">
				  &lt;td>'.$date_R[$i].'&lt;/td>
				  &lt;td style="word-break:break-all;">'.$mmWave_R[$i].'&lt;/td>
				  &lt;td>'.$class[$i].'&lt;/td>
				  &lt;td>&lt;img src="detections/images/'.$img[$i].'"/>&lt;/td>
			    &lt;/tr>
			    ';
}
```

⭐ Then, create a JSON object with multiple key/value pairs from the generated HTML table rows consisting of the retrieved data records and the fetched model detection results.

```
$result = array("records" => $records, "results" => $results);
$res = json_encode($result);
```

⭐ Finally, return the recently created JSON object.

```
echo($res);
```

📁 *index.php*

⭐ Create the web application interface to display the stored information in the MySQL database tables with the captured deformed pipe images as HTML table rows.

You can inspect and download the *index.php* file below.

📁 *index.js (jQuery and AJAX)*

⭐ If requested, open a confirmation window to download the generated CSV file *(data\_records.csv)* consisting of the data records saved in the *entries* database table as samples.

```
$(".records").on("click", "button", () => {
	if(confirm("💻 Download the generated CSV file!\n\n🗂 data_records.csv")){
		window.location = "./update_server.php?create_CSV=OK";
	}
});
```

⭐ Every 5 seconds, make an HTTP GET request to the *show\_records.php* file.

⭐ Then, decode the retrieved JSON object to obtain the HTML table rows generated from the MySQL database table rows.

⭐ Assign the obtained table rows to the corresponding HTML elements on the web application interface to inform the user of the recently collected data parameters and the latest model detection results automatically.

```
setInterval(function(){
	$.ajax({
		url: "./show_records.php",
		type: "GET",
		success: (response) => {
			// Decode the obtained JSON object.
			const res = JSON.parse(response);
			// Assign the data record HTML table rows.
			$(".records table").html(res.records);
			// Assign the model detection HTML table rows.
			$(".results table").html(res.results);
		}
	});
}, 5000);
```

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_web_1.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=4b2ae42cba4fba8a2f974db8de962165" width="1600" height="756" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_web_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_web_2.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=f6f396f80232a1e46246647baa71c38f" width="1600" height="752" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_web_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_web_3.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=0150bee93a65ead058b0010ec9ed5542" width="1600" height="732" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_web_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_web_4.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=879dee9936c28685e8e850e0a8cfdeee" width="1600" height="732" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_web_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_web_5.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=8a25faf29d6fa3dacf3289f2a4cedb27" width="1600" height="751" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_web_5.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_web_6.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=636f2794161931a7e127104e938a2c82" width="1600" height="752" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_web_6.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_web_7.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=58a2eac13f35d0864d85cdf916170614" width="1600" height="754" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_web_7.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_web_8.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=7252dc7c2ae938edc705b5d7b18a1649" width="1600" height="735" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_web_8.png" />
</Frame>

## Step 3.1: Converting the raw image buffers transferred by Nicla Vision via POST requests to JPG files

Since Nicla Vision can only produce raw image buffers (RGB565) due to its built-in 2-megapixel CMOS camera (GC2145) and camera library, I needed to convert the generated raw image buffers to readable image files so as to display them on the web application interface. Since Nicla Vision cannot convert the generated raw image buffer due to memory allocation issues, I decided to convert the captured raw image buffer to a JPG file through the web application.

Even though PHP can handle converting image buffers to different file formats, converting images in PHP causes bad request issues since the web application receives raw image buffers from Nicla Vision via HTTP POST requests. Hence, I decided to utilize Python to create JPG files from raw image buffers since Python provides built-in modules for image conversion in seconds, even for byte swapping.

By employing the terminal on LattePanda 3 Delta, the web application executes the *rgb565\_converter.py* file directly to convert raw image buffers.

:hash: Since the *numpy* module is required to convert uint16\_t to 3x8-bit pixels, you may require to install the *numpy* module on the terminal manually to avoid errors.

*python -m pip install numpy*

📁 *rgb565\_converter.py*

⭐ Include the required modules.

```
from glob import glob
import numpy as np
from PIL import Image
```

⭐ Obtain all RGB565 buffer arrays transferred by Nicla Vision as text (TXT) files under the *detections* folder.

:hash: Since the web application requires to access the absolute paths via the terminal to execute the Python script in order to convert images, provide the *detections* folder's exact location.

```
path = "C:\\Users\\kutlu\\New E\\xampp\\htdocs\\pipeline_diagnostics_interface\\detections"
images = glob(path + "/*.txt")
```

⭐ Then, convert each retrieved TXT file (RGB565 buffer array) to a JPG file via the *frombytes* function.

⭐ Finally, save the generated JPG files to the *images* folder.

* RGB565 (uint16\_t) ➜ RGB (3x8-bit pixels, true color)

```
for img in images:
    loc = path + "/images/" + img.split("\\")[8].split(".")[0] + ".jpg"
    size = (320,320)
    # RGB565 (uint16_t) to RGB (3x8-bit pixels, true color)
    raw = np.fromfile(img).byteswap(True)
    file = Image.frombytes('RGB', size, raw, 'raw', 'BGR;16', 0, 1)
    file.save(loc)
    #print("Converted: " + loc)
```

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_convert_1.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=29826f90a5131406f38d7dbccf17a71b" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_convert_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/web_app_4.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=317e16bf8869962d59e7279857edbc33" width="1600" height="648" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_4.png" />
</Frame>

## Step 3.2: Setting and running the web application on LattePanda 3 Delta 864

Since I have got a test sample of the brand-new [LattePanda 3 Delta 864](https://www.dfrobot.com/product-2594.html?tracking=60f546f8002be), I decided to host my web application on LattePanda 3 Delta. Therefore, I needed to set up a LAMP web server.

LattePanda 3 Delta is a pocket-sized hackable computer that provides ultra performance with the Intel 11th-generation Celeron N5105 processor.

Plausibly, LattePanda 3 Delta can run the XAMPP application. So, it is effortless to create a server with a MariaDB database on LattePanda 3 Delta.

As explained in the previous steps, I also designed a unique deck for LattePanda by utilizing Elecrow's 8.8" IPS monitor.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/lattepanda_1.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=d9f5ccde106435e56867a0461113fbcf" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/lattepanda_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/lattepanda_2.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=f10232c0ce5a3d863e22152bffc8b9ba" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/lattepanda_2.jpg" />
</Frame>

:hash: First of all, install and set up [the XAMPP application](https://www.apachefriends.org/).

:hash: Then, go to the *XAMPP Control Panel* and click the *MySQL Admin* button.

:hash: Once the *phpMyAdmin* tool pops up, create a new database named *pipeline\_diagnostics*.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/app_server_set_1.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=3f2cc5e651eff91daaf72b0ff5fcc10a" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/app_server_set_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/database_create_1.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=0ff2d39a9ffcb77a7ec27a53692ae8dc" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/database_create_1.png" />
</Frame>

:hash: After adding the database successfully, go to the SQL section to create two different MySQL database tables named *entries* and *detections* with the required data fields.

```
CREATE TABLE `entries`(
	id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
	`date` varchar(255) NOT NULL,
    mmwave varchar(255) NOT NULL,
    `class` varchar(255) NOT NULL
);

CREATE TABLE `detections`(
	id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
	`date` varchar(255) NOT NULL,
    mmwave varchar(255) NOT NULL,
    img varchar(255) NOT NULL,
    `class` varchar(255) NOT NULL
);
```

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/database_create_2.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=6e52cebc760db0cd36e4183646b20f54" width="1600" height="775" data-path=".assets/images/ai-pipeline-inspection-mmwave/database_create_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/database_create_3.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=0a1a44753e9e570e48de3fdc709046ca" width="1600" height="776" data-path=".assets/images/ai-pipeline-inspection-mmwave/database_create_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/database_create_4.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=9ddbe84397ea4319f743f2ddb8efd4db" width="1600" height="760" data-path=".assets/images/ai-pipeline-inspection-mmwave/database_create_4.png" />
</Frame>

:hash: When Nicla Vision transmits the collected 60GHz mmWave sensor data parameters with the selected pipeline diagnostic class, the web application saves the received information to the *entries* MySQL database table.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/database_create_5.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=476b668bf570a8f9a871a56748adf352" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/database_create_5.png" />
</Frame>

:hash: When Nicla Vision transfers the model detection results and the captured image of the deformed pipe, the web application saves the received information to the *detections* MySQL database table.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/database_create_6.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=15b01fd7511034d83a64f29186d33259" width="1600" height="775" data-path=".assets/images/ai-pipeline-inspection-mmwave/database_create_6.png" />
</Frame>

## Step 3.3: Generating data samples and displaying real-time model detection results transferred by Nicla Vision

After setting the web application on LattePanda 3 Delta 864:

🚿🔎📲 The web application *(update\_server.php)* saves the mmWave data parameters with the selected class transferred by Nicla Vision via an HTTP GET request to the *entries* MySQL database table.

*/pipeline\_diagnostics\_interface/update\_server.php?data=OK\&mmWave=32.06314106,65.51403019,27.04366461,0.59400105,0.58607824,5.429632,0.81743312\&class=Cracked*

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_0.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=56c4e6129b6ac134777c0851cf513543" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_0.png" />
</Frame>

🚿🔎📲 When Nicla Vision transmits raw image buffer (RGB565), model detection results, and inference data parameters via an HTTP POST request with URL query parameters, the web application *(update\_server.php)* stores the received information in the *detections* MySQL database table. Then, the application converts the received raw image buffer to a JPG file by executing the *rgb565\_converter.py* file via the terminal.

*python "C:\Users\kutlu\New E\xampp\htdocs\pipeline\_diagnostics\_interface\detections\rgb565\_converter.py"*

🚿🔎📲 On the web application interface *(index.php)*, the application displays the concurrent list of data records saved in the *entries* database table as an HTML table.

🚿🔎📲 When the user clicks the HTML button *(Create CSV)*, the application opens a confirmation window to generate and download a CSV file *(data\_records.csv)* consisting of the data records saved in the *entries* database table as samples.

🚿🔎📲 Also, on the application interface, the application shows the concurrent list of model detection results with the captured images of the deformed pipes to inform the user of the latest diagnosed pipeline defects.

🚿🔎📲 The web application updates its interface every 5 seconds automatically via the jQuery script to display the latest stored information in the MariaDB database on LattePanda 3 Delta.

🚿🔎📲 For each pipeline diagnostic class (label), the web application changes the row color in the HTML tables to clarify and emphasize the collected mmWave data parameters and the model detection results:

* Leakage ➜ Dark Blue
* Cracked ➜ Violet
* Clogged ➜ Red

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_1.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=e5808215fc539d380c4b5790d4040d1b" width="1600" height="852" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_2.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=eece9406a083ab028be55c958f43d74e" width="1600" height="852" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_3.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=2da9baf46aa69fa1eb422d82a36f664f" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_4.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=e4beee12d26b1d203e1e0cb63b82e3d1" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_5.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=1b68c0b52215646eefb67b5479252d93" width="1600" height="846" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_5.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_6.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=e39aa5c171ab8d28d8bd42ed1b63e80c" width="1600" height="851" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_6.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_7.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=8f0bb7f5fbda6cf2c179c2043001467a" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_7.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_8.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=6be0067cbae3d87d6429f1c003d0f1f6" width="1600" height="852" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_8.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_9.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=1edd1e318bb3da4cbf910c754b0a695d" width="1600" height="656" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_9.png" />
</Frame>

🚿🔎📲 When the user hovers the cursor over the image frames, the web application highlights the selected frame.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_10.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=e89bbcb229551c7d03ade03f4dcfe563" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_10.png" />
</Frame>

🚿🔎📲 If Nicla Vision has not transferred any information yet, the web application notifies the user through the HTML tables.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/e64LP-KHz5O4v8wN/.assets/images/ai-pipeline-inspection-mmwave/web_app_work_11.png?fit=max&auto=format&n=e64LP-KHz5O4v8wN&q=85&s=8c8f21fa6577f5229bd9133b4847cb07" width="1600" height="851" data-path=".assets/images/ai-pipeline-inspection-mmwave/web_app_work_11.png" />
</Frame>

## Step 4: Setting up Nicla Vision on Arduino IDE

Before proceeding with the following steps, I needed to set up Nicla Vision on the Arduino IDE and install the required libraries for this project.

Although Arduino provides an official board package and libraries for Nicla Vision, the Wi-Fi firmware is not installed out of the box. Therefore, I had to install the Wi-Fi firmware manually to utilize the built-in Wi-Fi module.

:hash: To install the required core for Nicla boards, navigate to *Tools ➡ Board ➡ Boards Manager* and search for *Arduino Mbed OS Nicla Boards*.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/vision_set_1.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=2b1c3ba4c27e297cc1373e6fe337eef0" width="1600" height="900" data-path=".assets/images/ai-pipeline-inspection-mmwave/vision_set_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/vision_set_2.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=35bc1c6b337e5c646ac72f18e8f083c1" width="1600" height="900" data-path=".assets/images/ai-pipeline-inspection-mmwave/vision_set_2.png" />
</Frame>

:hash: After installing the core, navigate to *Tools ➡ Board ➡ Arduino Mbed OS Nicla Boards* and select *Arduino Nicla Vision*.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/vision_set_3.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=c717be98396ac6c747bb7199de3c7eef" width="1600" height="850" data-path=".assets/images/ai-pipeline-inspection-mmwave/vision_set_3.png" />
</Frame>

:hash: Since the Wi-Fi firmware has not been installed yet out of the box, Nicla Vision throws an error while attempting to utilize the built-in Wi-Fi module.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_1.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=e7f8dd77396f4f5a3310dcba7ca68958" width="1600" height="847" data-path=".assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_1.png" />
</Frame>

:hash: To install the Wi-Fi firmware manually, go to *Examples ➡ STM32H747\_System ➡ WiFiFirmwareUpdater* and execute the provided code.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_2.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=d5cb2695a9793d4559af37d275dcb041" width="1600" height="850" data-path=".assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_3.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=4a5a052309e94a5eba35bd269759b53f" width="1600" height="852" data-path=".assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_3.png" />
</Frame>

:hash: After running the *WiFiFirmwareUpdater* example, Arduino IDE flashes Nicla Vision to install the required Wi-Fi firmware and certificates.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_4.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=495620a8e4730a40826a9028d6401a7e" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_5.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=2b3a5c710c0ab065660073f0b64a900c" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/nicla_wifi_update_5.png" />
</Frame>

:hash: Finally, download the required libraries to utilize the 60GHz mmWave module and the ILI9341 TFT LCD screen with Arduino Nano:

MR60BHA1-Sensor | [Download](https://github.com/limengdu/Seeed-Studio-MR60BHA1-Sensor)

Adafruit\_ILI9341 | [Download](https://github.com/adafruit/Adafruit_ILI9341)

Adafruit-GFX-Library | [Download](https://github.com/adafruit/Adafruit-GFX-Library)

## Step 5.0: Building a basic pipeline system demonstrating different defects

To diagnose different pipeline defects, I needed to collect accurate vibration measurements from a pipeline system so as to train my neural network model with notable validity. Therefore, I decided to build a simple pipeline system by utilizing pipes and fittings (adapters) with mediocre thermal conductivity, demonstrating three different pipeline defects in each primary section — color-coded:

* Blue Section ➡ Cracked
* Red Section➡ Clogged
* Green Section ➡ Leakage

:hash: First of all, I cut pieces of pipes according to my pipeline system requirements.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/pipe_set_1.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=57ee53b8655246819caaf06f513563bd" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/pipe_set_1.jpg" />
</Frame>

:hash: In the red primary section, I jammed the pipe with a bead.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/pipe_set_2.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=ceba4898eec07934d9a01a5c462d0c79" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/pipe_set_2.jpg" />
</Frame>

:hash: In the green primary section, I left a fitting (adapter) joint leaking.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/pipe_set_3.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=3a374c9aad697680571dd89418587a0a" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/pipe_set_3.jpg" />
</Frame>

:hash: In the blue primary section, I cracked the pipe by utilizing a staple gun.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/pipe_set_4.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=c8a50dfbc324c42aa20db0499527d837" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/pipe_set_4.jpg" />
</Frame>

:hash: Then, I fastened all pipes and fittings (adapters) via the hot glue gun.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/pipe_set_5.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=5022608ddd43bce612f7ed86c1161fe4" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/pipe_set_5.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/pipe_set_6.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=ead17357aacf0d7854d925c1605c3ce1" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/pipe_set_6.jpg" />
</Frame>

:hash: Finally, I connected a mini aquarium pump to the pipeline system via the threaded elbow pipe fitting.

In that regard, I was able to pump air or water through the pipeline system to collect mmWave data parameters of different pipeline defects.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/pipe_set_7.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=4ecb15e43afab384337786c8b368b9d4" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/pipe_set_7.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/pipe_set_8.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=915215288ab16b515ad0ab108f2dc774" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/pipe_set_8.jpg" />
</Frame>

## Step 5: Collecting mmWave data parameters and communicating with Nicla Vision via serial communication w/ Arduino Nano

After setting up Nicla Vision and installing the required libraries, I programmed Arduino Nano to extract data parameters from the 60GHz mmWave radar module and transmit the collected data parameters to Nicla Vision via serial communication. As explained in the previous steps, I encountered architecture and library incompatibilities when I connected the mmWave module and the ILI9341 TFT LCD screen directly to Nicla Vision.

Since I needed to assign pipeline diagnostic classes as labels for each data record while collecting mmWave data parameters of different pipeline defects to create a valid data set for my neural network model, I utilized three control buttons connected to Arduino Nano so as to choose among classes and transfer data records via serial communication. After selecting a pipeline diagnostic class by pressing a control button, Arduino Nano transmits the selected class and the recently collected data parameters to Nicla Vision.

* Control Button (A) ➡ Leakage
* Control Button (B) ➡ Cracked
* Control Button (C) ➡ Clogged

You can download the *AI\_assisted\_Pipeline\_Diagnostics\_data\_collect.ino* file to try and inspect the code for extracting mmWave data parameters and transferring the collected data via serial communication.

⭐ Include the required libraries.

```
#include &lt;SoftwareSerial.h>
#include &lt;Adafruit_GFX.h>
#include &lt;Adafruit_ILI9341.h>
#include &lt;60ghzbreathheart.h>
```

⭐ Define the software serial port (Nicla) to communicate with Nicla Vision via serial communication.

⭐ Define the software serial port (mmWave) to communicate with the 60GHz mmWave sensor via serial communication.

```
SoftwareSerial Nicla(A0, A1); // RX, TX

SoftwareSerial mmWave(A2, A3); // RX, TX
```

⭐ Define the 60GHz mmWave sensor object.

```
BreathHeart_60GHz radar = BreathHeart_60GHz(&mmWave);
```

⭐ Use hardware SPI (on Nano, SCK, MISO, MOSI) and define the required pins to initialize the ILI9341 TFT LCD screen.

```
#define TFT_CS   10
#define TFT_RST  9
#define TFT_DC   8

// Use hardware SPI (on Nano, SCK, MISO, MOSI) and the above for DC/CS/RST.
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC, TFT_RST);
```

⭐ Define the mmWave radar and menu button color schemes for the user interface on the ILI9341 screen.

```
uint16_t b = ILI9341_BLACK; uint16_t g = ILI9341_GREEN; uint16_t y = ILI9341_YELLOW; uint16_t r = ILI9341_RED;
uint16_t * circle_colors[] = {g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b,g,b,r,b,y,b};
// Define the menu button color schemes and names.
uint16_t button_colors[4][2] = {{ILI9341_DARKGREY, ILI9341_BLUE}, {ILI9341_DARKGREY, ILI9341_YELLOW}, {ILI9341_DARKGREY, ILI9341_RED}, {ILI9341_DARKGREY, ILI9341_CYAN}};
String button_names[] = {"A", "B", "C", "D"};
```

⭐ Define the pipeline diagnostic class names.

```
String classes[] = {"Leakage", "Cracked", "Clogged"};
```

⭐ Initialize the software serial ports (Nicla and mmWave).

```
  Nicla.begin(115200);
  mmWave.begin(115200);
```

⭐ To extract accurate data parameters, activate the real-time data transmission mode of the 60GHz mmWave sensor.

```
  // radar.reset_func(); delay(1000);
  radar.ModeSelect_fuc(1);
```

⭐ Initialize the ILI9341 TFT LCD screen.

⭐ Then, show the mmWave radar indicator and interface menu buttons.

```
  tft.begin();
  tft.setRotation(TFT_ROTATION);
  tft.fillScreen(ILI9341_NAVY);
  tft.setTextColor(ILI9341_WHITE);  tft.setTextSize(2);
  tft.setCursor(10, 10);
  tft.println("Initializing...");
  delay(5000);
  adjustColor(255,0,255);

  // Show the mmWave radar and menu buttons.
  int s[4] = {0,0,0,0}; menu_buttons(40,10,5,s,true);
  screen_radar(10);
  delay(1000);
```

⭐ In the *collect\_mmWave\_data* function:

⭐ Clear the *data\_packet* string.

⭐ Initiate the breath and heartbeat information output.

⭐ Add the evaluated breath and heartbeat parameters (vibration frequencies) to the *data\_packet* string.

⭐ Initiate the object-measuring information output.

⭐ Add the extracted measuring parameters to the *data\_packet* string.

⭐ Print the collected mmWave data parameters on the serial monitor.

```
void collect_mmWave_data(bool p){
  // Clear the data_packet string.
  data_packet = "";

  // Initiate the breath and heartbeat information output.
  radar.Breath_Heart();
  // Add the evaluated breath and heartbeat parameters to the data_packet string.
  if(radar.sensor_report != 0x00){
    if(radar.heart_rate){ data_packet += String(radar.heart_rate, DEC); }else{ data_packet += "0"; }
    if(radar.breath_rate){ data_packet += "," + String(radar.breath_rate, DEC); }else{ data_packet += ",0"; }
  }else{
    data_packet += "0,0";
  }
  delay(500);

  // Initiate the measuring information output.
  radar.HumanExis_Func();
  if(radar.sensor_report != 0x00){
    if(radar.bodysign_val){ data_packet += "," + String(radar.bodysign_val, DEC); }else{ data_packet += ",0"; }
    if(radar.distance){ data_packet += "," + String(radar.distance, DEC); }else{ data_packet += ",0"; }
    if(radar.Dir_x){ data_packet += "," + String(radar.Dir_x, DEC); }else{ data_packet += ",0"; }
    if(radar.Dir_y){ data_packet += "," + String(radar.Dir_y, DEC); }else{ data_packet += ",0"; }
    if(radar.Dir_z){ data_packet += "," + String(radar.Dir_z, DEC); }else{ data_packet += ",0"; }
  }else{
    data_packet += ",0,0,0,0,0";
  }
  delay(500);

  // Print the collected mmWave data parameters.
  if(p) Serial.println("mmWave Data Parameters: " + data_packet);
}
```

⭐ In the *menu\_buttons* function:

⭐ Depending on the declared integer button status array, draw the interface menu buttons indicating the control button status.

⭐ Then, display the activated feature on the screen.

```
void menu_buttons(int a, int e, int offset, int _select[4], bool _init){
  int w = tft.width();
  int h = tft.height();
  int b = (w-(4*a)) / 5;
  int x = b;
  int y = h - a - e;
  // If required, clear the screen.
  if(_init) tft.fillScreen(ILI9341_BLACK);
  // Draw the menu buttons indicating the control button status.
  for(int i=0; i&lt;4; i++){
    tft.fillRect(x+(i*(a+b)), y, a, a, ILI9341_LIGHTGREY);
    tft.fillRect((x+(i*(a+b))+offset), y+offset, a-(2*offset), a-(2*offset), button_colors[i][_select[i]]);
    tft.setTextSize(3);
    tft.setCursor((x+(i*(a+b))+offset+8), y+offset+5);
    tft.println(button_names[i]);
  }
  // Print the activated feature.
  tft.fillRect(0, y-26, w, 25, ILI9341_BLACK);
  tft.setTextSize(2);
  tft.setCursor(20, y-25);
  if(_select[0]) tft.println("Selected: " + classes[0]);
  if(_select[1]) tft.println("Selected: " + classes[1]);
  if(_select[2]) tft.println("Selected: " + classes[2]);
  if(_select[3]) tft.println("EI Model Running!");
}
```

⭐ In the *screen\_radar* function, draw the mmWave radar to visualize the extracted and collected data parameters on the screen.

```
void screen_radar(int radius){
  int w = tft.width();
  int h = tft.height();
  int x = w/2; int y = w/2;
  int limit = w / (2*radius);
  // Draw the mmWave radar data visualization.
  for(int i=limit; i>0; i--){
    tft.fillCircle(x, y, i*radius, circle_colors[(limit+1)-i]);
    delay(150);
  }
}
```

⭐ If one of the control buttons (A, B, or C) is pressed:

⭐ Add the selected pipeline diagnostic class and the *Data* command to the collected mmWave data parameters.

⭐ Transmit the generated string to Nicla Vision via serial communication.

⭐ Adjust the RGB LED color depending on the selected class.

⭐ Highlight the pressed button on the interface.

⭐ Then, activate the mmWave radar on the interface to visualize the collected data and notify the user.

```
  if(!digitalRead(button_A)) { Nicla.print("Data&" + data_packet + "&Leakage"); Serial.println("\nData Sent! Selected Class: Leakage\n"); adjustColor(0,0,255); delay(2000); adjustColor(255,0,255); int s[4] = {1,0,0,0}; menu_buttons(40,10,5,s,false); screen_radar(5); command = true; delay(2000); }
  if(!digitalRead(button_B)) { Nicla.print("Data&" + data_packet + "&Cracked"); Serial.println("\nData Sent! Selected Class: Cracked\n"); adjustColor(255,255,0); delay(2000); adjustColor(255,0,255); int s[4] = {0,1,0,0}; menu_buttons(40,10,5,s,false); screen_radar(5); command = true; delay(2000); }
  if(!digitalRead(button_C)) { Nicla.print("Data&" + data_packet + "&Clogged"); Serial.println("\nData Sent! Selected Class: Clogged\n"); adjustColor(255,0,0); delay(2000); adjustColor(255,0,255); int s[4] = {0,0,1,0}; menu_buttons(40,10,5,s,false); screen_radar(5); command = true; delay(2000); }
```

⭐ If the control button (D) is pressed:

⭐ Add the *Run* command to the collected mmWave data parameters.

⭐ Send the generated string to Nicla Vision via serial communication so as to run the Edge Impulse neural network model.

⭐ Adjust the RGB LED color to cyan.

⭐ Highlight the pressed button on the interface.

⭐ Then, activate the mmWave radar on the interface to visualize the collected data and notify the user.

```
  if(!digitalRead(button_D)) { Nicla.print("Run&" + data_packet); Serial.println("\nData Parameters Transferred Successfully!\n"); adjustColor(0,255,255); delay(2000); adjustColor(255,0,255); int s[4] = {0,0,0,1}; menu_buttons(40,10,5,s,false); screen_radar(5); command = true; delay(2000); }
```

⭐ Undo the button highlights on the interface and clear the latest command.

```
  if(command){
    int s[4] = {0,0,0,0}; menu_buttons(40,10,5,s,false);
    command = false;
  }
```

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/code_collect_1.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=2f2948635c0f104326e11a167035bb38" width="1600" height="723" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_collect_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/code_collect_2.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=25aade3e8f5e319cf2c7bb4f73b586cf" width="1600" height="726" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_collect_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/code_collect_3.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=b39404b5ed04769cf4886101d8e40811" width="1600" height="723" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_collect_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/code_collect_4.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=f121b11704df1631fbca42393634c6fc" width="1600" height="723" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_collect_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/code_collect_5.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=a426f1f144228e705cf9edfb18d812fd" width="1600" height="719" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_collect_5.png" />
</Frame>

## Step 5.1: Storing and converting the collected data parameters to samples via the web application

After uploading and running the code for collecting mmWave data parameters and transferring the collected data with the selected class to Nicla Vision via serial communication:

🚿🔎📲 If the 60GHz mmWave radar module works accurately, the device turns the RGB LED to magenta and displays the simple radar indicator visualizing the extracted mmWave data parameters and the interface menu buttons on the ILI9341 TFT LCD screen.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_1.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=d8c9ccff45b95bf2d2abbba54f988c89" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_2.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=f0ef0a0da569c7344256ec0984d551f9" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_2.jpg" />
</Frame>

🚿🔎📲 If the control button (A) is pressed, Arduino Nano adds *Leakage* as the selected pipeline diagnostic class to the recently extracted mmWave data parameters, transfers the modified data record to Nicla Vision via serial communication, and turns the RGB LED to blue.

🚿🔎📲 Then, it switches the interface button (A) color to blue and shows the simple radar indicator visualizing the extracted mmWave data parameters on the ILI9341 TFT LCD screen.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_3.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=1473607e90067a4eb311e03c7fca4000" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_3.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_4.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=73260fa64728efb77b7c258cf1879a3c" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_4.jpg" />
</Frame>

🚿🔎📲 If the control button (B) is pressed, Arduino Nano adds *Cracked* as the selected pipeline diagnostic class to the recently extracted mmWave data parameters, transfers the modified data record to Nicla Vision via serial communication, and turns the RGB LED to yellow.

🚿🔎📲 Then, it switches the interface button (B) color to yellow and shows the simple radar indicator visualizing the extracted mmWave data parameters on the ILI9341 TFT LCD screen.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_5.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=aee6e2d43bab64f96ab311334a2167f2" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_5.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_6.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=368a74b6a6ba7c2ec8421fa438e80666" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_6.jpg" />
</Frame>

🚿🔎📲 If the control button (C) is pressed, Arduino Nano adds *Clogged* as the selected pipeline diagnostic class to the recently extracted mmWave data parameters, transfers the modified data record to Nicla Vision via serial communication, and turns the RGB LED to red.

🚿🔎📲 Then, it switches the interface button (C) color to red and shows the simple radar indicator visualizing the extracted mmWave data parameters on the ILI9341 TFT LCD screen.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_7.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=50ab19b8a6dde3d83a25de47b9167fc0" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_7.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/collect_8.jpg?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=47086d844a871accbf99e44b294baa0b" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/collect_8.jpg" />
</Frame>

🚿🔎📲 After pressing the control buttons (A, B, or C), Arduino Nano sends the *Data* command to Nicla Vision via serial communication. When Nicla Vision receives the *Data* command, it transmits the received mmWave data parameters and selected pipeline diagnostic class to the web application via an HTTP GET request.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/finished_1.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=869585d6fe03c3ed7319205c9dfb7f3a" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/finished_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/finished_2.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=27625a8ba6dfb98762fd4af56a01e527" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/finished_2.jpg" />
</Frame>

🚿🔎📲 Also, Arduino Nano prints notifications and sensor measurements on the serial monitor for debugging.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/serial_collect_1.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=524da8eed7aa13ee7668a397014107d5" width="1600" height="821" data-path=".assets/images/ai-pipeline-inspection-mmwave/serial_collect_1.png" />
</Frame>

After collecting mmWave data parameters (vibration fluctuations) from my pipeline system that manifests three different pipeline defects and creating the pre-formatted CSV file consisting of the stored data records as samples via the web application, I elicited my data set with eminent validity and veracity.

<Frame caption="image">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/ai-pipeline-inspection-mmwave/gif_collect_1.gif" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/ai-pipeline-inspection-mmwave/gif_collect_2.gif" />
</Frame>

## Step 6: Building a neural network model with Edge Impulse

In this project, I needed to obtain precise mmWave data parameters indicating vibration fluctuations of different pipeline defects in order to train my neural network model accurately. Therefore, as explained in the previous steps, I built a simple pipeline system by utilizing pipes and fittings (adapters) with mediocre thermal conductivity, demonstrating three different pipeline defects in each primary section — color-coded.

* Blue Section ➡ Cracked
* Red Section➡ Clogged
* Green Section ➡ Leakage

While collecting data parameters, I utilized the three basic pipeline defects demonstrated by each main line as labels:

* Clogged
* Cracked
* Leakage

When I completed logging the collected data and assigning labels, I started to work on my artificial neural network model (ANN) to diagnose pipeline defects so as to inform the user with prescient warnings before a faulty pipeline system engenders various manufacturing problems.

Since Edge Impulse supports almost every microcontroller and development board due to its model deployment options, I decided to utilize Edge Impulse to build my artificial neural network model. Also, Edge Impulse makes scaling embedded ML applications easier and faster for edge devices such as Nicla Vision.

As of now, Edge Impulse supports CSV files to upload samples in different data structures thanks to its *CSV Wizard*. So, Edge Impulse lets the user upload all data records in a single file even if the data type is not time series. But, I usually need to follow the steps below to format my data set saved in a single CSV file so as to train my model accurately:

* Data Scaling (Normalizing)
* Data Preprocessing

Nevertheless, as explained in the previous steps, I employed Nicla Vision to transfer the collected mmWave data parameters to the web application that generates a pre-formatted CSV file by utilizing the stored data records in the database. Therefore, I did not need to preprocess my data set before uploading samples.

Plausibly, Edge Impulse allows building predictive models optimized in size and accuracy automatically and deploying the trained model as an Arduino library. Therefore, after collecting my samples, I was able to build an accurate neural network model to diagnose pipeline defects and run it on Nicla Vision effortlessly.

You can inspect [my neural network model on Edge Impulse](https://studio.edgeimpulse.com/public/214371/latest) as a public project.

## Step 6.1: Preprocessing and scaling the data set to create formatted samples for Edge Impulse

As long as the CSV file includes a header defining data fields, Edge Impulse can distinguish data records as individual samples in different data structures thanks to its *CSV Wizard* while adding existing data to an Edge Impulse project. Therefore, there is no need for splitting single CSV file data sets even if the data type is not time series.

After collecting the extracted mmWave data parameters of different pipeline defects and generating a pre-formatted CSV file via the web application, I obtained my appropriately formatted samples.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/data_collected.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=f62f8be0c387d8243ada062b6c6394ae" width="1600" height="781" data-path=".assets/images/ai-pipeline-inspection-mmwave/data_collected.png" />
</Frame>

## Step 6.2: Uploading formatted samples to Edge Impulse

After generating training and testing samples successfully, I uploaded them to my project on Edge Impulse.

:hash: First of all, sign up for [Edge Impulse](https://www.edgeimpulse.com/) and create a new project.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_1.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=469875a7fe95d0aaca1ae73e6e63bc06" width="1600" height="777" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_1.png" />
</Frame>

:hash: Navigate to the *Data acquisition* page and click the *Upload data* button.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_2.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=df6fa8020344673ce6063afbba7a1546" width="1600" height="753" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_2.png" />
</Frame>

:hash: Before uploading samples, go to the *CSV Wizard* to set the rules to process all uploaded CSV files.

:hash: Upload the CSV file to specify data fields and items.

:hash: Select the data structure (time-series data or not).

:hash: Define a column to obtain labels for each data record if it is a single CSV file data set.

:hash: Then, define the columns containing data items and click the *Finish wizard* button.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_3.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=3f4c1d14a7b990b0f98ae0d6123b92c6" width="1600" height="775" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_4.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=f1557ebf26a785ccef84f085f9b61749" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_5.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=a9fa82c28ad2cef81c931ca893e2cb10" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_5.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_6.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=9a42f802af1107f0c2e2b7015a19cb69" width="1600" height="777" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_6.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_7.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=a33dca833400ee8b5e0db76cc9a87307" width="1600" height="774" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_7.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_8.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=e34909b1dd1747a5fc1fddf5009cc25a" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_8.png" />
</Frame>

:hash: After setting the rules, choose the data category (training or testing) and upload the single CSV file data set.

:hash: Then, all given samples are labeled by utilizing the selected label column (data field) automatically.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_9.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=59aab98daeb1548d2fbd0f6a8df83604" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_9.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_10.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=f5499e3ead411c31c92a9faf357a37ef" width="1600" height="772" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_10.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_11.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=1238faf0e7ca75ce0a56bc68eb7d84f7" width="1600" height="776" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_11.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_12.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=9b94e0cc4c4c7ffe021d9382fbb508f7" width="1600" height="776" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_12.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_13.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=b77ec3b6f07f93c2e835319689d5ee58" width="1600" height="775" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_13.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_set_14.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=f8ebccc0b942ecb098d2e77b62fe51a4" width="1600" height="776" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_set_14.png" />
</Frame>

## Step 6.3: Training the model on various pipeline defects

After uploading my training and testing samples successfully, I designed an impulse and trained it on pipeline diagnostic classes.

An impulse is a custom neural network model in Edge Impulse. I created my impulse by employing the *Raw Data* processing block and the *Classification* learning block.

The *Raw Data* processing block generate windows from data samples without any specific signal processing.

The *Classification* learning block represents a Keras neural network model. Also, it lets the user change the model settings, architecture, and layers.

:hash: Go to the *Create impulse* page. Then, select the *Raw Data* processing block and the *Classification* learning block. Finally, click *Save Impulse*.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/edge_train_1.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=20b34202abf972e67a266d6ccba63557" width="1600" height="775" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_train_1.png" />
</Frame>

:hash: Before generating features for the neural network model, go to the *Raw data* page and click *Save parameters*.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/edge_train_2.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=a07e7f273acd3492334c00f68f5355f3" width="1600" height="772" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_train_2.png" />
</Frame>

:hash: After saving parameters, click *Generate features* to apply the *Raw Data* processing block to training samples.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/edge_train_3.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=0157d4e6d572fecae68e4319c344f154" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_train_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/edge_train_4.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=c624236a52216f401fbe8761e62b599a" width="1600" height="772" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_train_4.png" />
</Frame>

:hash: Finally, navigate to the *Classifier* page and click *Start training*.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/edge_train_5.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=c3c12a73584346934f32169d17f7e9f0" width="1600" height="776" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_train_5.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/edge_train_6.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=48c956a208019166be955ce0e441bcbd" width="1600" height="772" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_train_6.png" />
</Frame>

According to my experiments with my neural network model, I modified the neural network settings and layers to build a neural network model with high accuracy and validity:

📌 Neural network settings:

* Number of training cycles ➡ 50
* Learning rate ➡ 0.005
* Validation set size ➡ 20

📌 Extra layers:

* Dense layer (30 neurons)
* Dense layer (60 neurons)
* Dense layer (10 neurons)

After generating features and training my model with training samples, Edge Impulse evaluated the precision score (accuracy) as *94.4%*.

The precision score (accuracy) is approximately *95%* due to the modest volume and variety of training samples since I only collected mmWave data parameters of three basic pipeline defects. In technical terms, the model trains on limited validation samples of very few defects. Therefore, I highly recommend retraining the model with mmWave data parameters of specific pipeline defects before running inferences to diagnose more complex system flaws.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/edge_train_7.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=a8ae471d522f21536445da826089a1bb" width="1600" height="775" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_train_7.png" />
</Frame>

## Step 6.4: Evaluating the model accuracy and deploying the model

After building and training my neural network model, I tested its accuracy and validity by utilizing testing samples.

The evaluated accuracy of the model is *90%*.

:hash: To validate the trained model, go to the *Model testing* page and click *Classify all*.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_test_1.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=6f453fe9da0370066869c77499b500eb" width="1600" height="768" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_test_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_test_2.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=c9232fc8674687698b0098aee88e4e54" width="1600" height="771" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_test_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/edge_test_3.png?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=dd15e2e02a54661dd2c6c1e17f1726ae" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_test_3.png" />
</Frame>

After validating my neural network model, I deployed it as a fully optimized and customizable Arduino library.

:hash: To deploy the validated model as an Arduino library, navigate to the *Deployment* page and select *Arduino library*.

:hash: Then, choose the *Quantized (int8)* optimization option to get the best performance possible while running the deployed model.

:hash: Finally, click *Build* to download the model as an Arduino library.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_deploy_1.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=d32eb42886479e758f52bada9f138017" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_deploy_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_deploy_2.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=f7af5484943b28b8f952051eb8ea7978" width="1600" height="777" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_deploy_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/edge_deploy_3.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=b12022e8e73fcbdf7fc981ae77c33c5b" width="1600" height="773" data-path=".assets/images/ai-pipeline-inspection-mmwave/edge_deploy_3.png" />
</Frame>

## Step 7: Setting up the Edge Impulse model on Nicla Vision

After building, training, and deploying my model as an Arduino library on Edge Impulse, I needed to upload the generated Arduino library on Nicla Vision to run the model directly so as to create a user-friendly and capable mechanism operating with minimal latency, memory usage, and power consumption.

Since Edge Impulse optimizes and formats signal processing, configuration, and learning blocks into a single package while deploying models as Arduino libraries, I was able to import my model effortlessly to run inferences.

:hash: After downloading the model as an Arduino library in the ZIP file format, go to *Sketch ➡ Include Library ➡ Add .ZIP Library...*

:hash: Then, include the *AI\_assisted\_Pipeline\_Diagnostics\_run\_model.h* file to import the Edge Impulse neural network model.

```
#include &lt;AI_assisted_Pipeline_Diagnostics_run_model.h>
```

After importing my model successfully to the Arduino IDE, I programmed Nicla Vision to run inferences to diagnose pipeline defects and capture pictures of the deformed pipes for further examination when it receives the *Run* command and the extracted mmWave data parameters from Arduino Nano via serial communication.

* Control Button (D) \[Nano] ➡ Run Inference

Then, I employed Nicla Vision to transfer the received data parameters, the model detection results, and the captured image of the deformed pipe (raw image buffer) to the web application via an HTTP POST request after running an inference successfully.

Furthermore, as explained in the previous steps, Nicla Vision transmits the mmWave data parameters and the selected pipeline diagnostic class to the web application via an HTTP GET request when it receives the *Data* command from Arduino Nano via serial communication so as to store data records in a particular MySQL database table for further usage.

You can download the *AI\_assisted\_Pipeline\_Diagnostics\_run\_model.ino* file to try and inspect the code for running Edge Impulse neural network models and transferring data to a web application via Nicla Vision.

⭐ Include the required libraries.

```
#include &lt;WiFi.h>
#include "camera.h"
#include "gc2145.h"
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

⭐ Define the pipeline diagnostic class names:

* Clogged
* Cracked
* Leakage

```
float threshold = 0.60;

// Define the pipeline diagnostic class names:
String classes[] = {"Clogged", "Cracked", "Leakage"};
```

⭐ Define the Wi-Fi network and the web application settings hosted by LattePanda 3 Delta 864.

⭐ Initialize the *WiFiClient* object.

```
char ssid[] = "&lt;_SSID_>";        // your network SSID (name)
char pass[] = "&lt;_PASSWORD_>";    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;                // your network key Index number (needed only for WEP)

// Define the server on LattePanda 3 Delta.
char server[] = "192.168.1.22";
// Define the web application path.
String application = "/pipeline_diagnostics_interface/update_server.php";

// Initialize the WiFiClient object.
WiFiClient client; /* WiFiSSLClient client; */
```

⭐ Define the required settings for the built-in 2-megapixel CMOS camera (GC2145) on Nicla Vision.

⭐ Define the camera (image) buffer array.

```
GC2145 galaxyCore;
Camera cam(galaxyCore);

// Define the camera frame buffer.
FrameBuffer fb;
```

⭐ Create a struct including all extracted mmWave data parameters as its elements.

```
struct data {
  float p1;
  float p2;
  float p3;
  float p4;
  float p5;
  float p6;
  float p7;
};
```

⭐ Initialize the hardware serial port (Serial1) to communicate with Arduino Nano via serial communication.

```
Serial1.begin(115200, SERIAL_8N1);
```

⭐ Initialize the Wi-Fi module and attempt to connect to the given Wi-Fi network.

```
  WiFi.begin(ssid, pass);
  // Attempt to connect to the Wi-Fi network:
  while(WiFi.status() != WL_CONNECTED){
    // Wait for the connection:
    delay(500);
    Serial.print(".");
  }
  // If connected to the network successfully:
  Serial.println("Connected to the Wi-Fi network successfully!");
```

⭐ Define the frame size, the pixel format, and the FPS settings.

⭐ Then, initialize the built-in GC2145 camera.

```
  if (!cam.begin(CAMERA_R320x320, CAMERA_RGB565, 30)) { // CAMERA_R320x240, CAMERA_R320x320
    Serial.println("GC2145 camera: initialization failed!");
  }else{
    Serial.println("GC2145 camera: initialized successfully!");
  }
```

⭐ Obtain the data packet and commands transferred by Arduino Nano via serial communication.

```
  if(Serial1.available() > 0){
    data_packet = Serial1.readString();
  }
```

⭐ In the *make\_a\_get\_post\_request* function:

⭐ Connect to the web application named *pipeline\_diagnostics\_interface*.

⭐ Create the *query* string by adding the given URL query (GET) parameters depending on the received user command (*Data* or *Run*).

⭐ If the *post* boolean is true:

⭐ Define the boundary parameter named *PipeDetection* so as to send the captured raw image buffer (RGB565) as a TXT file to the web application.

⭐ Get the total content length.

⭐ Make an HTTP POST request with the created *query* string to the web application in order to transfer the captured raw image buffer as a TXT file and the model detection results.

⭐ Wait until transferring the image buffer.

⭐ If the *post* boolean is false:

⭐ Make an HTTP GET request with the created *query* string to the web application in order to transmit the collected mmWave data parameters and the selected pipeline diagnostic class (label).

```
void make_a_get_post_request(bool post, String request){
  // Connect to the web application named pipeline_diagnostics_interface. Change '80' with '443' if you are using SSL connection.
  if (client.connect(server, 80)){
    // If successful:
    Serial.println("\nConnected to the web application successfully!\n");
    // Create the query string:
    String query = application + request;
    // Transfer information to the web application via an HTTP POST or GET request depending on the given data parameter type.
    if(post){
      // Make an HTTP POST request:
      String head = "--PipeDetection\r\nContent-Disposition: form-data; name=\"captured_image\"; filename=\"new_image.txt\"\r\nContent-Type: text/plain\r\n\r\n";
      String tail = "\r\n--PipeDetection--\r\n";
      // Get the total message length.
      uint32_t totalLen = head.length() + cam.frameSize() + tail.length();
      // Start the request:
      client.println("POST " + query + " HTTP/1.1");
      client.println("Host: 192.168.1.22");
      client.println("Content-Length: " + String(totalLen));
      client.println("Content-Type: multipart/form-data; boundary=PipeDetection");
      client.println();
      client.print(head);
      client.write(fb.getBuffer(), cam.frameSize());
      client.print(tail);
      client.println("Connection: close");
      client.println();
      // Wait until transferring the image buffer.
      delay(3000);
      // If successful:
      Serial.println("HTTP POST => Data transfer completed!\n");
    }else{
      // Make an HTTP GET request:
      // Start the request:
      client.println("GET " + query + " HTTP/1.1");
      client.println("Host: 192.168.1.22");
      client.println("Connection: close");
      client.println();
      //client.println("Connection: close");
      delay(2000);
      // If successful:
      Serial.println("HTTP GET => Data transfer completed!\n");
    }
  }else{
    Serial.println("\nConnection failed to the web application!\n");
    delay(2000);
  }
}
```

⭐ If Arduino Nano sends the *Data command* with the recently collected mmWave data parameters and the selected pipeline diagnostic class:

⭐ Glean information as substrings from the transferred data packet by utilizing the ampersand (&) as the delimiter.

⭐ Create the *request* string, including the *data* URL parameter.

⭐ Send the obtained mmWave data parameters and the selected pipeline diagnostic class to the web application via an HTTP GET request.

```
  if(data_packet != ""){

    Serial.print("\nReceived Data Packet: "); Serial.println(data_packet+"\n");

    if(data_packet.startsWith("Data")){
      // Glean information as substrings from the transferred data packet by Arduino Nano.
      del_1 = data_packet.indexOf("&");
      del_2 = data_packet.indexOf("&", del_1 + 1);
      String data_record = data_packet.substring(del_1 + 1, del_2);
      String selected_class = data_packet.substring(del_2 + 1);

      // Create the request string.
      String request = "?data=OK&mmWave=" + String(data_record)
                     + "&class=" + String(selected_class);
      // Send the obtained mmWave data parameters and the selected pipeline diagnostic class to the web application via an HTTP GET request.
      make_a_get_post_request(false, request);
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

⭐ The detection result greater than the given threshold (0.60) represents the most accurate label (pipeline diagnostic class) predicted by the model.

⭐ Print the detected anomalies on the serial monitor, if any.

⭐ Finally, clear the features buffer (frame).

```
void run_inference_to_make_predictions(int multiply){
  // Scale (normalize) data items depending on the given model:
  float scaled_p1 = mm.p1;
  float scaled_p2 = mm.p2;
  float scaled_p3 = mm.p3;
  float scaled_p4 = mm.p4;
  float scaled_p5 = mm.p5;
  float scaled_p6 = mm.p6;
  float scaled_p7 = mm.p7;

  // Copy the scaled data items to the features buffer.
  // If required, multiply the scaled data items while copying them to the features buffer.
  for(int i=0; i&lt;multiply; i++){
    features[feature_ix++] = scaled_p1;
    features[feature_ix++] = scaled_p2;
    features[feature_ix++] = scaled_p3;
    features[feature_ix++] = scaled_p4;
    features[feature_ix++] = scaled_p5;
    features[feature_ix++] = scaled_p6;
    features[feature_ix++] = scaled_p7;
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

⭐ In the *take\_picture* function:

⭐ Capture a picture with the built-in GC2145 camera on Nicla Vision and save it to the image buffer.

```
void take_picture(){
  // Capture a picture with the GC2145 camera.
  // If successful:
  if(cam.grabFrame(fb, 3000) == 0){
   Serial.println("\nGC2145 camera: image captured successfully!");
  }else{
    Serial.println("\nGC2145 camera: image capture failed!");
  }
  delay(2000);
}
```

⭐ If Arduino Nano sends the *Run* command with the recently collected mmWave data parameters:

⭐ Glean information as substrings from the transferred data packet by utilizing the ampersand (&) as the delimiter.

⭐ Then, split all mmWave data parameters individually by utilizing the comma (,) as the delimiter.

⭐ Convert the separated data items from strings to their corresponding data types and copy them to the struct as its elements.

⭐ Start running an inference with the Edge Impulse model to make predictions on the pipeline diagnostic classes.

⭐ Capture a picture with the built-in GC2145 camera on Nicla Vision.

⭐ Create the *request* string, including the *results* URL parameter.

⭐ Send the obtained mmWave data parameters, the recently captured image of the deformed pipe, and the model detection results to the web application via an HTTP POST request.

⭐ Finally, clear the received data packet.

```
    if(data_packet.startsWith("Run")){
      // Glean information as substrings from the transferred data packet by Arduino Nano.
      del_1 = data_packet.indexOf("&");
      String data_record = data_packet.substring(del_1 + 1);
      // Elicit data items from the generated substring.
      del_1 = data_record.indexOf(",");
      del_2 = data_record.indexOf(",", del_1 + 1);
      del_3 = data_record.indexOf(",", del_2 + 1);
      del_4 = data_record.indexOf(",", del_3 + 1);
      del_5 = data_record.indexOf(",", del_4 + 1);
      del_6 = data_record.indexOf(",", del_5 + 1);
      // Convert and store the elicited data items.
      mm.p1 = data_record.substring(0, del_1).toFloat();
      mm.p2 = data_record.substring(del_1 + 1, del_2).toFloat();
      mm.p3 = data_record.substring(del_2 + 1, del_3).toFloat();
      mm.p4 = data_record.substring(del_3 + 1, del_4).toFloat();
      mm.p5 = data_record.substring(del_4 + 1, del_5).toFloat();
      mm.p6 = data_record.substring(del_5 + 1, del_6).toFloat();
      mm.p7 = data_record.substring(del_6 + 1).toFloat();

      // Run the Edge Impulse model to make predictions on the pipeline diagnostic classes.
     run_inference_to_make_predictions(1);

      // Capture a picture with the GC2145 camera.
      take_picture();

      // Create the request string.
      String request = "?results=OK&mmWave=" + String(data_record)
                     + "&class=" + classes[predicted_class];
      // Send the obtained mmWave data parameters, the recently captured image, and the model detection result to the web application via an HTTP POST request.
      make_a_get_post_request(true, request);
    }

    // Clear the received data packet.
    data_packet = "";
  }
```

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_run_1.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=f7f45411abec26e814249da8022e57af" width="1600" height="723" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_run_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_run_2.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=80d3fdbd42f068d560b61891c14920ca" width="1600" height="723" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_run_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_run_3.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=bda4ebc3f920a85869e68936564a44f2" width="1600" height="723" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_run_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_run_4.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=a4050cbd136b98e266af72e59ec56bbb" width="1600" height="721" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_run_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_run_5.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=0aaa73638afe2e0f4978e5b834ac2fce" width="1600" height="722" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_run_5.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_run_6.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=45503b4e712c00d6b84998f06958aba6" width="1600" height="721" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_run_6.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/DAzpKIr3HVrIsRBP/.assets/images/ai-pipeline-inspection-mmwave/code_run_7.png?fit=max&auto=format&n=DAzpKIr3HVrIsRBP&q=85&s=490b36e2b27d6617a6be6e0801c0dff7" width="1600" height="723" data-path=".assets/images/ai-pipeline-inspection-mmwave/code_run_7.png" />
</Frame>

## Step 8: Running the model on Nicla Vision to diagnose pipeline defects and transferring model results w/ captured images of the deformed pipes via POST requests

My Edge Impulse neural network model predicts possibilities of labels (pipeline diagnostic classes) for the given features buffer as an array of 3 numbers. They represent the model's *"confidence"* that the given features buffer corresponds to each of the three different pipeline diagnostic classes \[0 - 2], as shown in Step 6:

* 0 — Clogged
* 1 — Cracked
* 2 — Leakage

After executing the *AI\_assisted\_Pipeline\_Diagnostics\_run\_model.ino* file on Nicla Vision:

🚿🔎📲 If the control button (D) connected to Arduino Nano is pressed, it adds the *Run* command to the recently extracted mmWave data parameters, transfers the given information to Nicla Vision via serial communication, and turns the RGB LED to cyan.

🚿🔎📲 Then, it switches the interface button (D) color to cyan and shows the simple radar indicator visualizing the extracted mmWave data parameters on the ILI9341 TFT LCD screen.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/run_1.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=b70fb21699db6b3102b7a3e9311746a3" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/run_1.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/run_2.jpg?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=756d146f8856540e54c19100525ba593" width="750" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/run_2.jpg" />
</Frame>

🚿🔎📲 After Nicla Vision receives the mmWave data parameters with the *Run* command, it runs an inference with the Edge Impulse neural network model by applying the received mmWave data parameters to diagnose pipeline defects and captures an image of the deformed pipe with the built-in GC2145 camera.

🚿🔎📲 Then, it transfers the applied mmWave data parameters, the model detection results, and the captured image of the deformed pipe (raw image buffer) as a TXT file to the web application via an HTTP POST request with URL query parameters.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/finished_3.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=63e11b7b042259ed926eed3caa1cd703" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/finished_3.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/finished_4.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=f4c3bec7a573149b133119219bb6561d" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/finished_4.jpg" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/finished_5.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=f4b581b802037d5fa3f2421d6dd3b47f" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/finished_5.jpg" />
</Frame>

🚿🔎📲 Also, Nicla Vision prints notifications and model detection results on the serial monitor for debugging.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/serial_run_1.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=fcee2fdf6e50fedee3dc195dd71e0755" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/serial_run_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/serial_run_2.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=3eaaaa9ea4091e984da5df294892403b" width="1600" height="848" data-path=".assets/images/ai-pipeline-inspection-mmwave/serial_run_2.png" />
</Frame>

As far as my experiments go, the device diagnoses pipeline defects demonstrated by my custom pipeline system precisely, captures images of deformed pipes, and communicates with the web application flawlessly :)

<Frame caption="image">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/ai-pipeline-inspection-mmwave/gif_run_1.gif" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/ai-pipeline-inspection-mmwave/gif_run_2.gif" />
</Frame>

## Videos and Conclusion

[Data collection | AI-assisted Pipeline Diagnostics w/ mmWave](https://youtu.be/q-59Bzygct8)

[Data collection (web app interface) | AI-assisted Pipeline Diagnostics w/ mmWave](https://youtu.be/G0mbCyk6J3E)

[Experimenting with the model | AI-assisted Pipeline Diagnostics w/ mmWave](https://youtu.be/ghSaefzzEXY)

[Experimenting with the model (web app interface) | AI-assisted Pipeline Diagnostics w/ mmWave](https://youtu.be/ZXVweTodrrc)

## Further Discussions

By applying neural network models trained on pipeline diagnostic classes in detecting pipeline system defects, we can achieve to:

🚿🔎📲 keep machine operations sustainable, profitable, and stable,

🚿🔎📲 prevent faulty pipeline systems from engendering expensive manufacturing problems,

🚿🔎📲 assist small businesses with limited budgets in establishing an efficient and accurate pipeline diagnostics mechanism,

🚿🔎📲 reducing repair costs of high-value machine components,

🚿🔎📲 provide a non-destructive testing and evaluation (NDT\&E) mechanism based on vibration characteristics.

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/D0DCzT3MJCBnkg9J/.assets/images/ai-pipeline-inspection-mmwave/home_0.jpg?fit=max&auto=format&n=D0DCzT3MJCBnkg9J&q=85&s=19d2576d93c5906424c8e1ee7bed3554" width="1333" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/home_0.jpg" />
</Frame>

## References

\[^1] Ahmed Sachit Hashim, Bogdan Gramescu, Constantin Nitu, *PIPE CRACKS DETECTION METHODS – A REVIEW*, International Journal of Mechatronics and Applied Mechanics, 2018, Issue 3, *[https://ijomam.com/wp-content/uploads/2017/02/pag.-114-119\\\_PIPE-CRACKS-DETECTION-METHODS.pdf](https://ijomam.com/wp-content/uploads/2017/02/pag.-114-119\\_PIPE-CRACKS-DETECTION-METHODS.pdf)*

\[^2] Prabhat Sharma, Bambam Kumar, Dharmendra Singh, *Novel Adaptive Buried Nonmetallic Pipe Crack Detection Algorithm for Ground Penetrating Radar*, Progress In Electromagnetics Research M, Vol. 65, 79-90, 2018, *doi:10.2528/PIERM17101002*

\[^3] M. D. Buhari, G. Y. Tian and R. Tiwari, *Microwave-Based SAR Technique for Pipeline Inspection Using Autofocus Range-Doppler Algorithm*, IEEE Sensors Journal, vol. 19, no. 5, pp. 1777-1787, March, 2019, *[https://ieeexplore.ieee.org/document/8520883](https://ieeexplore.ieee.org/document/8520883)*

## Schematics

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_0.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=4896155b43dd0d4abaf68ef9808fbd3d" width="1020" height="822" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_0.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_1.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=18b5f78769da013efe6510cf5b2eb57c" width="675" height="775" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_1.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_2.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=46cd16c1b61ac415867712fda42010b4" width="652" height="772" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_2.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_3.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=99221faa0522d806eb03584ebb393e60" width="647" height="775" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_3.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_4.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=7d8a242b815319c08fd44d264d38bd7c" width="691" height="780" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_4.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_5.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=d599e9322a50c70bb5e573723f1ae171" width="1098" height="885" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_5.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/iMH6bFC2KrA_GsHP/.assets/images/ai-pipeline-inspection-mmwave/PCB_6.png?fit=max&auto=format&n=iMH6bFC2KrA_GsHP&q=85&s=a86a73652ba10c92604d9a830e13a56a" width="823" height="887" data-path=".assets/images/ai-pipeline-inspection-mmwave/PCB_6.png" />
</Frame>

<br />

<Frame caption="image">
  <img src="https://mintcdn.com/edgeimpulse/gYeiu5y8FvZDYHfU/.assets/images/ai-pipeline-inspection-mmwave/nicla_vision_pinout.png?fit=max&auto=format&n=gYeiu5y8FvZDYHfU&q=85&s=362de3c759507711b766f57096e3d9a4" width="1093" height="1000" data-path=".assets/images/ai-pipeline-inspection-mmwave/nicla_vision_pinout.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).