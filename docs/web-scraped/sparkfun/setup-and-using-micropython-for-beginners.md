# Source: https://learn.sparkfun.com/tutorials/setup-and-using-micropython-for-beginners

## Introduction

In this tutorial our goal is to help guide you through setting up and use MicroPython, a simple, yet effective implementation of Python 3 tailored for microcontrollers (MCUs) that are not running an OS. Thanks to its more direct method of coding, MicroPython makes programming embedded systems more accessible and enjoyable than ever. We\'ll walk you through the entire process, from flashing the firmware to running your first lines of code.

We will also go over Python running on single-board computers (SBCs) as an alternative to running MicroPython on SBCs.

Additionally, this entire guide is featured on GitHub, as well as instructions on how to setup [Linux](https://github.com/sparkfun/sparkfun-python/blob/main/docs/linux_setup.md) and [Qwiic](https://github.com/sparkfun/sparkfun-python/blob/main/docs/qwiic_setup.md) systems. If you would prefer to follow along there, click the button below!

[Setup and Using MicroPython GitHub Guide](https://github.com/sparkfun/sparkfun-python/blob/main/docs/mcu_setup.md)

## Setup and Using MicroPython on MCUs

In this first section, you\'ll learn the essential first steps: installing MicroPython firmware onto your specific MCU, with dedicated instructions for popular platforms like the RP2350, Teensy, ESP32 and more. From there, we\'ll explore several powerful development environments, including the command-line tool mpremote and full-featured IDEs like Thonny and PyCharm. By following along with our examples, you\'ll gain hands-on experience writing, uploading, and executing code, enabling you with the foundational skills to start building your own MicroPython projects.

### Supported Platforms

While there are a multitude of boards you can chose from, we will be focusing on the ones capable of working with the SparkFun Firmware Updater (we\'ll explain more on that in the next section). These boards include:

[![Teensy 4.1](https://cdn.sparkfun.com/r/140-140/assets/parts/1/5/6/6/3/16771-Teensy-4-1-Feature.jpg)](https://www.sparkfun.com/teensy-4-1.html)

### [Teensy 4.1](https://www.sparkfun.com/teensy-4-1.html) 

[ DEV-16771 ]

The Teensy 4.1 features an ARM Cortex-M7 processor at 600MHz, four times larger flash memory than the 4.0, and optional locat...

[ [\$31.50] ]

[![Teensy 4.0](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/1/8/9/15583-Teensy-4-0-Feature.jpg)](https://www.sparkfun.com/teensy-4-0.html)

### [Teensy 4.0](https://www.sparkfun.com/teensy-4-0.html) 

[ DEV-15583 ]

Teensy 4.0 is the latest Teensy, offering the fastest microcontroller and powerful peripherals in the Teensy 1.4 by 0.7 inch ...

[ [\$23.80] ]

[![SparkFun Experiential Robotics Platform (XRP) Controller](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/6/3/6/26619-XRP-Controller-Board-Feature.jpg)](https://www.sparkfun.com/sparkfun-experiential-robotics-platform-xrp-controller.html)

### [SparkFun Experiential Robotics Platform (XRP) Controller](https://www.sparkfun.com/sparkfun-experiential-robotics-platform-xrp-controller.html) 

[ ROB-26619 ]

The XRP Controller, driven by an RP2350 dual-core processor, serves as the brain of your XRP robot, enabling complex function...

[ [\$52.95] ]

[![SparkFun Pro Micro - RP2350](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/1/6/2/DEV-24870-Pro-Micro-RP2350-Feature.jpg)](https://www.sparkfun.com/sparkfun-pro-micro-rp2350.html)

### [SparkFun Pro Micro - RP2350](https://www.sparkfun.com/sparkfun-pro-micro-rp2350.html) 

[ DEV-24870 ]

The SparkFun RP2350 Pro Micro provides a powerful development platform in our compact Pro Micro form factor built around the...

[ [\$16.95] ]

[![SparkFun IoT RedBoard - ESP32 MicroPython Development Board](https://cdn.sparkfun.com/r/140-140/assets/parts/3/0/2/5/7/28434-Redboard-Iot-ESP32-Micropython-Feature.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-micropython-development-board.html)

### [SparkFun IoT RedBoard - ESP32 MicroPython Development Board](https://www.sparkfun.com/sparkfun-iot-redboard-esp32-micropython-development-board.html) 

[ WRL-28434 ]

The IoT RedBoard is an ESP32 WROOM-equipped development board with everything you need in an Arduino Uno with extra perks lik...

[ [\$29.95] ]

[![SparkFun Thing Plus - RP2040](https://cdn.sparkfun.com/r/140-140/assets/parts/1/6/8/7/0/17745-SparkFun_Thing_Plus_-_RP2040-01a.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-rp2040.html)

### [SparkFun Thing Plus - RP2040](https://www.sparkfun.com/sparkfun-thing-plus-rp2040.html) 

[ DEV-17745 ]

The SparkFun Thing Plus - RP2040 is a low-cost, high performance board with flexible digital interfaces featuring the Raspber...

[ [\$19.95] ]

[![SparkFun IoT RedBoard - RP2350](https://cdn.sparkfun.com/r/140-140/assets/parts/2/9/2/2/4/27708-Redboard-RP2350-Feature.jpg)](https://www.sparkfun.com/sparkfun-iot-redboard-rp2350.html)

### [SparkFun IoT RedBoard - RP2350](https://www.sparkfun.com/sparkfun-iot-redboard-rp2350.html) 

[ WRL-27708 ]

The RP2350 IoT RedBoard merges the RP2350 MCU and Raspberry Pi RM2 for wireless development in an Arduino R4 format.

[ [\$39.95] ]

[![SparkFun Thing Plus - RP2350](https://cdn.sparkfun.com/r/140-140/assets/parts/2/5/5/9/0/25134-Thing-Plus-RP2350-Feature.jpg)](https://www.sparkfun.com/sparkfun-thing-plus-rp2350.html)

### [SparkFun Thing Plus - RP2350](https://www.sparkfun.com/sparkfun-thing-plus-rp2350.html) 

[ WRL-25134 ]

The SparkFun RP2350 Thing Plus is a dynamic and powerful wireless development platform in the Thing Plus form factor.

[ [\$30.95] ]

[![SparkFun Pro Micro - RP2040](https://cdn.sparkfun.com/r/140-140/assets/parts/1/7/6/0/9/18288-SparkFun_Pro_Micro_-_RP2040-01.jpg)](https://www.sparkfun.com/sparkfun-pro-micro-rp2040.html)

### [SparkFun Pro Micro - RP2040](https://www.sparkfun.com/sparkfun-pro-micro-rp2040.html) 

[ DEV-18288 ]

The SparkFun Pro Micro RP2040 is a low-cost, high performance board with flexible digital interfaces featuring the Raspberry ...

[ [\$11.25] ]

[![SparkFun IoT Node for LoRaWAN®](https://cdn.sparkfun.com/r/140-140/assets/parts/2/6/8/8/3/26060-IoT-Node-LoRaWAN-Feature-new.jpg)](https://www.sparkfun.com/sparkfun-iot-node-lorawan.html)

### [SparkFun IoT Node for LoRaWAN®](https://www.sparkfun.com/sparkfun-iot-node-lorawan.html) 

[ WRL-26060 ]

The IoT Node brings an entirely new level of usability to the often convoluted and configuration intensive effort to setup a ...

[\$99.95] [ [\$49.95] ]

[![SparkFun Experiential Robotics Platform (XRP) Controller - Beta](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/4/3/2/22727-_01.jpg)](https://www.sparkfun.com/sparkfun-experiential-robotics-platform-xrp-controller-beta.html)

### [SparkFun Experiential Robotics Platform (XRP) Controller - Beta](https://www.sparkfun.com/sparkfun-experiential-robotics-platform-xrp-controller-beta.html) 

[ ROB-22727 ]

At the heart of the Experiential Robotics Platform (XRP) lies the powerful yet easy-to-use XRP Controller Board, the brains o...

[ [\$49.95] ]

And more to come\...

## Installing Firmware

### SparkFun Firmware Updater

The recommended way to install MicroPython firmware on a SparkFun board is with the [SparkFun MicroPython Firmware Updater](https://github.com/sparkfun/SparkFun_MicroPython_Firmware_Uploader). Follow the [instructions](https://github.com/sparkfun/SparkFun_MicroPython_Firmware_Uploader/blob/main/README.md) in that repository to download and install the correct firmware updater version for your computer. Then you can utilize the app to flash your board directly with the latest firmware from GitHub or a custom firmware file from another source. If you follow this route you can skip the platform-specific methods below.

You can also get our latest MicroPython firmware for your board from our directly from [MicroPython release page](https://github.com/sparkfun/micropython/releases) and flash with the dedicated method for your platform. Different platforms have different methods of flashing:

#### RP2 Boards

While connected to your computer, hold the \"boot\" button on the RP2 board while you press and release the \"reset\" button to enter bootloader mode. Your board will appear as a regular drive on your computer that you can add files to. Drag and drop the correct .uf2 file from the most recent release from the link above onto your board and it will reboot, now running MicroPython.

Connect to it with one of the [suggested development environments](https://learn.sparkfun.com/tutorials/setup-and-using-micropython-for-beginners#suggested-development-environments) below.

#### ESP32 Boards

Download the .zip archive for your board from the release link above and extract it. If you have not already, [download the esptool utility](https://docs.espressif.com/projects/esptool/en/latest/esp32/installation.html). Then, use esptool to flash your board using the command specified below. Make sure you run the command from within that directory as well. For example, one ESP32 release contains a `bootloader.bin`, `partition-table.bin`, `micropython.bin`, and `README.md`. By reading the `README.md` I see that the command I must run FROM WITHIN THIS EXTRACTED DIRECTORY is:

`python -m esptool --chip esp32 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 4MB --flash_freq 40m 0x1000 bootloader.bin 0x8000 partition-table.bin 0x10000 micropython.bin`

Connect to it with one of the [suggested development environments](https://learn.sparkfun.com/tutorials/setup-and-using-micropython-for-beginners#suggested-development-environments) below.

## Suggested Development Environments

### mpremote: MicroPython remote control

[mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html) is a command line utility that provides tons of options for interfacing with a MicroPython board. A simple way to use it is to execute it standalone with no options. If you have installed mpremote you can simply execute mpremote in a command line to get direct access to the Python REPL on your board. A useful way to navigate the file system from this repl is to execute import os and then use the os methods. For example, os.listdir() will show everything in the current directory on your MicroPython board. os.getcwd() will print the name of the current directory and os.chdir(\'dir_name\') will change the directory. An example of navigating around directories for a user who has installed the [mpy_tmp117_web_server](https://github.com/sparkfun/sparkfun-python/tree/main/examples/mpy_tmp117_web_server) demo from this repository can be seen below.

    C:\Users\qwiic_guy> mpremote

    Connected to MicroPython at COM14
    Use Ctrl-] or Ctrl-x to exit this shell
    MicroPython on SparkFun IoT RedBoard RP2350 with RP2350
    Type "help()" for more information.
    >>>
    >>>
    >>> import os
    >>> os.listdir()
    ['lib', 'static', 'tmp117_server_ap.py']
    >>> os.getcwd()
    '/'
    >>> os.chdir('static')
    >>> os.getcwd()
    '/static'
    >>> os.listdir()
    ['index.css', 'index.html', 'logo.png']

Once you have navigated to the directory containing the python script that you want to run, run it with the exec command:

    >>> exec(open('your_script.py').read())

Other MicroPython development environments like the IDE\'s below will also provide you with a REPL where you can directly execute MicroPython commands. So skills gained from navigating the REPL directly with `mpremote` will carry over into other environments.

To get files from your computer onto your micropython board you can use `mpremote cp` or install them directly from repositories that support mip installation with `mpremote mip install github:reponame` for example, to install our qwiic_i2c_py driver, execute:

    mpremote mip install github:sparkfun/qwiic_i2c_py

Let\'s walk through a quick example where we develop a program on a local code editor and then run it on a MicroPython board.

We can either develop our files first and then manually copy them over to our board (with `mpremote cp`) each time we want to test them, or we can \"mount\" a directory such that files are \"shared\" between the local file system and the MicroPython board.

Let\'s explore using [mpremote mount](https://docs.micropython.org/en/latest/reference/mpremote.html#mpremote-command-mount) to map a local directory onto our remote device. First create a new directory named `hello_world` and then open it in your code editor of choice. Now lets add our Python/MicroPython program. Add a file called `print_platform.py` to your hello_world directory. Paste the following code into the file:

    import sys

    print ("Hello from (Micro)Python! I am running on the following platform:", sys.platform)

The `sys` module exists both in Python and MicroPython so this code can run on both, and will let us know if we are successfully running it on an MCU. `sys.platform` will display your computer\'s OS if we interpret this program with a Python interpreter on your computer (for example on Windows it is `win32` and on linux it is `linux` or `linux2`). However, if we interpret/execute it via MicroPython on your MCU, it will be the MicroPython port representing your MCU (for example for RP2350 it is `rp2` and for ESP32 it is `esp32`).

Now, our local directory structure in our code editor should look like this:

[![Sublime Print Platform](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/4/sublime-print-platform.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/sublime-print-platform.png)

If we run `mpremote` and use `os.listdir` to list the current contents on my board, we see that it is empty:

    C:\Users\awesome_qwiic_user> mpremote
    Connected to MicroPython at COM14
    Use Ctrl-] or Ctrl-x to exit this shell

    >>> import os
    >>> os.listdir()
    []
    >>>

Now let\'s mount our directory. Issue `mpremote mount `. When we issue the command and again view the contents on our board, we see that our file has appeared!

[![mpremote Mount](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/mpremote-mount.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/mpremote-mount.png)

Notice that our file `print_platform.py` is now accessible to us from our MicroPython board and how we have automatically been moved into a directory called `/remote` on the remote device that maps to the local `hello_world` directory.

Now let\'s run our file using the same `exec(open('print_platform.py').read())` and see what happens.

    >>> exec(open('print_platform.py').read())
    Hello from (Micro)Python! I am running on the following platform: rp2

If all went well, we\'ll see our hello message and the name of an MCU platform (in this case RP2 for the RP2350).

You can add any number of files to the `hello_world` directory in a local code-editor, and modify them as you wish and the changes will be reflected \"on-the-fly\" in your mpremote session.

### Thonny

[Thonny](https://thonny.org/) is an IDE that provides a GUI environment with builtin support for MicroPython development. To get started, visit the [Thonny Downloads page](https://thonny.org/) and download the correct version for your operating system. Run the installation/setup program that you just downloaded for Thonny and click through each of the setup pages by accepting the default settings and pressing Next.

Connect your board that already has [MicroPython Firmware installed](https://learn.sparkfun.com/tutorials/setup-and-using-micropython-for-beginners#installing-firmware) to your computer and then configure your interpreter by clicking the bottom right-hand corner of Thonny. If your serial drivers are up to date and your board has proper MicroPython firmware installed, clicking this interpreter box should show several MicroPython options:

[![Thonny Board Select](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-board.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-board.png)

Select the version of MicroPython that makes the most sense for your board. Not sure? Select `MicroPython (generic)`.

This will connect to your board and show a Python REPL in the \"shell\" tab. To run a MicroPython program, open it from the `MicroPython device` tab. Then press the green arrow (Run Current Script). If you ever want to stop the running program, soft reset your board, or reconnect to your board, click the red stop sign (Stop/Restart backend).

Let\'s run the same Python example in Thonny as we did for mpremote. Once connected to your board, via the instructions above, ensure that the `View > Files` option is selected from the Toolbar:

[![Thonny View Files](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-view.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-view.png)

Now, in the `Files` tab, you should see two filel explorers, one called \"This computer\" for your local filesystem and one called \"MicroPython device\" representing the files on your board. Right click in the \"MicroPython device\" area and select `New file...`.

[![Thonny New File Select](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-new.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-new.png)

Lets call our new file `print_platform.py`. Let\'s copy and paste the same python code from the `mpremote` section above into our new file and save it. Now it should appear in our `Files > MicroPython device` tab:

[![A Thonny File](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/4/thonny-file.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-file.png)

Finally, let\'s click on the green `Run current script` button and in the `Shell` tab we should see the expected print with a platform that matches the MCU of our MicroPython board:

[![Thonny Run Current Script](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-run.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-run.png)

[![Thonny Shell](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/4/thonny-shell.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/thonny-shell.png)

Remember that you can also still use the REPL directly from the `Shell` tab and execute MicroPython commands on your board just as if you were using `mpremote`.

### PyCharm

[PyCharm](https://www.jetbrains.com/pycharm/) is a popular and modern Python IDE with plugin support for interfacing with MicroPython boards. PyCharm Professional is a paid version, but we suggest installing the free community version. To get started, visit the [PyCharm Downloads Page]() and scroll down until you see the \"PyCharm Community Addition\" section and click the `Download` button. Open the setup executable that you downloaded and configure your installation. We suggest accepting the default installation folder and adding the Desktop Shortcut and Context Menu.

[![PyCharm Install](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pycharm-install.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pycharm-install.png)

Once your install is complete, open PyCharm. Skip any import settings that pop up when you open it for the first time.

Navigate to Plugins and in the \"Marketplace\" tab search for \"MicroPython Tools\".

**Note:** This is a third-party plugin with no explicit support or maintenance from Jetbrain or SparkFun. Older versions of PyCharm contain a JetBrains-supported plugin called simply \"MicroPython\" but they no longer update it and it cannot run on the latest PyCharm versions.

[![MicroPython Tools](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/4/micropython-tools.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/micropython-tools.png)

After installing the plugin, restart your IDE. Then, select the gear icon and choose \"Settings\" then navigate to Languages & Frameworks and select `MicroPython Tools`.

[![PyCharm Framework](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pycharm-framework.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pycharm-framework.png)

Select `Enable MicroPython support` and leave the other defaults checked. SparkFun is in the process of getting stubs for SparkFun MicroPython boards added to the official repository, but in the meantime in the `stubs package` field, choose a generic MicroPython stubs package corresponding to your MCU. For an RP2350 or RP2040 board, we suggest the most recent version of `micropython-rp2-stubs_x.xx.x`. For ESP32 boards, we suggest the most recent version of `micropython-esp32-stubs_x.xx.x`. These stubs packages simply provide useful code-completion, highlighting, and warnings for MicroPython development.

[![PC MicroPython Settings](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-mp-settings.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-mp-settings.png)

A good starting place for the use of this plugin is the [MicroPython Tools README](https://github.com/lukaskremla/micropython-tools-jetbrains/blob/main/README.md). Let\'s create our first project. Click the \"+\" sign or select `file > New Project...` to create a new project. Let\'s name our project \"hello_world\" and accept the default interpreter/environment:

[![PyCharm New Project](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/4/pycharm-new-project.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pycharm-new-project.png)

When our new project first opens up, it has our `hello_world` directory as well as several components like `.venv` and `External Libraries` that are helpful when doing regular Python Development.

[![PC Start Directory](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-start-dir.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-start-dir.png)

But we are anything but regular. We will be using the MicroPython running on our MCU to interpret our code, not a Python interpreter installed on your computer. So you can mostly disregard these files.

Now, right click the `hello_world` directory and select `Mark Directory as > MicroPython Sources Root`. The MicroPython Tools plugin will now map this `hello_world` directory that exists on our computer to the root file system of our MicroPython board when we perform upload commands.

[![PC Sources Root](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-sources-root.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-sources-root.png)

Now lets add our MicroPython program. Right click the `hello_world` directory and select `new > Python File` and add a file called `print_platform.py`. Paste the following code into the file:

    import sys

    print ("Hello from (Micro)Python! I am running on the following platform:", sys.platform)

This is the same code as is discussed in the [mpremote](https://learn.sparkfun.com/tutorials/setup-and-using-micropython-for-beginners#installing-firmware) section.

Now lets configure an upload command and a run command. At the top of PyCharm next to the execute and debug buttons, select `Current File > Edit Configurations`:

[![Edit Configurations](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/edit-configurations.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/edit-configurations.png)

In the Run/Debug Configurations window that pops up, select the \"+\" sign and then select `MicoPython Tools > Upload Project`. Check the boxes for `Reset on success`, `Switch to REPL tab on success`. Then, click `Apply`.

[![PC Upload Project](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/4/pc-upload-project.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-upload-project.png)

While we\'re at it, lets create an execute command. Again, click the \"+\" sign and select `MicroPython Tools > Execute`. Input the path to our print_platform.py file we have created and check the box for `Switch to REPL tab on success`. Click `Apply` and finally `OK` to save our upload and execute commands.

[![PC Execute](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/3/8/0/4/pc-execute.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-execute.png)

The upload command will take the directory that is configured as `MicroPython Sources Root` (in our case the hello_world directory) and load that onto the root directory of our MicroPython connected board. The execute command will run whatever file we have selected from the local computer\'s file system and run it on our board (without explicitly uploading it to the device).

Now, let\'s connect to our device! Plug in your board that already has [MicroPython Firmware installed](https://learn.sparkfun.com/tutorials/setup-and-using-micropython-for-beginners#installing-firmware) and then in the bottom-left of PyCharm, select the MicroPython Tools extension. Select the correct COM port for your board. And then click the plug symbol to connect.

[![PC Connect](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-connect.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-connect.png)

Now that we are connected, let\'s upload our program. Select our upload configuration from the drop-down at the top of PyCharm and then click the green `Run` arrow.

[![PC Run Upload](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-run-upload.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-run-upload.png)

Select the `File System` tab in the MicroPython tools extension tab and we should now see `print_platform.py` file uploaded to the device!

[![PC File System](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-file-system.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-file-system.png)

Finally, let\'s select our execute configuration and run it as well.

[![PC Run Execute](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-run-execute.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-run-execute.png)

If all goes well, you should see a hello statement printed in the REPL tab of the MicroPython Tools extension. The platform printed should match the MCU of your board and not be your computer\'s operating system.

[![PC Running Smoothly](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-run.png)](https://cdn.sparkfun.com/assets/learn_tutorials/3/8/0/4/pc-run.png)

**Some Things to Note:**

The execute job we configured uses the version of the file currently in our local `hello_world` directory and runs it directly without uploading it. The upload step is helpful however if we have multiple files that we want to upload at once, for example if the file we are actually running relies on other files.

Drag and drop is supported by this extension, such that you can simply drag files from the project explorer on the left of PyCharm to the `File System` tab of the extension to copy files from your local computer to your MicroPython board.

Another alternative to explicitly using an upload configuration is to select a file from the PyCharm project explorer and right click it and select either `Execute file in MicroPython REPL` or `Upload file to MicroPython device`.

Remember that you can still use the REPL directly from the `REPL` tab and execute MicroPython commands on your board just as if you were using `mpremote`.

### Other Tools

- [VSCode with MicroPico Extension](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go): If you happen to be developing on a Raspberry Pi pico platform, this offers a similar experience to Thonny and PyCharm.
- [Arduino Lab For MicroPython](https://labs.arduino.cc/en/labs/micropython): Offers a simple IDE for MicroPython development with a similar look and feel to Arduino IDE.

## Using Python on Linux

Alternatively, you can use Python on Linux-based, single-board computers (SBCs)!

This next section of the tutorial focuses on on just that, getting you up and running on the Raspberry Pi and NVIDIA Jetson Orin Nano. We\'ll walk you through the entire setup process, starting with the initial hardware configuration. This includes preparing your SBC\'s operating system and safely connecting your Qwiic devices then we\'ll dive into the software installation, where you\'ll learn how to create a clean Python virtual environment (`venv`) and install the core `qwiic_i2c library`. By the end of this tutorial, you\'ll have a fully configured system, ready to install any of our Qwiic Python drivers and start bringing your projects to life.

### Supported Platforms

We carry plenty of linux-based SBCs in our catalog, but for the intents and purposes of this section of our tutorial, we\'ll be focusing on Raspberry Pi 5 line and the NVIDIA Jetson Orin Nano via the [SparkFun Qwiic SHIM](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html) and/or [Qwiic Cable](https://www.sparkfun.com/flexible-qwiic-cable-female-jumper-4-pin.html). These boards include:

[![NVIDIA Jetson Orin™ Nano Super Developer Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/2/1/9/6/0/Jetson-Orin-Nano-Feature.jpg)](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html)

### [NVIDIA Jetson Orin™ Nano Super Developer Kit](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html) 

[ DEV-22098 ]

The NVIDIA® Jetson OrinTM Nano comprises of a Jetson Orin Nano 8GB module and a carrier board that can accommodate all Orin...

[ [\$249.00] ]

[![SparkFun Qwiic Cable Kit](https://cdn.sparkfun.com/r/140-140/assets/parts/1/3/4/3/1/15081-_01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html)

### [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/sparkfun-qwiic-cable-kit.html) 

[ KIT-15081 ]

To make it even easier to get started, we\'ve assembled this Qwiic Cable Kit with a variety of Qwiic cables from 50mm to 500mm...

[ [\$12.95] ]

[![Raspberry Pi 5 - 16GB](https://cdn.sparkfun.com/r/140-140/assets/parts/2/8/6/0/3/DEV-27446-Raspberry-Pi-5-16GB-Feature.jpg)](https://www.sparkfun.com/raspberry-pi-5-16gb.html)

### [Raspberry Pi 5 - 16GB](https://www.sparkfun.com/raspberry-pi-5-16gb.html) 

[ DEV-27446 ]

The next iteration of the Raspberry Pi single board computer featuring a 64-bit quad-core Arm Cortex-A76 processor running at...

[ [\$150.00] ]

[![Raspberry Pi 5 - 8GB](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/8/4/2/23551-Raspberry-Pi-5-8G-feature.jpg)](https://www.sparkfun.com/raspberry-pi-5-8gb.html)

### [Raspberry Pi 5 - 8GB](https://www.sparkfun.com/raspberry-pi-5-8gb.html) 

[ DEV-23551 ]

The next iteration of the Raspberry Pi single board computer featuring a 64-bit quad-core Arm Cortex-A76 processor running at...

[ [\$100.00] ]

[![Raspberry Pi 5 - 4GB](https://cdn.sparkfun.com/r/140-140/assets/parts/2/3/8/4/1/23550-Raspberry-Pi-5-4G-feature.jpg)](https://www.sparkfun.com/raspberry-pi-5-4gb.html)

### [Raspberry Pi 5 - 4GB](https://www.sparkfun.com/raspberry-pi-5-4gb.html) 

[ DEV-23550 ]

The next iteration of the Raspberry Pi single board computer featuring a 64-bit quad-core Arm Cortex-A76 processor running at...

[ [\$75.00] ]

[![Raspberry Pi 5 - 2GB](https://cdn.sparkfun.com/r/140-140/assets/parts/2/7/0/4/3/DEV-26125-Raspberry-Pi-5-2G-Feature2.jpg)](https://www.sparkfun.com/raspberry-pi-5-2gb.html)

### [Raspberry Pi 5 - 2GB](https://www.sparkfun.com/raspberry-pi-5-2gb.html) 

[ DEV-26125 ]

The next iteration of the Raspberry Pi single board computer featuring a 64-bit quad-core Arm Cortex-A76 processor running at...

[ [\$60.00] ]

[![SparkFun Qwiic SHIM for Raspberry Pi](https://cdn.sparkfun.com/r/140-140/assets/parts/1/4/3/9/9/16385-15794-SparkFun_Qwiic_SHIM_for_Raspberry_Pi-01.jpg)](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html)

### [SparkFun Qwiic SHIM for Raspberry Pi](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html) 

[ DEV-15794 ]

The SparkFun Qwiic SHIM for Raspberry Pi is a small, easily removable breakout that easily adds a Qwiic connector to your Ras...

[ [\$1.95] ]

## SBC Setup

### Raspberry Pi Setup

Follow the [instructions here](https://www.raspberrypi.com/software/operating-systems/) to to download a Raspberry PI OS image. It is expected that most/all RaspberryPi OS versions will work with our Qwiic I^2^C drivers, but testing was done with Kernel v6.6, Debian GNU/Linux 12 (bookworm). Image an SD card with your favorite SD card imager, we recommend the [Raspberry Pi Imager](https://www.raspberrypi.com/software/).

### Jetson Orin Nano Setup

Follow the [in-depth instructions here](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#intro) to set up your Jetson Orin Nano Developer kit with a JetPack 6.2 (or higher) Linux image.

### Qwiic Shim or Qwiic Cable Female Jumper Setup

On either of the above platforms, a pysical hardware interface is required to connect the I^2^C pins of the board to a qwiic connector on a qwiic device. Connect a [Qwiic Shim](https://www.sparkfun.com/sparkfun-qwiic-shim-for-raspberry-pi.html) or a [Qwiic Cable Female Jumper](https://www.sparkfun.com/flexible-qwiic-cable-female-jumper-4-pin.html) to your board, making sure to connect the correct pins for PWR, GND, SDA, and SCL. See the [instructions here](https://learn.sparkfun.com/tutorials/qwiic-shim-for-raspberry-pi-hookup-guide) for more information. Then connect a qwiic cable to your SparkFun Qwiic Device.

**Warning:** IMPROPER ORIENTATION OF A QWIIC SHIM CAN SHORT POWER TO GROUND, DAMAGING YOUR BOARD!

## SBC Python Installation

You can install the [qwiic_i2c_py](https://github.com/sparkfun/Qwiic_I2C_Py) package to get Qwiic I^2^C support for your board. Also check out our comprehensive [qwiic_py](https://github.com/sparkfun/Qwiic_Py) repository.

The qwiic_i2c_py package is primarily installed using the `pip3` command, downloading the package from the Python Index - \"PyPi\".

First, setup a virtual environment from a specific directory using venv:

    python3 -m venv ~/sparkfun_venv

You can pass any path instead of \~/sparkfun_venv, just make sure you use the same one for all future steps. For more information on venv [click here](https://docs.python.org/3/library/venv.html).

Next, install the qwiic package with:

    ~/sparkfun_venv/bin/pip3 install sparkfun-qwiic-i2c

Now you should be able to run any example or custom python scripts that have `import qwiic_i2c` by running e.g.:

    ~/sparkfun_venv/bin/python3 example_script.py

To get started with any of the Qwiic Drivers, check out our list of Qwiic Python Driver Repos below and follow the device-specific \"PyPi Installation\" instructions in your device\'s repository.

As an alternative to pip, at you could also manually clone/download the qwiic_i2c_py repository and the repository for your desired driver and then utilize the qwiic files directly.