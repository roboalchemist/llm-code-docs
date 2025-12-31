# Source: https://learn.sparkfun.com/tutorials/artemis-development-on-arm-mbed-os-beta

## Get a Jump on the Release

With the latest Artemis DK, board, we now offer full Bluetooth support within the Arduino IDE and development with [Arm® Mbed™ OS](https://os.mbed.com/mbed-os). While we have worked tirelessly to get the Artemis module supported in the next Mbed™ OS release, the next release isn\'t slated until after the Artemis DK becomes available to the public. Therefore, this post will provide users with a jump start for developing with Mbed™ Studio, prior to the next release (in a *beta* of sorts), by utilizing our fork of Mbed™ OS.

[![mbed os logo](https://cdn.sparkfun.com/r/500-500/assets/home_page_posts/3/3/7/7/mbedos-logo.png)](https://os.mbed.com/mbed-os)

In case you missed it, check out our livestream demonstration with the Mbed™ team:

*Users may need to watch the video on [YouTube](https://youtu.be/o3ffhf3z6so).*

## Clone the Fork

Users will first need to clone our fork of Mbed™ OS from the `ambiq-apollo3-dev` branch of the [GitHub repository](https://github.com/sparkfun/mbed-os-ambiq-apollo3/tree/ambiq-apollo3-dev). Feel free to use the method you are most familiar with.

**Note:** For users who need a little more direction, [install the GitHub desktop application](https://desktop.github.com/) and [register a GitHub account](https://github.com/join?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home). Once an account has been created and the application has been installed, open the application and log in.

From the GitHub desktop application, clone the `sparkfun/mbed-os-ambiq-apollo3` repository (*please note the location of the repository on the computer, it will be utilized later.*). Once the repository has been cloned, pull the `ambiq-apollo3-dev` branch.

[![cloning the fork](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/7/clone_mbed_os.gif)](https://cdn.sparkfun.com/assets/learn_tutorials/1/2/9/7/clone_mbed_os.gif)

*Cloning the our fork of Mbed™ OS from the `ambiq-apollo3-dev` branch of the [GitHub repository](https://github.com/sparkfun/mbed-os-ambiq-apollo3/tree/ambiq-apollo3-dev) with the [GitHub desktop application](https://desktop.github.com/). (Click to enlarge)*

## Install Mbed™ Studio

Users should install the latest version of Mbed™ Studio. Installation instructions can be found [here on the Mbed™ website](https://os.mbed.com/docs/mbed-studio/current/installing/installing-mbed-studio.html). Documentation for Mbed™ Studio is also hosted on the [Mbed™ website](https://os.mbed.com/docs/mbed-studio/current/introduction/index.html).

[Go to Installation Instructions](https://os.mbed.com/docs/mbed-studio/current/installing/installing-mbed-studio.html)

## Project Setup

Once users have installed Mbed™ Studio, the fun begins! First, open Mbed™ Studio and create a new project.

- From the menu, select **File** \> **New Program**\....
  - A New program dialog box should open.

    ::: 
    [![dialog box](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/NewProgram.PNG)](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/NewProgram.PNG)
    :::

    ::: 
    *A screenshot of dialog box.*
    :::
- To begin with the **Blinky** example, from the **Example program** drop-down list, select in the MBED OS 6 list:
  - For the Mbed OS full profile: `mbed-os-example-blinky`

    ::: 
    [![select program](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/SelectBlinky.gif)](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/SelectBlinky.gif)
    :::

    ::: 
    *Selecting the **Blinky** example.*
    :::
- For the **Mbed™ OS Location**, select the \"Link to an existing shared Mbed™ OS instance\" option.
  - Browse for the location noted earlier, to the `ambiq-apollo3-dev` branch of our fork of Mbed™ OS.

    ::: 
    [![link port](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/MbedLocation.gif)](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/MbedLocation.gif)
    :::

    ::: 
    *Setting the Mbed™ OS Location.*
    :::
- Click **Add Program**.
  - The program is loaded to your workspace and is the active program.

## Configure Build Target and Profile

A build target tells Mbed™ Studio how to build Mbed™ OS so that it matches your hardware.

The options for selecting a target are:

- Connect your board to your computer. Mbed Studio will detect the board and suggest a matching target.
- Use the **Target** drop-down list.
  - Click the Manage Custom Target icon.
    - Select the **USB device**
    - Select the **Build target**
      - Name that matches the Artemis board you are using.

[![manage custom target](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/SelectTargetMenu.gif)](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/SelectTargetMenu.gif)\
*Click the Manage Custom Target icon.*

[![configuring settings](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/SelectTarget.gif)](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/SelectTarget.gif)\
*Selecting the custom target options.*

## Programming the Artemis DK

This method will be utilized for an Artemis board with a DAPLink interface chip, like the Artemis DK. The process requires building the project in Mbed™ Studio. Once the `.bin` file is generated, Mbed™ Studio automatically loads the file onto the mass storage device for the board to program the Artemis module.

- With board connected, click the [Build and Run], play icon. This builds the **Blinky** example and flashes it to the connected board. (*You may need to restart your board for the code to run.*)

[![programming target](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/BuildAndRun.gif)](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/BuildAndRun.gif)

## Start Something

Now its time to make your own project! If you want a starting point for some more examples check out the [Mbed API](https://os.mbed.com/docs/mbed-os/v6.2/apis/index.html) or try out some of the [BLE examples](https://github.com/armmbed/mbed-os-example-ble).

[![start something](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/start_something.gif)](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/start_something.gif)

## Build and Flashing other Artemis Boards

Development boards that utilize a WCH CH340C or CH340C Uart-to-serial chip will be programmed using the Ambiq Secure Bootloader (ASB). However, users will need to build the project, first, to utilize the required `.bin` file.

### Build Project

- Click the [Build], hammer icon. This builds Blinky and stops.
- Check the build output for the location of the `.bin` file.

[![file location](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/BuildOutput.gif)](https://cdn.sparkfun.com/assets/home_page_posts/3/3/7/7/BuildOutput.gif)

### ASB Upload

- [Ambiq Secure Bootloader (ASB) documentation](https://github.com/sparkfun/Apollo3_Uploader_ASB)

  - Example usage:

    `python asb.py --bin "$.bin" --load-address-blob 0x20000 --magic-num 0xCB -o "$" --version 0x0 --load-address-wired 0xC000 -i 6 --options 0x1 -b 115200 -port "" -r 2 -v`