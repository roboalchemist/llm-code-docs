# Source: https://learn.sparkfun.com/tutorials/installing-an-arduino-library

## What\'s a Library?

Arduino libraries take a complex task and boil it down to simple to use functions. Arduino users have written lots of exciting add-ons for Arduino. For example, [capacitive sensing](http://en.wikipedia.org/wiki/Capacitive_sensing) takes difficult timing and pulsing of digital pins. We can write the code from scratch, or we can stand on the shoulders of great people who are smarter than we are.

Capacitive touch sensing is a very popular interface. The [CapacitiveSensor library](http://playground.arduino.cc/Main/CapacitiveSensor) takes care of everything so that we don't have to write code like this:

    language:c
    *sOut &= ~sBit;        // set Send Pin Register low
    *rReg &= ~rBit;        // set receivePin to input
    *rOut &= ~rBit;        // set receivePin Register low to make sure pullups are off
    *rReg |= rBit;         // set pin to OUTPUT - pin is now LOW AND OUTPUT
    *rReg &= ~rBit;        // set pin to INPUT 
    *sOut |= sBit;         // set send Pin High
    interrupts();         // enable interrupts

    while ( !(*rIn & rBit)  && (total < CS_Timeout_Millis) ) 

    if (total > CS_Timeout_Millis) 
        return -2;         //  total variable over timeout

    // set receive pin HIGH briefly to charge up fully
    noInterrupts();         // disable interrupts
    *rOut  |= rBit;        // set receive pin HIGH - turns on pullup 
    *rReg |= rBit;         // set pin to OUTPUT - pin is now HIGH AND OUTPUT
    *rReg &= ~rBit;        // set pin to INPUT 
    *rOut  &= ~rBit;       // turn off pullup
    *sOut &= ~sBit;        // set send Pin LOW
    interrupts();         // re-enable interrupts

    while ( (*rIn & rBit) && (total < CS_Timeout_Millis) ) 

    if (total >= CS_Timeout_Millis)
        return -2;     // total variable over timeout
    else
        return 1;

All that code can be replaced with a much easier to use and understand statement such as:

    language:c
    senseReading = myCapPad.capacitiveSensor(30);

The `myCapPad.capacitiveSensor()` takes care of all the heavy lifting and the `senseReading` variable contains the value sensed from our capacitive pad. Libraries make complex tasks easier so that we can focus on larger projects.

There are thousands of libraries out there! And luckily it's pretty easy to install them. This tutorial will show you how to install a library in [Arduino v1.0.5](http://arduino.cc/en/Main/Software) but should apply for many past, present, and future versions of Arduino.

### Suggested Reading

Make sure you have a good understanding of the following concepts before getting any further into this tutorial.

[](https://learn.sparkfun.com/tutorials/what-is-an-arduino)

### What is an Arduino? 

What is this \'Arduino\' thing anyway? This tutorials dives into what an Arduino is and along with Arduino projects and widgets.

[](https://learn.sparkfun.com/tutorials/installing-arduino-ide)

### Installing Arduino IDE 

A step-by-step guide to installing and testing the Arduino software on Windows, Mac, and Linux.

The Arduino website also has great instructions on installing libraries if you need more information for using the Arduino IDE\'s library manager, importing a **\*.zip** library, and manual installation.

[Arduino\'s Official Library Instructions](https://www.arduino.cc/en/Guide/Libraries)

## Using the Arduino Library Manager

The library manager was added starting with Arduino IDE versions 1.5 and greater (1.6.x). It is found in the \'Sketch\' menu under \'Include Library\', \'Manage Libraries\...\'

[![Manage libraries menu option](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/1/LibraryManager.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/LibraryManager.png)

*Arduino 1.5+ Library Manager Menu Option*

When you open the Library Manager you will find a large list of libraries ready for one-click install. To find a library for your product, search for the product name or a keyword such as \'k type\' or \'digitizer\', and the library you want should show up. Click on the desired library, and the \'Install\' button will appear. Click that button, and the library should install automatically. When installation finishes, close the Library Manager.

[![Example library in library manager](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/1/LibInstall.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/LibInstall.png)

*Library in the Library Manager, Ready to be Installed*

Alternatively, if you have a library of your own you would like to add or a library that hasn\'t been added to the Library Manger yet, you can click the \'**Add .ZIP Library**\' option, which will then allow you to choose a folder or **\*.zip** file containing the library of your choice.

**Heads up!** In previous version of the Arduino IDE, all libraries were stored together deep within the contents folder of the Arduino application. However, in newer versions of the IDE, libraries added through the Library Manger can be found in a folder named \'**libraries**\' found in your Arduino Sketchbook folder.\
For more information on the Library manger, including deleting and updating info, visit the [GitHub: Arduino - Library Manager FAQ](https://github.com/arduino/Arduino/wiki/Library-Manager-FAQ).\
\

[GitHub: Arduino - Library Manager FAQ](https://github.com/arduino/Arduino/wiki/Library-Manager-FAQ)

\

Now that the library is installed, an example sketch can be found in the \'Examples\' submenu.

[![Example sketch](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/1/example.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/1/example.png)

*Example Sketch*

Since this is a relatively new feature of the Arduino IDE at the time of this writing not all SparkFun products will have libraries in the library manager. We are adding new products and working our way through older products over time. If you don\'t find the library you need in the manager or for some reason cannot install one of the modern IDE releases, follow the instructions in the following sections.

## Manually Installing a Library - Windows

This section covers manually installing a library under the Windows environment and utilizes quite a few screen shots. If you're more of a text learner then check out the Arduino tutorial on [installing libraries](http://arduino.cc/en/Guide/Libraries).

We are going to use the [Capacitive Sense](http://playground.arduino.cc/Main/CapacitiveSensor) library for this example. Navigate to the library's page and download the zip file.

[![Example of Installed Capacitive Touch Arduino Library on Windows](//cdn.sparkfun.com/assets/9/d/e/2/b/51280175ce395fec2c000002.jpg)](//cdn.sparkfun.com/assets/9/d/e/2/b/51280175ce395fec2c000002.jpg)

*The contents of the Capacitive Sense zip file*

Find the zip file on your local computer (wherever downloaded files end up). Under Windows, you should be able to double click on the file to open it up.

This particular library contains libraries for both the basic Arduino and the more advanced Arduino Due. You can use both if you'd like, but, for this example, we will be copying and installing only the *CapacitiveSensor* folder.

[![Zipped Arduino Library](//cdn.sparkfun.com/assets/c/e/4/a/8/50f04a47ce395fed5d000000.jpg)](//cdn.sparkfun.com/assets/c/e/4/a/8/50f04a47ce395fed5d000000.jpg)

Libraries will usually contain a **\*.cpp** file and **.h** file. Most will also contain an *examples* folder.

[![Arduino Libraries Path](//cdn.sparkfun.com/assets/5/c/e/c/2/51280267ce395fba2c000000.jpg)](//cdn.sparkfun.com/assets/5/c/e/c/2/51280267ce395fba2c000000.jpg)

Under Windows, Arduino stores all the add-on libraries within the *My Documents* folder. Here we see the location of the Arduino *libraries* folder.

Open an explorer window and navigate to the libraries folder under *My Documents*. Now copy the new *CapacitiveSensor* folder to the *libraries* folder.

[![Capacitive Sensor Library in Arduino Libaries Folder](//cdn.sparkfun.com/assets/6/1/5/f/e/5128042fce395f022d000001.jpg)](//cdn.sparkfun.com/assets/6/1/5/f/e/5128042fce395f022d000001.jpg)

Success!

**Note:** Arduino does not allow library folders to contain symbols such as hyphens ' - '. Arduino will throw an error upon starting up. If the library you are installing has a funky folder name then this step is the ideal time to clean it up.\
\

[![](http://cdn.sparkfun.com/assets/3/c/d/f/9/50f04a48ce395fe460000001.jpg "arduino error")](http://cdn.sparkfun.com/assets/3/c/d/f/9/50f04a48ce395fe460000001.jpg)

To verify the library has been installed correctly, open up the *Examples* folder under the Arduino IDE. Wait. Where's the *CapacitiveSensor* example? Did you have Arduino open when you copied and pasted the directory? Arduino checks the library directory at startup so if you already have Arduino open, you will need to restart Arduino any time you add to the libraries directory.

[![Missing Arduino Capacitive Sensor Library](//cdn.sparkfun.com/assets/4/b/f/e/e/51280533ce395f662d000000.jpg)](//cdn.sparkfun.com/assets/4/b/f/e/e/51280533ce395f662d000000.jpg)

If you don't see the CapacitiveSensor example try closing and re-opening Arduino IDE.

[![Verify Arduino Capacitive Sensor Library](//cdn.sparkfun.com/assets/f/b/b/e/5/51280488ce395f932d000000.jpg)](//cdn.sparkfun.com/assets/f/b/b/e/5/51280488ce395f932d000000.jpg)

There it is! Let's open the example provided with our new library.

[![Example Capacitive Touch Library](//cdn.sparkfun.com/assets/9/0/5/f/8/50f04a47ce395f0f5e000000.jpg)](//cdn.sparkfun.com/assets/9/0/5/f/8/50f04a47ce395f0f5e000000.jpg)

**Examples** are the greatest thing about libraries! Good libraries will have well written examples showing how to use the library. These sketches are wonderful resources for example code and learning how to write good code under Arduino.

You now have the Capacitive Sensor library installed! Feel free to start from the example sketch, or begin writing your own code using the functions provided by the library. A library usually has documentation either on its site or written into readme files and example code. In general, to quickly learn how to use a library check out the example code.

## Manually Installing a Library - Mac

This section covers manually installing a library under the Mac OS X environment. If you're more of a text learner then check out the Arduino tutorial on [installing libraries](http://arduino.cc/en/Guide/Libraries).

We are going to use the [Capacitive Sense](http://playground.arduino.cc/Main/CapacitiveSensor) library for this example. Navigate to the library's page and download the zip file.

Find the zip file on your local computer (wherever downloaded files end up). Unzip it, and look at the folder contents.

[![Example of Installed Capacitive Touch Arduino Library on Mac OS X](https://cdn.sparkfun.com/assets/a/9/5/7/b/52af4a1f757b7fce6c8b4567.jpg)](https://cdn.sparkfun.com/assets/a/9/5/7/b/52af4a1f757b7fce6c8b4567.jpg)

*The contents of the Capacitive Sense zip file. Libraries will usually contain a \*.cpp\* file and \*.h\* file. Most will also contain an \*examples\* folder.*

This particular library contains libraries for both the basic Arduino and the more advanced Arduino Due. You can use both if you'd like, but, for this example, we will be copying and installing only the *CapacitiveSensor* folder.

Now we need to add this folder to the Libraries folder for Arduino. This folder is somewhat hidden in OS X. To get there you can do one of two things. Option one, right-click on the Arduino icon located in your Dock. Go up to \'**Options**\', then click \'**Show in Finder**\'.

[![Getting to the Arduino Libraries 1](https://cdn.sparkfun.com/assets/c/2/b/7/0/52af48ed757b7fa25e8b4567.jpg)](https://cdn.sparkfun.com/assets/c/2/b/7/0/52af48ed757b7fa25e8b4567.jpg)

Option two, find the Arduino app located in your applications folder within Finder. Now, right-click on the Arduino app, and select \'**Show Package Contents**\'. Either option should get you to this point.

[![Getting to the Arduino Libraries 2 ](https://cdn.sparkfun.com/assets/7/0/2/4/1/52af48da757b7f795e8b4567.jpg)](https://cdn.sparkfun.com/assets/7/0/2/4/1/52af48da757b7f795e8b4567.jpg)

Navigate through the following folders, \'**Contents -\> Resources -\> Java**\', until you reach the \'**libraries**\' folder.

**Note:** If you don\'t have a libraries folder, simply create one here in this location.

[![Arduino Libraries Path](https://cdn.sparkfun.com/assets/5/b/9/5/9/52af48da757b7f9b5e8b4567.jpg)](https://cdn.sparkfun.com/assets/5/b/9/5/9/52af48da757b7f9b5e8b4567.jpg)

Inside the libraries folder is where you want to copy/move the library folder you just downloaded and unzipped. You\'ll also notice this is where all the default libraries live as well as any other libraries you may have installed in the past.

[![Capacitive Sensor Library in Arduino Libraries Folder](https://cdn.sparkfun.com/assets/9/9/2/e/6/52af4db8757b7f0b388b4567.jpg)](https://cdn.sparkfun.com/assets/9/9/2/e/6/52af4db8757b7f0b388b4567.jpg)

**Note:** Arduino does not allow library folders to contain symbols such as hyphens ' - '. Arduino will throw an error upon starting up. If the library you are installing has a funky folder name then this step is the ideal time to clean it up.\
\

[![](http://cdn.sparkfun.com/assets/3/c/d/f/9/50f04a48ce395fe460000001.jpg "arduino error")](http://cdn.sparkfun.com/assets/3/c/d/f/9/50f04a48ce395fe460000001.jpg)

Next, make sure that restart the Arduino IDE if it was open when you installed the library. This is a very important, often overlooked step. If you don\'t restart, the library you just installed will not yet be available to the IDE.

To verify the library has been installed correctly, open up the \'**File \> Examples**\' folder under the Arduino IDE.

[![Capacitive Sense Library Installed](https://cdn.sparkfun.com/r/700-700/assets/2/f/c/4/9/52af4e11757b7f85238b4568.jpg)](https://cdn.sparkfun.com/assets/2/f/c/4/9/52af4e11757b7f85238b4568.jpg)

There it is! Let's open the example provided with our new library.

[![Example Capacitive Sensor Code](//cdn.sparkfun.com/assets/9/0/5/f/8/50f04a47ce395f0f5e000000.jpg)](//cdn.sparkfun.com/assets/9/0/5/f/8/50f04a47ce395f0f5e000000.jpg)

**Examples** are the greatest thing about libraries! Good libraries will have well written examples showing how to use the library. These sketches are wonderful resources for example code and learning how to write good code under Arduino.

You now have the Capacitive Sensor library installed! Feel free to start from the example sketch, or begin writing your own code using the functions provided by the library. A library usually has documentation either on its site or written into readme files and example code. In general, to quickly learn how to use a library check out the example code.