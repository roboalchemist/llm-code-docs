# Source: https://docs.edgeimpulse.com/hardware/boards/renesas-rz-g2l.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Renesas RZ/G2L

The Renesas RZ/G2L is a state-of-the-art general-purpose 64-bit Linux MPU with a dual-core ARM Cortex-A55 processor running at 1.2GHz.

The RZ/G2L EVK consists of a SMARC SOM module and an I/O carrier board that provides a USB serial interface, 2 channel Ethernet interfaces, a camera and an HDMI display interface, in addition to many other interfaces (PMOD, microphone, audio output, etc.). The RZ/G2L EVK can be acquired directly through the Renesas website.

<Frame caption="Renesas RZ/G2L">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/RZ_G2L.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=3ed0af354ed5146e4eac286e651809c4" width="600" height="436" data-path=".assets/images/RZ_G2L.png" />
</Frame>

For more technical information about RZ/G2L, please [refer to the Renesas RZ/G2L documentation](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rzg2l-general-purpose-microprocessors-dual-core-arm-cortex-a55-12-ghz-cpus-and-single-core-arm-cortex-m33).

Please create an account on Renesas' website to be able to download the packages and files outlined in the subsequent sections.

### Installing dependencies

#### Yocto image preparation/patch/build for G2L

Renesas provides Yocto build system to build all the necessary packages and create the Linux image. In this section, we will build the Linux image with the nodejs/npm packages required by Edge Impulse CLI tools. Renesas requires using the Ubuntu 20.04 Linux distribution to build the Linux image. Please follow instructions provided [here](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev103) to setup your build environment for your G2L yocto build. These instructions will also provide you with the necessary bootloader settings required to boot your G2L from sdcard.

In order to use the Edge Impulse CLI tools, NodeJS v18 needs to be installed into the yocto image that you build. Given the instructions called out [here](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev103), once the following files are downloaded from Renesas (specific versions specified are required):

```
	RTK0EF0045Z0021AZJ-v3.0.6-update2.zip
	RTK0EF0045Z13001ZJ-v1.2.2_EN.zip
	RTK0EF0045Z15001ZJ-v1.2.1_EN.zip
	oss_pkg_rzg_v3.0.6-update2.7z
```

... and extracted, you need to download the patch file [RZG2L\_VLP306u1\_switch\_to\_nodejs\_18.17.1.patch](https://cdn.edgeimpulse.com/firmware/RZG2L_VLP306u1_switch_to_nodejs_18.17.1.patch) and place the patch file into the same directory.

After putting all of these files into a single directory + patch file, you will need to create and patch your G2L yocto build environment as follows (this can be exported into a script that can be run):

```
	#!/bin/bash

	DIR=`pwd`
	TEMPLATECONF=$DIR/meta-renesas/meta-rzg2l/docs/template/conf/
	unzip ./RTK0EF0045Z0021AZJ-v3.0.6-update2.zip
	unzip ./RTK0EF0045Z13001ZJ-v1.2.2_EN.zip
	unzip ./RTK0EF0045Z15001ZJ-v1.2.1_EN.zip
	tar zxf ./RTK0EF0045Z0021AZJ-v3.0.6-update2/rzg_vlp_v3.0.6.tar.gz
	tar zxf ./RTK0EF0045Z13001ZJ-v1.2.2_EN/meta-rz-features_graphics_v1.2.2.tar.gz
	tar zxf ./RTK0EF0045Z15001ZJ-v1.2.1_EN/meta-rz-features_codec_v1.2.1.tar.gz
	7z x ./oss_pkg_rzg_v3.0.6-update2.7z
	source poky/oe-init-build-env build
	cd $DIR/meta-renesas
	patch -p1 < ../extra/0002-trusted-firmware-a-add-rd-wr-64-bit-reg-workaround.patch
	patch -p1 < ../extra/0003-rz-common-linux-renesas-add-WA-GIC-access-64bit.patch
	cd $DIR/build
	bitbake-layers add-layer ../meta-qt5
	bitbake-layers add-layer ../meta-rz-features/meta-rz-graphics
	bitbake-layers add-layer ../meta-rz-features/meta-rz-codecs
	bitbake-layers add-layer ../meta-openembedded/meta-filesystems
	bitbake-layers add-layer ../meta-openembedded/meta-networking
	bitbake-layers add-layer ../meta-virtualization
	cd $DIR
	patch -p1 < ./RZG2L_VLP306u1_switch_to_nodejs_18.17.1.patch
	cd $DIR/build
	echo ""                                     >> ./conf/local.conf
	echo "IMAGE_INSTALL_append = \" \\"         >> ./conf/local.conf
	echo "    nodejs \\"                        >> ./conf/local.conf
	echo "    nodejs-npm \\"                    >> ./conf/local.conf
	echo "    \""                               >> ./conf/local.conf
	echo ""                                     >> ./conf/local.conf
	echo ""                                     >> ./conf/local.conf
	echo "IMAGE_INSTALL_append = \" \\"         >> ./conf/local.conf
	echo "    nvme-cli \\"                      >> ./conf/local.conf
	echo "    \""                               >> ./conf/local.conf
	echo ""                                     >> ./conf/local.conf
	#-# glibc2.31 instead of glibc2.28
	sed -i 's/^CIP_MODE = "Buster"/CIP_MODE = "Bullseye"/g' ./conf/local.conf
```

You can then invoke your G2L yocto build process via:

```
	#!/bin/bash

	DIR=`pwd`
	export TEMPLATECONF=$PWD/meta-renesas/meta-rzg2l/docs/template/conf/
	export MACHINE=smarc-rzg2l
	source poky/oe-init-build-env build
	time bitbake core-image-weston
```

Renesas documentation [here](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev103) then shows you different build options + how to flash your compiled images onto your G2L board. Once your build completes, your files that will be used in those subsequent instructions called out [here](https://www.renesas.com/us/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev103) to flash your G2L board can be found here:

```
	#!/bin/bash

	DIR=`pwd`
	ls -al $DIR/build/tmp/deploy/images/smarc-rzg2l
```

#### Accessing the board using `screen`

The easiest way is to connect through serial to the RZ/G2L board using the USB mini b port.

1. After connecting the board with a USB-C cable, please power the board with the red power button.
2. Please install `screen` to the host machine and then execute the following command from Linux to access the board:

   ```
   screen /dev/ttyUSB0 115200
   ```
3. You will see the boot process, then you will be asked to log in:
   * Log in with username `root`
   * There is no password

Note that, it should be possible to use an Ethernet cable and log in via SSH if the daemon is installed on the image. However, for simplicity purposes, we do not refer to this one here.

#### Installing Edge Impulse Linux CLI

Once you have logged in to the board, please run the following command to install Edge Impulse Linux CLI

```
npm install edge-impulse-linux -g --unsafe-perm
```

### Connecting to Edge Impulse

With all software set up, connect your google coral camera to your Renesas board (see 'Next steps' further on this page if you want to connect a different sensor), and run:

```
edge-impulse-linux
```

This will start a wizard which will ask you to log in and choose an Edge Impulse project. If you want to switch projects run the command with `--clean`.

#### Verifying that your device is connected

That's all! Your device is now connected to Edge Impulse. To verify this, go to [your Edge Impulse project](https://studio.edgeimpulse.com/studio/profile/projects), and click **Devices**. The device will be listed here.

<Frame caption="Device connected to Edge Impulse.">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/renesas_mpu.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=1e9ceeee97dc9da30586d0fdb83109df" width="1600" height="164" data-path=".assets/images/renesas_mpu.png" />
</Frame>

### Next steps: building a machine learning model

Currently, all Edge Impulse models can run on the RZ/G2L CPU which is a dedicated Cortex A55. In addition, you can bring your own model to Edge Impulse and use it on the device. However, if you would like to benefit from the DRP-AI hardware acceleration support including higher performance and power efficiency, please use one of the following models:

For object detection:

* Yolov5 (v5)
* FOMO (Faster objects More Objects)

For Image classification:

* MobileNet v1, v2

It supports as well models built within the studio using the available layers on the training page.

Note that, on the training page you **have** to select the **target** before starting the training in order to tell the studio that you are training the model for the RZ/G2L. This can be done on the top right in the training page.

<Frame caption="Selecting the target from the training page">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/target-renesas-g2l.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=e8b156bdfc49e4fbbdde18b444fc299c" width="329" height="65" data-path=".assets/images/target-renesas-g2l.png" />
</Frame>

If you would like to do object detection with Yolov5 (v5) you need to fix the image resolution in the impulse design to **320x320**, otherwise, you might risk that the training fails.

With everything set up you can now build your first machine learning model with these tutorials:

* [Image classification](/tutorials/end-to-end/image-classification).
* [Detect objects using FOMO](/tutorials/end-to-end/object-detection-centroids).

### Deploying back to device

To run your impulse locally, just connect to your Renesas RZ/G2L and run:

```
edge-impulse-linux-runner
```

This will automatically compile your model with full hardware acceleration and download the model to your Renesas board, and then start classifying.

Or you can select the RZ/G2L board from the deployment page, this will download an `eim` model that you can use with the above runner as follows:

Go to the deployment page and select:

<Frame caption="EIM model for the RZ/G2L">
  <img src="https://mintcdn.com/edgeimpulse/BCrJzLAs8FGQ0Eny/.assets/images/rz-g2l-eim.png?fit=max&auto=format&n=BCrJzLAs8FGQ0Eny&q=85&s=aee3c546e6f098495f8506146a1228b4" width="686" height="99" data-path=".assets/images/rz-g2l-eim.png" />
</Frame>

Then run the following on the RZ/G2L:

```
edge-impulse-linux-runner --model-file downloaded-model.eim
```

You will see the model inferencing results in the terminal also we stream the results to the local network. This allows you to see the output of the model in real-time in your web browser. Open the URL shown when you start the `runner` and you will see both the camera feed and the classification results.


Built with [Mintlify](https://mintlify.com).