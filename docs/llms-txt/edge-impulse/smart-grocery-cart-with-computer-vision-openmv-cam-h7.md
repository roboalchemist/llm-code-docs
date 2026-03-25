# Source: https://docs.edgeimpulse.com/projects/expert-network/smart-grocery-cart-with-computer-vision-openmv-cam-h7.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Grocery Cart Using Computer Vision - OpenMV Cam H7

Created By: Kutluhan Aktar

Public Project Link: [https://studio.edgeimpulse.com/public/166688/latest](https://studio.edgeimpulse.com/public/166688/latest)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_3.0.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=03c0459622d70ada6b25e154c15f2363" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_3.0.jpg" />
</Frame>

## Description

Especially after the recent success of Amazon Go cashierless convenience stores, there is a surge in adaptations of this relatively new approach to the shopping experience, including computer vision, sensor fusion, and deep learning. Since the nonpareil concept of cashierless stores is to make shoppers avoid tedious checkout lines and self-checkout stations, the stores equipped with this technology improve the customer experience and increase profit margins comparatively. While implementing this technology in a grocery or convenience store, smart grocery carts are the most prominent asset to provide an exceptional customer experience like Amazon Go.

Although smart grocery carts improve the customer experience and plummet maintenance costs by providing an automated product tracking and payment system, the current integration methods are expensive investments for small businesses in the food retail industry since these methods require renovating (remodeling) store layouts or paying monthly fees to cloud services.

After perusing recent research papers on smart grocery carts, I noticed there is no appliance devised for converting regular grocery carts into smart grocery carts without changing anything else in an existing establishment. Therefore, I decided to build a budget-friendly and easy-to-use device giving smart grocery cart perks to regular grocery carts with a user-friendly interface.

To detect different food retail products accurately, I needed to create a valid data set in order to train my object detection model with notable veracity. Since OpenMV Cam H7 is a considerably small high-performance microcontroller board designed specifically for machine vision applications, I decided to utilize OpenMV Cam H7 in this project. Also, I was able to capture product images easily while collecting data and store them on an SD card since OpenMV Cam H7 has a built-in MicroSD card module. Then, I employed a color TFT screen (ST7735) to display a real-time video stream, the prediction (detection) results, and the selection (options) menu.

After completing my data set including various food retail products, I built my object detection model with Edge Impulse to detect products added or removed to/from the grocery cart. I utilized Edge Impulse FOMO (Faster Objects, More Objects) algorithm to train my model, which is a novel machine learning algorithm that brings object detection to highly constrained devices. Since Edge Impulse is nearly compatible with all microcontrollers and development boards, I had not encountered any issues while uploading and running my model on OpenMV Cam H7. As labels, I utilized the product brand names, such as Nutella and Snickers.

After training and testing my object detection (FOMO) model, I deployed and uploaded the model on OpenMV Cam H7 as an OpenMV firmware. Therefore, the device is capable of detecting products by running the model independently without any additional procedures or latency.

Since I wanted to create a full-fledged device providing a wholesome shopping experience, I decided to build a web application from scratch in PHP, JavaScript, CSS, and MySQL. Therefore, I installed an Apache HTTP Server (XAMPP) on LattePanda 3 Delta, which also has a MariaDB database.

This complementing web application lets customers create accounts via its interface, receives requests from the device to add or remove products to/from the customer's database table, and creates a concurrent shopping list from the products added to the grocery cart. Also, the application sends an HTML email to the customer's registered email address when the customer finishes shopping and is ready to leave the store, including the generated shopping list and the payment link.

Since OpenMV Cam H7 does not provide Wi-Fi or cellular connectivity, I employed Beetle ESP32-C3 to get commands from OpenMV Cam H7 via serial communication and communicate with the web application via HTTP GET requests, which is an ultra-small size development board intended for IoT applications. To send commands via serial communication and control the selection menu after a product is detected by the model, I connected a joystick to OpenMV Cam H7. I also utilized the joystick while taking and storing pictures of various food retail products.

To enable the device to determine when the customer completes shopping and is ready to leave the store, I connected an MFRC522 RFID reader to Beetle ESP32-C3 so as to detect the assigned RFID key tag provided by the store per grocery cart. Also, I connected a buzzer and an RGB LED to Beetle ESP32-C3 to inform the customer of the device status.

After completing the wiring on a breadboard for the prototype and testing my code and object detection model, I decided to design a PCB for this project to make the device assembly effortless. Since Scrooge McDuck is one of my favorite cartoon characters and is famous for his wealth and stinginess, I thought it would be hilarious to design a shopping-related PCB based on him.

Lastly, to make the device as robust and sturdy as possible while being attached to a grocery cart and utilized by customers, I designed a semi-transparent hinged case compatible with any grocery cart due to its hooks and snap-fit joints (3D printable).

So, this is my project in a nutshell 😃

In the following steps, you can find more detailed information on coding, capturing food retail product images, storing pictures on an SD card, building an object detection (FOMO) model with Edge Impulse, running the model on OpenMV Cam H7, developing a full-fledged web application, and communicating with the web application via Beetle ESP32-C3.

🎁🎨 Huge thanks to [PCBWay](https://www.pcbway.com/) for sponsoring this project.

🎁🎨 Huge thanks to [DFRobot](https://www.dfrobot.com/?tracking=60f546f8002be) for sponsoring these products:

⭐ Beetle ESP32-C3 | [Inspect](https://www.dfrobot.com/product-2566.html?tracking=60f546f8002be)

⭐ LattePanda 3 Delta 864 | [Inspect](https://www.dfrobot.com/product-2594.html?tracking=60f546f8002be)

⭐ DFRobot 8.9" 1920x1200 IPS Touch Display | [Inspect](https://www.dfrobot.com/product-2007.html?tracking=60f546f8002be)

🎁🎨 Also, huge thanks to [Creality](https://store.creality.com/) for sending me a [Creality Sonic Pad](https://www.creality.com/products/creality-sonic-pad), a [Creality Sermoon V1 3D Printer](https://www.creality.com/products/creality-sermoon-v1-v1-pro-3d-printer), and a [Creality CR-200B 3D Printer](https://www.creality.com/products/cr-200b-3d-printer).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/show_0.jpg?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=f24c61b49d03c9181b060c60f2a4b5e4" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/show_0.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_3.0.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=03c0459622d70ada6b25e154c15f2363" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_3.0.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/completed_3.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=ddf193fb475abae3c2bdced3a411f626" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/completed_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/collect_2.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=5071262e126c5b519f6d7f94ab32f842" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/collect_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/smart-grocery-cart-with-computer-vision/gif_collect.gif" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_16.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=9b2b504ad5c9994f16e987527ce36e6d" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_16.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_17.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=d4eeb758cd9b0faae236d32aca2d99a5" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_17.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_13.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=e839e6fde3be3e4fee15b30759a7896c" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_13.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_8.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=6beb481055a8e652a6e4362a463a337e" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_18.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=d4239cbcc71c24580921233ed208d09c" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_18.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/lattepanda_run_2.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=7f5b8d52dda060cd33e0cf14780aaa35" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/lattepanda_run_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/smart-grocery-cart-with-computer-vision/gif_run.gif" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_working.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=ce47c2c99ffd61a63757d533e3ae5607" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_working.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/email_working.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=99a9c2626dcf2f41387550fc6eb6e667" width="1571" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/email_working.png" />
</Frame>

## Step 1: Designing and soldering the Scrooge McDuck-inspired PCB

Before prototyping my Scrooge McDuck-inspired PCB design, I tested all connections and wiring with OpenMV Cam H7 and Beetle ESP32-C3. Then, I checked the connection status between Beetle ESP32-C3 and the web application hosted on LattePanda 3 Delta.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/breadboard_1.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=3af0f04d724580e397b68c8c1d2d31b9" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/breadboard_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/breadboard_2.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=5d1a74cec9bd6988942c32120e4353de" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/breadboard_2.jpg" />
</Frame>

Then, I designed my Scrooge McDuck-inspired PCB by utilizing KiCad. As mentioned earlier, I chose to design my PCB based on Scrooge McDuck since I loved the juxtaposition of shopping and his well-known stinginess :) I attached the Gerber file of the PCB below. Therefore, if you want, you can order this PCB from PCBWay to build this device giving smart grocery cart perks to any grocery cart.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/PCB_1.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=667b0da4a66b0d5e71b0e3fe320870a9" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/PCB_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/PCB_2.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=a78c9916744182cf52b47142a85669cf" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/PCB_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/PCB_3.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=723e7d6dfb63fac9396c4e3011a9a166" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/PCB_3.jpg" />
</Frame>

First of all, by utilizing a soldering iron, I attached headers (female), a COM-09032 analog joystick, a buzzer, a 5mm common anode RGB LED, and a power jack to the PCB.

📌 Component list on the PCB:

*OpenMV\_H7\_1, OpenMV\_H7\_2 (Headers for OpenMV Cam H7)*

*Beetle\_C3\_1, Beetle\_C3\_2 (Headers for Beetle ESP32-C3)*

*MFRC522 (Headers for MFRC522 RFID Reader)*

*ST7735 (Headers for ST7735 1.8" Color TFT Display)*

*U1 (COM-09032 Analog Joystick)*

*BZ1 (Buzzer)*

*D1 (5mm Common Anode RGB LED)*

*J1 (Power Jack)*

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/PCB_4.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=2b693a22ec7aa8e59920468d0159fb3b" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/PCB_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/PCB_5.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=70dc331c50eb6216a9bf56b1839ace39" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/PCB_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/PCB_6.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=ced48d929266c795d88d6b1ca81f4a36" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/PCB_6.jpg" />
</Frame>

## Step 1.1: Making connections and adjustments

```
// Connections
// Beetle ESP32-C3 :
//                                MFRC522
// D7   --------------------------- RST
// D2   --------------------------- SDA
// D6   --------------------------- MOSI
// D5   --------------------------- MISO
// D4   --------------------------- SCK
//                                OpenMV Cam H7
// D0   --------------------------- P4
// D1   --------------------------- P5
//                                5mm Common Anode RGB LED
// D21  --------------------------- R
// D8   --------------------------- G
// D9   --------------------------- B
//                                Buzzer
// D20  --------------------------- +
//
//
// OpenMV Cam H7 :
//                                ST7735 1.8" Color TFT Display
// 3.3V --------------------------- LED
// P2   --------------------------- SCK
// P0   --------------------------- SDA
// P8   --------------------------- AO
// P7   --------------------------- RESET
// P3   --------------------------- CS
// GND  --------------------------- GND
// 3.3V --------------------------- VCC
//                                JoyStick
// P6   --------------------------- VRX
// P9   --------------------------- SW
```

After completing soldering, I attached all remaining components to the Scrooge McDuck PCB via headers — OpenMV Cam H7, Beetle ESP32-C3, MFRC522 RFID reader, and ST7735 color TFT display.

I connected a color TFT screen (ST7735) to [OpenMV Cam H7](https://openmv.io/products/openmv-cam-h7) so as to display the real-time video stream, the detection results after running the object detection (FOMO) model, and the selection (options) menu. To save images under two categories and control the selection menu after a product is detected by the model, I connected an analog joystick (COM-09032) to OpenMV Cam H7.

To be able to transfer commands to [Beetle ESP32-C3](https://wiki.dfrobot.com/SKU_DFR0868_Beetle_ESP32_C3) via serial communication, I connected the hardware serial port of OpenMV Cam H7 (UART 3) to the hardware serial port of Beetle ESP32-C3 (Serial1). To enable the device to determine when the customer finishes shopping and is ready to leave the store, I connected an MFRC522 RFID reader to Beetle ESP32-C3. Also, I connected a buzzer and an RGB LED to inform the customer of the device status, denoting web application connection and serial communication success.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/PCB_7.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=a148ab0b577af8ed0f5f3bd405fd5727" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/PCB_7.jpg" />
</Frame>

## Step 2: Designing and printing a semi-transparent hinged case

Since I focused on building a budget-friendly and easy-to-use device that captures food retail product images, detects products with object detection, and provides an exceptional customer experience, I decided to design a robust and sturdy semi-transparent hinged case allowing the customer to access the RFID reader and the joystick effortlessly. To avoid overexposure to dust and prevent loose wire connections, I added two snap-fit joints to the hinged case. Also, I decided to emboss different grocery cart icons on the top part of the hinged case to emphasize the shopping theme gloriously :)

Since I needed to connect the top and bottom parts of the hinged case seamlessly, I designed a pin with pin ends (caps). To make the device compatible with any grocery cart, I added two hooks on the back of the bottom part. Also, I added a ring to the bottom part to attach the assigned RFID key tag.

I designed the top and bottom parts of the hinged case, the pin, and the pin ends in Autodesk Fusion 360. You can download their STL files below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_1.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=7037e3fe330ede177a70460a34a9302e" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_2.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=d4a5adcbce3c59b3bae700914adc02da" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_3.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=7aaf32b9437013695df9ab5bf11fc096" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_4.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=485649b845c0624c95df66f77e65c210" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_5.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=f88da3eb007f5b5c49acaff54f2f9474" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_6.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=df7d0789a07aff5aca01fd4a81d987f9" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_7.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=f212f0d94db97882f10ed6c30f4e9278" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_7.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_8.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=63ad473eac7c3bf0252a9b20dc4204c9" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_8.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_9.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=b97e197eeeed650ba81dfb69df272a23" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_9.png" />
</Frame>

Then, I sliced all 3D models (STL files) in Ultimaker Cura.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_10.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=ec981d6b5659ec0e256d20757e7d82a5" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_10.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_11.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=60f55503be9162a99f3983ad4483751b" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_11.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_12.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=17fd553589ea728e9deb206e9386953b" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_12.png" />
</Frame>

Since I wanted to create a semi-transparent solid structure for the hinged case representing product packaging, I utilized this PLA filament:

* Natural

Finally, I printed all parts (models) with my Creality Sermoon V1 3D Printer and Creality CR-200B 3D Printer in combination with the Creality Sonic Pad. You can find more detailed information regarding the Sonic Pad in Step 2.1.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_finished_1.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=d0b370f5d495757b0a14cecac4d8de03" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_finished_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/model_finished_2.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=7c946e0e3b390fe9389da3ce7528b573" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/model_finished_2.jpg" />
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

## Step 2.1: Improving print quality and speed with the Creality Sonic Pad

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

## Step 2.2: Assembling the semi-transparent hinged case

After printing all parts (models), I placed the pin through the hinges on the top and bottom parts and fixed the pin via the pin ends (caps).

I affixed the Scrooge McDuck PCB to the bottom part of the hinged case via a hot glue gun.

Then, I attached the ST7735 TFT display to the hinged case via its slot on the bottom part to make customers see the screen even if the hinged case is closed via its built-in snap-fit joints.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_1.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=9f47f961780b5bc1dec81a03d67dc386" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_2.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=6ac1342b6f1ebb8b0cde256d863ab48e" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_3.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=d98d5466a0ab3b6d0f54e6561105b74d" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_3.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_4.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=d94f0c18e86fcd573ede344594d1dce0" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_5.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=8e2eefdb2e9faa0483fa96fb88ca7d54" width="750" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_6.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=7b278e8932d95233b9f9406cc396ee9a" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_7.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=e23d2be37b4653c21e2659eb80824c6b" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_7.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_8.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=42ffd311f2eec22c04058d7ff82ca1d2" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_9.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=568d729979e0ab8eeaa9b2613f4f4963" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_9.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_10.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=3d0f140be663cb2752177bb7e312d074" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_10.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_11.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=429a585c022a0359d845091bb32a3901" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_11.jpg" />
</Frame>

Finally, I attached the assigned RFID key tag to the ring on the bottom part of the hinged case. Via the slot on the top part of the hinged case, the customer can approximate the key tag to the MFRC522 RFID reader even if the case is closed.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/assembly_12.jpg?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=e5674e9f9136aa80dd4d08652f03d9ca" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/assembly_12.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/completed_3.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=ddf193fb475abae3c2bdced3a411f626" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/completed_3.jpg" />
</Frame>

## Step 3: Creating a Twilio SendGrid account to send emails from localhost

Since I wanted to provide a wholesome user experience with this device, I decided to make it able to send the list of the products added to the grocery cart and the payment link to the customer's registered email address on the database. However, I did not want to make this feature dependent on a paid email forwarder or cloud service. Therefore, I decided to send HTML emails directly from localhost via Twilio's SendGrid Email API.

[SendGrid Email API](https://sendgrid.com/solutions/email-api/) provides proven email deliverability with its cloud-based architecture and has free of charge plan with 100 emails per day for relatively small projects like this. Also, SendGrid API provides official libraries for different programming languages, including PHP.

:hash: First of all, sign up for [SendGrid](https://signup.sendgrid.com/) and create a new free trial account.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_1.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=878698cba596eb170de76b59bd710024" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_1.png" />
</Frame>

:hash: Then, click the *Create a Single Sender* button and enter the required information to comply with the anti-spam laws. It is recommended to use a unique email service provider other than Gmail, Hotmail, etc.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_2.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=6203013183e95d0b33e644ce26f47396" width="1600" height="768" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_3.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=633a9c28654712820b4196b4de0e9bab" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_3.png" />
</Frame>

:hash: After verifying the entered email address, choose PHP as the integration API option for localhost.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_4.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=404e26d24e21f48f5829f041d9cdf195" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_5.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=34e57c65380a1fa6188536d25c871d6d" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_5.png" />
</Frame>

:hash: Click the *Create API Key* button to generate an API key with full feature access.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_6.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=aa75a1b31411f4c49215ce32117b5f32" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_7.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=28d9432b771afa7e475d25c86b53f9fa" width="1600" height="776" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_7.png" />
</Frame>

:hash: After generating the API key, install the latest release of the SendGrid Email API PHP Library on localhost directly from [this GitHub repository](https://github.com/sendgrid/sendgrid-php/releases).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_8.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=f83cecf27753f6f2d665151159a17d7d" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_8.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_9.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=bbf24b72b8f8711c4f588f1abdf0a252" width="1600" height="772" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_9.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_10.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=b262f5914fb9e2209be27928140b90c4" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/send_grid_set_10.png" />
</Frame>

## Step 4: Developing a web application with a user-friendly interface in PHP, JavaScript, CSS, and MySQL

To provide an exceptional online customer experience, I developed a full-fledged web application from scratch in PHP, JavaScript, CSS, and MySQL. This web application lets customers create accounts via its interface, receives requests from the device to add or remove the products detected by the object detection model to/from the customer's database table, and creates a concurrent shopping list. Also, it sends an HTML email to the customer's registered email address via SendGrid Email API when the customer finishes shopping and is ready to leave the store, including the generated shopping list and the payment link.

As shown below, the web application consists of one folder and 7 code files:

* /assets
* \-- /sendgrid-php
* \-- background.jpg
* \-- class.php
* \-- icon.png
* \-- index.css
* \-- index.js
* \-- update\_list.php
* index.php
* product\_list.php
* shopping.php

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/app_1.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=b9ee85d08a76e4a9a35165307be54a45" width="1076" height="725" data-path=".assets/images/smart-grocery-cart-with-computer-vision/app_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/app_2.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=db4f7ab68939fc0f379d50ed64334333" width="1210" height="725" data-path=".assets/images/smart-grocery-cart-with-computer-vision/app_2.png" />
</Frame>

📁 *class.php*

In the *class.php* file, I created a class named *\_main* to bundle the following functions under a specific structure.

⭐ Include the Twilio SendGrid Email API PHP Library.

```
require("sendgrid-php/sendgrid-php.php");
```

⭐ Define the *\_main* class and its functions.

⭐ Define the API key and the sender email address required by SendGrid Email API.

```
	public $conn;

	private $sendgrid_API_Key = "&lt;_API_KEY_>";
	private $from_email = "&lt;_FROM_EMAIL_>";

	public function __init__($conn){
		$this->conn = $conn;
	}
```

⭐ In the *database\_create\_customer\_table* function, create a database table on the MariaDB database and add the given customer information to the recently created database table.

⭐ If the customer information is added to the database table successfully, redirect the customer to the product list page — *product\_list.php*.

⭐ Redirect the customer to the home page if there is a pertinent database error.

```
	public function database_create_customer_table($table, $firstname, $lastname, $card_info, $email){
		// Create a new database table.
		$sql_create = "CREATE TABLE `$table`(
							id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
							firstname varchar(255) NOT NULL,
							lastname varchar(255) NOT NULL,
							card_info varchar(255) NOT NULL,
							email varchar(255) NOT NULL,
							product_id varchar(255) NOT NULL,
							product_name varchar(255) NOT NULL,
							product_price varchar(255) NOT NULL
					   );";
		if(mysqli_query($this->conn, $sql_create)){
			echo("&lt;br>Database Table Created Successfully!");
			// Add the customer information to the recently created database table.
			$sql_insert = "INSERT INTO `$table`(`firstname`, `lastname`, `card_info`, `email`, `product_id`, `product_name`, `product_price`)
						   VALUES ('$firstname', '$lastname', '$card_info', '$email', 'X', 'X', 'X')"
					      ;
			if(mysqli_query($this->conn, $sql_insert)) echo("&lt;br>&lt;br>Customer information added to the database table successfully!");
			// If the customer information is added to the database table successfully, redirect the customer to the product list page.
            header("Location: product_list.php");
			exit();
		}else{
			// Redirect the customer to the home page if there is an error.
			header("Location: ./?databaseTableAlreadyCreated");
			exit();
		}
	}
```

⭐ In the *insert\_new\_data* function, insert the given product information into the customer's database table.

```
	public function insert_new_data($table, $product_id, $product_name, $product_price){
		$sql_insert = "INSERT INTO `$table`(`firstname`, `lastname`, `card_info`, `email`, `product_id`, `product_name`, `product_price`)
		               SELECT `firstname`, `lastname`, `card_info`, `email`, '$product_id', '$product_name', '$product_price'
				       FROM `$table` WHERE id=1"
			          ;
		if(mysqli_query($this->conn, $sql_insert)){ return true; } else{ return false; }
	}
```

⭐ In the *remove\_data* function, delete the first row with the given product ID from the customer's database table.

```
	public function remove_data($table, $product_id){
		$sql_delete = "DELETE FROM `$table` WHERE `product_id`='$product_id' limit 1";
		if(mysqli_query($this->conn, $sql_delete)){ return true; } else{ return false; }
	}
```

⭐ In the *get\_purchased\_product\_list* function, get all saved product information in the database table and return it as three lists — product names, product IDs, and product prices.

```
	public function get_purchased_product_list($table){
		$product_names = []; $product_ids = []; $product_prices = [];
		$sql_list = "SELECT * FROM `$table` WHERE id!=1 ORDER BY `id` ASC";
		$result = mysqli_query($this->conn, $sql_list);
		$check = mysqli_num_rows($result);
		if($check > 0){
			while($row = mysqli_fetch_assoc($result)){
				array_push($product_names, $row["product_name"]);
				array_push($product_ids, $row["product_id"]);
				array_push($product_prices, $row["product_price"]);
			}
			return array($product_names, $product_ids, $product_prices);
		}else{
			return array(["Not Found!"], ["Not Found!"], ["Not Found!"]);
		}
	}
```

⭐ In the *get\_table\_name* function, obtain the latest registered customer's (via the web application interface) assigned table name from the database.

⭐ If the *return* value is true, return the obtained table name as a variable.

⭐ If the *return* value is false, print the obtained table and its creation date.

*%kutluhan%2022-12-16 23:49:39%*

```
	public function get_table_name($return){
		$sql_get = "SELECT `table_name`, `create_time` FROM `information_schema`.`TABLES` WHERE `table_schema` = 'smart_grocery_cart' ORDER BY `CREATE_TIME` DESC limit 1";
		$result = mysqli_query($this->conn, $sql_get);
		$check = mysqli_num_rows($result);
		if($check > 0){
			while($row = mysqli_fetch_assoc($result)){
				if(!$return) echo("%".$row["table_name"]."%".$row["create_time"]."%");
				else return $row["table_name"];
			}
		}
	}
```

⭐ In the *get\_email* function, obtain the email address of the given customer from the database.

```
    private function get_email($table){
		$sql_email = "SELECT * FROM `$table` WHERE id=1";
		$result = mysqli_query($this->conn, $sql_email);
		$check = mysqli_num_rows($result);
		if($check > 0){
			if($row = mysqli_fetch_assoc($result)){ return $row["email"]; }
			else{ return "Not Found!"; }
		}
	}
```

⭐ In the *send\_product\_list\_email* function, obtain (and assign) the three product information arrays generated by the *get\_purchased\_product\_list* function and create HTML table rows by utilizing these arrays.

Then, send an HTML email via SendGrid Email API to the customer's registered email address, including the list of the products added to the grocery cart and the link to the payment page — *product\_list.php*.

```
	public function send_product_list_email($table, $tag){
		// Get the customer's email address.
		$to_email = $this->get_email($table);
		// Obtain the list of the products added to the cart from the customer's database table.
	    $product_names = []; $product_ids = []; $product_prices = [];
	    list($product_names, $product_ids, $product_prices) = $this->get_purchased_product_list($_GET['table']);
		$list = "";
		for($i=0; $i&lt;count($product_names); $i++){
			$list .= '&lt;tr>
						&lt;td>'.$product_names[$i].'&lt;/td>
						&lt;td>'.$product_ids[$i].'&lt;/td>
						&lt;td>'.$product_prices[$i].'&lt;/td>
					  &lt;/tr>
					 ';
		}
		// Send an HTML email via the SendGrid Email PHP API.
		$email = new \SendGrid\Mail\Mail();
		$email->setFrom($this->from_email, "Smart Grocery Cart");
		$email->setSubject("Cart Product List");
		$email->addTo($to_email, "Customer");
		$email->addContent("text/html",
		                   '&lt;!DOCTYPE html>
							&lt;html>
							&lt;head>
							&lt;style>
								h1{text-align:center;font-weight:bold;color:#25282A;}
								table{background-color:#043458;width:100%;border:10px solid #25282A;}
								th{background-color:#D1CDDA;color:#25282A;border:5px solid #25282A;font-size:25px;font-weight:bold;}
								td{color:#AEE1CD;border:5px solid #25282A;text-align:left;font-size:20px;font-weight:bold;}
                                a{text-decoration:none;background-color:#5EB0E5;}
							&lt;/style>
							&lt;/head>
							&lt;body>
						    &lt;h1>Thanks for shopping at our store :)&lt;/h1>
						    &lt;h1>Your Customer Tag: '.$tag.'&lt;/h1>
						    &lt;table>
						     &lt;tr>
						      &lt;th>Product Name&lt;/th>
						      &lt;th>Product ID&lt;/th>
						      &lt;th>Product Price&lt;/th>
						     &lt;/tr>
							 '.$list.'
							 &lt;/table>
							 &lt;a href="http://localhost/smart_grocery_cart/product_list.php">&lt;h1>🛒 Checkout 🛒&lt;/h1>&lt;/a>
							 &lt;/body>
							 &lt;/html>
						   '
                          );

		$sendgrid = new \SendGrid($this->sendgrid_API_Key);
		try{
			$response = $sendgrid->send($email);
			print $response->statusCode() . "\n";
			print_r($response->headers());
			print $response->body() . "\n";
		}catch(Exception $e){
			echo 'Caught exception: '. $e->getMessage() ."\n";
		}
	}
}
```

⭐ Define the required MariaDB database connection settings for LattePanda 3 Delta 864.

```
$server = array(
	"name" => "localhost",
	"username" => "root",
	"password" => "",
	"database" => "smart_grocery_cart"
);

$conn = mysqli_connect($server["name"], $server["username"], $server["password"], $server["database"]);
```

📁 *shopping.php*

⭐ Include the *class.php* file.

⭐ Define the *customer* object of the *\_main* class with its required parameters.

```
include_once "assets/class.php";

// Define the new 'customer' object:
$customer = new _main();
$customer->__init__($conn);
```

⭐ If the customer requests to create an account via the web application interface *(index.php)*, create a new database table for the customer and insert the given customer information as the first row.

```
if(isset($_GET['table']) && isset($_GET['firstname']) && isset($_GET['lastname']) && isset($_GET['card_info']) && isset($_GET['email'])){
	$customer->database_create_customer_table($_GET['table'], $_GET['firstname'], $_GET['lastname'], $_GET['card_info'], $_GET['email']);
}
```

⭐ If Beetle ESP32-C3 transfers the information of the product added to the grocery cart via an HTTP GET request, insert the received product data into the customer's database table.

```
if(isset($_GET['add']) && isset($_GET['table']) && isset($_GET['product_id']) && isset($_GET['product_name']) && isset($_GET['product_price'])){
	if($customer->insert_new_data($_GET['table'], $_GET['product_id'], $_GET['product_name'], $_GET['product_price'])){
		echo("Product information saved successfully to the customer's database table!");
	}else{
		echo("Database error!");
	}
}
```

⭐ If Beetle ESP32-C3 transfers the information of the product removed from the grocery cart via an HTTP GET request, delete the removed product's data from the customer's database table.

```
if(isset($_GET['remove']) && isset($_GET['table']) && isset($_GET['product_id'])){
	if($customer->remove_data($_GET['table'], $_GET['product_id'])){
		echo("Product information removed successfully from the customer's database table!");
	}else{
		echo("Database error!");
	}
}
```

⭐ If requested by Beetle ESP32-C3, send an HTML email to the customer's registered email address via SendGrid Email API, including the list of the products added to the cart, the link to the payment page *(product\_list.php)*, and the assigned RFID key tag UID.

```
if(isset($_GET['table']) && isset($_GET['send_email']) && isset($_GET['tag'])){
	$customer->send_product_list_email($_GET['table'], $_GET['tag']);
}
```

⭐ If requested, get the latest registered table name from the database and print it with its creation date.

```
if(isset($_GET["deviceChangeTable"])){
	$customer->get_table_name(false);
}
```

📁 *index.php*

⭐ Create the web application interface, including the HTML form for creating a new account.

You can inspect and download the *index.php* file below.

📁 *update\_list.php*

⭐ Include the *class.php* file.

⭐ Define the *customer* object of the *\_main* class with its required parameters.

```
include_once "class.php";

// Define the new 'customer' object:
$customer = new _main();
$customer->__init__($conn);
```

⭐ Obtain the latest registered customer's table name.

```
$table = $customer->get_table_name(true);
```

⭐ Get all saved product information in the database table as three different lists — product names, product IDs, and product prices — and create HTML table rows by utilizing these arrays.

```
$product_names = []; $product_ids = []; $product_prices = [];
list($product_names, $product_ids, $product_prices) = $customer->get_purchased_product_list($table);
$list = "&lt;tr>&lt;th>Product Name&lt;/th>&lt;th>Product ID&lt;/th>&lt;th>Product Price&lt;/th>&lt;/tr>";
for($i=0; $i&lt;count($product_names); $i++){
	$list .= '&lt;tr>
				&lt;td>'.$product_names[$i].'&lt;/td>
				&lt;td>'.$product_ids[$i].'&lt;/td>
				&lt;td>'.$product_prices[$i].'&lt;/td>
			  &lt;/tr>
			 ';
}
```

⭐ Finally, return the generated table rows as the added product list.

```
echo($list);
```

📁 *index.js*

⭐ In JavaScript (jQuery and AJAX), every 3 seconds, retrieve the list of the products added to the cart from the database table to inform the customer concurrently via the product list (payment) page — *product\_list.php*.

```
setInterval(function(){
	$.ajax({
		url: "./assets/update_list.php",
		type: "GET",
		success: (response) => {
			$(".container table").html(response);
		}
	});
}, 3000);
```

📁 *product\_list.php*

⭐ In the *product\_list.php* file, create the concurrent HTML table showing the information of the products added to the grocery cart, which is updated every three seconds via the jQuery script.

⭐ You can inspect and download the *product\_list.php* file below.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_1.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=b2bc347dac66aa1130ef46cff972022b" width="1600" height="907" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_2.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=2e66d5a7e2d98db14b0571d4ede7cd4d" width="1600" height="779" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_3.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=05d81311a4036ca745dee61cd470e1aa" width="1600" height="830" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_4.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=b3b05a6ef3e1d59d8c559e6e2f6c3311" width="1600" height="790" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_5.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=fa3052c5461de8fdfef7daae06d275a7" width="1600" height="892" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_6.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=ea8e886111622cb10da1733fffce4e22" width="1600" height="888" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_7.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=271097bb644c5413ed6b6e9b3faedd6c" width="1600" height="749" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_7.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_8.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=b98cfd7b5572ce89c66ede5ee7adeb6c" width="1600" height="774" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_8.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_9.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=679f10cc7d645ec22d60919ac9efdf02" width="1600" height="602" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_9.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_app_10.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=ec6be8b076d259d9320c48f6c14abd00" width="1600" height="597" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_app_10.png" />
</Frame>

## Step 4.1: Setting and running the web application on LattePanda 3 Delta 864

Since I have got a test sample of the brand-new [LattePanda 3 Delta 864](https://www.dfrobot.com/product-2594.html), I decided to host my web application on LattePanda 3 Delta. Therefore, I needed to set up a LAMP web server.

LattePanda 3 Delta is a pocket-sized hackable computer that provides ultra performance with the Intel 11th-generation Celeron N5105 processor.

Plausibly, LattePanda 3 Delta can run the XAMPP application. So, it is effortless to create a server with a MariaDB database on LattePanda 3 Delta.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/lattepanda_run_1.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=d04e7fd28e4f0855f30669319cefe2a1" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/lattepanda_run_1.jpg" />
</Frame>

:hash: First of all, install and set up [the XAMPP application](https://www.apachefriends.org/).

:hash: Then, go to the *XAMPP Control Panel* and click the *MySQL Admin* button.

:hash: Once the *phpMyAdmin* tool pops up, create a new database named *smart\_grocery\_cart*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/A2Bwlb7Fn9Ob3CFt/.assets/images/egg-counting-openmv/app_server_set_1.png?fit=max&auto=format&n=A2Bwlb7Fn9Ob3CFt&q=85&s=0358da8cb1fb2b2edc29e36f49f5bdc7" width="1600" height="848" data-path=".assets/images/egg-counting-openmv/app_server_set_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/database_1.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=08158d6a8906798547485453340d6e6a" width="1600" height="775" data-path=".assets/images/smart-grocery-cart-with-computer-vision/database_1.png" />
</Frame>

## Step 4.2: Providing a wholesome retail customer experience via the web application

After setting the web application on LattePanda 3 Delta 864:

🛒🛍️📲 The web application interface *(index.php)* lets the customer create an account by filling out the form:

* First name
* Last name
* Email
* Account name
* Card number

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_1.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=16abed3ac3996999f3376b4e63551c42" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_2.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=49e2f679427d3145e85c3bca2688a5d5" width="1600" height="852" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_2.png" />
</Frame>

🛒🛍️📲 The web application creates and names the customer's database table with the given account name. Then, it inserts the given customer information into the database table as the first row.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/database_2.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=c902f66f717b3883447e2acd68b39cca" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/database_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/database_3.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=6ef6acc15a16f5396f6c95d9693a0dce" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/database_3.png" />
</Frame>

🛒🛍️📲 The web application communicates with Beetle ESP32-C3 via HTTP GET requests on the *shopping.php* file:

*?table=kutluhan\&firstname=kutluhan\&lastname=aktar\&card\_info=5236896598245668\&email=[info@theamplituhedron.com](mailto:info@theamplituhedron.com)*

*?add=OK\&table=kutluhan\&product\_id=001\&product\_name=Barilla\&product\_price=\$4.72*

*?remove=OK\&table=kutluhan\&product\_id=001*

*?table=kutluhan\&tag=56\_1B\_0D\_F8\&send\_email=OK*

*?deviceChangeTable*

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_6.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=e25fbe5619b9907c4e00225485d0098c" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_7.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=b27be979a68d4cc77c581b96e73d104b" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_7.png" />
</Frame>

🛒🛍️📲 The web application saves the list of the products added to the grocery cart in the database.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/database_4.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=c8d2629fe954ecd285ff073e69260e45" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/database_4.png" />
</Frame>

🛒🛍️📲 On the *product\_list.php* file, the web application displays the concurrent list of the products added to the cart as an HTML table, updated every three seconds via the jQuery script.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_3.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=1d1d6b5969239a8663c47cb24036b636" width="1600" height="853" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_4.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=843dee38a3bc2c2ec6592ce82eaa886c" width="1600" height="851" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_5.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=af290f9986bd80d350156bdbc9ea3516" width="1600" height="851" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_5.png" />
</Frame>

🛒🛍️📲 Also, the web application sends an HTML email to the customer's registered email address via SendGrid Email API when the customer finishes shopping, including the list of the products added to the cart, the link to the payment page *(product\_list.php)*, and the assigned RFID key tag UID.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_8.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=ed7c528153ca6fec75db6bf54f3cda2f" width="1578" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_8.png" />
</Frame>

## Step 5: Capturing and storing product images w/ OpenMV Cam H7

Before proceeding with the following steps, I needed to install the OpenMV IDE in order to program OpenMV Cam H7.

Plausibly, the OpenMV IDE includes all required libraries and modules for this project. Therefore, I did not need to download additional modules after installing the OpenMV IDE from [here](https://openmv.io/pages/download).

You can get more information regarding the specific OpenMV MicroPython libraries from [here](https://docs.openmv.io/library/index.html#libraries-specific-to-the-openmv-cam).

After setting up OpenMV Cam H7 on the OpenMV IDE, I programmed OpenMV Cam H7 to capture product images in order to store them on the SD card and create appropriately labeled samples for the Edge Impulse object detection (FOMO) model.

Since I decided to distinguish foods and drinks with classes while creating a valid data set for the object detection model, I utilized the joystick attached to OpenMV Cam H7 so as to choose among two different classes. After selecting a class, OpenMV Cam H7 captures a picture, appends the selected class name (Food or Drink) with the current date & time to the file name, and then saves the captured image to the SD card under the *samples* folder.

* Joystick (Up) ➡ Food
* Joystick (Down) ➡ Drink

You can download the *smart\_grocery\_cart\_data\_collect.py* file to try and inspect the code for capturing images and storing them on the SD card via OpenMV Cam H7.

⭐ Include the required modules.

```
import sensor, image, math, lcd
from time import sleep
from pyb import RTC, Pin, ADC, LED
```

⭐ Initialize the camera sensor with its required settings (pixel format and frame size).

```
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QQVGA2) # Special 128x160 framesize for LCD Shield.
```

⭐ Initialize the ST7735 1.8" color TFT screen.

⭐ Set the built-in RTC (real-time clock).

```
lcd.init()

# Set the built-in RTC (real-time clock).
rtc = RTC()
rtc.datetime((2022, 12, 6, 5, 15, 35, 52, 0))
```

⭐ Define the RGB LED and joystick pins.

```
red = LED(1)
green = LED(2)
blue = LED(3)

# Joystick:
J_VRX = ADC(Pin('P6'))
J_SW = Pin("P9", Pin.IN, Pin.PULL_UP)
```

⭐ In the *adjustColor* function, adjust the color of the built-in RGB LED on OpenMV Cam H7.

```
def adjustColor(leds):
    if leds[0]: red.on()
    else: red.off()
    if leds[1]: green.on()
    else: green.off()
    if leds[2]: blue.on()
    else: blue.off()
```

⭐ In the *save\_sample* function:

⭐ Get the current date and time.

⭐ Capture an image with OpenMV Cam H7 as a sample in the given frame settings (160X160).

⭐ Save the captured image in the JPG format and turn the built-in RGB LED to the selected class' assigned color.

⭐ Show a glimpse of the captured image on the ST7735 1.8" color TFT screen.

⭐ Also, show the selected class name with its assigned color on the screen.

⭐ Finally, turn off the built-in RGB LED.

```
def save_sample(name, color, leds):
    # Get the current date and time.
    date = rtc.datetime()
    date = ".{}_{}_{}_{}-{}-{}".format(date[0], date[1], date[2], date[4], date[5], date[6])
    # Take a picture with the given frame settings (160X160).
    sensor.set_framesize(sensor.B160X160)
    sample = sensor.snapshot()
    sleep(1)
    # Save the captured image.
    file_name = "/samples/" + name + date + ".jpg"
    sample.save(file_name, quality=20)
    adjustColor(leds)
    print("\nSample Saved: " + file_name + "\n")
    # Show a glimpse of the captured image on the ST7735 1.8" color TFT screen.
    sensor.set_framesize(sensor.QQVGA2)
    lcd_img = sensor.snapshot()
    lcd_img.draw_rectangle(0, 0, 128, 30, fill=1, color =(0,0,0))
    lcd_img.draw_string(int((128-16*len(name))/2), 3, name, color=color, scale=2)
    lcd_img.draw_rectangle(0, 130, 128, 160, fill=1, color =(0,0,0))
    lcd_img.draw_string(int((128-16*len("Saved!"))/2), 132, "Saved!", color=color, scale=2)
    lcd_img.draw_cross(64, 80, color=color, size=8, thickness=2)
    lcd.display(lcd_img)
    sleep(5)
    adjustColor((0,0,0))
```

⭐ In the *readJoystick* function, get the joystick movements and switch button value.

```
def readJoystick():
    j_x = ((J_VRX.read() * 3.3) + 2047.5) / 4095
    j_x = math.ceil(j_x)
    sw = J_SW.value()
    return (j_x, sw)
```

⭐ In the *while* loop, display a real-time video stream on the ST7735 1.8" color TFT screen and save image samples named with the selected class (Food or Drink), depending on joystick movements.

```
while(True):
    # Display a real-time video stream on the ST7735 1.8" color TFT screen.
    sensor.set_framesize(sensor.QQVGA2)
    lcd_img = sensor.snapshot()
    lcd.display(lcd_img)

    # Read controls from the joystick.
    j_x, sw = readJoystick()

    # Save samples (images) distinguished by 'food' and 'drink' labels.
    if(j_x > 3):
        save_sample("Food", (255,0,255), (1,0,1))
    if(j_x &lt; 2):
        save_sample("Drink", (0,255,255), (0,1,1))
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_collect_1.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=42ff8b5166b9796742aa8d65efc13bb5" width="1536" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_collect_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_collect_2.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=e46360b1276bdeca824c3db8917c100a" width="1541" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_collect_2.png" />
</Frame>

## Step 5.1: Saving the captured product images to the SD card as samples

After uploading and running the code for capturing product images and saving them to the SD card on OpenMV Cam H7:

🛒🛍️📲 The device shows a real-time video stream on the ST7735 color TFT display.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/collect_0.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=10602370918fee942a6ee340c7dacf64" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/collect_0.jpg" />
</Frame>

🛒🛍️📲 If the joystick is moved up, the device captures a picture of the given food retail product in the 160x160 frame size. If the device captures the picture successfully, it pauses the video stream, turns the built-in RGB LED to magenta, appends the selected class name (Food) with the current date & time to the file name, and stores the recently captured image on the SD card under the *samples* folder.

*Food.2022\_12\_6\_15-36-21.jpg*

🛒🛍️📲 Then, the device displays the selected class name and the crosshair with the assigned class color (magenta) on the ST7735 TFT screen.

🛒🛍️📲 Finally, the device resumes the video stream and turns off the built-in RGB LED.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/collect_1.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=634e077c665de57dfb2c38c9913a2f20" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/collect_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/collect_2.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=5071262e126c5b519f6d7f94ab32f842" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/collect_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/collect_3.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=d545fa428a13aa497b71ea7fed205884" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/collect_3.jpg" />
</Frame>

🛒🛍️📲 If the joystick is moved down, the device captures a picture of the given food retail product in the 160x160 frame size. If the device captures the picture successfully, it pauses the video stream, turns the built-in RGB LED to cyan, appends the selected class name (Drink) with the current date & time to the file name, and stores the recently captured image on the SD card under the *samples* folder.

*Drink.2022\_12\_6\_15-39-26.jpg*

🛒🛍️📲 Then, the device displays the selected class name and the crosshair with the assigned class color (cyan) on the ST7735 TFT screen.

🛒🛍️📲 Finally, the device resumes the video stream and turns off the built-in RGB LED.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/collect_4.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=90d7c1bf9c07715126fadb1806922325" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/collect_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/collect_5.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=cea5031abe1723c3404e9be47d8f4641" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/collect_5.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/collect_6.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=887a12f2614c3bd3ce596858f4b1fef7" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/collect_6.jpg" />
</Frame>

🛒🛍️📲 Also, the device prints notifications and the captured image data on the OpenMV IDE serial monitor for debugging.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/serial_collect_1.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=a70643d7c59d5e7b7a8e22523116c6e5" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/serial_collect_1.png" />
</Frame>

I decided to add two different classes (Food and Drink) to the file names while collecting product images in order to distinguish products under two main categories. Although I utilized the product brand names, such as Nutella and Snickers, to label my images, these classes helped me to label foods and drinks separately and saved the time of labeling on Edge Impulse.

As far as my experiments go, the device operates impeccably while capturing food retail product images and saving them to the SD card :)

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/smart-grocery-cart-with-computer-vision/gif_collect.gif" />
</Frame>

After capturing numerous images of different food retail products, I elicited my relatively modest data set under the *samples* folder on the SD card, including training and testing samples for my object detection (FOMO) model.

Since OpenMV Cam H7 runs my object detection (FOMO) model, I decided to focus on a small group of products so as to avoid exceeding the memory limitations.

* Barilla
* Milk
* Nutella
* Pringles
* Snickers

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/products.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=d0a40e83a37b6f732e5a26b77f5b0e72" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/products.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/data_collected.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=e622570ff527a8ece00d4a58f70021bb" width="1600" height="829" data-path=".assets/images/smart-grocery-cart-with-computer-vision/data_collected.png" />
</Frame>

## Step 6: Building an object detection (FOMO) model with Edge Impulse

When I completed capturing food retail product images and storing them on the SD card, I started to work on my object detection (FOMO) model to detect different products.

Since Edge Impulse supports almost every microcontroller and development board due to its model deployment options, I decided to utilize Edge Impulse to build my object detection model. Also, Edge Impulse provides an elaborate machine learning algorithm (FOMO) for running more accessible and faster object detection models on edge devices such as OpenMV Cam H7.

[Edge Impulse FOMO (Faster Objects, More Objects)](/studio/projects/learning-blocks/blocks/object-detection/fomo) is a novel machine learning algorithm that brings object detection to highly constrained devices. FOMO models can count objects, find the location of the detected objects in an image, and track multiple objects in real-time, requiring up to 30x less processing power and memory than MobileNet SSD or YOLOv5.

Even though Edge Impulse supports JPG or PNG files to upload as samples directly, each training or testing sample needs to be labeled manually. Therefore, I needed to follow the steps below to format my data set so as to train my object detection model accurately:

* Data Scaling (Resizing)
* Data Labeling

Since I collected images of food retail products, I preprocessed my data set effortlessly to label each image sample on Edge Impulse by utilizing the product brand names:

* Barilla
* Milk
* Nutella
* Pringles
* Snickers

Plausibly, Edge Impulse allows building predictive models optimized in size and accuracy automatically and deploying the trained model as an OpenMV firmware. Therefore, after scaling (resizing) and preprocessing my data set to label samples, I was able to build an accurate object detection model to detect a small group of products, which runs on OpenMV Cam H7 without getting memory allocation errors.

You can inspect [my object detection (FOMO) model on Edge Impulse](https://studio.edgeimpulse.com/public/166688/latest) as a public project.

## Step 6.1: Uploading images (samples) to Edge Impulse and labeling samples

After collecting training and testing image samples, I uploaded them to my project on Edge Impulse. Then, I utilized the product brand names to label each sample.

:hash: First of all, sign up for [Edge Impulse](https://www.edgeimpulse.com/) and create a new project.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_1.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=28bcdae106403309cffff5591477b79d" width="1600" height="775" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_1.png" />
</Frame>

:hash: To be able to label image samples manually on Edge Impulse for object detection models, go to *Dashboard ➡ Project info ➡ Labeling method* and select *Bounding boxes (object detection)*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_2.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=1a5c3050f22dd932229c84e9e26a74a5" width="1600" height="776" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_2.png" />
</Frame>

:hash: Navigate to the *Data acquisition* page and click the *Upload existing data* button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_3.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=32c21590b99541523eb894733aff9a04" width="1600" height="755" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_4.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=16a1ecfe5e59a9b9d720a9a876a96415" width="1600" height="752" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_4.png" />
</Frame>

:hash: Then, choose the data category (training or testing), select image files, and click the *Begin upload* button.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_5.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=4b1da74f1fcd1bfbe69fc0119d17fcd0" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_6.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=f625bf1b5ad322c36911c8cf7b9fa694" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_6.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_7.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=bc11eb641b31899737e523d1824fc814" width="1600" height="769" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_7.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_8.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=9c04ec0fba3f1b09d8bbd464cb41955b" width="1600" height="772" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_8.png" />
</Frame>

After uploading my data set successfully, I labeled each sample by utilizing the product brand names. In Edge Impulse, labeling an object is as easy as dragging a box around it and entering a label. Also, Edge Impulse runs a tracking algorithm in the background while labeling objects, so it moves bounding boxes automatically for the same objects in different images.

:hash: Go to *Data acquisition ➡ Labeling queue (Object detection labeling)*. It shows all the unlabeled images (training and testing) remaining in the given data set.

:hash: Finally, select an unlabeled image, drag bounding boxes around objects, click the *Save labels* button, and repeat this process until the whole data set is labeled.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_9.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=d10f558711c3c4c52a1f774c2744d4c3" width="1600" height="775" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_9.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_10.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=d4c82b12995db9871a50ab9dfade0770" width="1600" height="777" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_10.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_11.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=f26c9d72c274e485426a8ede6275474c" width="1600" height="776" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_11.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_12.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=6fbb53af5f70656b9cee16ac21d74b73" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_12.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_13.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=eed3673c448786f4b8167cb04ba2304c" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_13.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_14.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=d38e3e831e6563f5a9f607f5aefc05b8" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_14.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_15.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=166f01c4aa7a4072a88b361118852d8c" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_15.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_16.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=550bc6b5ef8d6680d803673984a1ed8c" width="1600" height="776" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_16.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_17.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=761ec05cad7ddd100665e0f8fccb34ef" width="1600" height="777" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_17.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_18.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=4fbb495e43cc7b6cc3be0372e479cf6c" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_18.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_19.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=8f1b8dda06099a20c678cecb16dbacee" width="1600" height="775" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_19.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_set_20.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=164adc46aba76293fed082aa485c5ea6" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_set_20.png" />
</Frame>

## Step 6.2: Training the FOMO model on various food retail products

After labeling my training and testing samples successfully, I designed an impulse and trained it on detecting a small group of food retail products.

An impulse is a custom neural network model in Edge Impulse. I created my impulse by employing the *Image* preprocessing block and the *Object Detection (Images)* learning block.

The *Image* preprocessing block optionally turns the input image format to grayscale and generates a features array from the raw image.

The *Object Detection (Images)* learning block represents a machine learning algorithm that detects objects on the given image, distinguished between model labels.

:hash: Go to the *Create impulse* page and set image width and height parameters to 160. Then, select the resize mode parameter as *Fit shortest axis* so as to scale (resize) given training and testing image samples.

:hash: Select the *Image* preprocessing block and the *Object Detection (Images)* learning block. Finally, click *Save Impulse*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_train_1.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=5f132873d242d45cb882b37e3376654b" width="1600" height="776" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_train_1.png" />
</Frame>

:hash: Before generating features for the object detection model, go to the *Image* page and set the *Color depth* parameter as *Grayscale*. Then, click *Save parameters*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_train_2.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=d6dc20492057038f800da16f7d24f959" width="1600" height="771" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_train_2.png" />
</Frame>

:hash: After saving parameters, click *Generate features* to apply the *Image* preprocessing block to training image samples.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_train_3.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=193cf30c004e476f9a44772b594375db" width="1600" height="775" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_train_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/edge_train_4.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=b63c5d5af1f04f75a67b9d702b47a55a" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_train_4.png" />
</Frame>

:hash: Finally, navigate to the *Object detection* page and click *Start training*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/edge_train_5.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=317a3e24e71033190050c8356caf1f8f" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_train_5.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/edge_train_6.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=30db05d4ae39b1d03992057daa0c968b" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_train_6.png" />
</Frame>

According to my experiments with my object detection model, I modified the neural network settings and architecture to build an object detection model with high accuracy and validity:

📌 Neural network settings:

* Number of training cycles ➡ 100
* Learning rate ➡ 0.005
* Validation set size ➡ 5

📌 Neural network architecture:

* FOMO (Faster Objects, More Objects) MobileNetV2 0.35

After generating features and training my FOMO model with training samples, Edge Impulse evaluated the F1 score (accuracy) as *100%*.

The F1 score (accuracy) is approximately *100%* due to the modest volume and variety of training samples showing a small group of food retail products. In technical terms, the model trains on limited validation samples. Therefore, I am still collecting different product images to broaden the range of products in my data set.

If you encounter any memory allocation errors while uploading the model to OpenMV Cam H7 as an OpenMV firmware, try utilizing 96 x 96 or 80 x 80 image resolutions instead of 160 x 160 while creating your impulse. Even though smaller resolutions plummet the model accuracy, they also reduce the model size.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/edge_train_7.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=13d4af645886bcba21617ec2abf52b0c" width="1600" height="775" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_train_7.png" />
</Frame>

## Step 6.3: Evaluating the model accuracy and deploying the model

After building and training my object detection model, I tested its accuracy and validity by utilizing testing image samples.

The evaluated accuracy of the model is *90%*.

:hash: To validate the trained model, go to the *Model testing* page and click *Classify all*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_test_1.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=e9256e53b48f3d33996950fe4ab65afe" width="1600" height="775" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_test_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_test_2.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=30d57186e82b4c014be6b59a409c0923" width="1600" height="775" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_test_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_test_3.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=7ed20abeada6e621e0fa553f4f054b5d" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_test_3.png" />
</Frame>

After validating my object detection model, I deployed it as fully optimized OpenMV firmware. This is the preferred method since the deployed firmware contains merely the object detection model and what is necessary to run the impulse. So, it does not consume much memory space and cause running into memory allocation issues.

:hash: To deploy the validated model as an OpenMV firmware, navigate to the *Deployment* page and select *OpenMV firmware*.

:hash: Then, choose the *Quantized (int8)* optimization option to get the best performance possible while running the deployed model.

:hash: Finally, click *Build* to download the model as an OpenMV firmware in [the generated ZIP folder](/hardware/deployments/run-openmv#deploying-your-impulse-as-an-openmv-firmware).

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_deploy_1.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=9679537fffa3a534ba071e2d5353abd3" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_deploy_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_deploy_2.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=8e94aeddfd26cb58381865882c01b901" width="1600" height="773" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_deploy_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/edge_deploy_3.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=fa1f773ffa6dde6aa79b3b6a09dd0038" width="1600" height="777" data-path=".assets/images/smart-grocery-cart-with-computer-vision/edge_deploy_3.png" />
</Frame>

## Step 7: Setting up Beetle ESP32-C3 on the Arduino IDE

Before proceeding with the following steps, I needed to set up Beetle ESP32-C3 on the Arduino IDE and install the required libraries for this project.

If your computer cannot recognize Beetle ESP32-C3 when plugged in via a USB cable, connect Pin 9 to GND (pull-down) and try again.

:hash: To add the ESP32-C3 board package to the Arduino IDE, navigate to *File ➡ Preferences* and paste the URL below under *Additional Boards Manager URLs*.

*[https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package\\\_esp32\\\_index.json](https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package\\_esp32\\_index.json)*

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/577XzA-QE9Zpi0WI/.assets/images/food-irradiation/espC3_set_1%20(1).png?fit=max&auto=format&n=577XzA-QE9Zpi0WI&q=85&s=0807137f3d2d4f7dbff66c02791d1431" width="689" height="674" data-path=".assets/images/food-irradiation/espC3_set_1 (1).png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/cTLnQohdrJO-nQ6f/.assets/images/dairy-manufacturing-with-ai/set_xiao_wifi_1%20(2).png?fit=max&auto=format&n=cTLnQohdrJO-nQ6f&q=85&s=880d841d2c984d0925dce6813451f491" width="799" height="530" data-path=".assets/images/dairy-manufacturing-with-ai/set_xiao_wifi_1 (2).png" />
</Frame>

:hash: Then, to install the required core, navigate to *Tools ➡ Board ➡ Boards Manager* and search for *esp32*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/577XzA-QE9Zpi0WI/.assets/images/food-irradiation/espC3_set_3%20(1).png?fit=max&auto=format&n=577XzA-QE9Zpi0WI&q=85&s=f86627550a4afc46e8e03c062732ac4f" width="1106" height="602" data-path=".assets/images/food-irradiation/espC3_set_3 (1).png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/577XzA-QE9Zpi0WI/.assets/images/food-irradiation/espC3_set_4.png?fit=max&auto=format&n=577XzA-QE9Zpi0WI&q=85&s=7a782d408cd33f981c03591d00aed8fa" width="788" height="443" data-path=".assets/images/food-irradiation/espC3_set_4.png" />
</Frame>

:hash: After installing the core, navigate to *Tools ➡ Board ➡ ESP32 Arduino* and select *DFRobot Beetle ESP32-C3*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/espC3_set_5.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=973be26bf7836f6528e2e6e8f7e59297" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/espC3_set_5.png" />
</Frame>

:hash: To print data on the serial monitor, enable *USB CDC On Boot* after setting Beetle ESP32-C3.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/espC3_set_6.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=7ec11deaa742067db2552f36cbdb8a59" width="829" height="377" data-path=".assets/images/smart-grocery-cart-with-computer-vision/espC3_set_6.png" />
</Frame>

:hash: Finally, download the required library for the MFRC522 RFID reader:

rfid | [Download](https://github.com/miguelbalboa/rfid)

## Step 7.1: Programming Beetle ESP32-C3 to get commands from OpenMV Cam H7 and communicate with the web application

Since OpenMV Cam H7 does not provide Wi-Fi or cellular connectivity, I employed Beetle ESP32-C3 to get commands from OpenMV Cam H7 via serial communication and communicate with the web application via HTTP GET requests.

Also, Beetle ESP32-C3 determines when the customer concludes shopping and is ready to leave the store if it detects the assigned RFID key tag UID of the grocery cart via the MFRC522 RFID reader.

You can download the *smart\_grocery\_cart\_app\_connection.ino* file to try and inspect the code for obtaining commands from OpenMV Cam H7 via serial communication and communicating with the web application.

⭐ Include the required libraries.

```
#include &lt;WiFi.h>
#include &lt;SPI.h>
#include &lt;MFRC522.h>
```

⭐ Define the Wi-Fi network settings and the web application server settings on LattePanda 3 Delta 864.

⭐ Then, initialize the *WiFiClient* object.

```
char ssid[] = "&lt;_SSID_>";        // your network SSID (name)
char pass[] = "&lt;_PASSWORD_>";    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;                // your network key Index number (needed only for WEP)

// Define the server on LattePanda 3 Delta 864.
char server[] = "192.168.1.22";
// Define the web application path.
String application = "/smart_grocery_cart/shopping.php";

// Initialize the WiFiClient object.
WiFiClient client; /* WiFiSSLClient client; */
```

⭐ Define the MFRC522 instance and module key input.

```
#define RST_PIN   7
#define SS_PIN    2
MFRC522 mfrc522(SS_PIN, RST_PIN);

// Define the MFRC522 module key input.
MFRC522::MIFARE_Key key;
```

⭐ Initialize the hardware serial port (Serial1) to communicate with OpenMV Cam H7.

```
  Serial1.begin(SERIAL_BAUDRATE ,SERIAL_8N1,/*RX =*/0,/*TX =*/1);
```

⭐ Adjust the PWM pin settings for the RGB LED.

```
  ledcSetup(3, pwm_frequency, resolution); ledcSetup(4, pwm_frequency, resolution); ledcSetup(5, pwm_frequency, resolution);
  ledcAttachPin(red_p, 3); ledcAttachPin(green_p, 4); ledcAttachPin(blue_p, 5);
```

⭐ Initialize the MFRC522 RFID reader.

```
  SPI.begin();
  mfrc522.PCD_Init();
  Serial.println("\n----------------------------------\nApproximate a New Card or Key Tag : \n----------------------------------\n");
  delay(3000);
```

⭐ Initialize the Wi-Fi module.

⭐ Attempt to connect to the given Wi-Fi network.

⭐ If connected to the network successfully, turn the RGB LED to blue.

```
  WiFi.begin(ssid, pass);
  // Attempt to connect to the WiFi network:
  while(WiFi.status() != WL_CONNECTED){
    // Wait for the connection:
    delay(500);
    Serial.print(".");
  }
  // If connected to the network successfully:
  Serial.println("Connected to the WiFi network successfully!");
  adjustColor(0,0,255);
```

⭐ In the *adjustColor* function, adjust the color of the RGB LED via the PWM pins.

```
void adjustColor(int r, int g, int b){
  ledcWrite(3, 255-r);
  delay(100);
  ledcWrite(4, 255-g);
  delay(100);
  ledcWrite(5, 255-b);
  delay(100);
}
```

⭐ In the *read\_UID* function, get the new card or key tag UID if detected.

⭐ Then, copy the detected UID to the *lastRead* string, process the *lastRead* string, and print it on the Arduino IDE serial monitor.

⭐ After detecting a UID successfully, turn the RGB LED to magenta.

```
int read_UID(){
  // Detect the new card or tag UID.
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return 0;
  }
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return 0;
  }

  // Display the detected UID on the serial monitor.
  Serial.print("\n----------------------------------\nNew Card or Key Tag UID : ");
  for (int i = 0; i &lt; mfrc522.uid.size; i++) {
    lastRead += mfrc522.uid.uidByte[i] &lt; 0x10 ? " 0" : " ";
    lastRead += String(mfrc522.uid.uidByte[i], HEX);
  }
  lastRead.trim();
  lastRead.toUpperCase();
  Serial.print(lastRead);
  Serial.print("\n----------------------------------\n\n");
  adjustColor(255,0,255);
  mfrc522.PICC_HaltA();
  delay(2000);
  return 1;
}
```

⭐ In the *make\_a\_get\_request* function:

⭐ Connect to the web application named *smart\_grocery\_cart*.

⭐ Create the query string depending on the given command.

⭐ Make an HTTP GET request with the created query string to the web application.

⭐ Turn the RGB LED to yellow and wait until the client is available. Then, retrieve the response from the web application.

⭐ If there is a response from the web application, save the response and turn the RGB LED to green.

```
void make_a_get_request(String request){
  // Connect to the web application named smart_grocery_cart. Change '80' with '443' if you are using SSL connection.
  if (client.connect(server, 80)){
    // If successful:
    Serial.println("\nConnected to the web application successfully!\n");
    // Create the query string:
    String query = application + request;
    // Make an HTTP GET request:
    client.println("GET " + query + " HTTP/1.1");
    client.println("Host: 192.168.1.22");
    client.println("Connection: close");
    client.println();
  }else{
    Serial.println("\nConnection failed to the web application!\n");
    adjustColor(255,0,0);
    delay(2000);
  }
  adjustColor(255,255,0);
  delay(2000); // Wait 2 seconds after connecting...
  // If there are incoming bytes available, get the response from the web application.
  response = "";
  while(client.available()) { char c = client.read(); response += c; }
  if(response != ""){ Serial.println(response); adjustColor(0,255,0); }
}
```

⭐ If the customer shows the assigned RFID key tag of the grocery cart to the MFRC522 RFID reader:

⭐ Remove spaces from the detected UID.

⭐ Make an HTTP GET request to the web application so as to send an HTML email to the customer's registered email address, including the list of the products added to the cart and the link to the payment page.

⭐ Clear the detected UID.

```
  read_UID();
  delay(500);
  if(lastRead != ""){
    // Remove spaces from the detected UID.
    lastRead.replace(" ", "_");
    // Send an HTML email to the customer's registered email address via the web application, including the list of the products added to the cart and the link to the payment page.
    make_a_get_request("?table="+table_name+"&send_email=OK&tag="+lastRead);
    // Clear the latest detected UID.
    lastRead = "";
    adjustColor(0,0,0);
  }
```

⭐ In the *get\_data\_from\_OpenMV* function, obtain the transferred data packet from OpenMV Cam H7 via serial communication. After getting the data packet, notify the customer via the RGB LED and the buzzer.

```
void get_data_from_OpenMV(){
  // Obtain the transferred data packet from the OpenMV Cam H7 via serial communication.
  if(Serial1.available() > 0){
    Serial.println("\nTransferred query from the OpenMV Cam H7:");
    OpenMV_data = "";
    OpenMV_data = Serial1.readString();
    Serial.println(OpenMV_data);
    adjustColor(0,51,0);
    delay(2000);
    tone(buzzer_pin, 500);
    delay(1000);
    noTone(buzzer_pin);
    delay(1000);
  }
}
```

⭐ If OpenMV Cam H7 transfers a command (data packet) via serial communication:

⭐ If the received command is *get\_table*, make an HTTP GET request to obtain the latest registered table name in the MariaDB database. Then, elicit the latest registered table name from the web application's response as a substring by utilizing the percentage (%) sign as the delimiter.

⭐ Otherwise, make an HTTP GET request directly to the web application by combining the stored table name and the received command (data packet).

⭐ Finally, clear the latest received command.

```
  get_data_from_OpenMV();
  if(OpenMV_data != ""){
    // If the customer requested to change the table name to the latest registered table name in the database:
    if(OpenMV_data == "get_table"){
      // Make an HTTP Get request to obtain the latest registered table name:
      make_a_get_request("?deviceChangeTable");
      if(response != ""){
        // Elicit and format the received table name:
        int delimiter_1, delimiter_2;
        delimiter_1 = response.indexOf("%");
        delimiter_2 = response.indexOf("%", delimiter_1 + 1);
        // Glean information as substrings.
        table_name = response.substring(delimiter_1 + 1, delimiter_2);
        Serial.println("\nLatest Registered Table Name Obtained: " + table_name);
      }
    }else{
      // Make an HTTP Get request directly with the received command:
      make_a_get_request("?table="+table_name+OpenMV_data);
    }
    // Clear the latest received command:
    OpenMV_data = "";
    adjustColor(0,0,0);
  }
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/code_web_1.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=530979d15b318e8b71295fbc34f38139" width="1483" height="777" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_web_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/code_web_2.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=aadc299b3e735a1adb6ee4179bb88653" width="1570" height="770" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_web_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/code_web_3.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=e1592c19e9b2b8d7b4061cddfcdfb86f" width="1600" height="663" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_web_3.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/code_web_4.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=75ca06ca42f11fe27ed9a9f93edf4f4b" width="1600" height="696" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_web_4.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/code_web_5.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=b9e0cb64330a32e463635e968f0e905c" width="1468" height="771" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_web_5.png" />
</Frame>

## Step 8: Setting up the Edge Impulse FOMO model on OpenMV Cam H7

After building, training, and deploying my object detection (FOMO) model as an OpenMV firmware on Edge Impulse, I needed to flash OpenMV Cam H7 with the generated firmware to run the model directly so as to create an easy-to-use and capable device operating with minimal latency, memory usage, and power consumption.

FOMO object detection models do not output bounding boxes but provide the detected object's location using centroids. Therefore, I was able to modify the returned object location variables to draw circles around the detected objects on the ST7735 color TFT screen with the assigned circle color — magenta.

Since Edge Impulse optimizes and formats preprocessing, configuration, and learning blocks into BIN files for each OpenMV version while deploying models as OpenMV firmware, I was able to flash OpenMV Cam H7 effortlessly to run inferences.

:hash: After downloading the generated OpenMV firmware in the ZIP file format, plug OpenMV Cam H7 into your computer and open the OpenMV IDE.

:hash: Then, go to *Tools ➡ Run Bootloader (Load Firmware)*.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/openmv_set_1.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=3cd4423e2025de551b36381e1b6fd60c" width="1600" height="852" data-path=".assets/images/smart-grocery-cart-with-computer-vision/openmv_set_1.png" />
</Frame>

:hash: Choose the firmware file for OpenMV Cam H7 after extracting the generated ZIP folder.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/openmv_set_2.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=8d5924ca16f1af8bb40b66cdb50f1423" width="1600" height="825" data-path=".assets/images/smart-grocery-cart-with-computer-vision/openmv_set_2.png" />
</Frame>

:hash: Select *Erase internal file system* and click *Run* to flash OpenMV Cam H7.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/openmv_set_3.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=8671493e03ed556bb2f1cfb1b77f1c86" width="1600" height="851" data-path=".assets/images/smart-grocery-cart-with-computer-vision/openmv_set_3.png" />
</Frame>

After flashing the firmware successfully via the OpenMV IDE, I programmed OpenMV Cam H7 to run inferences so as to detect food retail products.

Also, I employed OpenMV Cam H7 to transmit commands to Beetle ESP32-C3 via serial communication by utilizing the joystick movements and switch button:

* Joystick (Button) ➡ Get the latest registered table name in the database

After running an inference successfully:

* Joystick (Up + Button) ➡ Add the detected product to the database table
* Joystick (Down + Button) ➡ Remove the detected product from the database table

You can download the *smart\_grocery\_cart\_run\_model.py* file to try and inspect the code for running Edge Impulse neural network models on OpenMV Cam H7.

You can inspect the corresponding functions and settings in Step 5.

⭐ Import the required modules and the *product\_list.py* file, including the product information for detected products — IDs, names, and prices.

```
import sensor, image, math, lcd, tf
from time import sleep
from pyb import Pin, ADC, LED, UART
from product_list import products
```

⭐ Initialize the camera sensor with its required settings (pixel format and frame size).

```
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QQVGA2) # Special 128x160 framesize for LCD Shield.
```

⭐ Define the required parameters to run an inference with the Edge Impulse FOMO model.

```
net = None
labels = None
min_confidence = 0.7
```

⭐ Load the Edge Impulse FOMO model integrated into the firmware. Then, print errors, if any.

```
try:
    labels, net = tf.load_builtin_model('trained')
except Exception as e:
    raise Exception(e)
```

⭐ Initiate the built-in (hardware) serial port (UART 3) on the OpenMV Cam H7.

```
uart = UART(3, 115200, timeout_char=1000)
```

⭐ Initialize the ST7735 color TFT screen.

```
lcd.init()
```

⭐ Define the RGB LED and joystick pins.

```
red = LED(1)
green = LED(2)
blue = LED(3)

# Joystick:
J_VRX = ADC(Pin('P6'))
J_SW = Pin("P9", Pin.IN, Pin.PULL_UP)
```

⭐ In the *while* loop:

⭐ Display a real-time video stream on the ST7735 color TFT screen.

⭐ If the joystick button is pressed, transfer the *get\_table* command to Beetle ESP32-C3 via serial communication in order to obtain the latest registered customer's table name for subsequent requests to the web application.

⭐ If transferred successfully, turn the built-in RGB LED to blue and notify the customer via the ST7735 color TFT screen.

⭐ Run an inference with the object detection (FOMO) model to detect food retail products.

⭐ Via the *detect* function, obtain all detected objects found in the recently captured image, split out per label (product brand name).

⭐ Exclude the class index 0 since it is the background class.

⭐ If the FOMO model detects an object successfully, activate the selection (options) menu for adding or removing the detected product to/from the database table.

⭐ Obtain the detected product's label to retrieve its details saved in the given product list — *product\_list.py*.

⭐ Get the prediction (detection) results for each label and print them on the serial terminal.

⭐ Draw a circle in the center of the detected object (product) with the assigned color — magenta.

```
while(True):
    menu_config = 0

    # Read controls from the joystick.
    j_x, sw = readJoystick()

    # Take a picture with the given frame settings.
    img = sensor.snapshot()
    lcd.display(img)

    # Change the table name on Beetle ESP32-C3 with the latest registered customer's table name in the database.
    if(sw == 0):
        query = "get_table"
        print("\nQuery: " + query + "\n")
        img.draw_rectangle(0, int(160/4), 128, int(160/2), fill=1, color =(0,0,255))
        img.draw_string(int((128-16*len("Query"))/2), int((160/2)-28), "Query", color=(255,255,255), scale=2)
        img.draw_string(int((128-16*len("Sent!"))/2), int((160/2)+8), "Sent!", color=(255,255,255), scale=2)
        lcd.display(img)
        uart.write(query)
        adjustColor((0,0,1))
        sleep(5)
        adjustColor((0,0,0))

    # Run an inference with the FOMO model to detect products.
    # Via the detect function, obtain all detected objects found in the recently captured image, split out per label (class).
    for i, detection_list in enumerate(net.detect(img, thresholds=[(math.ceil(min_confidence * 255), 255)])):
        # Exclude the class index 0 since it is the background class.
        if (i == 0): continue

        # If the Edge Impulse FOMO model predicted a label (class) successfully:
        if (len(detection_list) == 0): continue

        # Activate the selection (options) menu for adding or removing products to/from the database table.
        menu_config = 1

        # Obtain the detected product's label to retrieve its details saved in the given product list.
        detected_product = i

        # Get the prediction (detection) results and print them on the serial terminal.
        print("\n********** %s **********" % labels[i])
        for d in detection_list:
            # Draw a circle in the center of the detected objects (products).
            [x, y, w, h] = d.rect()
            center_x = math.floor(x + (w / 2))
            center_y = math.floor(y + (h / 2))
            img.draw_circle((center_x, center_y, 20), color=(255,0,255), thickness=3)
            print('\nDetected Label: %d | p: (%d, %d)' % (i, center_x, center_y))
```

⭐ If the selection (options) menu is activated:

⭐ Pause the real-time video stream.

⭐ Display the cart choice options on the ST7735 color TFT screen:

* Add Cart
* Remove

⭐ If the joystick is moved up, change the cart choice option to *add*, inform the customer via the ST7735 TFT screen, and turn the built-in RGB LED to green.

⭐ If the joystick is moved down, change the cart choice option to *remove*, inform the customer via the ST7735 TFT screen, and turn the built-in RGB LED to red.

⭐ After selecting a cart choice option, if the joystick button is pressed, generate the query string with the selected cart choice and the given information of the detected product (ID, name, and price) and send it to Beetle ESP32-C3 via serial communication.

⭐ After transferring the query string, turn the built-in RGB LED to blue, notify the customer via the ST7735 TFT screen, and close the selection (options) menu.

⭐ Finally, clear the detected label and the selected cart choice.

```
    if(menu_config == 1):
        # Display the selection (options) menu.
        img.draw_rectangle(0, 0, 128, 30, fill=1, color =(0,0,0))
        img.draw_string(int((128-16*len("Add Cart"))/2), 3, "Add Cart", color=(0,255,0), scale=2)
        img.draw_rectangle(0, 130, 128, 160, fill=1, color =(0,0,0))
        img.draw_string(int((128-16*len("Remove"))/2), 135, "Remove", color=(255,0,0), scale=2)
        lcd.display(img)
        print("Selection Menu Activated!")
        while(menu_config == 1):
            j_x, sw = readJoystick()
            # Add the detected product to the database table.
            if(j_x > 3):
                cart_choice = "add"
                print("Selected Cart Option: " + cart_choice)
                img.draw_rectangle(0, 0, 128, 30, fill=1, color =(0,255,0))
                img.draw_string(int((128-16*len("Add Cart"))/2), 3, "Add Cart", color=(255,255,255), scale=2)
                img.draw_rectangle(0, 130, 128, 160, fill=1, color =(0,0,0))
                img.draw_string(int((128-16*len("Remove"))/2), 135, "Remove", color=(255,0,0), scale=2)
                lcd.display(img)
                adjustColor((0,1,0))
                sleep(1)
            # Remove the detected product from the database table.
            if(j_x &lt; 2):
                cart_choice = "remove"
                print("Selected Cart Option: " + cart_choice)
                img.draw_rectangle(0, 0, 128, 30, fill=1, color =(0,0,0))
                img.draw_string(int((128-16*len("Add Cart"))/2), 3, "Add Cart", color=(0,255,0), scale=2)
                img.draw_rectangle(0, 130, 128, 160, fill=1, color =(255,0,0))
                img.draw_string(int((128-16*len("Remove"))/2), 135, "Remove", color=(255,255,255), scale=2)
                adjustColor((1,0,0))
                lcd.display(img)
                sleep(1)
            # Send the generated query (command), including the selected option (cart choice) and
            # the detected product's details, to the web application via Beetle ESP32-C3.
            if(sw == 0):
                query = "&"+cart_choice+"=OK&product_id="+products[detected_product]["id"]+"&product_name="+products[detected_product]["name"]+"&product_price="+products[detected_product]["price"]
                print("\nQuery: " + query + "\n")
                img.draw_rectangle(0, int(160/4), 128, int(160/2), fill=1, color =(0,0,255))
                img.draw_string(int((128-16*len("Query"))/2), int((160/2)-28), "Query", color=(255,255,255), scale=2)
                img.draw_string(int((128-16*len("Sent!"))/2), int((160/2)+8), "Sent!", color=(255,255,255), scale=2)
                lcd.display(img)
                uart.write(query)
                adjustColor((0,0,1))
                sleep(5)
                adjustColor((0,0,0))
                # Close the selection menu after transferring the product information and the selected option to the web application via Beetle ESP32-C3.
                menu_config = 0
                # Clear the detected label and the selected option (cart choice).
                detected_product = 0
                cart_choice = "EMPTY"
```

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_product.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=a74b78e0cd2219f0594c1a5009dd6b36" width="1542" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_product.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_run_1.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=4b5492a0e8f00673cbc061c4ed828062" width="1529" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_run_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/ozj75hxjb3AqW2JQ/.assets/images/smart-grocery-cart-with-computer-vision/code_run_2.png?fit=max&auto=format&n=ozj75hxjb3AqW2JQ&q=85&s=f6c2c7d7234e16918402cf9260b5040e" width="1537" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_run_2.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/code_run_3.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=6a161b0a38ebbe1707352f23b9eafddb" width="1566" height="993" data-path=".assets/images/smart-grocery-cart-with-computer-vision/code_run_3.png" />
</Frame>

## Step 9: Running the FOMO model on OpenMV Cam H7 to detect products and communicating with the web application via Beetle ESP32-C3

My Edge Impulse object detection (FOMO) model scans a captured image and predicts possibilities of trained labels to recognize an object on the given captured image. The prediction result (score) represents the model's *"confidence"* that the detected object corresponds to each of the five different labels (classes) \[0 - 4], as shown in Step 6:

* Barilla
* Milk
* Nutella
* Pringles
* Snickers

To run the *smart\_grocery\_cart\_run\_model.py* file on OpenMV Cam H7 when powered up automatically, save it as *main.py* on the SD card.

🛒🛍️📲 When Beetle ESP32-C3 connects successfully to the given Wi-Fi network, the device turns the RGB LED to blue.

🛒🛍️📲 Also, the device prints notifications and the received commands on the Arduino IDE serial monitor for debugging.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_1.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=356975013906248a804e28da77d33f39" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/serial_web_1.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=5a93116bf14de72693d9026d84d351bf" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/serial_web_1.png" />
</Frame>

🛒🛍️📲 The device shows a real-time video stream on the ST7735 color TFT display.

🛒🛍️📲 If the joystick button is pressed, OpenMV Cam H7 transfers the *get\_table* command to Beetle ESP32-C3 via serial communication. Then, Beetle ESP32-C3 makes an HTTP GET request to the web application to obtain the latest registered customer's table name from the database for subsequent requests to the web application.

🛒🛍️📲 After transferring the command, the device informs the customer via the ST7735 color TFT screen and turns the built-in RGB LED on OpenMV Cam H7 to blue.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_2.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=4699dcc5b2da9196865c7fcd57b6c49f" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/serial_web_2.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=de9b7bea7e8c611e11e872fbb0d2ef4f" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/serial_web_2.png" />
</Frame>

🛒🛍️📲 The device captures a picture and runs an inference with the Edge Impulse object detection (FOMO) model.

🛒🛍️📲 When the object detection (FOMO) model detects a product, the device pauses the real-time video stream and displays the selection (options) menu on the ST7735 color TFT screen, including two cart choice options:

* Add Cart
* Remove

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_3.0.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=03c0459622d70ada6b25e154c15f2363" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_3.0.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_3.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=6cf168031648c1c05772fcc8d54fe7b4" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_3.jpg" />
</Frame>

🛒🛍️📲 On the selection menu, if the joystick is moved up, the device changes the cart choice option to *add*, informs the customer via the ST7735 TFT screen, and turns the built-in RGB LED on OpenMV Cam H7 to green.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_4.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=fa7dd19d3737811e7ab15a21f7315404" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_4.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_5.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=82bc3dec604866f2ece883a6774e67c9" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_5.jpg" />
</Frame>

🛒🛍️📲 On the selection menu, if the joystick is moved down, the device changes the cart choice option to *remove*, informs the customer via the ST7735 TFT screen, and turns the built-in RGB LED on OpenMV Cam H7 to red.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_6.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=7ad72aa93d5e147bb02a66bf3a57f733" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_6.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_7.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=eba5ba028dd7de8d95d39d3fcfbb5973" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_7.jpg" />
</Frame>

🛒🛍️📲 After selecting a cart choice, if the joystick button is pressed, OpenMV Cam H7 transfers the generated query string with the selected cart choice and the detected product's given details (ID, name, and price) to Beetle ESP32-C3 via serial communication.

🛒🛍️📲 If OpenMV Cam H7 transfers the query successfully, the device turns the built-in RGB LED to blue, notifies the customer via the ST7735 TFT screen, and closes the selection menu to resume the real-time video stream.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_8.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=6beb481055a8e652a6e4362a463a337e" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_8.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_9.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=789a0726c417bf56bd574115390b5b2f" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_9.jpg" />
</Frame>

🛒🛍️📲 If Beetle ESP32-C3 receives the transferred data packet from OpenMV Cam H7 via serial communication successfully, the device turns the RGB LED to dark green and notifies the customer via the buzzer.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_10.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=c891049797ded8edb2a2af7c5839efc0" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_10.jpg" />
</Frame>

🛒🛍️📲 Depending on the received command, Beetle ESP32-C3 makes an HTTP GET request to the web application so as to add products to the database table, remove products from the database table, or obtain the latest registered customer's table name.

🛒🛍️📲 If Beetle ESP32-C3 connects to the web application successfully, the device turns the RGB LED to yellow.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_11.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=147b84858c7773a7ad0cede0982ad800" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_11.jpg" />
</Frame>

🛒🛍️📲 If Beetle ESP32-C3 gets a response from the web application successfully, the device turns the RGB LED to green and prints the response on the Arduino IDE serial monitor.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_12.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=10570eac9f339ae9190eac1510a54cda" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_12.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/serial_web_3.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=af2bba8e5514d6ee4dbddf01362e2923" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/serial_web_3.png" />
</Frame>

🛒🛍️📲 On each recognized object (product), the device draws circles (centroids) with the assigned color — magenta.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_13.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=e839e6fde3be3e4fee15b30759a7896c" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_13.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_14.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=8c3ff1f48c3e4e0bda724be6339f66fa" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_14.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_15.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=7f80f957b44cac426dc6062de4d0c1d9" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_15.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_16.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=9b2b504ad5c9994f16e987527ce36e6d" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_16.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_17.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=d4eeb758cd9b0faae236d32aca2d99a5" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_17.jpg" />
</Frame>

🛒🛍️📲 The web application adds or removes products to/from the customer's database table according to the HTTP GET requests made by Beetle ESP32-C3.

🛒🛍️📲 Then, the web application displays a concurrent shopping list of the products added to the grocery cart on the product list (payment) page — *product\_list.php* — as explained in Step 4.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/database_working.png?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=6a98be001d0360a673c049e609077939" width="1600" height="776" data-path=".assets/images/smart-grocery-cart-with-computer-vision/database_working.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/web_app_working.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=ce47c2c99ffd61a63757d533e3ae5607" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/web_app_working.png" />
</Frame>

🛒🛍️📲 If Beetle ESP32-C3 detects the assigned RFID key tag of the grocery cart via the MFRC522 RFID reader, the device turns the RGB LED to magenta.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_18.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=d4239cbcc71c24580921233ed208d09c" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_18.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_19.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=e2df9a09f738a3a86a22f34d679de822" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_19.jpg" />
</Frame>

🛒🛍️📲 In this regard, the device determines the customer concluded shopping and is ready to leave the store. Therefore, Beetle ESP32-C3 makes an HTTP GET request to the web application so as to send an HTML email to the customer's registered email address, including the generated shopping list and the payment link.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_20.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=3010f4babcf90727aff41212f9b759fb" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_20.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/run_model_21.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=2e2222abd032ddd04391e7fa2627f22c" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_21.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/serial_web_4.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=5c8495ef74a2f65995679138cc8361e8" width="1600" height="848" data-path=".assets/images/smart-grocery-cart-with-computer-vision/serial_web_4.png" />
</Frame>

🛒🛍️📲 Then, the web application sends the HTML email via SendGrid Email API to the customer's registered email address.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/email_working.png?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=99a9c2626dcf2f41387550fc6eb6e667" width="1571" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/email_working.png" />
</Frame>

🛒🛍️📲 If Beetle ESP32-C3 throws an error, the device turns the RGB LED to red and prints the error details on the Arduino IDE serial monitor.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/run_model_err.jpg?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=997c92a5071b57e99bbe6555dd9aea5c" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/run_model_err.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/serial_web_err.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=f69d1bc96591ba2713bf602e17423fa8" width="1600" height="847" data-path=".assets/images/smart-grocery-cart-with-computer-vision/serial_web_err.png" />
</Frame>

🛒🛍️📲 Furthermore, the device prints notifications and the generated query string on the OpenMV IDE serial monitor for debugging.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/serial_run_1.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=2cbd3a08edcfc1fd95b6911122e0e0d7" width="1600" height="850" data-path=".assets/images/smart-grocery-cart-with-computer-vision/serial_run_1.png" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/serial_run_2.png?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=fd57a97b7161c8d012f370e99c09069d" width="1600" height="852" data-path=".assets/images/smart-grocery-cart-with-computer-vision/serial_run_2.png" />
</Frame>

As far as my experiments go, the device recognizes different food retail products precisely, communicates with the web application faultlessly, and shows accurate circles around the detected objects :)

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/RMWez-k2dQiqKwAo/.assets/images/smart-grocery-cart-with-computer-vision/lattepanda_run_2.jpg?fit=max&auto=format&n=RMWez-k2dQiqKwAo&q=85&s=7f5b8d52dda060cd33e0cf14780aaa35" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/lattepanda_run_2.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/edgeimpulse/.assets/images/smart-grocery-cart-with-computer-vision/gif_run.gif" />
</Frame>

## Videos and Conclusion

[Data collection | IoT AI-driven Smart Grocery Cart w/ Edge Impulse](https://youtu.be/QGrXR1z1t0A)

[Experimenting with the model | IoT AI-driven Smart Grocery Cart w/ Edge Impulse](https://youtu.be/AEBy1O7QDJk)

## Further Discussions

By applying object detection models trained on numerous food retail product images in detecting products automatically while shopping, we can achieve to:

🛒🛍️📲 convert regular grocery carts into AI-assisted smart grocery carts,

🛒🛍️📲 make shoppers avoid tedious checkout lines and self-checkout stations,

🛒🛍️📲 improve the customer experience,

🛒🛍️📲 provide an automated product tracking and payment system,

🛒🛍️📲 reduce the total cost of integrating smart grocery carts for small businesses in the food retail industry,

🛒🛍️📲 provide an exceptional online shopping experience.

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/effHVD5v0gY_iz8B/.assets/images/smart-grocery-cart-with-computer-vision/completed_1.jpg?fit=max&auto=format&n=effHVD5v0gY_iz8B&q=85&s=1d71363ceadabe7541dfdb2f72375c1d" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/completed_1.jpg" />
</Frame>

<br />

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/0Yr5kW97l1shMZQ2/.assets/images/smart-grocery-cart-with-computer-vision/show_1.jpg?fit=max&auto=format&n=0Yr5kW97l1shMZQ2&q=85&s=890ef827ae1e394c93f91a88e17fc15e" width="1333" height="1000" data-path=".assets/images/smart-grocery-cart-with-computer-vision/show_1.jpg" />
</Frame>


Built with [Mintlify](https://mintlify.com).