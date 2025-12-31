# Source: https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison

## Introduction

[libmraa](https://github.com/intel-iot-devkit/mraa) contains helpful bindings for addressing hardware on Intel [Galileo](https://www.sparkfun.com/products/13096) and [Edison](https://www.sparkfun.com/categories/272) that work in a variety of languages. In this tutorial we will use a python script to make an LED blink. You will need an [Intel Edison](https://www.sparkfun.com/products/13024), a way to connect to it (e.g. a [Base Block](https://www.sparkfun.com/products/13045)), and access to some GPIO pins (e.g. a [GPIO Block](https://www.sparkfun.com/products/13038)).

### Prerequisites

You need to have [Ubilinux](http://www.emutexlabs.com/ubilinux), a version of Debian, running on your Edison. You can do that by following [this tutorial](https://learn.sparkfun.com/tutorials/loading-debian-ubilinux-on-the-edison).

[![Blinking an LED using mraa on Ubilinux](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/6/mraa_on_Ubilinux_06.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/mraa_on_Ubilinux_06.jpg)

### Suggested Reading

- [Edison Getting Started Guide](https://learn.sparkfun.com/tutorials/edison-getting-started-guide)
- [Loading Debian (Ubilinux) on the Edison](https://learn.sparkfun.com/tutorials/loading-debian-ubilinux-on-the-edison)
- [General Guide to SparkFun Blocks for Intel Edison](https://learn.sparkfun.com/tutorials/general-guide-to-sparkfun-blocks-for-intel-edison)
- [Edison Console Block Guide](https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---console-block)
- [Edison GPIO Block Guide](https://learn.sparkfun.com/tutorials/sparkfun-blocks-for-intel-edison---gpio-block)

## The Circuit

The first thing to do is connect up the LED. For this tutorial, we used an [Intel Edison](https://www.sparkfun.com/products/13024), a [Base Block](https://www.sparkfun.com/products/13045), and a [GPIO Block](https://www.sparkfun.com/products/13038). You can also use the [Console Block](https://www.sparkfun.com/products/13039), [Mini Breakout Board](https://www.sparkfun.com/products/13025), or [Arduino Breakout Board](https://www.sparkfun.com/products/13097).

### Parts List

In addition to the Edison and breakout board(s), you will need some basic components. Below is the list of components used in this tutorial. Note that from the resistor kit, we used a 1 kΩ and 220 Ω resistor.

\

### Schematic

Unless you are using the Edison Arduino Breakout board, the Edison cannot supply enough current to fully (and safely) light an LED. As a result, we need to make a basic switch using a [BJT transistor](http://en.wikipedia.org/wiki/Bipolar_junction_transistor).

[![Connecting an LED to Edison](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/6/libmraa_blinky.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/libmraa_blinky.png)

**Note:** If you are using the Arduino Breakout Board, you do not need to use this circuit, as the Arduino board can provide enough current. You will want to use the pin labeled A0, as noted in Table 3 of the [Arduino Breakout Hardware Guide](https://communities.intel.com/docs/DOC-23161).

**Also Note:** if you are using the Mini Breakout Board, you will want to use GP44 (J19, pin 4) according to the [Breakout Board Hardware Guide](https://communities.intel.com/docs/DOC-23252).

### Connections

Connect your LED circuit to the GPIO Block as shown.

[![View of the GPIO Block connected to the LED circuit](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/6/mraa_on_Ubilinux_05.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/mraa_on_Ubilinux_05.jpg)

- 220 Ω Resistor (Pin 2) → LED (Anode)
- 2N3904 (Collector) → LED (Cathode)
- 2N3904 (Base) → 1 kΩ Resistor (Pin 2)
- GPIO Block (GND) → 2N3904 (Emitter)
- GPIO Block (VSYS) → 220 Ω Resistor (Pin 1)
- GPIO Block (GP44) → 1 kΩ Resistor (Pin 1)

**Important:** Note the direction of the LED and transistor! In the photo, the flat edge of the LED is pointing down (towards the transistor), and the flat edge of the transistor is pointing to the right (towards the resistors).

## Install Libraries

### Install Dependencies

We\'ll be using Debian\'s [Advanced Package Manager](https://wiki.debian.org/Apt) to install the dependencies needed for libmraa. Log in as root (or use \"su\" or \"sudo\") on your Edison and type:

    apt-get update

*apt-get update* will update your local cache of all currently available packages in the repository.

The first dependency of this install is the [PCRE](http://www.pcre.org/) development files.

    apt-cache search pcre

*apt-cache search* does just what it sounds like \-- searches apt packages. Look through the list and you should see:

    libpcre3-dev - Perl 5 Compatible Regular Expression Library - development files

Looks like the right thing.

    apt-get install libpcre3-dev

Now that we are familiar with installing packages from apt, let\'s get everything else we need for the build:

    apt-get install git
    apt-get install cmake
    apt-get install python-dev
    apt-get install swig

### Build and Install mraa

libmraa is not in apt so we\'ll have to compile it from source. Don\'t worry, it\'s easy:

    git clone https://github.com/intel-iot-devkit/mraa.git
    mkdir mraa/build && cd $_
    cmake .. -DBUILDSWIGNODE=OFF
    make
    make install
    cd

**Important:** Make sure you run the final command, \"make install\" with root or \"sudo.\"

That `DBUILDSWIGNODE` flag turns off node.js support, which isn\'t available in the version of swig in apt. If you need node.js, you can compile a [newer version of swig from source (3.01+)](http://www.swig.org/download.html).

### Update Shared Library Cache

To use the library in C or C++ programs, we need to add it to our shared library cache. With root (or using \"sudo\"), open up the ld.so.conf file:

    nano /etc/ld.so.conf

Scroll down to the bottom of the file and add:

    /usr/local/lib/i386-linux-gnu/

Your ld.so.conf file should look like this:

[![Appending library location in ld.so.conf](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/appending_ld_file.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/appending_ld_file.png)

Save and exit (\'Crtl-x\' and \'y\' with nano). Type the command (using root or \"sudo\"):

    ldconfig

You can check to make sure that the cache was updated by typing the command:

    ldconfig -p | grep mraa

You should see that the libraries have been included in the cache.

[![Verifying that libmraa was added to the cache](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/verifying_ldconfig.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/verifying_ldconfig.png)

### Export Library Path for Python

If you plan to use Python with mraa, you will need to export its location to the Python path. Enter the command:

    export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))

Note that this command lets us use the mraa module for this terminal session only. If we restart the Edison, we will have to retype the command.

**Optional:** You can modify the .bashrc file to run the commands automatically every time the Edison starts. Open the .bashrc file with your favorite editor. For example:

    nano ~/.bashrc

Scroll all the way down to the bottom of the file, and add the command from above in a new line.

    export PYTHONPATH=$PYTHONPATH:$(dirname $(find /usr/local -name mraa.py))

The bottom of your .bashrc file should look like the screenshot below.

[![Appending export command in .bashrc](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/appending_bashrc.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/appending_bashrc.png)

Save and exit (\'Crtl-x\' and \'y\' with nano).

### Updating Sudoers File

This part is also **optional**. If you installed [sudo](http://www.sudo.ws/), you might notice that PYTHONPATH is not updated properly when you try to run a Python script with \"sudo.\" For example, you might get an error like \"ImportError: No module named mraa.\"

Open up the sudoers file:

    sudo visudo

Right under the first \"Defaults\" line, add the following:

    Defaults        env_keep += PYTHONPATH

Your sudoers file should look like the screenshot below.

[![Adding PYTHONPATH to the sudoers file](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/adding_pythonpath_to_sudoers.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/adding_pythonpath_to_sudoers.png)

Save and exit (\'Crtl-x\' and \'y\' with nano). Reboot your Edison for this to take effect.

## Blink an LED

### Using C

If you want to use C, create a file with your favority text editor:

    nano blink.c

Copy the following code into that file:

    language:c
    /* Blinky test using mraa */

    #include <stdio.h>
    #include <unistd.h>
    #include <errno.h>
    #include <signal.h>
    #include <stdlib.h>

    #include "mraa.h"

    #define LED_PIN 31

    int running = 0;

    void sig_handler(int signo)
    
    }

    int main()
    

        /* Set GPIO direction to out */
        r = mraa_gpio_dir(gpio, MRAA_GPIO_OUT);
        if ( r != MRAA_SUCCESS ) 

        /* Create signal handler so we can exit gracefully */
        signal(SIGINT, sig_handler);

        /* Turn LED off and on forever until SIGINT (Ctrl+c) */
        while ( running == 0 ) 
            sleep(1);

            r = mraa_gpio_write(gpio, 1);
            if ( r != MRAA_SUCCESS ) 
            sleep(1);
        }

        /* Clean up GPIO and exit */
        r = mraa_gpio_close(gpio);
        if ( r != MRAA_SUCCESS ) 

        return r;
    }

Save and exit the file (\'Crtl-X\' and \'y\' for nano). Compile the program with:

    gcc blink.c -o blink -lmraa

Note the \"-lmraa\" that tells the compiler to include the mraa library. Run the program by typing:

    ./blink

**Important:** You need to run blink as root! If you get an error such as "Invalid GPIO pin specified" or \"FATAL error, libmraa program must be run as root (EUID 0), cannot proceed\" it means that you do not have permissions to modify GPIO. Either switch to root using the "su" command or run the command with "sudo" (if you have "sudo" installed).

You should see your LED start turning on and off!

### Using Python

For Python, use your favorite text editor to create this simple script, called something like blink.py. For example:

    nano blink.py

In that file, enter the following:

    language:python
    import mraa
    import time

    # Setup
    x = mraa.Gpio(31)
    x.dir(mraa.DIR_OUT)

    # Loop
    while True:
        x.write(1)
        time.sleep(0.5)
        x.write(0)
        time.sleep(0.5)

Save and exit the file (if you are using nano, press \'Crtl-X\' and \'y\').

Run it with:

    python blink.py

**Important:** You need to run blink.py as root! If you get an error such as \"ValueError: Invalid GPIO pin specified\" it means that you do not have permissions to modify GPIO. Either switch to root using the \"su\" command or run the command with \"sudo\" (if you have \"sudo\" installed).

[![Blinking an LED with Debian on Edison](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/3/6/mraa_on_Ubilinux_07.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/3/3/6/mraa_on_Ubilinux_07.jpg)

*Probably not the first time you\'ve made an LED blink, but maybe the first time in python on Debian!*

### Pin Map

You might have noticed that we used GP44 in hardware and GPIO 31 in our example code. This is because the mraa library uses a different number for the pins. If you would like to use mraa to control hardware, figure out which GPIO pins you plan to use on the table below (labeled \"Edison Pin\") and then use the MRAA Number in software.

Note that the \"Edison Pin\" numbers are the same GPIO pin numbers found on Linux in the Edison. They are also listed on the GPIO Block. The \"Pinmode\" allows you to change the function of each pin.

**Notes:**

- Input/output voltage on the GPIO Block is 3.3V by default
- Input/output voltage on the Arduino Breakout is 5V
- Input/output voltage on the Mini Breadboard is 1.8V

*MRAA pin map table based on [Intel\'s IOT Dev Kit Repository](https://github.com/intel-iot-devkit/mraa/blob/master/docs/edison.md)*

  Edison Pin (Linux)   Arduino Breakout   Mini Breakout     MRAA Number Pinmode0   Pinmode1     Pinmode2
  -------------------- ------------------ --------------- ------------- ---------- ------------ ----------
  GP12                 3                  J18-7                      20 GPIO-12    PWM0         
  GP13                 5                  J18-1                      14 GPIO-13    PWM1         
  GP14                 A4                 J19-9                      36 GPIO-14                 
  GP15                                    J20-7                      48 GPIO-15                 
  GP19                                    J18-6                      19 GPIO-19    I2C-1-SCL    
  GP20                                    J17-8                       7 GPIO-20    I2C-1-SDA    
  GP27                                    J17-7                       6 GPIO-27    I2C-6-SCL    
  GP28                                    J17-9                       8 GPIO-28    I2C-6-SDA    
  GP40                 13                 J19-10                     37 GPIO-40    SSP2_CLK     
  GP41                 10                 J20-10                     51 GPIO-41    SSP2_FS      
  GP42                 12                 J20-9                      50 GPIO-42    SSP2_RXD     
  GP43                 11                 J19-11                     38 GPIO-43    SSP2_TXD     
  GP44                 A0                 J19-4                      31 GPIO-44                 
  GP45                 A1                 J20-4                      45 GPIO-45                 
  GP46                 A2                 J19-5                      32 GPIO-46                 
  GP47                 A3                 J20-5                      46 GPIO-47                 
  GP48                 7                  J19-6                      33 GPIO-48                 
  GP49                 8                  J20-6                      47 GPIO-49                 
  GP77                                    J19-12                     39 GPIO-77    SD           
  GP78                                    J20-11                     52 GPIO-78    SD           
  GP79                                    J20-12                     53 GPIO-79    SD           
  GP80                                    J20-13                     54 GPIO-80    SD           
  GP81                                    J20-14                     55 GPIO-81    SD           
  GP82                                    J19-13                     40 GPIO-82    SD           
  GP83                                    J19-14                     41 GPIO-83    SD           
  GP84                                    J20-8                      49 GPIO-84    SD           
  GP109                                   J17-11                     10 GPIO-109   SPI-5-SCK    
  GP110                                   J18-10                     23 GPIO-110   SPI-5-CS0    
  GP111                                   J17-10                      9 GPIO-111   SPI-5-CS1    
  GP114                                   J18-11                     24 GPIO-114   SPI-5-MISO   
  GP115                                   J17-12                     11 GPIO-115   SPI-5-MOSI   
  GP128                2                  J17-14                     13 GPIO-128   UART-1-CTS   
  GP129                4                  J18-12                     25 GPIO-129   UART-1-RTS   
  GP130                0                  J18-13                     26 GPIO-130   UART-1-RX    
  GP131                1                  J19-8                      35 GPIO-131   UART-1-TX    
  GP134                                   J20-3                      44                         
  GP135                                   J17-5                       4 GPIO-135   UART         
  GP165                A5                 J18-2                      15 GPIO-165                
  GP182                6                  J17-1                       0 GPIO-182   PWM2         
  GP183                9                  J18-8                      21 GPIO-183   PWM3