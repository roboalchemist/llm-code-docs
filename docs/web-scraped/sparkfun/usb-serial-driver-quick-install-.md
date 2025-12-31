# Source: https://learn.sparkfun.com/tutorials/usb-serial-driver-quick-install-

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- USB Serial Driver Quick Install

# USB Serial Driver Quick Install

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1b00b259d107c598ffacb3664a190c26?d=retro&s=20&r=pg) Joel_E_B]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft609&name=USB+Serial+Driver+Quick+Install+ "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft609 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=USB+Serial+Driver+Quick+Install+&url=http%3A%2F%2Fsfe.io%2Ft609&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft609&t=USB+Serial+Driver+Quick+Install+ "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft609&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F0%2F9%2F51acdb85ce395fd23d000000.jpg&description=USB+Serial+Driver+Quick+Install+ "Pin It")

## FTDI Driver Installation 

Development boards such as the SparkFun RedBoard for Arduino and the Arduino Uno require special drivers or code that tells the computer how to interact with them. This guide is here to help you get this driver software installed as quickly as possible so you can get back to building circuits and learning about electronics!

These instructions apply to both the Arduino Uno, the Arduino Uno SMD, and the SparkFun RedBoard for Arduino.

**Note:** You should only have to complete this process one time. Once the correct drivers are installed, your board will be recognized by your computer every time you plug it in afterwards.

**Note for Educators:** You will most likely need to obtain administrative privileges from your network or IT administrator in order to install these drivers.

Scroll down to the corresponding section for whichever operating system (OS) you are using.

## Windows

Plug the board into your computer. Windows will likely complain about the device not having the correct driver. It may attempt to find it. If you have never plugged in a similar device to your computer, it probably won\'t find a driver to use. Luckily, when you downloaded the Arduino IDE, it also came with all the necessary drivers.

To install the correct driver, open the **Device Manger**. This can be found be searching for \"device manager\" in the start menu. Once Device Manager is open, you should see a device with a tiny yellow triangle and exclamation mark next to it.

If you plugged in a SparkFun RedBoard, it will look like the image on the left. Plugging in an Arduino Uno will result in the image on the right.

![](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/win1.jpg)

![](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/win00.jpg)

\

Right-click on the unknown device, and select **Properties**.

[![properties](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windowsRightClickProperties.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windowsRightClickProperties.PNG)

In the properties window, select **Driver Details**.

[![driver details](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows2.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows2.PNG)

Select the **Browse my computer for driver software** option.

[![browse](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows3.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows3.PNG)

Navigate to the destination where you installed the Arduino IDE. On Windows, this will most likely be in your Program Files folder. Navigate to the drivers folder found inside the main Arduino folder. You can select the entire folder or the specific driver. needed Your path should look something like this but may vary:

[![find](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows4.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows4.PNG)

Once the driver installation is complete, you should see the device reappear in the Device Manager window as a usable COM port. The number will vary depending on how many devices you have plugged into your computer. The RedBoard will appear as a `USB Serial Port`, as shown in the left image. The Uno will appear as an `Arduino Uno`, as shown in the right image.

![](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows6.PNG)

![](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows08.PNG)

\

In the Arduino IDE, you should see that same serial port available under Tools -\> Port.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows7.PNG)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/windows7.PNG)

If you are experiencing problems, please see our [in-depth instructions](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers/windows---in-depth).

## MacOS

Plug the board into your computer. Once plugged in, the operating system should recognize it as the appropriate device. In the Arduino IDE, click Tool -\> Ports to ensure the device has been recognized. The SparkFun RedBoard will appear a `cu.usbserial-XXXXXX` device.

[![mac RedBoard](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/mac1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/mac1.png)

The Arduino Uno will appear as a `cu.usbmodemXXXXXX` device.

[![mac Uno](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/mac2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/mac2.png)

If you do not see an available serial port in the Arduino IDE after plugging in your board and waiting a moment, then you may need to install the drivers by hand. To do so, please see our [in-depth instructions](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers/mac).

## Linux

Plug the board into your computer. Once plugged in, the operating system should recognize it as the appropriate device. In the Arduino IDE, click Tool -\> Ports to ensure the device has been recognized. The SparkFun RedBoard will appear a `ttyUSBXX` device.

[![Linux RedBoard](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/linux1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/linux1.png)

The Arduino Uno will appear as a `ttyACMXX` device.

[![Linux Uno](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/linux2.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/0/9/linux2.png)

If you do not see an available serial port in the Arduino IDE after plugging in your board and waiting a moment, then you may need to install the drivers by hand. To do so, please see our [in-depth instructions](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers/linux).

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft609&name=USB+Serial+Driver+Quick+Install+ "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft609 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=USB+Serial+Driver+Quick+Install+&url=http%3A%2F%2Fsfe.io%2Ft609&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft609&t=USB+Serial+Driver+Quick+Install+ "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft609&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F0%2F9%2F51acdb85ce395fd23d000000.jpg&description=USB+Serial+Driver+Quick+Install+ "Pin It")

[**Sections**] [FTDI Driver Installation](#ftdi-driver-installation-)

[Comments [1]](https://learn.sparkfun.com/tutorials/usb-serial-driver-quick-install-/discuss) [View Paginated](https://learn.sparkfun.com/tutorials/usb-serial-driver-quick-install-/ftdi-driver-installation-) [Print](#)

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Skill](https://learn.sparkfun.com/tutorials/tags/skill)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]