# Source: https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board

## Introduction

The [SparkFun Blynk Board -- ESP8266](https://www.sparkfun.com/products/13794) is your hardware gateway to the app-controlled wonderland that is [Blynk](http://www.blynk.cc/). Combining the Blynk Board with the Blynk app (on your iOS or Android device), will allow you to control LEDs from your phone, send a tweet when it\'s time to water your plants, monitor local weather conditions, and much more!

[![Blynk Board and app action shot](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/13794-action.jpg)](https://www.sparkfun.com/products/13794)

This tutorial will explain how to get your Blynk Board connected to a local Wi-Fi network \-- in a process called **provisioning** \-- *and* connected to a **project within the Blynk app**. Once you\'ve completed the tutorial, you\'ll have already created your first project: a zebra-controlled multicolored LED (it\'ll make sense when you see it).

### Gather the Gear

To follow along with this tutorial, you\'ll need the following physical and digital goods:

**[SparkFun Blynk Board \-- ESP8266](https://www.sparkfun.com/products/13794)** \-- The Blynk Board comes fully programmed \-- ready to start Blynking. All you need to do is connect it to Wi-Fi and your Blynk account. You can obtain the Blynk board individually or from the IoT Starter Kit.

[![SparkFun Blynk Board - ESP8266](https://cdn.sparkfun.com/r/600-600/assets/parts/1/1/3/6/4/13794-01a.jpg)](https://www.sparkfun.com/sparkfun-blynk-board-esp8266.html)

### [SparkFun Blynk Board - ESP8266](https://www.sparkfun.com/sparkfun-blynk-board-esp8266.html) 

[ WRL-13794 ]

The SparkFun Blynk Board is specially designed to work with the 'widgets' within the Blynk mobile app to create your next...

**Retired**

[![SparkFun IoT Starter Kit with Blynk Board](https://cdn.sparkfun.com/r/600-600/assets/parts/1/2/8/8/4/13794_Action.jpg)](https://www.sparkfun.com/products/14682)

### [SparkFun IoT Starter Kit with Blynk Board](https://www.sparkfun.com/products/14682) 

[ KIT-14682 ]

The SparkFun IoT Starter Kit with Blynk Board is a great way to gain a solid introduction to the world of IoT technology with...

**Retired**

The Blynk Board also includes a **Blynk Subscription code card**, which you\'ll need to connect the Blynk Board to your Blynk account (and to charge it up!).

**[Micro-B USB Cable](https://www.sparkfun.com/products/10215)** \-- The Blynk Board can be powered via a USB cable connected on the other end to either a computer, laptop, or [USB wall adapter](https://www.sparkfun.com/products/11456).

[![Wall Adapter Power Supply - 5VDC, 2A (USB Micro-B)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/8/1/4/TOL-15311-1.jpg)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-usb-micro-b.html)

### [Wall Adapter Power Supply - 5VDC, 2A (USB Micro-B)](https://www.sparkfun.com/wall-adapter-power-supply-5vdc-2a-usb-micro-b.html) 

[ TOL-15311 ]

This is a high quality switching \'wall wart\' AC to DC 5V 2000mA USB Micro-B wall power supply manufactured specifically for S...

[ [\$9.50] ]

[![USB Micro-B Cable - 6 Foot](https://cdn.sparkfun.com/r/140-140/assets/parts/4/5/5/8/10215-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html)

### [USB Micro-B Cable - 6 Foot](https://www.sparkfun.com/usb-micro-b-cable-6-foot.html) 

[ CAB-10215 ]

USB 2.0 type A to Micro-B 5-pin. This is a new, smaller connector for USB devices. Micro-B connectors are about half the heig...

[ [\$6.50] ]

[![USB Wall Charger - 5V, 1A (Black)](https://cdn.sparkfun.com/r/140-140/assets/parts/7/3/1/0/11456-USB_Wall_Charger_-_5V__1A__Black_-01.jpg)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html)

### [USB Wall Charger - 5V, 1A (Black)](https://www.sparkfun.com/usb-wall-charger-5v-1a-black.html) 

[ TOL-11456 ]

USB is being implemented as a power connection standard more and more these days, but you don\'t always have a computer on han...

[ [\$5.95] ]

[![USB Micro-B Cable - 6\"](https://cdn.sparkfun.com/r/140-140/assets/parts/1/0/4/3/0/13244-01.jpg)](https://www.sparkfun.com/usb-micro-b-cable-6.html)

### [USB Micro-B Cable - 6\"](https://www.sparkfun.com/usb-micro-b-cable-6.html) 

[ CAB-13244 ]

This is a USB 2.0 type A to Micro-B 5-pin black cable. You know, the mini-B connector that usually comes with cell phones, Ca...

[ [\$2.50] ]

#### Powering the Blynk Board with Lithium-Polymer Batteries

The Blynk Board is equipped with LiPo battery support for truly wireless Blynking. The 2-pin, white JST connector adjacent to the USB port, mates with a variety of SparkFun LiPo batteries. The batteries are [available in a range of capacities](https://www.sparkfun.com/search/results?term=lithium+polymer), but we recommend either the [400mAh](https://www.sparkfun.com/products/10718), [850mAh](https://www.sparkfun.com/products/341), or [1000mAh](https://www.sparkfun.com/products/339) varieties.

A USB cable is still recommended -- it\'s used to **charge the battery**. But once you find a Blynk project that requires your board not be tied down to a wall or computer, definitely consider equipping it with a battery.

**Blynk App** \-- The Blynk smartphone app comes in two flavors: [iOS](https://itunes.apple.com/us/app/blynk-control-arduino-raspberry/id808760481?ls=1&mt=8) and [Android](https://play.google.com/store/apps/details?id=cc.blynk). Before going any further, download the app to your smart device:

[![AS_link](https://cdn.sparkfun.com/assets/learn_tutorials/4/9/4/AS_link.png)](https://itunes.apple.com/us/app/blynk-control-arduino-raspberry/id808760481?ls=1&mt=8)

[![GP_link](https://cdn.sparkfun.com/assets/learn_tutorials/4/9/4/GP_link.png)](https://play.google.com/store/apps/details?id=cc.blynk)

[![Blynk app in action](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/Blynk-app-example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/Blynk-app-example.png)

The Blynk app is compatible with iDevices running iOS 7.0+, and Android\'s running any version above or equal to 4.0.

**Local Internet-Connected Wireless (Wi-Fi) Network** \-- The Blynk Board is equipped with Wi-Fi support, and should be able to connect to most home wireless networks: **2.4GHz** Wi-Fi networks, that are either open (no password) or protected with WPA, WPA-2, or WEP authentication.

[![alt text](https://cdn.sparkfun.com/r/400-400/assets/learn_tutorials/4/8/6/Wireless-icon-1000.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/Wireless-icon-1000.png)

Note that the Blynk Board cannot connect the 5GHz band of a dual-band Wi-Fi router. If your Wi-Fi router has two visible options, like `HOME-AB12-2.4` and `HOME-AB12-5`, connect the Blynk Board to the \"2.4\" option.

## Powering Up the Blynk Board

Once you\'ve gathered all of the materials from above, it\'s time to power up the Blynk Board! Grab your **USB Cable**, plug one end into a computer or USB wall adapter, and plug the other into the Blynk Board.

[![Blynk Board plugged in, powered, LEDs on](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/power-01-pluggedin.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/power-01-pluggedin.jpg)

*Blynk Board plugged in, PWR LED (in the upper-left of this image) is illuminated*

You should immediately see the small, **red \"PWR\" LED** illuminate, followed shortly thereafter by a random-looking blinking of the large, RGB LED.

## Identifying Your Blynk Board

While the Blynk Board\'s RGB blinking may look random at first, it will follow a repeating pattern \-- a unique **sequence of four colors** including either red, green, blue, purple, or yellow, with a long stop in between. This color-code will help identify your board, just in case you\'re not the only one in town setting up a Blynk Board.

**Four characters matching that color code** will be added to the name of your Blynk Board. For example, if the RGB LED is blinking a pattern of blue, green, red, green..

[![Blynk Board blinking blue, green, red, green](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/identify-gif-bgrg.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/identify-gif-bgrg.gif)

\...the Blynk Board name will be **BlynkMe-BGRG**.

The table below documents which color matches which character.

  Color    Blynk Name Character
  -------- ----------------------
  Red      R
  Green    G
  Blue     B
  Purple   P
  Yellow   Y

That\'s not all the RGB LED does though!

## RGB Status Codes

During setup, the RGB LED on the Blynk Board will be your window into its soul. The board uses this multi-colored LED to indicate all sorts of status modes. If you\'re ever unclear of what the RGB color-code means, consult the table below:

+-----------------------------------------------------------+------------------------+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RGB Color                                                 | Blink Speed            | Status                          | Notes                                                                                                                                                                                                                                                                                                       |
+=============+:===========================================:+========================+=================================+=============================================================================================================================================================================================================================================================================================================+
| Purple      | [●] | Medium (2Hz)           | Device connected to Blynk Board | Verifies that your phone (or possibly someone else\'s) is connected to the Blynk Board.                                                                                                                                                                                                                     |
+-------------+---------------------------------------------+------------------------+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Blue        | ●                                           | Fast (4Hz)             | Connecting to Wi-Fi network     | After sending it the info, the Blynk Board will attempt to connect to your Wi-Fi network for up to 30 seconds.                                                                                                                                                                                              |
+-------------+---------------------------------------------+------------------------+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Blynk Green | [●] | Slow (1Hz)             | Connecting to Blynk Cloud       | After connecting to your Wi-Fi network, the Blynk Board will establish a connection with the Blynk server.                                                                                                                                                                                                  |
+-------------+---------------------------------------------+------------------------+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Blynk Green | [●] | Smoothly fading in/out | Connected to Blynk              | After successfully connecting to Wi-Fi and Blynk, this is the sign that everything is working! The LED will continue to \"breathe\" until you tell it to do something else.                                                                                                                                 |
+-------------+---------------------------------------------+------------------------+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Yellow      | [●] | Slow (1Hz)             | Re-connecting to Blynk          | Connection issues should resolve themselves, but the Blynk board will likely be unresponsive while blinking yellow. If it continues to Blynk yellow for over a minute, try cycling power to the Blynk Board.                                                                                                |
+-------------+---------------------------------------------+------------------------+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| White       | [●] | Medium (2Hz)           | Blynk Board waiting for config  | If your Blynk Board was unable to connect to either Wi-Fi or Blynk, it\'ll sit in this mode -- waiting for you to press a button. More on this in the [Reconfiguring a Blynk Board section](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board#reconfiguring-a-blynk-board) |
+-------------+---------------------------------------------+------------------------+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Provisioning the Blynk Board

In order to connect the Blynk Board to your local Wi-Fi network \-- and the Blynk app \-- you\'ll need to send it a few pieces of information, including the **name and password** of your Wi-Fi network. This is a process called provisioning.

#### Provisioning?

In the provisioning process, we\'ll use a smartphone, laptop, or computer to connect to directly (over Wi-Fi) to the Blynk Board. Once connected, your smart-device will send the necessary data and tell the Blynk Board to go connect to your Internet-connected wireless network and Blynk.

The Blynk Board is initially configured to operate as a **Wi-Fi access point** (abbreviated \"AP\", kind of like a router). A smartphone or Wi-Fi-enabled computer can briefly connect to the Blynk Board, and, using either the Blynk app or a browser, send all of the necessary information over to it. After the Blynk Board receives that info, it\'ll transition from AP to Wi-Fi device and connect to your Wi-Fi network.

### Blynk QR-Code Card

The Blynk Board has plenty of backup provisioning options, but the easiest method is through the Blynk app. Both iOS and Android versions of the Blynk app support Blynk Board provisioning. All you\'ll need is the **Blynk QR-Code Card**, included with your Blynk Board.

[![Blynk QR Code Card](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/13794-qrcard-02.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/13794-qrcard-02.jpg)

#### Don\'t Throw Away Your Blynk QR-Code Card!

Although you\'ll only be able to benefit from the 15,000 energy points once, the QR-Code card can be used to **re-provision** your Blynk Board, should the need ever arise. We recommend you keep it hand, for now, just in case!

### Provisioning on a Smartphone (or Tablet)

The setup process in each OS looks and feels a little different. **Select one of the sections below** to get directions for your phone (or tablet) OS.

[iOS Provisioning](#iosProvision) [Android Provisioning](#android-provision)

### iOS Provisioning

If you haven't already, download the [Blynk App from the App store](https://itunes.apple.com/us/app/blynk-control-arduino-raspberry/id808760481?ls=1&mt=8). Then open it, **create an account** and log in.

If you already have the Blynk app installed on your phone, make sure it's **updated to the latest release**!

#### Step 1: Scan the Blynk Board QR Code

Click the QR-code icon in the **top-right** corner of the Blynk app.

[![Select QR icon](https://cdn.sparkfun.com/r/337-337/assets/learn_tutorials/4/8/6/ios-01-OpenQR-cropped.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ios-01-OpenQR-cropped.PNG)

Then scan your phone camera over the QR code on your Blynk Board card. Blynk should pop up a new screen -- congrats, you've got some new Blynk energy to play with!

[![Blynk congrats](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/ios-02-congrats.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ios-02-congrats.PNG)

#### Step 2: Connect to the Blynk Board

From the "Congrats!" page, hit **Set Up New Device**, read through the \"Pre-Flight Checklist\", and -- as long as your **Blynk Board is powered up** and blinking the unique color code -- **hit Continue**.

Read through the \"Connect to Device\" screen, and hit **Open Wi-Fi Settings** to swap over to your iDevice's Wi-Fi settings.

You may have to wait a few seconds for your device to scan for networks, but you should eventually see a Wi-Fi network named **BlynkMe-CCCC**. If that color code matches your Blynk Board's pattern, **select that network**.

The connecting process may take up to a minute to complete -- eventually, though, you should see a **checkmark next to the BlynkMe network**. The Blynk Board will begin to **blink purple** -- faster than before -- when a device has connected to it.

[![Blynk Board connected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/ios-07-BlynkConnect.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ios-07-BlynkConnect.PNG)

The Blynk app may (or may not) pop up a notification indicating it has sensed a connection to a BlynkMe network. If so, **hit open**. If the notification isn't popping up, but you have a checkmark next to the BlynkMe network, hit **Back to Blynk** in the upper-left corner.

#### Step 3: Connect the Blynk Board to Wi-Fi/Blynk

On the next screen, **enter the name and password** of your Wi-Fi network. While typing the password, hit the eye icon (eyecon?) if you want/need to show your password.

[![Enter the Wi-Fi name and password](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/ios-08-wifi-enter.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ios-08-wifi-enter.PNG)

After typing both your network name and password in *exactly* (both fields are case-sensitive, and be careful not to add any spaces at the end), **hit continue**.

#### Step 4: Monitor the Blynk Board\'s RGB LED

While it connects to Wi-Fi and Blynk, the Blynk Board will use the RGB LED to keep you informed on its progress.

After hitting \"Continue\", your Blynk Board should begin to **blink blue**, which indicates it's attempting to **connect to your Wi-Fi network**. This process usually takes around 10 seconds, but if it still hasn't connected after 30 seconds, it will give up and go back to setup mode.

If the provisioning process isn\'t going as planned -- whether it\'s failing to connect to Wi-Fi or Blynk -- try cycling power to your Blynk Board (unplug and re-plug the USB cable in), and starting from the beginning.

If you\'re still not having any luck provisioning through the app, you may have to use an [alternative provisioning process](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board#troubleshooting).

After the Blynk Board successfully connects to your Wi-Fi network, it will establish a connection with the **Blynk Cloud**. During this process, it will blink a soft, Blynk-colored green.

Finally, after a successful Blynk cloud connection, you should see the "Finished!" page. The RGB should be smoothly fading in-and-out. If so, **click Done** and Blynk will take you to a fresh Blynk Board project. Head over to the **[Do the zeRGBa section](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board#do-the-zergba)** of this tutorial to start Blynking!

[![Blynk connect success](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/ios-10-success.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ios-10-success.PNG)

If you had trouble provisioning your Blynk Board, try giving the whole process one more shot. **Cycle power to your Blynk Board**, by unplugging it and plugging it back in. Then try again from step 1.

If you\'re still not having any luck, consult the [Troubleshooting](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board#troubleshooting) section of this tutorial.

### Android Provisioning

If you haven't already, download the [Blynk App from the Google Play store](https://play.google.com/store/apps/details?id=cc.blynk). Then open it, **create an account** and log in.

Or, if you already have the Blynk app installed on your phone, make sure it's **updated to the latest release**!

#### Step 1: Scan the Blynk Board QR Code

Click the QR-code icon in the **top-right** corner of the Blynk app (or the bigger icon on the main screen).

[![Android QR code button](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/android-01-qr.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/android-01-qr.png)

Then scan your phone over the QR code on your Blynk Board card. Blynk should pop up a new screen -- congrats, you've got some new Blynk energy to play with!

[![Android welcome screen](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/android-02-welcome.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/android-02-welcome.png)

#### Step 2: Connect to the Blynk Board

From the "Congrats!" page, hit **Set Up New Device**, read through the [Pre-flight checklist](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/android-03-preflight.png) and -- as long as your Blynk Board is powered up and blinking the unique color code -- **hit Continue**.

This next page is where you'll select your Blynk Board. Scroll through the device list and select a network named **BlynkMe-CCCC** (one may already be selected). Make sure that color code suffix matches your Blynk Board's RGB LED blinking.

[![Select a Blynk Board](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/android-04-chooseDevice.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/android-04-chooseDevice.png)

Hit **Continue**. The app should attempt to connect to your Blynk Board. After a few seconds you should see the Blynk Board's RGB LED **blink purple** -- faster than before -- and the app should present you with a "Connected to BlynkMe" page.

[![Blynk Board connected](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/android-05-connected.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/android-05-connected.png)

From there hit **Continue** to proceed to the Wi-Fi provisioning.

📌 **Troubleshooting Tip:** When connecting to the board in the app, you may need to manually connect to the board in the phone's wifi settings. Temporarily jump out of the Blynk app, and find your phone's **Wi-Fi** settings. On an Android, it should be in the Wi-Fi section of the phone\'s settings.

Have your phone scan for Wi-Fi networks, and look for something that starts with **BlynkMe-**. The last four characters should match the four-color sequence your board is blinking. Connect your phone to the "BlynkMe-CCCC" network. Upon a successful connection, your Blynk Board should begin to blink purple. Once you see this status, head back into the Blynk app to continue. Here is a [.pdf file](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/Blynk_App_Instructions.pdf) with screenshots for reference.

If you\'re still not having any luck provisioning through the app, you may have to use an [alternative provisioning process.](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board#troubleshooting)

#### Step 3: Connect the Blynk Board to Wi-Fi/Blynk

On the next screen, select your Wi-Fi network from the scroll bar. Then enter your network's password.

[![Enter the Wi-Fi configuration](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/android-06-wifiConfig.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/android-06-wifiConfig.png)

After both network and password are correctly entered (both fields are case-sensitive! be careful not to add any spaces at the end), **hit continue**.

#### Step 4: Monitor the Blynk Board\'s RGB LED

While it connects to Wi-Fi and Blynk, the Blynk Board will use the RGB LED to keep you informed on its progress.

Your Blynk Board will begin to blink **blue**, which indicates it's attempting to connect to your Wi-Fi network. This process usually takes around 10 seconds, if it still hasn't connected after 30 seconds, it will give up and go back to setup mode.

If the provisioning process isn\'t going as planned -- whether it\'s failing to connect to Wi-Fi or Blynk -- try cycling power to your Blynk Board (unplug and re-plug the USB cable in), and starting from the beginning.

If you\'re still not having any luck provisioning through the app, you may have to use an [alternative provisioning process](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board#troubleshooting).

After the Blynk Board successfully connects to your Wi-Fi network, it will establish a connection with the **Blynk Cloud**. During this process it will blink a soft, Blynk-colored green.

After a successful Blynk cloud connection, you should see the "Finished!" page. And the RGB should be smoothly fading in-and-out.

[![Blynk Board configuration finished](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/android-07-finished.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/android-07-finished.png)

From there, **click Done** and Blynk will take you to a fresh Blynk Board project. Head over to the **[Do the zeRGBa section](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board#do-the-zergba)** of this tutorial to start Blynking!

If you had trouble provisioning your Blynk Board, try giving the whole process one more shot. **Cycle power to your Blynk Board**, by unplugging it and plugging it back in. Then try again from step 1.

If you\'re still not having any luck, consult the [Troubleshooting](https://learn.sparkfun.com/tutorials/getting-started-with-the-sparkfun-blynk-board#troubleshooting) section of this tutorial.

## Do the zeRGBa

Once you\'ve connected the Blynk Board to a local Wi-Fi network \-- and connected it to your Blynk account \-- the Blynk app should present you with a nearly blank canvas of a Blynk project.

You should be greeted by a festively colored zebra \-- the **zeRGBa** \-- and an **LCD widget** with a rather helpful link.

[![Blynk Board default Blynk project - zeRGBa and LCD](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/zergba-01-default.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/zergba-01-default.PNG)

Your first Blynk project should be all set up to communicate with the Blynk Board. It should also already be running, meaning it\'s play time! **Poke and prod the zeRGBa** to select a new color \-- you should quickly see a physical manifestation of that color on the Blynk Board.

[![zeRGBa setting the Blynk Board\'s LED to purple!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/zergba-01purple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/zergba-01purple.jpg)

If your zeRGBa isn\'t making LEDs blink, first **make sure the project is running**. The icon in the upper-right corner of the app should be a square \"**stop**\" button. If it\'s a triangular \"**play**\" button, tap that to run the project.

**Caution**: As tempting as it may be to perform a hypnotic light show, dragging your finger along the zeRGBa may cause the Blynk Board and Blynk App to occassionaly \"lag out.\" If the Blynk Board is slow to update the RGB\'s color, wait a couple seconds for it to re-connect.

To avoid this occasional connection-drop, try \"poking\" at your zeRGBa color of choice.

**Congratulations! You\'re well on-your-way to being a professional Blynker. From here we recommend you visit the [Blynk Board Project Guide](https://learn.sparkfun.com/tutorials/blynk-board-project-guide) to explore over a dozen Blynk projects built into the Blynk Board.**

[](https://learn.sparkfun.com/tutorials/blynk-board-project-guide)

### Blynk Board Project Guide 

March 25, 2016

A series of Blynk projects you can set up on the Blynk Board without ever re-programming it.

Or, you may want to check out some of these other Blynk-related tutorials:

[](https://learn.sparkfun.com/tutorials/blynk-board-bridge-widget-demo)

### Blynk Board Bridge Widget Demo 

A Blynk project that demonstrates how to use the Bridge widget to get two (or more) Blynk Boards to communicate.

[](https://learn.sparkfun.com/tutorials/blynk-board-arduino-development-guide)

### Blynk Board Arduino Development Guide 

How to get your computer set up with Arduino and the Blynk Board hardware definitions \-- so you can start creating Blynk projects of your own!

------------------------------------------------------------------------

## Troubleshooting

If, for any reason, you can\'t successfully provision the Blynk Board through the Blynk app, you have a few alternatives. But first, you\'ll need to **create a new Blynk project**.

### Creating a Blynk Project

Each of the alternative provisioning methods below will require a Blynk project to be previously created. The new Blynk project will be assigned a **Blynk auth token** \-- a 32-character, unique string, which connects the Blynk Board to your Blynk project. That\'s what we\'re after in this process.

Follow these steps to create a new Blynk project and get a new auth token:

#### Step 1: Create a Blynk Project

Open the Blynk app, and log in if you haven\'t. Make sure your phone is connected to an Internet-connected Wi-Fi network. On the Blynk main page, select **Create new project**.

[![Create a Blynk Project](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/createProject-01.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/createProject-01.PNG)

*Create a new Blynk Project by tapping \"Create New Project\" on the Blynk main page.*

#### Step 2: Configure the Blynk Project

On the next page, select **SparkFun Blynk Board** under the \"Hardware Model\" list. You can give the project any name you please \-- the provisioning process sets it to \"BlynkMe\".

[![Configure the new project](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/createProject-02.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/createProject-02.PNG)

*Configure a new project: name it, and set the board type to \"SparkFun Blynk Board.\"*

**Do not** hit Create Project yet!

#### Step 3: Email and Copy the Auth Token

Depending on which alternative provisioning option you choose, you\'ll either need the auth token copied to your phone\'s clipboard, or sitting in your email inbox. Might as well do both while we\'re here!

[![Email and copy the auth token](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/createProject-03.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/createProject-03.PNG)

Tap the **E-Mail button** to send the auth token to your Blynk-connected email account. Then **tap the Auth token itself** to copy the string to your phone\'s clipboard. The phone should pop up a notification confirming that the token was copied.

#### Step 4: Create Project

Finally, with the token emailed and copied, click **Create** or **Create Project**. You should be brought to a new, blank project \-- perfect for now!

### [] Alternative Provisioning

There are a few options available for alternatively provisioning the Blynk board. In order of our recommendation, you can:

1.  Connect the Blynk Board to Wi-Fi/Blynk using a laptop or Wi-Fi-enabled computer.
2.  Configure the Blynk Board through a serial terminal on a computer connected over USB to the Blynk Board.
3.  Creatively use copy/paste, and app-switching on your smartphone to provision the Blynk Board.

Click one of the links below to see how.

[Option 1: Laptop/Computer, Browser-Based Provisioning](#collapseLaptop)

[Option 2: Serial Terminal Over a USB-Connected Computer/Laptop](#collapseSerial)

[Option 3: Smartphone Browser-Based Provisioning](#collapsePhoneBrowser)

### Option 1: Laptop/Computer, Browser-Based Provisioning

If the Blynk app isn't correctly provisioning your Blynk Board and you have a computer with Wi-Fi capability nearby, you can use your computer and smartphone to join forces to get your Blynk Board configured. Just follow these steps:

#### Step 1: Get the Auth Token From Your E-Mail Inbox

Make sure you\'ve followed the steps from above -- created a project, and emailed the auth token to yourself. Then open your email on your computer and **copy the auth token** -- either to your clipboard or a simple text editor.

[![Create a new project in the Blynk app](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/ts-computer-03-emailAuth.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ts-computer-03-emailAuth.png)

*Check your email, and copy the Auth token.*

#### Step 2: Connect to Your Computer to the Blynk Board's Wi-Fi Network

Find your computer's **Wi-Fi** settings, and have it scan for nearby Wi-Fi networks. You should see something that starts with **BlynkMe-**. The last four characters should match the four-color sequence your board is blinking.

[![Create a new project in the Blynk app](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/ts-computer-04-connect-cropped.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ts-computer-04-connect-cropped.png)

*Connect your computer to the BlynkMe Wi-Fi network.*

Select the "BlynkMe-CCCC" network to connect your computer to it. On successful connection your Blynk Board should begin to blink purple.

#### Step 3: Point a Web Browser to 192.168.4.1

Open Safari, Chrome, Firefox, Edge, or whatever your favorite web browser may be, and navigate to [192.168.4.1](http://192.168.4.1) (that link will only work on a device connected to the Blynk Board).

After a couple seconds, the Blynk Board should serve up the Blynk Board Config Page. It may take a couple of tries to load the page; if your browser says "Failed to load webpage," or something to that effect, try refreshing.

#### Step 4: Send your Wi-Fi Network and Blynk Auth Token

The config page will present a **list of visible Wi-Fi networks** within range. If you see your network on there, great! Select that. If your network is hidden, scroll down to "\[Enter manually ...\]", and type it in yourself.

Next **enter the password** for your Wi-Fi network. If it's an open network (no password), leave the box blank.

Finally, **paste the auth token** into the Blynk auth token box. This process varies by phone, either a light tap (iOS) or a tap-and-hold should bring up the paste option.

[![Create a new project in the Blynk app](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/ts-computer-05-browser-cropped.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ts-computer-05-browser-cropped.png)

Unless you're connecting to the Blynk Board to a custom server (which you're most likely not), leave the Blynk host and port entries as-is.

Now **click Apply**.

#### Step 5: Monitor the Blynk Board

After hitting apply, the Blynk Board should begin to **blink blue** as it attempts to connect to your Wi-Fi network.

If that's successful, it'll begin to **blink Blynk-green** while it establishes a connection with the Blynk server.

Once both parties are happy, the Blynk Board's RGB LED should "breathe" Blynk-green, fading in-and-out, in-and-out. That's a great sign! Swap back to your phone, open the Blynk app and [we'll set up a zeRGBa](#manual-zergba).

If that didn\'t work, [go back to the provisioning options](#alternative-provisioning), and try something else. Or consider getting in touch with our [technical support team](https://www.sparkfun.com/technical_assistance).

### Option 2: Serial Terminal Over a USB-Connected Computer/Laptop

If Wi-Fi-based commissioning doesn\'t seem to be working out, you can provision the board over a hard-wire -- and get a little debug info at the same time -- using a serial terminal. In order to use the serial terminal method, you'll need:

1.  The Blynk Board **connected over USB** to a computer or laptop
2.  **FTDI drivers** installed on your computer
3.  Serial **terminal software**

#### Step 1: Install FTDI Drivers

The Blynk Board uses a specialized chip called an "FTDI" to convert USB data to a more simple serial interface. If you've never used an FTDI-based device before, you'll probably need to install drivers on your computer. Our [How to Install FTDI Drivers tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers) should help get your drivers installed, whether you're on a Mac, Windows, or Linux machine.

[Install FTDI Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers)

Once you've installed the drivers, your Blynk Board should show up on your computer as either **COM#** (if you're on a Windows machine) or **/dev/tty.usbserial-########** (if you're on a Mac/Linux computer), where the #'s are unique numbers or alphabetic characters.

#### Step 2: Select, Download, Install, Run Terminal Software

There are many, many software variants on the serial terminal out there. If you don't already have one, read through our [Serial Terminal Basics tutorial](https://learn.sparkfun.com/tutorials/terminal-basics) for some suggestions.

[Download a Terminal](https://learn.sparkfun.com/tutorials/terminal-basics)

#### Step 3: Configure the Serial Terminal Settings, Open the Connection

Once you've selected terminal software -- and found your Blynk Board's serial port number -- open it and set the baud rate to **9600**.

[![serial terminal settings](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/terminal-01-settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/terminal-01-settings.png)

*Using TeraTerm to communicate with the Blynk Board over a serial interface on COM3.*

After opening the terminal connecting **press \'h\'** to print a help menu. This will also confirm that your Blynk Board and terminal are talking to each other.

[![terminal help message](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ts-terminal-02-helpmenu.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ts-terminal-02-helpmenu.png)

Don\'t be alarmed if your Blynk Board prints messages before that help message. The board is configured to print a few handy debug messages at startup.

#### Step 4: Configure Wi-Fi

There are four **single-character commands** available for configuring the Blynk Board's Wi-Fi network, password, and Blynk token. Typing any of these characters will initiate the command:

- **h** -- Prints a help menu.
- **s** -- Scan for Wi-Fi networks, and select from a list of visible networks.
- **w** -- Manually enter a Wi-Fi network.
- **b** -- Initiates Blynk Token configuration.

**Press 's\' in the terminal** to scan for Wi-Fi networks and begin configuration. After a couple seconds, you should be presented with a list of visible Wi-Fi networks.

[![scan for networks](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ts-terminal-03-scanresult-blur.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ts-terminal-03-scanresult-blur.png)

If you see your Wi-Fi network, type the number or letter next to which it's listed. If you don't see the network -- or if it's supposed to be hidden -- hit `0` to type it in manually.

Following the network selection, the configuration tool will immediately ask you for the **Wi-Fi network password** -- type that in, and hit enter. If you're Wi-Fi network is open, just hit enter, leaving the password blank.

#### Step 5: Configure Blynk

After following the \"Create a Blynk Project\" directions, you should have an email sitting in your inbox containing your Blynk project\'s auth token. Load up your e-mail, and copy that auth token to your computer\'s clipboard.

[![scan for networks](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ts-computer-03-emailAuth.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/ts-computer-03-emailAuth.png)

Once you have the token copied to your clipboard, **type 'b'** to enter **Blynk Auth Token config mode**. Then paste your token in, and **hit enter**. Terminal programs all deal with copying/pasting differently, but you usually can't go wrong with **Edit \> Paste**.

[![Blynk auth token configuration](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/terminal-02-pasting-token.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/terminal-02-pasting-token.png)

#### Step 6: Monitor the Blynk Board

After sending over your Wi-Fi and Blynk credentials, the Blynk Board should begin to **blink blue** as it attempts to connect to your Wi-Fi network.

If that's successful, it'll begin to **blink Blynk-green** while it establishes a connection with the Blynk server.

Once both parties are happy, the Blynk Board's RGB LED should "breathe" Blynk-green, fading in-and-out, in-and-out. That's a great sign! Swap back to your phone, open the Blynk app and [we'll set up a zeRGBa](#manual-zergba).

If that didn\'t work, [go back to the provisioning options](#alternative-provisioning), and try something else. Or consider getting in touch with our [technical support team](https://www.sparkfun.com/technical_assistance).

### Option 3: Smartphone Browser-Based Provisioning

If the Blynk app isn't correctly provisioning your Blynk Board, you can still use your phone to go about the process manually. Follow these steps to manually set up your Blynk Board:

From the \"Create a Blynk Project\" directions above, you should have a **32-character Blynk auth token copied to your phone\'s clipboard**. Make sure you do before proceeding -- you\'ll be cut off from the Internet for the next few steps.

#### Step 1: Connect Your Phone to the Blynk Board's Wi-Fi Network

Temporarily jump out of the Blynk app, and find your phone's **Wi-Fi** settings. On an iOS device, this will be the "Wi-Fi" entry under the **Settings app**. On an Android, it should be in the Wi-Fi section of the phone\'s settings.

Have your phone scan for Wi-Fi networks, and look for something that starts with **BlynkMe-**. The last four characters should match the four-color sequence your board is blinking.

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/phoneBrowser-01.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/phoneBrowser-01.PNG)

Connect your phone to the "BlynkMe-CCCC" network. Upon a successful connection, your Blynk Board should begin to blink purple.

#### Step 2: Point a Web Browser to 192.168.4.1

Open Safari, Chrome, Firefox, "Internet", or whatever your favorite phone web browser may be, and navigate to [192.168.4.1](http://192.168.4.1) (that link will only work on a device connected to the Blynk Board).

After a couple seconds, the Blynk Board should serve up a webpage like this:

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/phoneBrowser-02.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/phoneBrowser-02.PNG)

It may take a couple refreshes to load the Blynk Board Config page. If your browser says "Failed to load webpage", or something to that effect, try refreshing.

#### Step 3: Send your Wi-Fi Network and Blynk Auth Token

The config page will present a **list of visible Wi-Fi networks** within range. If you see your network on there, great! Select that. If your network is hidden, scroll down to "\[Enter manually ...\]", and type it in yourself.

Next, **enter the password** for your Wi-Fi network. If it's an open network (no password), leave the box blank.

Finally, **paste the auth token** into the Blynk auth token box. This process varies by phone, either a light tap (iOS) or a tap-and-hold should bring up the paste option.

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/phone-browser-03.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/phone-browser-03.PNG)

Unless you're connecting to the Blynk Board to a custom server (which you're most likely not), leave the Blynk host and port entries as-are (blynk-cloud.com and 8442).

Now **click Apply**.

#### Step 4: Monitor the Blynk Board

After hitting apply, you should be served a confirmation page, informing you of what the Blynk Board is attempting to do.

[![](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/phoneBrowser-04.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/phoneBrowser-04.PNG)

The Blynk Board should immediately begin to **blink blue** as it attempts to connect to your Wi-Fi network.

If that's successful, it'll begin to **blink Blynk-green** while it establishes a connection with the Blynk server.

Once both parties are happy there, the Blynk Board's RGB LED should "breathe" Blynk-green, fading in-and-out, in-and-out. That's a great sign! Swap back to the Blynk app and [we'll set up a zeRGBa](#manual-zergba).

If that didn\'t work, [go back to the provisioning options](#alternative-provisioning), and try something else. Or consider getting in touch with our [technical support team](https://www.sparkfun.com/technical_assistance).

### [] Manually Adding a zeRGBa Widget

Hopefully one of the three alternative provisioning processes has worked for you. If not, please don\'t hesitate to get in touch with our [technical support team](https://www.sparkfun.com/technical_assistance).

If your Blynk Board is breathing Blynk-green, **open the Blynk app on your phone**, and select the bare project you\'ve created. Look at that blank canvas \-- room for so many widgets!

[![Blank Blynk project](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/manual-zergba-01-blank.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/manual-zergba-01-blank.png)

*A new Blank Blynk project. (Android left, iOS right)*

To add a widget to the Blynk app, first make sure the project **isn\'t running** \-- you should see a triangular-shaped \"play\" icon in the upper-right-hand corner. Now **tap anywhere in the grey project space** to bring up the Blynk widget box.

[![Adding a zergba](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/manual-zergba-02-widgetbox.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/manual-zergba-02-widgetbox.png)

*Add a zeRGBa widget from the Blynk widget box.*

**Select the zeRGBa** widget to add it to your project. You can **tap-and-hold** the widget to drag it around the project space. We find the zeRGBa prefers to be the center-of-attention.

Now **tap the zeRGBa** to enter the widget settings \-- you\'ll get very used to this. Slide the Split/Merge switch over to **Merge**. Then **tap \"PIN\"**, and set the box to **V0**. The widget settings should look like this:

[![zeRGBa settings](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/manual-zergba-03-zergbasettings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/manual-zergba-03-zergbasettings.png)

To back out of the settings tab, hit **OK** on iOS or the **upper-left back arrow** on an Android.

Back at the project screen, **tap the play button** in the upper-right corner to start Blynking! Once you\'ve got the project running, poke-and-prod that colorful zebra!

[![zeRGBa purple, LED purple!](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/zergba-01purple.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/zergba-01purple.jpg)

------------------------------------------------------------------------

**Congratulations! You\'re well on-your-way to being a professional Blynker. From here we recommend you visit the [Blynk Board Project Guide](https://learn.sparkfun.com/tutorials/blynk-board-project-guide) to explore over a dozen Blynk projects built into the Blynk Board.**

[](https://learn.sparkfun.com/tutorials/blynk-board-project-guide)

### Blynk Board Project Guide 

March 25, 2016

A series of Blynk projects you can set up on the Blynk Board without ever re-programming it.

Or, you may want to check out some of these other Blynk-related tutorials:

[](https://learn.sparkfun.com/tutorials/blynk-board-bridge-widget-demo)

### Blynk Board Bridge Widget Demo 

A Blynk project that demonstrates how to use the Bridge widget to get two (or more) Blynk Boards to communicate.

[](https://learn.sparkfun.com/tutorials/blynk-board-arduino-development-guide)

### Blynk Board Arduino Development Guide 

How to get your computer set up with Arduino and the Blynk Board hardware definitions \-- so you can start creating Blynk projects of your own!

## Reconfiguring a Blynk Board

If you\'ve taken your Blynk Board somwhere new, and need to **reconfigure its Wi-Fi** network \-- or if you need to update the Blynk auth token \-- there\'s a built-in method for re-entering configuration mode to reset both credentials.

While the Blynk Board is attempting to connect to a Wi-Fi network or Blynk \-- blinking blue or green \-- **press and hold the 0 button**.

[![Hold the 0 button for 3 seconds to reprovision](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/8/6/reprovisioning-01-button-press.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/4/8/6/reprovisioning-01-button-press.jpg)

You should see the RGB LED turn white and slowly increase in brightness. After about a second, the LED will begin to dim. Once you\'ve held the button for about **4 seconds** and the LED begins to brighten again, **release the button**.

If the reset was successful, you should see the Blynk Board revert back to its R/G/B/Y/P color-combo sequence. It should also show up as a Wi-Fi access point, and you\'ll be able to configure it over either Wi-Fi or a serial terminal.

You can even re-scan your Blynk Board QR-Code Card. No, you won\'t get another 15k energy, but you will be able to step through the provisioning process again!