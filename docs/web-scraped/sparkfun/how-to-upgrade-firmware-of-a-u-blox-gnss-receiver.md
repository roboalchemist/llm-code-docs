# Source: https://learn.sparkfun.com/tutorials/how-to-upgrade-firmware-of-a-u-blox-gnss-receiver

## Introduction

For GNSS positioning, u-blox has some of the most incredible receivers available. Over time they will release new versions of the firmware running on those receivers. This tutorial will demonstrate how to upgrade the firmware on the ZED-F9P but can be used for nearly all u-blox receivers including:

- [ZED-F9P](https://www.sparkfun.com/products/16481)
- [RTK Surveyor](https://www.sparkfun.com/products/17369) (uses the ZED-F9P)
- [RTK Express](https://www.sparkfun.com/products/18442) (uses the ZED-F9P)
- [RTK Express Plus](https://www.sparkfun.com/products/18590) (uses the ZED-F9R)
- [RTK Facet](https://www.sparkfun.com/products/19984) (uses the ZED-F9P)
- [ZED-F9R](https://www.sparkfun.com/products/16344)
- [NEO-M8P-02](https://www.sparkfun.com/products/15005)
- [NEO-M8U](https://www.sparkfun.com/products/16329)
- [NEO-M9N](https://www.sparkfun.com/products/15712)
- [SAM-M8Q](https://www.sparkfun.com/products/15210)
- [ZOE-M8Q](https://www.sparkfun.com/products/15193)

## Connecting

If you have not already installed [u-center](https://www.u-blox.com/en/product/u-center), do so now. If this is your first time using u-center, you should be fine, but just now we have a [Getting started with u-center](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox/all) tutorial that can be helpful.

**Note:** For these products, please download and use **u-center** *(original version)* and not **u-center 2** *(latest version)*. These products are not compatible with **u-center 2**.

\

[![software compatibility](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/9/2/ucenter_compaibility.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/ucenter_compaibility.jpg)

[![Connecting the ZED-F9P over USB](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_19.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_19.jpg)

*Connecting the [RTK Surveyor](https://www.sparkfun.com/products/17369) over USB*

For many modules like the ZED-F9P (shown inside the [RTK Surveyor](https://www.sparkfun.com/products/17369) above) or NEO-M8P, a USB connection is as simple as plugging in a USB cable.

[![SAM-M8Q connected to USB](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_18.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_18.jpg)

*A [USB adapter](https://www.sparkfun.com/products/15096) providing the serial connection*

For modules that do not have USB built in, you will need to use a [serial to USB adapter](https://www.sparkfun.com/products/15096) and solder in a 6-pin [right angle header](https://www.sparkfun.com/products/553). Note how the **GRN** and **BLK** labels align on both the serial adapter and the SAM-M8Q evaluation board.

[![COM power menu list](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_3.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_3.jpg)

Open u-center and connect to the appropriate COM port. Not sure what COM port to use? The easiest method is to view the listed COM ports, then unplug your device from USB. Now re-open the list. Which COM disappeared? That's the one you want.

Alternatively, you can Open Device Manager (press the Windows button then type 'device').

[![Device Manager list of COM ports](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_4.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_4.jpg)

In the image above COM3 is a COM port on my computer that never goes away. COM11 disappears when I unplug my ZED-F9P so COM11 is the port I need to connect to from u-center.

## Backup Device Settings

Updating the firmware will overwrite the device configuration. If you use stock settings or tweak just a few features then you can skip this step. If you have a highly configured receiver that you don't want to manually configure again, read on.

[![Receiver configuration sub menu](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_11.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_11.jpg)

Open the Receiver Configuration window. It's under **Tools**.

[![Receiver configuration tool](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_12.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_12.jpg)

We want to transfer from the receiver to a file. Give the configuration file an easy to remember name. Once complete, the receiver's settings will be committed to the file.

[![Loading a configuration to a u-blox receiver](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_13.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_13.jpg)

And just as easily, you can load a configuration file back onto the receiver. This is a handy tool for having a handful of different configurations or if you have a batch of receivers that all need to have the same settings applied.

## Identifying Current Firmware Version

This is perhaps the most difficult step of the process! Click on the *Messages* window button.

[![Messages window](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_14.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_14.jpg)

Within the Messages window, you will see a tremendous number of subtrees. Close them all so you only see NMEA, RTCM3, and UBX

[![All subtress collapsed](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_15.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_15.jpg)

Now expand UBX. We need to locate and expand MON, and finally locate VER.

[![VER message located](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_16.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_16.jpg)

Your device's firmware will be listed in the right window pane. In this example the Firmware Version is 1.13 and the module is the ZED-F9P.

## Getting Latest Firmware

Now that you know your current firmware, it's time to find out if there is anything more recent. SparkFun will generally not host the binary files that u-blox releases. This is because we want you to have the latest and greatest version directly from u-blox. You can usually find the firmware for a given product under the 'Documents and resources' tab for that given product. Here's the [ZED-F9P](https://www.u-blox.com/en/product/zed-f9p-module#tab-documentation-resources) as an example.

[![Documents tab](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_1.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_1.jpg)

Scroll or search this page for 'firmware'

[![Download firmware link](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_2.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_2.jpg)

Download this binary to a folder where you can easily find it.

## Upgrading Firmware

[![Firmware update sub-menu](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_5.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_5.jpg)

Select *Firmware Update* from the **Tools** menu. Note that while the menu says that Ctrl+U is the shortcut, it is **not**! Ctrl+U will open the legacy firmware update tool. Be careful and use your mouse.

[![Firmware update tool window](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_8.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_8.jpg)

Press the button with three dots \'\...\' and locate the firmware image you just downloaded. When you're ready, press the green dot button labeled 'GO' in the lower left corner.

[![Loading new firmware](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_9.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_9.jpg)

Sit back and wait. This upgrade took about 60s but your mileage may vary.

[![Firmware update success](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_17.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/1/6/9/2/u-blox_firmware_upgrade_-_17.jpg)

Upon completion, you should see the 'Firmware Update Success' message. The GNSS receiver will reset and re-enumerate over USB (if it has USB built-in). On the ZED-F9P all device settings and configurations were overwritten so if you previously saved your device's configuration now is a good time to reload them.