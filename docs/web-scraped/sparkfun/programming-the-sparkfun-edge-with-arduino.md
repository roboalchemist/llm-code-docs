# Source: https://learn.sparkfun.com/tutorials/programming-the-sparkfun-edge-with-arduino

## Introduction

When we released the [SparkFun Edge Development Board](https://www.sparkfun.com/products/15170) powered by TensorFlow, we knew that we were releasing it slightly ahead of the software wave that was promised to follow. One of the downsides that people mentioned was the fact that they had to learn a new SDK with which they were completely unfamiliar.

[![SparkFun Edge Development Board - Apollo3 Blue](https://cdn.sparkfun.com/r/600-600/assets/parts/1/3/5/6/7/15170-SparkFun_Edge_Development_Board_-_Apollo3_Blue-01a.jpg)](https://www.sparkfun.com/sparkfun-edge-development-board-apollo3-blue.html)

### [SparkFun Edge Development Board - Apollo3 Blue](https://www.sparkfun.com/sparkfun-edge-development-board-apollo3-blue.html) 

[ DEV-15170 ]

The SparkFun Edge Development Board powered by TensorFlow is perfect begin using voice recognition without relying on the ser...

**Retired**

With the promise it holds, offering AI and machine learning on a board sporting an ARM-Cortex-M4F, a camera connector, dual MEMS microphones, a Qwiic connector, Bluetooth antenna and much more, users were anxious to start experimenting, but not quite as eager to learn a new development environment. So with no small effort from our engineering department, and with help from Pete Warden, Google\'s lead engineer for TensorFlow Lite and Tiny ML, it is now possible to start programming several experiments using AI and machine learning on the SparkFun Edge board through the familiar Arduino IDE.

## Set Up for Success

### Required Materials

To follow along with this tutorial, you will need the following materials.

[![SparkFun Serial Basic Breakout - CH340C and USB-C](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/5/2/15096-SparkFun_Serial_Basic_Breakout_-_CH340C_and_USB-C-01.jpg)](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340c-and-usb-c.html)

### [SparkFun Serial Basic Breakout - CH340C and USB-C](https://www.sparkfun.com/sparkfun-serial-basic-breakout-ch340c-and-usb-c.html) 

[ DEV-15096 ]

This SparkFun Serial Basic Breakout is an easy-to-use USB-to-Serial adapter based on the CH340G and takes advantage of the ha...

[ [\$10.50] ]

[![Reversible USB A to C Cable - 2m](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/9/8/3/15424-Reversible_USB_A_to_C_Cable_-_2m-01.jpg)](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html)

### [Reversible USB A to C Cable - 2m](https://www.sparkfun.com/reversible-usb-a-to-c-cable-2m.html) 

[ CAB-15424 ]

These 2m cables have minor modifications that allow them to be be plugged into their ports regardless of orientation on the U...

[ [\$10.50] ]

[![Himax CMOS Imaging Camera - HM01B0 (Monochrome)](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/1/6/5/15570-Himax_Imaging_Camera-01.jpg)](https://www.sparkfun.com/himax-cmos-imaging-camera-hm01b0.html)

### [Himax CMOS Imaging Camera - HM01B0 (Monochrome)](https://www.sparkfun.com/himax-cmos-imaging-camera-hm01b0.html) 

[ SEN-15570 ]

An ultra low power CMOS Image Sensor that enables the integration of an "Always On" camera for computer vision applicatio...

[ [\$10.95] ]

[![SparkFun Edge Development Board - Apollo3 Blue](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/5/6/7/15170-SparkFun_Edge_Development_Board_-_Apollo3_Blue-01a.jpg)](https://www.sparkfun.com/sparkfun-edge-development-board-apollo3-blue.html)

### [SparkFun Edge Development Board - Apollo3 Blue](https://www.sparkfun.com/sparkfun-edge-development-board-apollo3-blue.html) 

[ DEV-15170 ]

The SparkFun Edge Development Board powered by TensorFlow is perfect begin using voice recognition without relying on the ser...

**Retired**

NOTE: You can also use the [USB-micro version of the Serial Basic Breakout](https://www.sparkfun.com/products/14050), and a micro-USB cord, as well as the [FTDI version](https://www.sparkfun.com/products/9873) (as opposed to the CH310 version listed), which may be a better option on macOS.

Before going on, you'll want to make sure you've gone through the original [SparkFun Edge Hookup Guide](https://learn.sparkfun.com/tutorials/sparkfun-edge-hookup-guide). Setting up the Ambiq Apollo3 SDK isn't necessary for this tutorial, however, you will want to roll up your sleeves and dig into it at some point to utilize the full potential of this board.

At this point it is assumed that you have the Arduino IDE installed on your machine, but if not, or if you need to upgrade to the latest release, you can get that from [Arduino's website](http://www.arduino.cc/en/Main/Software).

### Installing the Libraries

The examples utilize the TensorFlowLite Arduino library, which is installed using the Arduino Library Manager, and the Person Detection example also uses the Himax HM01B0 Camera Library.

To install this library, use the following steps:

- In Arduino, select the \"Manage Libraries\...\" menu item. Tools \> Manage Libraries\...
- In the Library Manager interface, search for tensorflow
- Select the library Arduino_TensorFlowLite by TensorFlow Authors
- Select the non-precompiled version of the library
- Select the Install button to install the library

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/0/3/LibraryTensorFlow.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/LibraryTensorFlow.JPG)

**NOTE**: It is imperative that you install the ***non-precompiled*** version of the library. Installing the pre-compiled library will only lead to failure and sadness.

To install the Himax HM01B0 Camera Library:

- While still in the Library Manager interface, search for Himax
- Select the SparkFun Himax HM01B0 Camera Library
- Select the Install button to install the library
- Close the dialog window

### Installing the SparkFun Boards Package

To install the necessary boards package, use the following steps:

- In Arduino, open the Preferences menu item. File \> Preferences, (macOS) Arduino \> Preferences
- Add the following path to the Additional Boards Manager URLs: path in preferences.

`https://raw.githubusercontent.com/sparkfun/Arduino_Boards/master/IDE_Board_Manager/package_sparkfun_index.json`

- Select the OK button to save the preferences.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/0/3/AdditionalBoardsURL.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/AdditionalBoardsURL.JPG)

Once the location of the SparkFun boards package is set in the preferences, the board definition package for the SparkFun Apollo3 boards must be installed. To install package, use the following steps:

- In Arduino, open the Board Manager. Tools \> Board \"\...\" \> Manage Boards\...
- Search for Apollo3
- Select the **SparkFun Apollo3 Boards** package
- Select the Install button to install the library
- Close the dialog window

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/BoardsManager.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/BoardsManager.JPG)

## Running the Examples

### Get the Code

We have three examples written for the Edge board using TensorFlow Lite and programmed with Arduino. They can be cloned or downloaded and unzipped from here:

`https://github.com/sparkfun/Tensorflow_AIOT2019`

With your Edge Board connected to your computer (via your Serial Breakout), go to your Tools\>Board\"\...\", and select SparkFun Edge. Next, you\'ll need to select the port to which your board is connected.That can be found under Tools\>Port\>. It will look slightly different depending on your OS.

- Windows - \"COM Port\"
- macOS - \"/dev/cu.usbserial\*\" (Note: You might have to check permissions)
- Linux - \"/dev/ttyUSB\*\"

You\'re now ready to open your first example. Go to the folder where you downloaded (and unzipped, if necessary) the examples folder.

### Micro Speech

From the micro_speech folder in your TensorFlow_AIOT2019-master folder, open the file micro_speech.ino. Full disclosure - this is the sketch that comes pre-loaded on your SparkFun Edge Board, so you should already see the blue LED blinking. If you open the Serial Monitor of your Arduino IDE, saying \"Yes\" will return something like \"Heard yes (203) \@4032ms,\" accompanied by a single blink of the yellow onboard LED; saying \"No\" will return a statement similar to \"Heard no (209) \@7936ms,\" along with a blink of the red onboard LED. Any other word or statement that the mics pick up will return \"Heard unknown (212) \@50304ms.\" I\'ve noticed that a more percussive \"yes\" seems be be picked up a little better, and a slightly slower, more drawn out \"no\" tends to be better recognized by the model. The model used for this example is called from within the void:setup(), here:

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/SpeechModel.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/SpeechModel.JPG)

**Support Tip:** When opening the Serial Monitor, be sure to check the port you are selecting for the board (*see previous section*) and make sure you are using select **9600 baud** from the drop down menu of the Serial Monitor (*bottom of window*).

### The Upload Sequence

By default, when you power up the SparkFun Edge Board, it immediately goes to Run mode and runs whatever file has been uploaded to it. In order to upload something new, we need to put it in bootloader mode. This is done using the two buttons on the Edge Board in a specific sequence. When you are ready to upload your code, take the following steps:

- Press and hold the Reset button
- While still holding down the Reset button, press and hold the 14 button
- Release the Reset Button
- Hit Upload in the Arduino IDE (or use your keyboard shortcut)
- Release the 14 button (after the upload has completed)

These files will take a bit longer than your standard Arduino sketches to compile and upload, so be patient. If you want to see what\'s going on during all that time, you can always go back into your Arduino preferences and check the boxes for verbose output.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/ArduinoPrefsVerbose.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/ArduinoPrefsVerbose.jpg)

The Arduino IDE will make three attempts to upload the sketch to your board. Ideally, when it finished, you should see \"Upload complete!\" in the output pane. However, we\'ve noticed that this process can sometimes be a little finicky. You may get a message that reads \"Tries = 3; Upload failed!\" You can always reset and try again, or lower the SVL Baud Rate down to 460800. We\'ve yet to nail down a specific reason for this issue - wind direction, pollen count, still not entirely sure - but a little patience should get you up and running.

### Person Detection

This example uses an imaged captured by a camera for the classification process. The model is trained to recognize when a person is present. When the model analyzes an image, the serial monitor will display scores for \"human detected\" and \"no human detected.\" Keep in mind that this isn\'t motion detection, nor is it reading pixel differences from frame to frame. The model here is looking for what it perceives to be a human figure based on its training model.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/0/3/ArduinoPersonDetectLoop.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/ArduinoPersonDetectLoop.JPG)

The upload protocol is the same as it was for the first example. The only difference is that you need the camera module attached. When attaching it to the Edge Board, make sure that the lens is facing out over the back, or battery side of the Edge Board, as in the image below.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/15570-Himax_CMOS_Imaging_Camera_-_HM01B0-05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/15570-Himax_CMOS_Imaging_Camera_-_HM01B0-05.jpg)

This is by far the largest of the three packages, and will therefore take the longest to upload. It sends the 284776 bytes in 140 frames of 2048 bytes each (except for the final frame, which only contains 104 bytes). Occasionally it will choke up about halfway through the upload. We\'ve found that, especially on Macs, adjusting the SVL Baud Rate (under \"Tools\>\") down to 460800 may do the trick, or sometimes it just needs a retry at the same speed. Once it uploads, reset your board and see how it does.

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/ArduinoPersonDetection.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/ArduinoPersonDetection.JPG)

Here you can see how it did with me - never really 100 percent sure I was a person, although once I put a little light on myself (the final score), it felt pretty sure that I was, in fact, human.

### Magic Wand

Time to get your Harry Potter on! For the final example, open the magic_wand sketch. This example uses a 20KB neural network and TensorFlowLite to recognize gestures. It reads data from the Edge Board\'s on-board accelerometer, and the recognized gestures are output to the serial monitor, as well as the on-board LEDs. This sketch recognizes three distinct gestures, which we\'re calling a wing, a ring and a slope.

[![alt text](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/1/0/3/WandGestures.JPG)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/WandGestures.JPG)

Note the direction of each gesture, as it does make a difference. For example, a counter-clockwise ring movement will not work. Go ahead and upload the sketch in the same fashion as the other two. Once that\'s done, you\'ll want to hold the board with the serial connector to your left, camera port away from you. In order for the board to properly read the gestures, you\'ll have the best luck if you keep your wrist rigid, and move your arm from the elbow. Arpit Shah, the Director of Technology & Partner Enablement at Ambiq Micro (makers of the Apollo3 chip on the Edge Board) who helped with the workshop we lead at the ARM AIoT Dev Summit, found he had the best luck taping or rubber banding the board to the end of a drumstick. (Apparently he was out of unicorn hair and/or dogwood). Hold the board still to allow it to orient itself, then make one of the gestures, holding at the end for a second as well. It may take a little practice to get it consistent, but isn\'t that true of all magic?

[![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/EdgeWandSerialOutput.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/3/EdgeWandSerialOutput.gif)

### More magic please!

If you\'re ready to dig deeper, and want to start adding additional gestures to your magical repertoire, you can find a good starting off point at TensorFlow\'s GitHub repository. Check out the instructions in the README.md that is linked to train your own model.

[Magic Wand: Train Your Own Model](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro/examples/magic_wand#train-your-own-model)

This is quite a bit more than just running a simple Arduino sketch, so be prepared to do some heavy brain lifting here.

## Troubleshooting

[] **Need help?**\
\
If your product is not working as you expected or you need technical assistance or information, head on over to the [SparkFun Technical Assistance](https://www.sparkfun.com/technical_assistance) page for some initial troubleshooting.\
\
If you don\'t find what you need there, the [SparkFun Forums](https://forum.sparkfun.com/index.php) are a great place to find and ask for help. If this is your first visit, you\'ll need to [create a Forum Account](https://forum.sparkfun.com/ucp.php?mode=register) to search product forums and post questions.\
\
[SparkFun Edge Board Forum](https://forum.sparkfun.com/viewforum.php?f=153)